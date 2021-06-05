# Add your Python code here. E.g.
from microbit import *

x=0
y=0
value = 5 # you can increase to be brighter

while True:
    display.set_pixel(x, y, value) # set current pixel to brightness value
    
    # Save the current x and y values
    xl=x
    yl=y
    
    # Alows time for pixel to be visible
    sleep(200)
    
    # keep dot within 5x5 array
    if(x<4):
        x=x+1
    else:
        x=0
        if(y<4):
            y=y+1
        else:
            display.clear()
            y=0
    display.set_pixel(xl, yl, 0) # set last used pixel to 0
