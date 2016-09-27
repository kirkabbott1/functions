
#Hello
# def hello(name):
#     return 'Hello %s' % name
#
# print hello('kirk')

#y = x + 1 plot
############# import matplotlib.pyplot as plot
# def f(x):
#     return x + 1
# xs = range(-3, 4)
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs, ys)
# plot.show()

# #Square of x
# def f(x):
#     return (x**2)
# xs = range(-100, 101)
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs, ys)
# plot.show()

# Odd or Even
# def f(x):
#     if x%2 != 0:
#         return 1
#     else:
#         return -1
# xs = range(-5, 6)
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.bar(xs, ys)
# plot.show()

# #Sine
# import math
#################### from numpy import arange
# def f(x):
#     return math.sin(x)
# xs = arange(-5, 6, 0.1)
# ys = []
# for x in xs:
#     ys.append(f(x))
# plot.plot(xs, ys)
# plot.show()
#
# convert celcius to farhenheit

# def converter(temp):
#     return temp * 1.8 + 32
# xs = range(1, 50)
# ys = []
# for F in xs:
#     ys.append(converter(F))
# plot.plot(xs, ys, "ro")
# plot.show()

from turtle import *

def draw_square():
    for i in range(4):
        forward(100)
        left(90)
draw_square()

# from draw_a_square import draw_square

# coord_list = [(-100, -100, 100), (100, 100, 200), (-100, 100, 120),]
#
# if __name__ == '__main__':
#
#     begin_fill()
#     draw_square()
#     end_fill()
#
#     up()
#     forward(200)
#     down()
#
#     draw_square()
#
#     left(100)
#     forward(200)
#     setheading(270)
#     forward(x)
#     setheading(0)
#     forward(y)
