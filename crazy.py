import tkinter as tk
import pygetwindow as gw
import win32gui
import time
import threading

def move_window_loop(hwnd):
    for _ in range(100):
        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0], rect[1]
        width = rect[2] - rect[0]
        height = rect[3] - rect[1]
        win32gui.MoveWindow(hwnd, x - 5, y, width, height, True)
        time.sleep(0.01)

def start():
    root = tk.Tk()
    root.title("MyCustomWindow")

    # Launch animation in separate thread so it doesn't block UI
    def animate():
        time.sleep(1)  # Give time for window to be fully created
        win = gw.getWindowsWithTitle("MyCustomWindow")[0]
        move_window_loop(win._hWnd)

    threading.Thread(target=animate, daemon=True).start()
    root.mainloop()

start()
