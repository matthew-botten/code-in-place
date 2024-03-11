# drawing a patch quilt using CIP library and a bit of code from the CIP forum to draw a star

from graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
COLUMNS = 4
ROWS = 2
CANVAS_WIDTH = PATCH_SIZE * COLUMNS
CANVAS_HEIGHT = PATCH_SIZE * ROWS

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (x % 2 == 0) ^ ((y+1) % 2 == 0):
                draw_square_patch(canvas, PATCH_SIZE*x, PATCH_SIZE*y)
            else:
                draw_circle_patch(canvas, PATCH_SIZE*x, PATCH_SIZE*y)
    
    
def draw_circle_patch(canvas, start_x, start_y):
    # draws a salmon circle of PATCH_SIZE with the start coordinates top left
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, "salmon")

def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, "purple")
    # then draw a smaller white square on top
    canvas.create_rectangle(start_x+inset, start_y+inset, 
        end_x-inset, end_y-inset, 'white')

    """
    Drawing a star from the collaboration forum - very cool
    """
    star(canvas, start_x+PATCH_SIZE/2, start_y+PATCH_SIZE/2, 0.5, "red")

def star(canvas, cx, cy, scale, color):
    # cx, cy - coordinates for the point of origin
    # scale  - float, determines the size of the shape
    shape_template = [
        # List of polygon vertices x, y
        # Coordinates can be negative because the shape is described
        # with the point of origin at coordinates (0, 0)
        -50, -14,
        -12, -14,
        0, -50,
        12, -14,
        50, -14,
        19, 9,
        31, 45,
        0, 23,
        -31, 45,
        -19, 9
    ]
    # Adjust the shape coordinates: scale and translate
    i = 0
    while i < len(shape_template):
        shape_template[i] = cx + shape_template[i] * scale
        i += 1
        shape_template[i] = cy + shape_template[i] * scale
        i += 1
    # Add the shape to the canvas
    canvas.create_polygon(*shape_template, color=color)







if __name__ == '__main__':
    main()
