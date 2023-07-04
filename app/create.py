# 实现 自由创作的功能

from time import *
from animation import *
from Myturtle import Myturtle
from MyButton import MyButton
import tkinter as tk
from drawfunc import *


def des_frame(window, frame, t):
    ender(t)
    frame.destroy()
    window.geometry("600x700")
    window.update()

    t.clear()
    t.screen.resetscreen()
    t.__del__()


def add_Keyframe(window, t):
    red = 69
    green = 149
    blue = 199

    frame = tk.Frame(window, width=600, height=700, bg=f"#{red:02x}{green:02x}{blue:02x}")
    frame.place(x=0, y=0)

    frame.config(bg=f"#{red:02x}{green:02x}{blue:02x}")

    # 添加功能 按钮
    button1 = MyButton(frame, "../material/picture/6.png")
    button1.place(x=50, y=20)
    button = [button1]
    for i in range(7, 12):
        j = i - 6
        button.append(MyButton(frame, f"../material/picture/{i}.png"))
        button[-1].place(x=50 + (j % 2) * 300, y=20 + (j // 2) * 150)

    for i in range(12, 18):
        j = i - 10
        button.append(MyButton(frame, f"../material/picture/{i}.png"))
        button[-1].place(x=50 + (j % 2) * 300, y=380 + (j // 2) * 80)
    button[-1].config(command=lambda: des_frame(window, frame, t))

    button.append(MyButton(frame, "../material/picture/28.png"))
    # button[-1].place(x=50, y=460)
    button.append(MyButton(frame, "../material/picture/29.png"))
    button[-1].place(x=350, y=460)

    # 添加功能按钮对应的选择功能
    func = [lambda: move(frame, t), lambda: rotate(frame, t), lambda: Circle(frame, t),
            lambda: fill(frame, t), lambda: pen_color(frame, t), lambda: pen_size(frame, t),
            lambda: pen_up(frame, button[-2], button[-1], t), lambda: pen_down(frame, button[-2], button[-1], t),
            lambda: cancel(frame, t),
            lambda: clear(t), lambda: save(frame, t), lambda: des_frame(window, frame, t),
            ]
    for i in range(0, 12):
        button[i].config(command=func[i])


def create(window, screen):
    t = Myturtle(screen)
    # 绘制党旗红色背景
    # 设置画笔颜色为红色，后期填充也是红色
    try:
        t.color("white")
    except:
        print(a)
        del t
        return

    # 左边是一个frame
    add_Keyframe(window, t)
    increase_window_size(window, 20, 1200, 0)

    welcome(t)
