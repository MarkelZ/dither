import numpy as np


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


def _get_matching_piece(brightness):
    diffs = np.array([abs(p - brightness) for p in piece_brightnesses3])
    return mosaic_pieces3[np.where(diffs == diffs.min())[0][0]]


def dither(img):
    w, l = img.shape[0], img.shape[1]
    nw, nl = w*3, l*3

    new_img = np.zeros((nw, nl))

    for i in range(w):
        for j in range(l):
            piece = _get_matching_piece(img[i, j])
            new_img[i*3:i*3+3, j*3:j*3+3] = piece

    return new_img
