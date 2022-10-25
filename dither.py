from importlib.resources import path
import numpy as np
from PIL import Image
import sys
import os
import json


# ======= Mosaics ========

_mosaic_str = [
    '0 0 0; 0 1 0; 0 0 0',
    '1 0 0; 0 0 0; 0 0 1',
    '0 1 0; 1 0 0; 0 0 1',
    '1 0 1; 0 0 0; 1 0 1',
    '1 0 1; 0 1 0; 1 0 1',

    '1 1 1; 1 0 1; 1 1 1',
    '0 1 1; 1 1 1; 1 1 0',
    '1 0 1; 0 1 1; 1 1 0',
    '0 1 0; 1 1 1; 0 1 0',
    '0 1 0; 1 0 1; 0 1 0',
]


mosaic_pieces3 = [np.matrix(m) for m in _mosaic_str]
piece_brightnesses3 = [np.sum(m) / m.size for m in mosaic_pieces3]


# Given the brightness value of a pixel, returns best matching mosaic piece
def get_matching_piece(brightness):
    diffs = np.array([abs(p - brightness) for p in piece_brightnesses3])
    return mosaic_pieces3[np.where(diffs == diffs.min())[0][0]]


# ======== Image dithering ========

# Given the path of an image, returns a matrix representing the dithered image
def dither_from_path(path):
    img = get_img_from_path(path)
    d_img = dither_img(img)
    return d_img


# Given the path of an image, returns a matrix representing said image
def get_img_from_path(path):
    img = Image.open(path).convert('L')
    img = np.asmatrix(img) / 255.0
    return img


# Given a matrix of an image and a path, saves the matrix as an image at the given path
def save_img(img, path):
    img_out = Image.fromarray((img * 255.0).astype(np.uint8))
    img_out.save(path)


# Dither an image represented as a matrix of values from 0 to 255
def dither_img(img):
    w, l = img.shape[0], img.shape[1]
    nw, nl = w*3, l*3

    new_img = np.zeros((nw, nl))

    for i in range(w):
        for j in range(l):
            piece = get_matching_piece(img[i, j])
            new_img[i*3:i*3+3, j*3:j*3+3] = piece

    return new_img


# ======== CUI ========

if len(sys.argv) <= 2:
    # If too few arguments are given, print usage
    print('Usage:')
    print('\tpython3 dither.py <input_image> <output_image>')
else:
    # Get paths of input and output images
    path_in = sys.argv[1]
    path_out = sys.argv[2]

    # Dither image and save it to path_out
    d_img = dither_from_path(path_in)
    save_img(d_img, path_out)
