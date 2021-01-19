from turtle import Turtle, Screen

import time
import random




delay = 0.1


score = 0
high_score = 0

wn = Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
#wn.tracer(0)


class Snake:
    def __init__(self, goto, color, forward_key, back_key, left_key, right_key):
        self.head = Turtle()
        #super().__init__(shape='square')
        self.head.color(color)
        self.head.shape('arrow')
        self.head.penup()
        self.head.pensize(2)
        self.head.speed(0)#
        self.head.goto(goto)
        self.distance = 5
        self.turn = 90

      

        self.sc = Screen()
        self.sc.listen()

        self.sc.onkey(self.forward,forward_key)
        self.sc.onkey(self.backward, back_key)
        ####self.sc.onkey(self.backward, 'Down')
        self.sc.onkey(self.left, left_key)
        self.sc.onkey(self.right, right_key)
        #self.sc.listen()

        #self.showturtle()

    def forward(self):
        self.head.forward(self.distance)

    def backward(self):
        self.head.backward(self.distance)

    def left(self):
        self.head.left(self.turn)

    def right(self):
        self.head.right(self.turn)

 

    #def change(self):
        #self.color('red')
    
    #def main(self):
        #self.sc.mainloop()

while True:
    wn.update()
    blue = Snake((20,20), 'blue', 'Up', 'Down', 'Left', 'Right')
    red = Snake((20, -20), 'red', 'w', 's', 'a', 'd')
    #d = Snake((40,40), 'red', 'Left')
    #d.main()
    #t = Snake((40,40), 'red')
    #draw.main()
    wn.mainloop()
    #draw.main()



    


