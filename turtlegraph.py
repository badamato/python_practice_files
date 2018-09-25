from turtle import *

bgcolor('#F39C12')

myPen = Turtle('turtle')
myPen.shapesize(1, 1, 0)
myPen.speed(2)
myPen.color("#5DADE2")
myPen.width(9) ##change this to 5 for normal

side=400

#position cursor at the bootom right of the screen
myPen.penup()
myPen.goto(-200,-200)
myPen.pendown()

#Start Spiral
for i in range (1,100):
    myPen.forward(side)
    myPen.left(90)
    side=side-10 ##change this to -4 for normal

bye()
