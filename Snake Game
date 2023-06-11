# colour changing snake game using the graphics library from CIP

from graphics import Canvas
from time import sleep
import random
    
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
SIZE = 20
FONT_SIZE = 50

#Bounds for the colours (within 0-255)
DARKEST = 96
LIGHTEST = 255
#Change in colour is random with range 1 to CHANGE
CHANGE = 20

def main():
    #setup variables
    variables = {
        "delay": 0.2,
        "direction": [1,0],
        "score" : 0,
        "colours": [[LIGHTEST,LIGHTEST,LIGHTEST]],
        "colour_change": [-1,-1,-1],
        "colour" : "#ffffff"
    }
    #setup initial canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0,0,CANVAS_WIDTH, CANVAS_HEIGHT) #background
    score_display = canvas.create_text(0,CANVAS_HEIGHT-FONT_SIZE, font_size=FONT_SIZE, text="Score: "+str(variables["score"]), color="#CBA92B") #score text
    goal = canvas.create_rectangle(200, 200, 200 + SIZE, 200 + SIZE, "#CBA92B") #goal
    player = [canvas.create_rectangle(0,0, 0+SIZE, 0+SIZE, variables["colour"])] #head of snake
    
    canvas.wait_for_click()
    #repeating each move
    while True:
        # try to move the player
        if not(move_possible(canvas, player, variables)):
            # if moving was unsuccessful then game over and break the loop
            game_over(canvas, player)
            break
        else:
            move(canvas, player, variables)
        
        #checking if scored a goal
        check_goal(canvas, player, goal, variables, score_display)
        
        
        sleep(variables["delay"])    






""""""
def move_possible(canvas, player, variables):
    # input from player
    key = canvas.get_last_key_press()
    
    if key == "ArrowLeft" and (variables["direction"] != [1,0] or len(player)==1):
        variables["direction"] = [-1,0]
        
    if key == "ArrowRight" and (variables["direction"] != [-1,0] or len(player)==1):
        variables["direction"] = [1,0]
        
    if key == "ArrowUp" and (variables["direction"] != [0,1] or len(player)==1):
        variables["direction"] = [0,-1]
        
    if key == "ArrowDown" and (variables["direction"] != [0,-1] or len(player)==1):
        variables["direction"] = [0,1]
    
    # check if the head of the snake moves in this direction will it be out of bounds
    if not(within_bounds(canvas, player, variables)):
        # if not within bounds of canvas then don't move, so stop the function and return false
        return False
    
    # check if the head of the snake moves in this direction will it collide with itself
    if overlapping_tail(canvas, player, variables):
        return False

    return True


""""""
def move(canvas, player, variables):
    # moving each segment to the one in front, from the back of the snake
    for i in range(len(player), 1, -1):
        x,y = position(canvas, player[i-2])
        canvas.moveto(player[i-1], x, y) 
    
    #move the head in the player inputted direction
    canvas.move(player[0], SIZE*variables["direction"][0], SIZE*variables["direction"][1])
    
    # changing colours:
    update_colours(canvas, player, variables)


""""""
def within_bounds(canvas, player, variables):
    # check if the head of the snake will be in the bounds of the canvas after moving
    positions = player_position(canvas, player)
    p_x = positions[0][0] + SIZE*variables["direction"][0]
    p_y = positions[0][1] + SIZE*variables["direction"][1]
    x_bound = (p_x >= 0) and (p_x+SIZE <= CANVAS_WIDTH)
    y_bound = (p_y >= 0) and (p_y+SIZE <= CANVAS_HEIGHT)
    
    if not(x_bound and y_bound):
        return False
    return True


""""""
def overlapping_tail(canvas, player, variables):
    # calculate position of head if it moves
    positions = player_position(canvas, player)
    p_x = positions[0][0] + SIZE*variables["direction"][0]
    p_y = positions[0][1] + SIZE*variables["direction"][1]
    
    overlapping = canvas.find_overlapping(p_x, p_y, p_x+SIZE, p_y+SIZE)
    for segment in player:
        for element in overlapping:
            if segment == element:
                return True
    return False


""""""
def check_goal(canvas, player, goal, variables, score_display):
    positions = player_position(canvas, player)
    on_goal = positions[0][0] == canvas.get_left_x(goal) and positions[0][1] == canvas.get_top_y(goal)
    
    if on_goal:
        variables["score"] += 1
        canvas.change_text(score_display, "Score: "+str(variables["score"]))
        variables["delay"] = round(variables["delay"]*0.9, 5)
        
        goal_x = random.randint(1,(CANVAS_WIDTH/SIZE)-2)*SIZE
        goal_y = random.randint(1,(CANVAS_HEIGHT/SIZE)-2)*SIZE
        canvas.moveto(goal, goal_x, goal_y)
        
        extra_colour = variables["colours"][-1].copy()
        update_colours(canvas, player, variables)
        variables["colours"].append(list(extra_colour))
        
        player.append(canvas.create_rectangle(positions[-1][0],positions[-1][1], positions[-1][0]+SIZE, positions[-1][1]+SIZE, convert_colour(extra_colour)))
    return score_display

""""""
def update_colours(canvas, player, variables):
    for i in range(len(player), 1, -1):
        colour = variables["colours"][i-2].copy()
        variables["colours"][i-1] = colour
        canvas.set_color(player[i-1], convert_colour(colour))
    new_colour(variables["colours"][0], variables["colour_change"])
    canvas.set_color(player[0], convert_colour(variables["colours"][0]))
""""""
def game_over(canvas, player):
    for i in range(len(player)):
        canvas.set_color(player[i], "red")
        canvas.set_outline_color(player[i], "salmon")
    canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2, font_size=98, text="GAME OVER", color="white", anchor="center")

""""""
def position(canvas, element):
    return canvas.get_left_x(element), canvas.get_top_y(element)

""""""
def player_position(canvas, player):
    positions = []
    for i in range(len(player)):
        positions.append(position(canvas, player[i]))
    return positions

"""
the colours array for each segment of the player is three integers that are the RBG components of the colour
variables["colours"] = [[red, green, blue], etc.]

the change array dictates whether the component of colour is increasing or decreasing
variables["colour_change"] = [+/-1, +/-1, +/-1]

variables["colour"] is a string with a hex colour such as #2f14b5


this function changes the colour by incrementing it slowly
each RBG component by a different random amount so it isn't just shades of gray
the colour is kept within bounds so it doesn't get too dark or light
"""
def new_colour(colours, colour_change):
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
""""""
def convert_colour(colours):
    # converts an array of rbg values into a 7 digit hex string for the canvas functions
    return "#"  +  "%02x%02x%02x" % (colours[0],colours[1],colours[2])

########  
if __name__ == '__main__':
    main()
