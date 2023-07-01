import tkinter as tk

# 创建窗口
window = tk.Tk()

# 设置窗口初始大小
window.geometry("200x200")

# 定义窗口变大的目标大小
target_width = 400
target_height = 400

# 定义初始步长
initial_step = 20


# 定义一个函数，在指定时间后调用，实现窗口变大的效果
def increase_window_size(k, x, y):
    current_width = window.winfo_width()
    current_height = window.winfo_height()
    if x - current_height > 1 or current_height - y > 1:
        new_width = current_width + (x - current_width) // k
        new_height = current_height + (y - current_height) // k
        window.geometry(f"{new_width}x{new_height}")
        # 递归调用，并逐渐减小步长的值，实现减速变化的效果
        window.after(1, increase_window_size, k, x, y)
    else:
        return


# 调用函数开始窗口变大的动画效果
increase_window_size(100, 600, 800)

# 运行窗口主循环
window.mainloop()
