from pyautogui import *
import pywinctl as wc
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller

mouse = Controller()


def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)


def check_star(r, g, b):
    return (
        b in range(0, 125) and
        r in range(102, 220) and
        g in range(200, 255)
    )


window_name = input('\n[✅] | Enter window name (default=TegegramDesktop): ')

if window_name == '':
    window_name = 'TelegramDesktop'

check = wc.getWindowsWithTitle(window_name)
if not check:
    print(f'[❌] | Window - {window_name} not found!')
    raise Exception("Window not found!")
else:
    print(f'[✅] | Window found - {window_name}')
    print('[✅] | Press "q" for toggle.')
telegram_window = check[0]
paused = True

while True:
    if keyboard.is_pressed('q'):
        paused = not paused
        if paused:
            print('[✅] | Paused.')
        else:
            print('[✅] | Continued.')
        time.sleep(0.1)
    if paused:
        continue

    window_rect = (
        telegram_window.left,
        telegram_window.top,
        telegram_window.width,
        telegram_window.height
    )

    if telegram_window != []:
        try:
            telegram_window.activate()
        except Exception:
            telegram_window.minimize()
            telegram_window.restore()

    screen = pyautogui.screenshot(
        region=window_rect
    )

    width, height = screen.size
    pixel_found = False
    if pixel_found:
        break

    # click(width, height - 101)  # Press "Play again"

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = screen.getpixel((x, y))
            if check_star(r, g, b):
                screen_x = window_rect[0] + x
                screen_y = window_rect[1] + y
                click(screen_x + 4, screen_y)
                time.sleep(0.001)
                pixel_found = True
                break
