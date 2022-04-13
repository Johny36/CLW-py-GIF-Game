

from lib import *



windowSetup()

showCrop(cropX, 0)
# key bindings
t.listen()
t.onkey(moveRight, "Right")
t.onkey(moveLeft, "Left")

t.mainloop()

#

# showImage('Mario-Game/GIF/anim.gif')
# showImage('Mario-Game/GIF/crop_2.gif')



