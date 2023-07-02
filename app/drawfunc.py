# 实现画笔的大部分功能

import turtle as t
import tkinter as tk
from MyButton import *
import math

flg = 0


def beginner(t):
    global flg
    if not flg:
        clear(t)
        t.down()
        flg = 1
    pass


def ender(t):
    global flg
    flg = 0


def move(frame, t):
    def judge(t, d):
        # 获取当前的位置
        x, y = t.position()

        # 获取海龟当前朝向角度
        heading = t.heading()

        # 根据朝向角度计算移动分量
        heading_radians = heading * 3.14159 / 180.0
        dx = d * round(math.cos(heading_radians), 2)
        dy = d * round(math.sin(heading_radians), 2)

        new_x = x + dx
        new_y = y + dy
        if new_y < - 332:
            new_y = - 332
        if new_y > 332:
            new_y = 332
        if new_x < - 255:
            new_x = -255
        if new_x > 255:
            new_x = 255
        d = math.sqrt(pow(new_x - x, 2) + pow(new_y - y, 2))
        return d

    def left(t, d):
        t.setheading(180)
        d = judge(t, d)
        t.forward(d)

    def right(t, d):
        t.setheading(0)
        d = judge(t, d)
        t.forward(d)

    def up(t, d):
        # 判断turtle 会不会走出画布
        t.setheading(90)
        d = judge(t, d)
        t.forward(d)

    def down(t, d):
        t.setheading(270)
        d = judge(t, d)
        t.forward(d)

    beginner(t)

    popup = tk.Frame()
    popup = tk.Frame(frame, width=300, height=150)
    popup.place(x=0, y=0)
    canvas = tk.Canvas(popup, width=300, height=150, bg=f"#{69:02x}{149:02x}{199:02x}")
    canvas.pack()

    def on_closing():
        popup.destroy()

    up_button = MyButton(popup, "../material/picture/18.png", lambda: up(t, scale.get()))
    up_button.place(y=5, x=55)
    down_button = MyButton(popup, "../material/picture/19.png", lambda: down(t, scale.get()))
    down_button.place(y=80, x=55)
    left_button = MyButton(popup, "../material/picture/20.png", lambda: left(t, scale.get()))
    left_button.place(x=5, y=40)
    right_button = MyButton(popup, "../material/picture/21.png", lambda: right(t, scale.get()))
    right_button.place(x=105, y=40)

    scale = tk.Scale(popup, from_=1, to=200, orient="horizontal", label="移动距离:")
    scale.place(x=180, y=5)
    scale.set(50)

    exit_button = MyButton(popup, "../material/picture/22.png", on_closing)
    exit_button.place(x=185, y=75)


def rotate(frame, t):
    beginner(t)
    print("rotate")
    pass


def Circle(frame, t):
    beginner(t)
    print("circle")
    t.circle(50)

    pass


def fill(frame, t):
    beginner(t)
    print("fill")
    pass


def pen_color(frame, t):
    print("pencolor")
    pass


def pen_size(frame, t):
    print("pensize")

    popup = tk.Frame(frame, width=200, height=100)
    canvas = tk.Canvas(popup, width=200, height=100, bg=f"#{69:02x}{149:02x}{199:02x}")
    popup.place(x=340, y=320)
    canvas.pack()

    button = MyButton(popup, "../material/picture/23.png", lambda: on_closing(t))

    def update_pensize(value):
        canvas.delete("pen_indicator")  # 清除之前的指示点
        pensize = int(value)
        x = 100  # 指示点的横坐标
        y = 50  # 指示点的纵坐标
        radius = pensize / 2  # 指示点的半径

        canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                           fill=t.pencolor(), tags="pen_indicator")

    scale = tk.Scale(popup, from_=1, to=50, orient=tk.HORIZONTAL,
                     command=update_pensize)
    scale.set(t.pensize())
    scale.pack()
    button.pack()

    def on_closing(t):
        t.pensize(scale.get())
        popup.destroy()


def pen_up(frame, t):
    print("pen_up")
    t.penup()

    pass


def pen_down(frame, t):
    beginner(t)
    print("pendown")
    t.down()
    pass


def cancel(frame, t):
    beginner(t)
    print("cancel")

    pass


def clear(t):
    print("clear")
    t.clear()


def save(frame, t):
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
