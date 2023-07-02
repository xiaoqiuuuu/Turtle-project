import tkinter as tk
from PIL import ImageTk, Image

# 创建主窗口
root = tk.Tk()

# 加载图像
image = Image.open("../material/picture/18.png")
photo = ImageTk.PhotoImage(image)

# 创建标签并显示图像
label = tk.Label(root, image=photo)
label.pack()

# 运行主循环
root.mainloop()
