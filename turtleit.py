#version 0.2
#Version History
# 0.1 = first working version, all dependencies bundled in folder
# 0.2 = changed to a class-based URL system to make identifying urls easier in code
import warnings
warnings.filterwarnings("ignore")

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from turtle import *
from turtleit_urls import *
import ast
import re

WALLCOL = "red"
TURTLECOL = "blue"
GOALCOL = "green"
WALLSIZE = 10
TURTLESIZE = 3
POOCOL = "brown"
POOSIZE = 20

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

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)



#Get the correct challenge/team number
while True:
    try:
        print(1)
        challenge = int(input('What is your challenge number? '))
        print(2)
        team = int(input('What is your team number? '))
        print(3)
        url = geturl(challenge,team)
        if not url:
          print('Sorry, I can\'t find those numbers. Try again?')
        else:
          break
    except:
        print('Sorry, they are not numbers I know. Try again?')

#Get the google doc
raw_html = simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')
#Get the modelchunk section
res = html.find_all(string=re.compile("DOCS_modelChunk = "))
#Get the bits out and split into a dict
ele = res[0].split('[')[1].split("},{")[0]+'}'
#Get the code as lines in a list
try:
    dic = ast.literal_eval(ele)
    lines = dic['s'].split('\n')
except:
    lines = []

#Draw the maze!
if challenge == 0:
    challenge0()
elif challenge == 1:
    challenge1()
elif challenge == 2:
    challenge2()

#Run through each line of code
#for idx,line in enumerate(lines):
idx = 0
while idx < len(lines):
    line = lines[idx]
    finished = False
    line = re.sub(' +',' ',line) #Sort out spaces (trim and single spacews)
    print('You said:',line,end=' ... ')
    cmds = line.upper().split(' ') #Get command and paramater(s)

    #forward command
    if not finished and cmds[0] in ['FORWARD','FROWARD','FWD','FD']:
        try:
            forward(float(cmds[1]))
            print('Ok!')
            finished = True
        except:
            print("Sorry, I think your number is wrong?")
            finished = True
    
    #right turn command
    if not finished and cmds[0] in ['RIGHT','RITE','RIT',"WRIGHT","WRITE",'RT']:
        try:
            right(float(cmds[1]))
            print('Ok!')
            finished = True
        except:
            print("Sorry, I think your number is wrong?")
            finished = True

    #left turn command
    if not finished and cmds[0] in ['LEFT','LFT','LT']:
        try:
            left(float(cmds[1]))
            print('Ok!')
            finished = True
        except:
            print("Sorry, I think your number is wrong?")
            finished = True   

    #poo command
    if not finished and cmds[0] in ['POO','POOH']:
        try:
            spot(POOSIZE,POOCOL)
            print('Ok!')
            finished = True
        except:
            print("Sorry, I think your number is wrong?")
            finished = True   

    #start loop
    if not finished and cmds[0] in ['LOOP','LOP','LP','LOOOP','REPEAT','RPR']:
        try:
            loopcount = int(cmds[1])
            loopline = idx+1
            print('You have asked me to repeat the next lines',loopcount,'times')
            print('Ok!')
            finished = True
        except:
            print("Sorry, I think your number is wrong?")
            finished = True   

    #end loop
    if not finished and cmds[0] in ['END','ENDLOOP']:
        loopcount -= 1
        if loopcount > 0:
            try:
                idx = loopline-1
                print('Looping,',loopcount,'times left')
                finished = True
            except:
                print("Oh no, something went wrong with the loop :(")
                finished = True
        else:
            print('Looping is finished')
            finished = True
    
    #Command wasn't caught
    if not finished:
        print("Sorry, I didn't understand that line")
    idx+=1
done()
