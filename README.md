# README
# stbobdctm = St Bernards Old Boys Diveristy Council Technology and Mentoring - 6/5/21 Session- Getting started with the Micro:bit

This repo contains the scripts used to introduce the participating students to practical programming concepts with microcotnrollers (a Micro:bit).  Some are original code while others are borrowed from the Microbit main site. Here is the order and approach to using this repo.

## Prerequisite Principals to explore (covered in live session)
1. Microcontroller Principals

    1. Inputs
    2. Outputs
    3. Were Microcontrollers are differeent and useful compared to things like raspberry pi/computers
 
1. Programming Principals:

    1. Delays
    2. Loops (while and for)
    3. If statements
    4. Lists and Arrays
    
1. Other Concepts:

    1. Reading the docs (like real developers) - https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html
    2. Using feedback to keep things interesting for your user (like the display)  

## Script order, usage, and concepts
1. Get Started Set up

    1. Getting Started
        1. Go to https://python.microbit.org/v/2
        2. plug in Microbit into USB port
        3. wait until the microbit is recognized (should be a few seconds)
        4. Click Connect icon
            1. A popup will appear and there should be a microbit available
            2. select the microbit and click connect
            3. the icon should be change to Disconnect
        5. Test your ability to flash your microbit and write your first program
            1. The code will show an area that says "Hello World".  No...its YOUR microbit.  It should say hello to you.  Change "world" to your name
            2. Click Flash
            3. A window will pop up, with a warning about the first flash taking the longest time
            4. A bar will appear showing you the progress, and you microbit's yellow LED will start flashing
            5. When done, you should see "Hello <Your Name>"
            6. Celebrate!
    2. Let's edit some code
         1. While Loop == True and why it's important (hint: forever loop, and how to shut it down)
         2. What else do you want it to say?
2. Intro to pseudocode
    1. what is pseudocode
    2. how does it help us
    3. how do you do it?
3. Using our outputs - the Display
    1. So we have this display.  we can make pictures and animations
          1. You can type in letters or make pictures
    2. Pixel manipulation
          1. Fill display
                1. What do you think it would take to fill the display?
                2. Let's understand arrays a bit
                3. Pseudocode the application
                4. Check out [fill_up_display.py](fill_up_display.py)
          2. Single dot
                1. Timing control: Controlling the led with timing
                2. Check out [single_dot.py](single_dot.py)
          3. Boat animation
                1. Let's expore the docs on how to make animations
                2. You can represent the values of your leds in this 5x5 matrix. 
                3. You can express scenes as lists of lists and use delays to make the animation faster or sllower
                4. [boat.py](boat.py)
		3. Adding inputs
			    1. Buttons
            1. Boat on button animation
              1. Turn to docs on buttons
              2. have class describe to me how it works
              3. code it or check out [boat_on_button](boat_on_button.py)

          2. Compass
            1. Magnetism as in input
              1. Google "mems sensors", to understand how these components work and help your microcontroller 
              2. How do you think we can show a compass on such a small screen? (hint: in your class, there is something that points to numbers in a big circle)
              3. Let's make pseudocode on how we can use it
              4. Check out code in [compass.py](compass.py)
              5. Let's understand how image groups be used to easily create visualizations
              6. Add your own comments to describe how it works
          3. Accelerometers and gyroscopes
            1. Tilt as an input
              1. describe a tilt sensing gyro
              2. Look up speed, velocity, and acceleration equations to understand how you can figure out one from the others
              3, Let's make pseudocode on how we can use it
              4. Check out code in [tilt_x.py](tilt_x.py)
              5. Add your own comments to describe how it works
            2. CODE ON YOUR OWN (15-20 minutes)
              1. Let's make a bubble level
              2. Check out [tilt_x.py](tilt_x.py) for an inspiration
              3. You can compare to [bubble_level.py](bubble_level.py)
          4. Optional/only for groups: comms and radios (you need multiple microbits for this to work)
            1. Understanding the Bluetooth radio
            2. Copy code for [firefly.py](firefly.py) and see how the microbits interact with each other
            3. Explain the behavior in your own words
            4. Try to get them to flash together faster.

