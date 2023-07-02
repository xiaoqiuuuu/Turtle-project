# 写了一个Button ，可以根据图片调整大小

import tkinter as tk
from tkinter import ttk


class MyButton(ttk.Button):
    def __init__(self, windows, image_path , command = None):
        ttk.Button.__init__(self, windows, style="Transparent.TButton",command = command )

        style = ttk.Style()
        red = 138
        green = 189
        blue = 221
        style.configure("Custom.TButton", background=f"#{red:02x}{green:02x}{blue:02x}" , focuscolor='none' ,radius = 200)
        self.image = tk.PhotoImage(file=image_path)
        self.configure(image=self.image , style= "Custom.TButton")



if __name__ == "__main__":
    window = tk.Tk()
    button = MyButton(window, "../material/picture/2.png")
    button.pack()
    window.mainloop()
