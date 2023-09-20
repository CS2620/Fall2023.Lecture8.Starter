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
        new_pixels = [0, 0, 0] * self.width * self.height
        for y in range(self.height):
            for x in range(self.width):
                from_pixel_x = x
                from_pixel_y = self.height - y - 1
                from_pixel_index = self.pixelIndex(from_pixel_x,from_pixel_y)
                from_pixel = self.pixels[from_pixel_index]

                new_pixel_index = self.pixelIndex(x,y)

                new_pixels[new_pixel_index] = from_pixel
        self.pixels = new_pixels

    def flip_vertical(self):
        new_pixels = [0, 0, 0] * self.width * self.height
        for y in range(self.height):
            for x in range(self.width):
                from_pixel_x = self.width - x - 1
                from_pixel_y = y
                from_pixel_index = self.pixelIndex(from_pixel_x,from_pixel_y)
                from_pixel = self.pixels[from_pixel_index]

                new_pixel_index = self.pixelIndex(x,y)

                new_pixels[new_pixel_index] = from_pixel
        self.pixels = new_pixels
    
    def rotate_counter_clockwise(self):
        new_pixels = [0, 0, 0] * self.width * self.height
        new_width = self.height
        new_height = self.width
        for y in range(self.height):
            for x in range(self.width):
                to_pixel_x = y 
                to_pixel_y = -x + self.width -1
                to_pixel_index = to_pixel_y*new_width + to_pixel_x
                from_index = self.pixelIndex(x,y)
                from_pixel = self.pixels[from_index]

                new_pixels[to_pixel_index] = from_pixel
        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height