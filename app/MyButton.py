# 写了一个Button ，可以根据图片调整大小

import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk

class MyButton(ttk.Button):
    def __init__(self, windows, image_path , command = None):
        ttk.Button.__init__(self, windows,command = command )

        style = ttk.Style()
        red = 138
        green = 189
        blue = 221
        style.configure("Custom.TButton", background=f"#{red:02x}{green:02x}{blue:02x}")
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)
        self.configure(image=self.image )


if __name__ == "__main__":
    popup = tk.Tk()
    button = MyButton(popup, "../material/picture/18.png" , lambda:print("123123"))
    button.pack()
    popup.mainloop()
