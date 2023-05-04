# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
name = input("File? ")
fileobj = open(name, 'r')
for line in fileobj: # for each line from the file
    line = line.rstrip()
    if line == "UP":
        t.up()
    elif line == "DOWN":
        t.down()
    else:
        xy=line.split(" ")
        x= int(xy[0])
        y= int(xy[1])
        t.goto(x, y)
fileobj.close() #close doc

# wait
turtle.Screen().exitonclick()