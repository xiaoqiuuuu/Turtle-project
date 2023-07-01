import tkinter as tk
from Myturtle import *
from turtle import TurtleScreen

if __name__ == "__main__":
    window = tk.Tk()

    # 设置窗口大小
    window.geometry("1200x700")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口在屏幕上的位置
    x = int((screen_width - 1200) / 2)
    y = int((screen_height - 700) / 2)

    # 设置窗口的位置
    window.geometry(f"+{x}+{y}")

    # 设置窗口大小为不可改变
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=600, height=700)
    canvas.pack(side=tk.RIGHT)

    screen = TurtleScreen(canvas)
    screen.bgcolor("white")

    # 创建Turtle对象
    myturtle = Myturtle(screen)

    window.mainloop()
