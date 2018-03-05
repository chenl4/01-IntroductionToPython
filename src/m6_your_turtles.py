"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Lilin Chen.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue',6)
blue_turtle.speed = 10

green_turtle = rg.SimpleTurtle('turtle')
green_turtle.pen = rg.Pen('green',6)
green_turtle.speed = 9

size = 300

for k in range(11):

    blue_turtle.draw_square(size)
    green_turtle.draw_square(size)

    blue_turtle.pen_up()
    green_turtle.pen_up()
    blue_turtle.right(45)
    green_turtle.right(135)
    blue_turtle.forward(20)
    green_turtle.forward(20)
    blue_turtle.left(45 + k)
    green_turtle.left(45 + k)

    blue_turtle.pen_down()
    green_turtle.pen_down()
    size = size - 30


window.close_on_mouse_click()