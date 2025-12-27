from machine import Pin
from time import sleep

button_a = Pin(32, Pin.IN, Pin.PULL_UP)
button_b = Pin(33, Pin.IN, Pin.PULL_UP)
button_x = Pin(25, Pin.IN, Pin.PULL_UP)
button_y = Pin(26, Pin.IN, Pin.PULL_UP)

count = 0

while True:
#     print(f"Button Status, A: {button_a.value()}, B: {button_b.value()}, X: {button_x.value()}, {count}")
    if button_a.value() == 0:
        print("button A pressed")
    if button_b.value() == 0:
        print("button B pressed")
    if button_x.value() == 0:
        print("button X pressed")
    if button_y.value() == 0:
        print("button Y pressed")
    sleep(0.01)
    count += 1