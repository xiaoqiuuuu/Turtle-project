from tkinter import *
import win32gui
from PIL import ImageGrab


# 然后是获取Canvas的实现
def CaptureScreen():
    HWND = win32gui.GetFocus()  # 获取当前窗口句柄
    rect = win32gui.GetWindowRect(HWND)  # 获取当前窗口坐标
    im = ImageGrab.grab(rect)  # 截取目标图像
    im.save("second.jpeg", 'jpeg')  # 前面一个参数是保存路径，后面一个参数是保存格式


root = Tk()
cv = Canvas(root, width=300, height=150)
cv.create_rectangle(10, 10, 50, 50)
cv.pack()
b = Button(root, text='截图', command=CaptureScreen)
b.pack()
mainloop()