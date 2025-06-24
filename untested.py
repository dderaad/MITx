import pygame
import time
import threading
import pygetwindow as gw
import win32gui

# 1. Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("MyPygameWindow")

# 2. Function to move the window
def move_pygame_window():
    time.sleep(1)  # Give the window time to appear
    win = gw.getWindowsWithTitle("MyPygameWindow")[0]
    hwnd = win._hWnd

    for _ in range(100):
        x, y = win.topleft
        win32gui.MoveWindow(hwnd, x - 5, y, win.width, win.height, True)
        time.sleep(0.01)
        # Update window object (since MoveWindow doesn't update `win`'s coords automatically)
        win = gw.getWindowsWithTitle("MyPygameWindow")[0]

# 3. Run window movement in a separate thread
threading.Thread(target=move_pygame_window, daemon=True).start()

# 4. Pygame event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()
