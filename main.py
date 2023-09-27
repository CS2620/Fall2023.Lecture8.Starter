# This program requires pillow
# `python -m pip` to install pillow

from PIL import Image
from container import Container
from layer import Layer

print("Start")

# Open an image, get its size, and access its pixel buffer

""" There are multiple lines here to ease debugging"""
# image = Image.open("./helpers/Debug1.png")
# image = Image.open("./helpers/DebugTiny.png")
image = Image.open("./images/address.jpg")

""" Load the image and get its height and width"""
bridge_buffer = image.load()
width = image.size[0]
height = image.size[1]

""" Building a container for the image"""
container:Container = Container(width,height)

""" Create the layer that wi will be transforming. Add that to the container"""
layer1:Layer = Layer(width, height, 0, 0)
container.add_layer(layer1)


""" Loop through all the layer(s) and give them their colors"""
for y in range(height):
    for x in range(width):
        pixel = bridge_buffer[x, y]

        layer1.set_pixel(x, y, pixel)


""" Choose a custom transformation """
# layer1.flip_horizontal_axis()
# layer1.flip_vertical_axis()
# layer1.rotate_counter_clockwise()
# layer1.translate(100,100)
# layer1.scale_backward(2,2)
# layer1.scale_forward(2,2)
# layer1.scale_forward(1.1,1.1)    
layer1.rotate(1)


container.save("done.png")