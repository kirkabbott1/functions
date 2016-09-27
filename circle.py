
from turtle import *

def circle(size):
    for i in range(360):
        forward(size)
        left(1)

circle(1)
right(180)
circle(1.5)
up()
left(90)
forward(180)
down()
right(90)
circle(2)

mainloop()
