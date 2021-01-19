from turtle import Turtle, Screen
import turtle
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
    def __init__(self, goto, color):
        self.head = Turtle()
        #super().__init__(shape='square')
        self.head.color(color)
        self.head.shape('arrow')
        self.head.penup()
        self.head.pensize(2)
        self.head.speed(0)#
        self.head.goto(goto)
        self.distance = 10
        self.turn = 90

     
    def move(self,forward_key, back_key, left_key, right_key):
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

    def border_c(self):
        if self.head.xcor()>290 or self.head.xcor()<-290 or self.head.ycor()>290 or self.head.ycor()<-290:

            #time.sleep(1)
            #self.head.color('black')
            self.head.goto(0,0)
        
            self.head.direction = 'stop'
 
    def test_m(self):
        #x = self.head.xcor()
        self.head.setx(self.head.xcor() + 100)

    def change(self):
        self.head.color('red')

    def food_c(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape('circle')
        self.food.color('red')
        self.food.penup()
        self.food.goto(0,0)
        self.random = random
        #self.food = food
        if self.head.distance(self.food) < 20:
            self.food.color('black')
            y = self.random.randint(-290, 290)
            x = self.random.randint(-290, 290)
            self.food.goto(x,y)
    
    #def main(self):
        #self.sc.mainloop()
blue = Snake((20,20), 'blue')

while True:

    wn.update()

    #red = Snake((20, -20), 'red', 'w', 's', 'a', 'd')
    blue.move('Up', 'Down', 'Left', 'Right')
    #blue.change()
    #blue.test_m()
    blue.border_c()
    blue.food_c()

    #blue.border_c()
    #d = Snake((40,40), 'red', 'Left')
    #d.main()
    #t = Snake((40,40), 'red')
    #draw.main()
    
wn.mainloop()
    #draw.main()



    


