#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Erica Hung
September 2, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

turtle.home()
turtle.width(5)
turtle.color("blue")
turtle.up()

turtle.clear()

turtle.fd(20)

turtle.fd(20)

turtle.lt(90)

turtle.fd(100)

turtle.rt(90)

turtle.down()

turtle.circle(23)

turtle.up()
turtle.home()

turtle.lt(90)

turtle.fd(95)

turtle.lt(90)

turtle.fd(20)

turtle.rt(180)

turtle.down()

turtle.circle(23)

turtle.up()

turtle.home()

turtle.lt(90)

turtle.fd(120)

turtle.rt(90)

turtle.fd(7)

turtle.down()

turtle.fd(11)

turtle.up()

turtle.home()

turtle.lt(180)

turtle.fd(40)

turtle.rt(90)

turtle.fd(115)

turtle.lt(65)

turtle.fd(5)


turtle.down()

turtle.fd(45)

turtle.up()

turtle.home()
turtle.width(10)
turtle.color("pink")

turtle.lt(90)

turtle.fd(170)

turtle.rt(90)

turtle.fd(80)

turtle.lt(180)

turtle.down()

turtle.fd(220)

turtle.up()

turtle.home()

turtle.fd(50)

turtle.lt(90)

turtle.fd(176)

turtle.down()

turtle.fd(50)

turtle.lt(40)

turtle.fd(30)

turtle.lt(50)

turtle.fd(120)

turtle.lt(40)

turtle.fd(30)

turtle.lt(50)

turtle.fd(55)

turtle.lt(90)

turtle.fd(155)

#organization

turtle.up()
turtle.home()
turtle.color("orange")

turtle.fd(43)

turtle.lt(90)

turtle.fd(185)

turtle.lt(90)

turtle.down()

turtle.fd(153)

turtle.color("pink")

turtle.rt(90)

turtle.fd(10)

turtle.rt(90)

turtle.fd(156)

turtle.color("orange")
turtle.up()

turtle.lt(90)

turtle.fd(10)

turtle.lt(90)

turtle.down()

turtle.fd(156)

turtle.color("pink")
turtle.up()

turtle.rt(90)

turtle.fd(10)

turtle.rt(90)

turtle.down()

turtle.fd(156)

turtle.color("orange")
turtle.up()

turtle.lt(90)

turtle.fd(10)

turtle.lt(90)

turtle.down()

turtle.fd(156)

turtle.color("pink")
turtle.up()

turtle.rt(90)

turtle.fd(10)

turtle.rt(90)

turtle.down()

turtle.fd(156)

turtle.color("orange")
turtle.up()

turtle.lt(90)

turtle.fd(10)

turtle.lt(90)

turtle.fd(15)

turtle.down()

turtle.fd(125)

turtle.up()

turtle.home()

turtle.color("blue")

turtle.fd(62)

turtle.lt(90)

turtle.fd(128)

turtle.rt(40)

turtle.down()

turtle.width(5)
turtle.color("blue")

turtle.fd(15)

turtle.up()
turtle.goto(111,-90)
turtle.width(2)
turtle.color("purple")
turtle.rt(40)
turtle.down()

turtle.fd(100)

turtle.up()
turtle.goto(111,-90)
turtle.rt(50)
turtle.width(3)
turtle.color("red")
turtle.down()

turtle.fd(150)

turtle.up()
turtle.goto(111,-90)
turtle.rt(45)
turtle.width(2)
turtle.color("green")
turtle.down()

turtle.fd(100)

turtle.up()
turtle.goto(111,-90)
turtle.rt(60)
turtle.width(2)
turtle.color("pink")
turtle.down()

turtle.fd(150)

turtle.up()
turtle.goto(111,-90)
turtle.rt(58)
turtle.width(3)
turtle.color("yellow")
turtle.down()

turtle.fd(100)

turtle.up()
turtle.goto(111,-90)
turtle.rt(60)
turtle.width(2)
turtle.color("orange")
turtle.down()

turtle.fd(150)

turtle.up()
turtle.goto(30,84)
turtle.color("#daf071")
turtle.begin_fill()

turtle.down()

turtle.circle(15)

turtle.end_fill()

turtle.up()
turtle.home()
turtle.goto(5,15)
turtle.down()
turtle.width(3)
turtle.begin_fill()

turtle.fd(35)

turtle.rt(120)

turtle.fd(35)

turtle.rt(120)

turtle.fd(35)

turtle.end_fill()

turtle.up()
turtle.goto(320,200)
turtle.width(1)
turtle.down()

turtle.fd(10)

turtle.rt(90)

turtle.fd(10)

turtle.rt(90)

turtle.fd(10)

turtle.rt(90)

turtle.fd(10)

turtle.home()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
