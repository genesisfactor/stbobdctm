from microbit import *

while True:
    reading_x = accelerometer.get_x()
    if reading_x > 20:
        display.show("R")
    elif reading_x < -20:
        display.show("L")
    else:
        display.show("-")
