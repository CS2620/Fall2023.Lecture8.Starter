import math


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

    def get_pixel(self, x, y):
        index = self.pixelIndex(x, y)
        return self.pixels[index]

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
                from_pixel_index = self.pixelIndex(from_pixel_x, from_pixel_y)
                from_pixel = self.pixels[from_pixel_index]

                new_pixel_index = self.pixelIndex(x, y)

                new_pixels[new_pixel_index] = from_pixel
        self.pixels = new_pixels

    def flip_vertical(self):
        new_pixels = [0, 0, 0] * self.width * self.height
        for y in range(self.height):
            for x in range(self.width):
                from_pixel_x = self.width - x - 1
                from_pixel_y = y
                from_pixel_index = self.pixelIndex(from_pixel_x, from_pixel_y)
                from_pixel = self.pixels[from_pixel_index]

                new_pixel_index = self.pixelIndex(x, y)

                new_pixels[new_pixel_index] = from_pixel
        self.pixels = new_pixels

    def rotate_counter_clockwise(self):
        new_pixels = [0, 0, 0] * self.width * self.height
        new_width = self.height
        new_height = self.width
        for y in range(self.height):
            for x in range(self.width):
                to_pixel_x = y
                to_pixel_y = -x + self.width - 1
                to_pixel_index = to_pixel_y*new_width + to_pixel_x
                from_index = self.pixelIndex(x, y)
                from_pixel = self.pixels[from_index]

                new_pixels[to_pixel_index] = from_pixel
        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height

    def translate(self, dx, dy):
        new_width = self.width + math.ceil(dx)
        new_height = self.height + math.ceil(dy)
        new_pixels = [0, 0, 0] * new_width * new_height
        for y in range(new_height):
            for x in range(new_width):
                to_pixel_x = x
                to_pixel_y = y
                to_pixel_index = to_pixel_y*new_width + to_pixel_x

                from_x = to_pixel_x - math.ceil(dx)
                from_y = to_pixel_y - math.ceil(dy)
                if from_x < 0 or from_y < 0:
                    continue
                from_index = self.pixelIndex(from_x, from_y)
                if(from_index >= 0):
                    from_pixel = self.pixels[from_index]

                    new_pixels[to_pixel_index] = from_pixel
        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height

    def scale(self, dx, dy):
        new_width = math.floor(self.width * dx)
        new_height = math.floor(self.height * dy)
        new_pixels = [0, 0, 0] * new_width * new_height
        for y in range(new_height):
            for x in range(new_width):
                to_pixel_x = x
                to_pixel_y = y
                to_pixel_index = to_pixel_y*new_width + to_pixel_x

                from_x = math.floor(to_pixel_x / dx)
                from_y = math.floor(to_pixel_y/dy)
                if from_x < 0 or from_y < 0:
                    continue
                from_index = self.pixelIndex(from_x, from_y)
                if(from_index >= 0):
                    from_pixel = self.pixels[from_index]

                    new_pixels[to_pixel_index] = from_pixel
        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height

    def scale_forward(self, dx, dy):
        new_width = math.floor(self.width * dx)
        new_height = math.floor(self.height * dy)
        new_pixels = [0, 0, 0] * new_width * new_height
        for y in range(self.height):
            for x in range(self.width):
                to_pixel_x = math.floor(x * dx)
                to_pixel_y = math.floor(y * dy)
                to_pixel_index = to_pixel_y*new_width + to_pixel_x

                from_x = x
                from_y = y
                from_index = self.pixelIndex(from_x, from_y)
                from_pixel = self.pixels[from_index]
                new_pixels[to_pixel_index] = from_pixel
        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height

    def interpolate_nearest_neighbor(self, x, y):
        from_x = math.floor(x)
        from_y = math.floor(y)
        if from_x < 0 or from_x >= self.width or from_y < 0 or from_y >= self.height:
            return None
        pixel_index = self.pixelIndex(from_x,from_y)
        return self.pixels[pixel_index]
    
    def color_at(self, x, y):
        from_x = math.floor(x)
        from_y = math.floor(y)
        if from_x < 0 or from_x >= self.width or from_y < 0 or from_y >= self.height:
            return [0,0,0]
        pixel_index = self.pixelIndex(from_x,from_y)
        return self.pixels[pixel_index]

    def interpolate_nearest_neighbor(self, x, y):
        return self.color_at(x,y)
    
    def interpolate_bilinear(self, x, y):
        color_UL = self.color_at(math.floor(x), math.floor(x))
        color_UR = self.color_at(math.ceil(x), math.floor(y))
        color_LL = self.color_at(math.floor(x), math.ceil(y))
        color_LR = self.color_at(math.ceil(x), math.ceil(y))

        x_percent = math.modf(x)[0]
        y_percent = math.modf(y)[0]


        top = color_UL * (1-x_percent) + color_UR * x_percent
        bottom = color_LL * (1-x_percent) + color_LR * x_percent

        color = top * (1-y_percent) + bottom * y_percent
        
        return color

    

    def rotate(self, theta):
        new_width = self.width*2
        new_height = self.height*2
        new_pixels = [0, 0, 0] * new_width * new_height
        for y in range(new_height):
            for x in range(new_width):
                to_pixel_x = x
                to_pixel_y = y
                to_pixel_index = to_pixel_y*new_width + to_pixel_x

                to_radius = math.sqrt(to_pixel_x**2 + to_pixel_y**2)
                to_theta = math.atan2(to_pixel_y, to_pixel_x)
                from_radius = to_radius
                from_theta = to_theta - theta
                from_x = math.cos(from_theta) * from_radius
                from_y = math.sin(from_theta) * from_radius
                # from_color = self.interpolate_nearest_neighbor(from_x,from_y)
                from_color = self.interpolate_bilinear(from_x,from_y)

                if from_color:
                    new_pixels[to_pixel_index] = from_color

        self.pixels = new_pixels
        self.width = new_width
        self.height = new_height
