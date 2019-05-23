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
    #top wall
    penup()
    goto(-200,50)
    right(90)
    pendown()
    forward(300)
    #middle wall
    penup()
    goto(240,-50)
    right(180)
    pendown()
    forward(300)
    #bottom wall
    penup()
    goto(-200,-150)
    right(180)
    pendown()
    forward(300)
    #return to start point
    penup()
    goto(20,-300)
    left(90)
    makeslow()
