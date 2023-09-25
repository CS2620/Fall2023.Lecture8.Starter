# This program requires pillow
# `python -m pip` to install pillow

from PIL import Image
from container import Container
from layer import Layer
import math

print("Start")

# Open an image, get its size, and access its pixel buffer
# image = Image.open("./helpers/Debug1.png")
image = Image.open("./helpers/DebugTiny.png")
# image = Image.open("./images/address.jpg")
bridge_buffer = image.load()
width = image.size[0]
height = image.size[1]


container:Container = Container(max(width, height)*2, max(width,height)*2)


layer1:Layer = Layer(width, height, 0, 0)
container.add_layer(layer1)


# Loop through all the layer(s) and give them pixels
for y in range(height):
    for x in range(width):
        pixel = bridge_buffer[x, y]

        layer1.set_pixel(x, y, pixel)


# layer1.scale_forward(1.1,1.1)    
layer1.rotate(.1)


container.save("done.png")