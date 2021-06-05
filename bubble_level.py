from microbit import *
x=2
y=2
value = 5
while True:
    display.set_pixel(x, y, 0)
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 40 :
        x = 4
    elif reading_x > 10:
        x = 3
    elif reading_x < -40:
        x = 0 
    elif reading_x < -10:
        x = 1
    else:
        #display.show("+")
        x = 2
    if reading_y > 40 :
        y = 4
    elif reading_y > 10:
        y = 3
    elif reading_y < -40: #fun stuff to try - switch -40 with -10 and see what happens.  can you tell me why?
        y = 0 
    elif reading_y < -10:
        y = 1
    
    else:
        #display.show("+")
        y = 2
    display.set_pixel(x, y, value)
    sleep(20)
