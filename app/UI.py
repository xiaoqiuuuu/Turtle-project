# 创建了主界面


import tkinter as tk
from turtle import TurtleScreen
from MyButton import MyButton
from create import create
from template import template



if __name__ == "__main__":
    window = tk.Tk()

    # 设置窗口大小
    window.geometry("600x700")
    window.title("数字赋能美育，代码描绘美景")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口在屏幕上的位置
    x = int((screen_width - 1200) / 2)
    y = int((screen_height - 700) / 2) - 30

    # 设置窗口的位置
    window.geometry(f"+{x}+{y}")

    # 设置窗口大小为不可改变
    window.resizable(False, False)

    # 设置背景图片
    image = tk.PhotoImage(file="../material/picture/1.png")
    background_label = tk.Label(window, image=image)
    background_label.place(x=0, y=0)

    # 添加turtle 画布
    canvas = tk.Canvas(window, width=600, height=700)
    canvas.place(x=600, y=0)
    red = 138
    green = 189
    blue = 221
    screen = TurtleScreen(canvas)
    screen.bgcolor(f"#{red:02x}{green:02x}{blue:02x}")

    # 添加主界面功能按钮
    button1 = MyButton(window, "../material/picture/2.png", lambda:[create(window,screen)])
    button1.place(x=100, y=60)

    button2 = MyButton(window, "../material/picture/3.png", lambda:template(window,screen))
    button2.place(x=100, y=180)

    button3 = MyButton(window, "../material/picture/4.png",lambda :exit(0))
    button3.place(x=100, y=300)

    window.mainloop()

