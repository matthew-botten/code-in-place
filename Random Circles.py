# draws some random circles using a specific library from CIP

from graphics import Canvas
import random
from time import sleep


CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500


def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circles(canvas)


def draw_random_circles(canvas):
    # random number of circles
    number_circles = random.randint(5,200)
    
    # draws a random circle N_CIRCLE times
    for i in range(number_circles):
        """
        each circle has a random size
        increments of 2 so size is even so the coordinates are integers
        """
        circle_size = random.randrange(6, 60, 2)
        
        # working out the range for the possible coordinates of the centre of the circle so it is completely inside the canvas
        minimum_x = 0 + circle_size/2
        minimum_y = 0 + circle_size/2
        maximum_x = CANVAS_WIDTH - circle_size/2
        maximum_y = CANVAS_HEIGHT - circle_size/2
        
        # generates a random coordinate for the centre and a random colour
        x = random.randint(minimum_x, maximum_x)
        y = random.randint(minimum_y, maximum_y)
        colour = random_colour()
        
        # draw the circle using the function we created
        sleep(0.01)
        draw_circle(canvas, x, y, circle_size, colour)


# draw a circle given its centre coordinates, size, and colour
def draw_circle(canvas, centre_x, centre_y, size, colour):
    #finds each corner of the circle given its centre and size
    top_x = centre_x - size/2
    top_y = centre_y - size/2
    bottom_x = centre_x + size/2
    bottom_y = centre_y + size/2
    canvas.create_oval(top_x, top_y, bottom_x, bottom_y, colour)


# generates a random colour from an array
def random_colour():
    colours = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen', 'black', 'red', 'yellow', 'pink', 'brown', 'dodgerblue', 'magenta', 'lightgreen', 'lime']
    return random.choice(colours)



if __name__ == '__main__':
    main
