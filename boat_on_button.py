# Add your Python code here. E.g.
from microbit import *

def play_boat():
    
    boat1 = Image("05050:"
                  "05050:"
                  "05050:"
                  "99999:"
                  "09990")
    
    boat2 = Image("00000:"
                  "05050:"
                  "05050:"
                  "05050:"
                  "99999")
    
    boat3 = Image("00000:"
                  "00000:"
                  "05050:"
                  "05050:"
                  "05050")
    
    boat4 = Image("00000:"
                  "00000:"
                  "00000:"
                  "05050:"
                  "05050")
    
    boat5 = Image("00000:"
                  "00000:"
                  "00000:"
                  "00000:"
                  "05050")
    
    boat6 = Image("00000:"
                  "00000:"
                  "00000:"
                  "00000:"
                  "00000")
    
    all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    display.show(all_boats, delay=200)

while True:
    if button_a.is_pressed():
        play_boat()
