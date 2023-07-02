# 实现UI窗口变大的动画
import cv2

def increase_window_size(window , k, x, flg):
    current_width = window.winfo_width()
    current_height = window.winfo_height()
    if flg >= 500 or x == current_width:
        window.geometry(f"{x}x{current_height}")
        return
    if x - current_width > 1:
        new_width = current_width + (x - current_width) // k + 5
        window.geometry(f"{new_width}x{current_height}")
        # 递归调用，并逐渐减小步长的值，实现减速变化的效果
        window.update()
        window.after(1, increase_window_size, window , k, x, flg + 1)


