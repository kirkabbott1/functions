from turtle import *
import random

from shapes import star
bgcolor("#040404")


# w_width = window_width()
# w_height = window_height()
#
# turt_x = position()[0]
# turt_y = position()[1]
#
# left(15)
# forward(200)
# print position()[0]
# print position()[1]
# print turt_x
# print turt_y
# left(180)
# forward(400)
# print position()[0]
# print position()[1]
# print turt_x
# print turt_y
# home()
# print position()[0]
# print position()[1]

def nightsky_star(star_size, turn, jump_forward):
    star(star_size, True, "#cecece")
    up()
    print 'position-x: ', abs(position()[0])
    print 'position-y: ', abs(position()[1])
    print 'window width: ', window_width()
    print 'window height: ', window_height()

    if abs(position()[0]) * 3 > window_width() or abs(position()[1]) * 3 > window_height():
        home()
    else:
        pass
    left(turn)
    forward(jump_forward)
    down()


for i in range(70):
    # generate a random number and store it in a variable
    star_size = random.randint(5, 41)
    turn = random.randint(10, 141)
    jump_forward = random.randint(200, 401)

    nightsky_star(star_size, turn, jump_forward)
mainloop()
