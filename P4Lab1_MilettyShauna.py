#Shauna Miletty
#04/25/2025
#P4Lab1
#use turtle and loops to draw a square and triangle

#import the library
import turtle

#create the turle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#set turtle options
pen.pensize(3)
pen.pencolor("purple")
pen.shape("arrow")

#code to draw shapes
for side in range(4):
    pen.forward(200)
    pen.right(90)
 
#while loop that executes 3 times
sides = 3

while sides > 0 :
    pen.forward(200)
    pen.right(120)
    sides = sides - 1
    


#wait for user to close window
win.mainloop()
