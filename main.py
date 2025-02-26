import base64
import os
from logo import img
from pynput import mouse
import time
import random
import tkinter as tk
from tkinter import scrolledtext
import threading

# 创建主窗口
root = tk.Tk()
root.title("CxReadTime")
root.configure(bg='gray')
root.geometry("350x90")

# 创建图标
icon = open("gui.ico", "wb+")
icon.write(base64.b64decode(img))
icon.close()
root.iconbitmap("gui.ico")
os.remove("gui.ico")

# 创建内容打印框
text_area = scrolledtext.ScrolledText(root, width=50, height=5, bg='gray',font=('Arial', 12), fg='white', state='disabled')
text_area.pack(pady=0)

def mouse_scoll(text_area, root):
    while True:
        up_time = random.randint(3, 15)
        down_time = random.randint(3, 15)
        up_length = random.randint(500, 3000)
        down_length = random.randint(-3000, -500)
        up_duration = random.randint(3,15)
        down_duration = random.randint(3,15)
        times = random.randint(0,1)
        if times == 0:
            print(up_time, "秒后,在",up_duration,"秒内上移", up_length, "个像素点")
            for i in range(up_time, 0, -1):
                text_area.config(state='normal', font=('Arial', 12))
                text_area.delete('1.0', tk.END)
                text_area.insert(tk.INSERT, f"{i}秒后,在{up_duration}秒内上移{up_length}个像素点\n")
                text_area.config(state='disabled')
                root.update()
                time.sleep(1)
            with mouse.Controller() as mouse_controller:
                mouse_controller.scroll(0, up_length)
            print(f"已执行上移{up_length}个像素点")
            text_area.config(state='normal', font=('Arial', 12))
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.INSERT, f"已执行上移{up_length}个像素点\n")
            text_area.config(state='disabled')
            root.update()
            time.sleep(1)
        else:
            print(down_time, "秒后,在秒",down_duration,"内下移", down_length, "个像素点")
            for i in range(down_time, 0, -1):
                text_area.config(state='normal', font=('Arial', 12))
                text_area.delete('1.0', tk.END)
                text_area.insert(tk.INSERT, f"{i}秒后,在{down_duration}秒内下移{down_length}个像素点\n")
                text_area.config(state='disabled')
                root.update()
                time.sleep(1)
            with mouse.Controller() as mouse_controller:
                mouse_controller.scroll(0, down_length)
            print(f"已执行下移{down_length}个像素点")
            text_area.config(state='normal', font=('Arial', 12))
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.INSERT, f"已执行下移{down_length}个像素点\n")
            text_area.config(state='disabled')
            root.update()
            time.sleep(1)

# 在单独的线程中运行 mouse_scoll 函数
thread = threading.Thread(target=mouse_scoll, args=(text_area, root))
thread.start()

# 运行主循环
root.mainloop()
