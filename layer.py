import math
from color import Color


class Layer:
    """Class that stores the pixel data of an image layer"""

    from _simple_transformations import flip_horizontal_axis
    from _simple_transformations import flip_vertical_axis
    from _simple_transformations import rotate_counter_clockwise

    from _advanced_transformations import color_at
    from _advanced_transformations import interpolate_bilinear
    from _advanced_transformations import interpolate_nearest_neighbor
    from _advanced_transformations import rotate
    from _advanced_transformations import scale_backward
    from _advanced_transformations import scale_forward
    from _advanced_transformations import translate


    def __init__(self, width: int, height: int, offset_x: float, offset_y: float):
        """Store the constructor arguments"""
        self.width, self.height = width, height
        self.offset_x, self.offset_y = offset_x, offset_y
        self.pixels = [0, 0, 0] * self.width * self.height

    def set_pixel(self, x, y, color) -> None:
        """Set a pixel in the layer buffer"""
        index = self.pixelIndex(x, y)
        self.pixels[index] = color

    def get_pixel(self, x: int, y: int):
        """ Given x and y, return the color of the pixel"""
        index = self.pixelIndex(x, y)
        return self.pixels[index]

    def pixelIndex(self, x:int, y:int) -> int:
        """Given x and y, find the index in our linear array."""
        index = y*self.width + x
        return index

   
    