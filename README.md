# Dithering tool

## Description
This is a tool for dithering images. 

## Example
![dithered_image](monadither.png)

## Dependencies
- Python 3.
- PIL, numpy, and sys packages for Python 3.

## Usage

Run the following command to dither an image:

```shell
python3 dither.py <input_image> <output_image>
```

## Custom tiles

- You can have custom tiles by edditing `tiles_str` in `dither.py` (line 11). 
- The tiles can be of any size, as long as all of them have the same dimensions. Rectangular tiles (non-square) are allowed.
- By default `INCLUDE_INVERSES` is set to `True`. This means that in adition to the tiles defined in `tiles_str`, their inverses are also included. The inverse of a tile is obtained by swapping all 1's for 0's and vice versa.


## License
This code is licensed under the terms of the MIT license.
