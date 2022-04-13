
import turtle as t
from unicodedata import name

# map size W x H (pixels)
CropFrame = 1
cropX = 0

def moveRight():
    global cropX
    global CropFrame
    cropX += 50
    CropFrame += 1
    if CropFrame == 4:
        CropFrame = 1
    showCrop(cropX, 0)

def moveLeft():
    global cropX
    global CropFrame

    cropX -= 50
    CropFrame += 1
    if CropFrame == 4:
        CropFrame = 1
    showCrop(cropX, 0)

def windowSetup():
    WIDTH  = 1200
    HEIGHT = 600
    t.setup(WIDTH, HEIGHT)
    t.showturtle()


# display an image
def showImage(name):
    s = t.Screen()
    s.addshape(name)
    t.shape(name)

def showCrop(x,y):
    global CropFrame
    name = f'Mario-Game/GIF/anim-{CropFrame}.gif'
    s = t.Screen()
    s.addshape(name)
    t.penup()
    t.setposition(x,y)

    t.shape(name)



