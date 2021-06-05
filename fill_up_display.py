# Add your Python code here. E.g.
from microbit import *

x=0
y=0
value = 5
while True:
    display.set_pixel(x, y, value)
    if(x<4):
        x=x+1
    else:
        x=0
        if(y<4):
            y=y+1
        else:
            display.clear()
            y=0
            
    # sleep(200) # Uncomment to see how changing timing changes the display
