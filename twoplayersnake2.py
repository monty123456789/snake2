import turtle
from turtle import Turtle, Screen

import time
import random




delay = 0.1


score = 0
high_score = 0

wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)


class Snake(Turtle):
    def __init__(self, goto, color):
        super().__init__(shape='square')
        self.color(color)
        self.penup()
        self.goto(goto)
      
      
        #self.showturtle()

    def go_up(self):
        
        self.head = turtle.Turtle()
        
       
        y = self.head.ycor()
        self.head.sety(y+70)

    def change(self):
        self.color('red')
    
    wn.listen()
    wn.onkey(change, 'w')


while True:
    wn.update()
    d = Snake((20,40), 'red')
    t = Snake((200,20), 'blue')
    


wn.mainloop()