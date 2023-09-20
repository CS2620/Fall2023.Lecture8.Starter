# This program requires pillow
# `python -m pip` to install pillow

from PIL import Image
from container import Container
from layer import Layer
import math

print("Start")

# Open an image, get its size, and access its pixel buffer
image = Image.open("./images/bridge.jpg")
bridge_buffer = image.load()
width = image.size[0]
height = image.size[1]


container:Container = Container(max(width, height), max(width,height))


layer1:Layer = Layer(width, height, 0, 0)
container.add_layer(layer1)


# Loop through all the layer(s) and give them pixels
for y in range(height):
    for x in range(width):
        pixel = bridge_buffer[x, y]

        layer1.set_pixel(x, y, pixel)

# layer1.flip_horizontal()        
#layer1.flip_vertical()        
# layer1.rotate_counter_clockwise()        
# layer1.rotate_counter_clockwise()        
# layer1.rotate_counter_clockwise()        
# layer1.rotate_counter_clockwise()        


container.save("done.png")