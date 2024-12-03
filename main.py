# Final Project
# By Nguyet Pham and Dowlah Ali
# CS 111, Summer 2024, Professor Reckinger
# Date worked: 07.22.2024
# Date finished: 07.31.2024
# Create an informative-based game about the Olympics

import turtle
import random
import math
import time

# Define global variables and/or turtles here
global currently_selected # Boolean that keeps track of what is currently selected
global sport # Boolean keeping track of what sport is chosen
global game
global medals_to_catch
global total_medals # the sum of bronze, silver, gold
global medals_count # Counting the medals that is collected 
global chosen_sport_name
global mascot

# Initialization of global variables
currently_selected = False
sport = False
game = False
chosen_sport_name = 'Sport'
total_medals = 0
medals_count = 0

# Initialization of global turtles
global start_label
start_label = turtle.Turtle()
start_label.penup()

def dict_conversion(afile):
    '''
    Open file and turn it into a dictionary with the first element in each element of the list as the key.
    '''
    alist = open(afile).readlines()
    adict = {}
    for i in range(1, len(alist)):
        # For each element in the list, split it into a new list.
        # The last element of the new list contains '\n', omit that.
        alist[i] = alist[i].split(',')
        alist[i][-1] = alist[i][-1][:-1]
        for j in range(len(alist[i][2:])):
            # change strings of number to integers
            alist[i][2 + j] = int(alist[i][2 + j])
        add = {alist[i][0]: alist[i][1:]}
        adict.update(add)

    return adict

def write_text():
    '''
    Write the text in Screen 1.
    No parameter, no return.
    '''
    
    file1 = open('general_info.txt').readlines()
    start_label.hideturtle()

    x = 0
    y = 130
    start_label.goto(x, y)
    start_label.color('white')
    for line in file1:
        start_label.write(f"{line}", False, align = "center", font = ('Times New Roman', 15, "bold"))
        y -= 20
        start_label.goto(x, y)

def draw_start():
    '''
    Screen 1 that informs and inspires user of women Olympics and gets the user
    to click the button to begin, switches to another screen.
    No parameter, no return.
    '''

    write_text()

    # start box width, height
    box_width = 250
    box_height = 60
    
    start_label.goto(-125, -200)
    start_label.setheading(0)
    start_label.fillcolor("black")
    start_label.pendown()
    start_label.begin_fill()
    start_label.forward(box_width)
    start_label.right(90)
    start_label.forward(box_height)
    start_label.right(90)
    start_label.forward(box_width)
    start_label.right(90)
    start_label.forward(box_height)
    start_label.penup()
    start_label.end_fill()

    start_label.goto(0, -240)
    start_label.color("white")
    start_label.write(f"LET'S GO!", False, align = "center", font = ('Times New Roman', 15, "bold"))
    start_label.hideturtle()

def check_click(x, y):
    '''
    Checks the user's click on the start button that leads to switching to the second screen
    that gets the user to choose one of the four sports in the Olympics.
    Parameters x and y is the coordinate of the click.
    No return.
    '''

    global currently_selected
    global sport
    global game
    global chosen_sport_name

    print(x, y)
    start_label.hideturtle()
    start_label.penup()
    start_label.goto(x, y)
    start_label.showturtle()

    # Check if the click is within the "LET'S GO!" button coordinate range/area
    width2 = 250
    height2 = 60
    start_x = -125
    start_y = -200
    height3 = 70
    width3 = 400

    # go to screen 2
    if (start_x <= x <= (start_x + width2)) and ((start_y - height2) <= y <= (start_y)):
        if not currently_selected:
            currently_selected = True
            choose_a_sport()

    # go to screen 3
    elif ((-500 <= x <= (-500 + width3)) and ((0 - height3) <= y <= 0)): # swimming
        if not sport: # to check that user won't be able to click on that again
            sport = True
            chosen_sport('swimming_olympics.txt')
            chosen_sport_name = 'Swimming'

    elif ((-500 <= x <= (-500 + width3)) and ((-160 - height3) <= y <= -160)): # figure skating
        if not sport: # to check that user won't be able to click on that again
            sport = True
            chosen_sport('figure_skating_olympics.txt')
            chosen_sport_name = 'Figure Skating'

    elif ((100 <= x <= (100 + width3)) and ((0 - height3) <= y <=  0)): # gymnastics
        if not sport: # to check that user won't be able to click on that again
            sport = True
            chosen_sport('gymnastics_olympics.txt')
            chosen_sport_name = 'Gymnastics'

    elif ((100 <= x <= (100 + width3)) and ((-160 - height3) <= y <= -160)): # tennis
        if not sport: # to check that user won't be able to click on that again
            sport = True
            chosen_sport('tennis_olympics.txt')
            chosen_sport_name = 'Tennis'

    # go to screen 4
    elif ((-150 <= x <= (-150 + 300)) and ((300 - 60) <= y <= 300)):
        if not game:
            game = True
            play_game()

def choose_a_sport():
    '''
    Screen 2 that gets the user to choose one of the four sports in the Olympics.
    No parameter, no return.
    '''
    s.clearscreen()
    s.bgcolor("midnight blue")

    start_label.speed(0)

    # choose the sport text
    start_label.goto(-300, 100)
    start_label.write('Choose a sport:', False, align = "right", font = ('Times New Roman', 25, "bold"))

    height = 70
    width = 400

    start_label.pencolor('white')
    
    # swimming label
    start_label.goto(-500, 0)
    start_label.fillcolor("gold")
    start_label.pendown()
    start_label.begin_fill()
    for i in range(2):
        start_label.right(90)
        start_label.forward(width)
        start_label.right(90)
        start_label.forward(height)
    start_label.penup()
    start_label.end_fill()
    start_label.goto(-300, -55)
    start_label.color("black")
    start_label.write('Swimming', False, align = "center", font = ('Times New Roman', 30, "bold"))

    # figure skating label
    start_label.goto(-500, -160)
    start_label.fillcolor("gold")
    start_label.pendown()
    start_label.begin_fill()
    for i in range(2):
        start_label.right(90)
        start_label.forward(width)
        start_label.right(90)
        start_label.forward(height)
    start_label.penup()
    start_label.end_fill()
    start_label.goto(-300, -215)
    start_label.color("black")
    start_label.write('Figure Skating', False, align = "center", font = ('Times New Roman', 30, "bold"))

    # gymnastics label
    start_label.goto(100, 0)
    start_label.fillcolor("gold")
    start_label.pendown()
    start_label.begin_fill()
    for i in range(2):
        start_label.right(90)
        start_label.forward(width)
        start_label.right(90)
        start_label.forward(height)
    start_label.penup()
    start_label.end_fill()
    start_label.goto(300, -55)
    start_label.color("black")
    start_label.write('Gymnastics', False, align = "center", font = ('Times New Roman', 30, "bold"))

    # tennis label
    start_label.goto(100, -160)
    start_label.fillcolor("gold")
    start_label.pendown()
    start_label.begin_fill()
    for i in range(2):
        start_label.right(90)
        start_label.forward(width)
        start_label.right(90)
        start_label.forward(height)
    start_label.penup()
    start_label.end_fill()
    start_label.goto(300, -215)
    start_label.color("black")
    start_label.write('Tennis', False, align = "center", font = ('Times New Roman', 30, "bold"))

    s.onclick(check_click)

def chosen_sport(sport_name):
    '''
    Screen 3 that shows the user general info about chosen sport and its top women.
    Parameter sport_name is the text file that will be converted to a dictionary.
    No return.
    '''

    global medals_to_catch
    global chosen_sport_name
    global total_medals
    global medals_count

    s.clearscreen()
    s.bgpic('screen3.gif')

    t = turtle.Turtle()
    t.hideturtle()
    t.penup()

    dict1 = dict_conversion(sport_name)

    x = 0
    y = 75
    t.goto(x, y)
    t.pencolor('white')
    script = f"{chosen_sport_name} has long been one of the top sport for Olympics female participants\nspecifically and for many sporting competitions in general.\nRight here you can see the top 4 women who won the most number of all medals:"
    t.write(script, False, align = "center", font = ('Times New Roman', 20, 'bold'))

    # draw a table
    t.speed(10)
    x = -500
    y = 20
    t.goto(x, y)
    t.right(90)
    width3 = 1020
    height3 = 275
    num_column = 4
    t.pensize(3)
    t.pendown()
    for i in range(2):
        t.forward(height3)
        t.left(90)
        t.forward(width3)
        t.left(90)
    t.penup()

    # display top women in the sport
    x = -475
    y = -25
    start_label.goto(x, y)
    dict2 = {'Name': ['Country', 'All Medals', 'Gold', 'Bronze', 'Silver']}
    dict2.update(dict1)
    dict1.clear()
    dict1.update(dict2)
    start_label.pencolor('white')
    
    for name in dict1:

        start_label.write(f'{name}', False, align = "left", font = ('Times New Roman', 15, 'bold'))
        start_label.goto(x + 230, y)

        for j in range(len(dict1[name])):
            start_label.write(f'{dict1[name][j]}', False, align = "left", font = ('Times New Roman', 15, 'bold'))
            x += 130
            start_label.goto(x + 380, y)
        x -= 130 * 5
        y -= 50
        start_label.goto(x, y)
    del dict1['Name']

    # create the list for number of medals
    x1 = 0 # gold
    y1 = 0 # silver
    z1 = 0 # bronze
    for i in dict1:
        x1 += dict1[i][2]
        y1 += dict1[i][3]
        z1 += dict1[i][4]
    medals_to_catch = [x1, y1, z1]
    total_medals = x1 + y1 + z1
    medals_count = total_medals

    # play a game box
    height_box = 60
    width_box = 300
    t.goto(150, 300)
    t.pencolor('white')
    t.fillcolor('white')
    t.left(90)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.right(90)
        t.forward(height_box)
        t.right(90)
        t.forward(width_box)
    t.goto(-150, 300)
    t.end_fill()
    t.penup()
    t.goto(0, 255)
    t.pencolor('black')
    t.write('Let\'s play a game', False, align = "center", font = ('Times New Roman', 20, 'bold'))

    s.onclick(check_click)

def check():
    '''
    Every time the user press key, check if the mascot has touched any medal. If it did, hide the turtle medal.
    If there is no more medals to catch, user wins.
    No parameter, no return.
    '''
    global total_medals
    global medals_count

    # You won
    if medals_count == 0: # Checks if medals is not an empty list, medals is list of turtles 
        s.clearscreen()
        s.bgcolor("light green")
        start_label.goto(0, 0)
        start_label.write("You won!", False, align='center', font=('Comic Sans MS', 60))
        turtle.done()
        return
    
    for i in range(len(medals)):
        if (mascot.distance(medals[i].xcor(), medals[i].ycor()) < 50 and medals[i].isvisible()):
            medals[i].hideturtle()
            # medals.remove(medals[i])
            medals_count -= 1

def up():
    mascot.setheading(90)
    mascot.forward(10)
    check()

def down():
    mascot.setheading(270)
    mascot.forward(10)
    check()

def left():
    mascot.setheading(180)
    mascot.forward(10)
    check()

def right():
    mascot.setheading(0)
    mascot.forward(10)
    check()

def play_game():
    '''
    Screen 4: Mascot catches the medals. Number of medals differs by the sport.
    No parameter,  no return.
    '''

    global mascot
    global medals
    
    s.clearscreen()
    s.bgpic('background.gif')

    turtle.addshape('game_mascot.gif')
    turtle.addshape('gold.gif')
    turtle.addshape('silver.gif')
    turtle.addshape('bronze.gif')

    medals = []
    for i in range(medals_to_catch[0]):
        gold = turtle.Turtle()
        gold.shape('gold.gif')
        gold.penup()
        medals.append(gold)

    for i in range(medals_to_catch[1]):
        silver = turtle.Turtle()
        silver.shape('silver.gif')
        silver.penup()
        medals.append(silver)

    for i in range(medals_to_catch[2]):
        bronze = turtle.Turtle()
        bronze.shape('bronze.gif')
        bronze.penup()
        medals.append(bronze)
    
    print(medals)
    random.shuffle(medals)
    for i in range(len(medals)):
        medals[i].goto(random.randint(-600, 600), random.randint(-300, 300))

    mascot = turtle.Turtle()
    mascot.shape('game_mascot.gif')
    mascot.penup()
    mascot.goto(0, 0)

    s.listen()
        
    s.onkey(up, "Up")
    s.onkey(down, "Down")
    s.onkey(left, "Left")
    s.onkey(right, "Right")

    s.mainloop()

# Main 
# Set up screen
turtle.hideturtle()
s = turtle.Screen()
s.title("Summer 2024 Olympics")     # Change the window title
s.bgcolor("pink")
# turtle.tracer(0)
draw_start() # draws start button
#s.listen()
s.onclick(check_click) # another function check 
# turtle.update()
s.mainloop()  # This will make sure the program continues to run 