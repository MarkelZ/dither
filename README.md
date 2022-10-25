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
- An example of a tile would be `'00;11;00'`, which represents a 2x3 tile where the two pixels at the top and two at the bottom are black, and the two in the middle are white. `tiles_str` is a list of such strings.
- By default, `INCLUDE_INVERSES` is set to `True`. This means that in adition to the tiles defined in `tiles_str`, their inverses are also included. The inverse of a tile is obtained by swapping all 1's for 0's and vice versa. To disable this feature, set `INCLUDE_INVERSES` to `False`.


## License
This code is licensed under the terms of the MIT license.
