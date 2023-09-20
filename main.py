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


container:Container = Container(width*2, height*2)


layer1:Layer = Layer(width, height, 0, 0)
container.add_layer(layer1)

layer2:Layer = Layer(width, height, width, 0)
container.add_layer(layer2)

layer3:Layer = Layer(width, height, 0, height)
container.add_layer(layer3)

layer4:Layer = Layer(width, height, width, height)
container.add_layer(layer4)


# Loop through all the layers and give them values
for y in range(height):
    for x in range(width):
        pixel = bridge_buffer[x, y]

        r, g, b = pixel
        avg = math.floor((r + g + b)/3)
        v = max(r,g,b)
        ntsc = math.floor(0.2126 *r + 0.7152 *g + 0.0722 * b )

        layer1.set_pixel(x, y, pixel)
        layer2.set_pixel(x, y, (avg, avg, avg))
        layer3.set_pixel(x, y, (v,v,v))
        layer4.set_pixel(x, y, (ntsc, ntsc, ntsc))


container.save("done.png")