import tkinter as tk
from turtle import TurtleScreen, RawTurtle

# 创建Tkinter窗口
window = tk.Tk()

# 创建Turtle画布并嵌入到窗口中
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

screen = TurtleScreen(canvas)
screen.bgcolor("white")

# 创建Turtle对象
turtle = RawTurtle(screen)

# 使用Turtle对象进行绘图
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# 启动Tkinter事件循环
window.mainloop()
