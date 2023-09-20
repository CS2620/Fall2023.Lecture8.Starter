from layer import Layer
from PIL import Image

class Container:
  """A list of layer objects
  
  Args:
    width (int): The width of the container
    height (int): The height of the container
  """
  def __init__(self, width:int, height:int):
    self.width, self.height = width, height
    self.image = Image.new("RGB", (width, height))
    self.buffer = self.image.load()
    self.layers = []

  def add_layer(self, layer:Layer):
    """Add a layer to the container
    
    Args:
      layer (Layer): The layer to add to the container
    """
    self.layers.append(layer)

  def save(self, filename):
    """
    Rasterize and save the layers
    
    Step 1: Rasterize all layers to this container's buffer
    Step 2: Save that buffer to the filesystem

    Args:
      filename (string): The filename to save to
    """
    for layer in self.layers:
      for y in range(layer.height):
        for x in range(layer.width):
          self.buffer[x+layer.offset_x,y+layer.offset_y] = layer.pixels[y*layer.width+x]
    self.image.save(filename, "png")

  

