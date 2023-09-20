class Layer:
    """Class that stores the pixel data of an image layer"""

    def __init__(self, width, height, offset_x, offset_y):
        """Store the constructor arguments"""
        self.width, self.height = width, height
        self.offset_x, self.offset_y = offset_x, offset_y
        self.pixels = [0, 0, 0] * self.width * self.height

    # Set the value of a specific pixel
    def set_pixel(self, x, y, color):
        """Set a pixel in the layer buffer"""
        index = self.pixelIndex(x, y)
        self.pixels[index] = color

    # Get the index of a pixel in our linear array
    def pixelIndex(self, x, y):
        """Given x and y, find the index in our linear array."""
        index = y*self.width + x
        return index

    def flip_horizontal(self):
        pass

    def flip_vertical(self):
        pass
    
    def rotate_counter_clockwise(self):
        pass