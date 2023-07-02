import tkinter as tk

def update_pensize(value):
    canvas.delete("pen_indicator")  # 清除之前的指示点

    pensize = int(value)
    x = 50  # 指示点的横坐标
    y = 50  # 指示点的纵坐标
    radius = pensize / 2  # 指示点的半径

    canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                       fill="black", tags="pen_indicator")

root = tk.Tk()

scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL,
                 command=update_pensize)
scale.pack()

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()

root.mainloop()
