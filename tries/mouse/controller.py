from pynput import mouse
from pynput.keyboard import Key, Controller

keyboard = Controller()

import numpy as np
import pandas as pd

def on_move(x, y):
    # print('Pointer moved to {0}'.format((x, y)))
    with open('imp.csv', 'a') as file:
        file.write('{},{}\n'.format(x, y))
    pass

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        # Stop listener
        # return False
        pass

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

with open('imp.csv', 'w') as file:
    file.write(','.join(['x', 'y']) + '\n')
    file.close()


# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()

# (topleft) -> (0, 0) to right and down
# def controlMouse():
#     mouse = Controller()
#     mouse.position = (300, 300)
#     mouse.scroll(0, 5)
#
# controlMouse()