from turtle import *

WALLCOL = "red"
TURTLECOL = "blue"
GOALCOL = "green"
WALLSIZE = 10
TURTLESIZE = 3
POOCOL = "brown"
POOSIZE = 5

def spot():
    tmppencol = pencolor()
    tmpfillcol = fillcolor()
    ht()
    speed(0)
    pencolor(POOCOL)
    fillcolor(POOCOL)
    begin_fill()
    circle(POOSIZE)
    end_fill()
    pencolor(tmppencol)
    fillcolor(tmpfillcol)
    st()
    speed(1)
def makefast():
    penup()
    ht()
    speed(0)
    goto(0,-300)
    pendown()
    pensize(WALLSIZE)
    pencolor(WALLCOL)

def makeslow():
    pendown()
    pensize(TURTLESIZE)
    pencolor(TURTLECOL)
    st()
    speed(1)
    shape("turtle")

def challenge0():
    #get to start
    makefast()
    left(90)
    penup()
    forward(20)
    pendown()
    #bottom line
    left(90)
    forward(205)
    right(90)
    #left line
    forward(450)
    right(90)
    #top line
    forward(450)
    right(90)
    #right line
    forward(205)
    pencolor(GOALCOL)
    forward(40)
    pencolor(WALLCOL)
    forward(205)
    right(90)
    #bottom line
    forward(205)
    penup()
    forward(20)
    right(90)
    pendown()
    #bottom wall
    penup()
    goto(240,-100)
    left(90)
    pendown()
    forward(150)
    #return to start
    penup()
    goto(20,-300)
    right(90)
    makeslow()

def challenge1():
    #get to start
    makefast()
    left(90)
    penup()
    forward(20)
    #bottom line pt1
    pendown()
    left(90)
    forward(205)
    #left wall
    right(90)
    forward(450)
    #top wall pt1
    right(90)
    forward(205)
    #goal
    pencolor(GOALCOL)
    forward(40)
    pencolor(WALLCOL)
    #top wall pt2
    forward(205)
    #right wall
    right(90)
    forward(450)
    #bottom wall pt2
    right(90)
    forward(205)
    #return to start
    penup()
    forward(20)
    right(90)
    pendown()
    #top wall
    penup()
    goto(-200,50)
    right(90)
    pendown()
    forward(300)
    #bottom wall
    penup()
    goto(240,-100)
    right(180)
    pendown()
    forward(300)
    #return to start point
    penup()
    goto(20,-300)
    right(90)
    makeslow()

def challenge2():
    #get to start
    makefast()
    left(90)
    penup()
    forward(20)
    #bottom line pt1
    pendown()
    left(90)
    forward(205)
    #left wall
    right(90)
    forward(450)
    #top wall pt1
    right(90)
    forward(205)
    #goal
    pencolor(GOALCOL)
    forward(40)
    pencolor(WALLCOL)
    #top wall pt2
    forward(205)
    #right wall
    right(90)
    forward(450)
    #bottom wall pt2
    right(90)
    forward(205)
    #return to start
    penup()
    forward(20)
    right(90)
    pendown()

    #Draw walls
    penup()
    goto(-205,100)
    right(90)
    pendown()
    angle = 90
    for i in range(6):
        forward(250)
        penup()
        forward(100)
        pendown()
        forward(100)
        right(angle)
        penup()
        forward(65)
        pendown()
        right(angle)
        if angle == 90:
            angle = 270
        else:
            angle = 90

    #return to start point
    penup()
    goto(20,-300)
    left(90)
    makeslow()

def challenge3():
    makefast()
    penup()
    goto(0,-180)
    pendown()
    setheading(180)
    fd(180)
    setheading(90)
    fd(60)
    setheading(0)
    fd(120)
    backward(120)
    setheading(90)
    fd(300)
    setheading(0)
    fd(120)
    color('green')
    fd(60)
    left(180)
    fd(60)
    left(180)
    color('red')
    setheading(-90)
    fd(120)
    setheading(180)
    fd(60)
    setheading(90)
    fd(60)
    setheading(-90)
    fd(120)
    setheading(90)
    fd(60)
    setheading(0)
    fd(120)
    setheading(-90)
    fd(60)
    setheading(0)
    fd(60)
    setheading(-90)
    fd(60)
    backward(60)
    setheading(0)
    fd(60)
    setheading(90)
    fd(60)
    penup()
    setheading(180)
    fd(60)
    pendown()
    setheading(90)
    fd(60)
    setheading(180)
    fd(60)
    setheading(90)
    fd(60)
    setheading(0)
    fd(120)
    setheading(-90)
    fd(60)
    backward(60)
    setheading(0)
    fd(60)
    setheading(-90)
    fd(240)
    setheading(180)
    fd(60)
    setheading(-90)
    fd(60)
    setheading(180)
    fd(120)
    setheading(90)
    fd(60)
    setheading(180)
    fd(60)
    setheading(90)
    fd(60)
    backward(60)
    setheading(180)
    fd(60)
    penup()
    setheading(0)
    fd(300)
    pendown()
    setheading(-90)
    fd(120)
    setheading(180)
    fd(120)
    penup()
    fd(30)
    right(90)
    pendown()
    makeslow()

def challenge4():
    #get to start
    makefast()
    left(90)
    penup()
    forward(20)
    pendown()
    #bottom line
    left(90)
    penup()
    forward(10)
    pendown()
    forward(195)
    right(90)
    #left line
    forward(450)
    right(90)
    #top line
    forward(450)
    right(90)
    #right line
    forward(205)
    pencolor(GOALCOL)
    forward(40)
    pencolor(WALLCOL)
    forward(205)
    right(90)
    #bottom line
    forward(205)
    penup()
    forward(20)
    right(90)
    pendown()
    #bottom circle wall
    penup()
    goto(240,-75)
    left(90)
    pendown()
    circle(200,90)
    #top circle wall
    penup()
    goto(240,-25)
    right(90)
    pendown()
    circle(250,90)
    #return to start
    penup()
    goto(20,-300)
    right(180)
    makeslow()

def challenge5():
    #get to start
    makefast()
    left(90)
    penup()
    forward(20)
    pendown()
    #bottom line
    left(90)
    penup()
    forward(10)
    pendown()
    forward(195)
    right(90)
    #left line
    forward(205)
    pencolor(GOALCOL)
    forward(40)
    pencolor(WALLCOL)
    forward(205)
    right(90)
    #top line
    forward(450)
    right(90)
    #right line
    forward(450)
    right(90)
    #bottom line
    forward(205)
    penup()
    forward(20)
    right(90)
    pendown()
    #bottom right circle wall
    penup()
    goto(240,-75)
    left(90)
    pendown()
    circle(200,90)
    #top right circle wall
    penup()
    goto(240,-25)
    right(90)
    circle(250,10)
    pendown()
    circle(250,80)
    #bottom left circle wall
    penup()
    goto(-200,-80)
    left(90)
    pendown()
    circle(250,80)
    #top left circle wall
    penup()
    goto(-200,-30)
    setheading(0)
    pendown()
    circle(195,90)
    #return to start
    penup()
    goto(20,-300)
    makeslow()
