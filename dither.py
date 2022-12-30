import numpy as np
from PIL import Image
import sys


# ======= Tiles ========

INCLUDE_INVERSES = True

tiles_str = [
    '0 0 0; 0 1 0; 0 0 0',
    '1 0 0; 0 0 0; 0 0 1',
    '0 1 0; 1 0 0; 0 0 1',
    '1 0 1; 0 0 0; 1 0 1',
    '1 0 1; 0 1 0; 1 0 1',
]


# Create list of tiles from their string representations
tiles = [np.matrix(m) for m in tiles_str]

# Add also their inverses
if INCLUDE_INVERSES:
    tiles += [np.matrix(1 - m) for m in tiles]

# List of the brightness of each tile
tile_brightnesses = [np.sum(m) / m.size for m in tiles]

# Dimensions of the mosaics (assuming consistency)
mwidth = tiles[0].shape[0]
mheight = tiles[0].shape[1]


# Given the brightness value of a pixel, returns best matching tile
def get_matching_piece(brightness):
    diffs = np.array([abs(p - brightness) for p in tile_brightnesses])
    return tiles[np.where(diffs == diffs.min())[0][0]]


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
    nw, nl = w*mwidth, l*mheight

    new_img = np.zeros((nw, nl))

    for i in range(w):
        for j in range(l):
            piece = get_matching_piece(img[i, j])
            new_img[i*mwidth:i*mwidth+mwidth, j *
                    mheight:j*mheight+mheight] = piece

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
