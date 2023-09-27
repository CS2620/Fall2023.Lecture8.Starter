import math
from color import Color

def translate(self, dx:float, dy:float):
  """ Translate the pixel (but don't translate the layer itself)"""
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

def scale_backward(self, dx:float, dy:float):
    """Scale the image polling backward"""
    pass

def scale_forward(self, dx, dy):
    """ Scale the image pushing forward """
    pass
    

def interpolate_nearest_neighbor(self, x, y):
    """ Find a pixel on the image using the nearest neighbor approach"""
    return (255, 0, 0)

def color_at(self, x, y):
    """ Find the color at a given point, gracefully handling out of bounds indeces"""
    from_x = math.floor(x)
    from_y = math.floor(y)
    if from_x < 0 or from_x >= self.width or from_y < 0 or from_y >= self.height:
        return [0, 0, 0]
    pixel_index = self.pixelIndex(from_x, from_y)
    return self.pixels[pixel_index]


def interpolate_bilinear(self, x, y):
    """ Find a pixel on the image using the bilinear approach"""
    return (255, 255, 255)

def rotate(self, theta):
    """ Rotate the image arbitrarily"""
    pass
