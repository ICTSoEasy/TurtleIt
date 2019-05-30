# TurtleIt

## Introduction
TurtleIt has been designed in response a perceived need; a simplified interface for young learners to use Python Turtle to solve mazes in a remotely paired programming environment. The intent is that TurtleIt:
- allows learners on multiple machines to work on the same code file without need to log in
- abstracts from the need for accurate spellings, capitalisaion, brackets, spaces etc
- removes the need to enter/opportunity to accidentally remove library code, imports, etc
The intended audience is KS2 students (age 8-10).

## Workflow (students)
1. Use a shortcut to open Google drive folder, select challenge number (incremental) and then team number (assigned by teacher
2. Type in code to instruct turtle
3. Double-click TurtleIt file and enter challenge/team numbers to plot maze and see how the turtle does to get through it
4. Repeat ad-infinitum

## Installation & Use
1. Minimum install is turtleit.py, turtleit_mazes.py and turtleit_urls.py. If dependencies aren't available and cannot be installed using pip (welcome to school CS education!) then the other folders provide the dependencies with versions known to work. 
2. Edit the turtleit_urls.py file with a list of empty Google doc anonymous sharing links. I made an apps script spreadsheet to automatically create the links - though you can only do 250 a day.
3. Edit the turtleit_mazes.py file to include a range of turtle mazes using standard turtle commands. 
4. Create a shortcut on the student computers to (a) the Google drive folder and (b) the turtleit.py file.
