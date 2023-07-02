# 实现画笔的大部分功能

import turtle as t
import tkinter as tk

flg = 0


def beginner(t):
    global flg
    if not flg:
        clear(t)
        flg = 1
    pass


def ender(t):
    global flg
    flg = 0


def move(frame , t):
    beginner(t)
    print("move")

    pass


def rotate(frame , t):
    beginner(t)
    print("rotate")
    pass


def Circle(frame ,t):
    beginner(t)
    print("circle")

    pass


def fill(frame ,t):
    beginner(t)
    print("fill")
    pass


def pen_color(frame ,t):
    print("pencolor")
    pass


def pen_size(frame ,t):
    print("pensize")




    pass


def pen_up(frame ,t):
    print("pen_up")
    pass


def pen_down(frame ,t):
    beginner(t)
    print("pendown")
    pass


def cancel(frame ,t):
    beginner(t)
    print("cancel")

    pass


def clear(t):
    print("clear")
    t.clear()


def save(frame ,t):
    print("save")
    pass

def welcome(t):
    # 绘制欢迎图案
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.color("white")
    font_style = ("方正有猫在_GBK", 36, "bold")
    # 绘制欢迎到
    t.penup()
    t.goto(-220, 40)
    t.write("欢迎来到，", font=font_style)
    t.goto(-220, - 40)
    t.write("今天的Turtle小课堂~", font=font_style)
    t.goto(220, -40)