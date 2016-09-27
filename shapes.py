from turtle import *

def triangle(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(3):
        forward(size)
        left(120)
    fill(False)

def square(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(4):
        forward(size)
        left(90)
    fill(False)

def pentagon(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(5):
        forward(size)
        left(72)
    fill(False)

def hexagon(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(6):
        forward(size)
        left(60)
    fill(False)

def star(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(5):
        forward(size)
        right(163)
        forward(size)
        left(90)
    fill(False)

def circle(size, fill_bool, color_shape):
    color(color_shape)
    fill(fill_bool)
    for i in range(360):
        forward(size)
        left(1)
    fill(False)
