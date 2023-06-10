# creates, smoothly changing colours, circles following the mouse using a CIP specific library

from graphics import Canvas
from time import sleep
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CIRCLE_SIZE = 30
DELAY = 0.002

#Bounds for the colours (within 0-255)
DARKEST = 64
LIGHTEST = 240
#Change in colour is random with range 1 to CHANGE
CHANGE = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    
    #set up for changing colours, explained further in the function at the end
    colours = [LIGHTEST,LIGHTEST,LIGHTEST]
    colour_change = [1,1,1]
    colour = "#000000"
    #
    
    
    while True:
        # get the mouse x and y coordinates
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        
        # boolean variables to check if the mouse coordinates are on the canvas
        # also makes the if statement cleaner
        valid_x = (mouse_x >= 0 + CIRCLE_SIZE/2) and (mouse_x <= CANVAS_WIDTH - CIRCLE_SIZE/2)
        valid_y = (mouse_y >= 0 + CIRCLE_SIZE/2) and (mouse_y <= CANVAS_HEIGHT - CIRCLE_SIZE/2)
        if valid_x and valid_y:
            
            
            # you can ignore this line, it calls the function to change the colour
            colours, colour_change, colour = update_colour(colours, colour_change, colour)
            
            
            # if both coordinates are valid then draw a circle
            # draws a circle with the mouse as the centre
            canvas.create_oval(
                mouse_x - CIRCLE_SIZE/2,
                mouse_y - CIRCLE_SIZE/2,
                mouse_x + CIRCLE_SIZE/2,
                mouse_y + CIRCLE_SIZE/2, 
                colour)
        
        # wait a short while so the code runs smoothly
        sleep(DELAY)

"""
you can ignore this code it was just for fun

the colours array is three integers that are the RBG components of the colour
colours = [red, green, blue]

the change array dictates whether the component of colour is increasing or decreasing
colour_change = [+/-1, +/-1, +/-1]

colour is a string with a hex colour such as #2f14b5


this function changes the colour by incrementing it slowly
each RBG component by a different random amount so it isn't just shades of gray
the colour is kept within bounds so it doesn't get too dark or light
"""
def update_colour(colours, colour_change, colour):
    # increments the R G and B parts of the hex colour by a random amount
    colours[2] += colour_change[2]*random.randint(1,CHANGE)
    colours[1] += colour_change[1]*random.randint(1,CHANGE)
    colours[0] += colour_change[0]*random.randint(1,CHANGE)
    """
    if the colour gets too dark or too light then reset it to within the bounds
    and change the direction of change, for example from increasing to decreasing
    """
    if colours[0] < DARKEST:
        colours[0] = DARKEST
        colour_change[0] = -colour_change[0]
    elif colours[0] > LIGHTEST:
        colours[0] = LIGHTEST
        colour_change[0] = -colour_change[0]
    
    if colours[1] < DARKEST:
        colours[1] = DARKEST
        colour_change[1] = -colour_change[1]
    elif colours[1] > LIGHTEST:
        colours[1] = LIGHTEST
        colour_change[1] = -colour_change[1]
    
    if colours[2] < DARKEST:
        colours[2] = DARKEST
        colour_change[2] = -colour_change[2]
    elif colours[2] > LIGHTEST:
        colours[2] = LIGHTEST
        colour_change[2] = -colour_change[2]


    # format the array of the colours to hex in a string
    # so it can be used in the create_oval function
    colour = "#"  +  "%02x%02x%02x" % (colours[0],colours[1],colours[2])
    return colours, colour_change, colour



if __name__ == "__main__":
    main()
