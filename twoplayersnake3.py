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


high_score = 0


##
#pen = turtle.Turtle()
#pen.speed(0)
#pen.shape('square')
#pen.color('white')
#pen.penup()
#pen.hideturtle()
#pen.goto(0,260)
#pen.write('Score:  0', align='center', font=('courier', 24, 'normal'))
##

class Snake:
    def __init__(self, goto, color, player, setx, sety, foodgoto):
        self.head = Turtle()
        #super().__init__(shape='square')
        self.head.color(color)
        self.head.shape('arrow')
        self.head.penup()
        self.head.pensize(2)
        self.head.speed(1)
        self.head.goto(goto)
        self.distance = 10
        self.turn = 90

        self.food = turtle.Turtle()
        self.food.penup()

        self.food.goto(foodgoto)
        self.food.speed(0)
        self.food.shape('circle')
        self.food.color(color)

        #self.score = score
        self.score = 0
        self.player = player
        
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape('square')
        self.pen.color('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(setx, sety)

        self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))

        
    
    def move(self, back_key, left_key, right_key):
        self.sc = Screen()
        self.sc.listen()

        #self.sc.onkey(self.forward,forward_key)
        self.sc.onkey(self.backward, back_key)
        ####self.sc.onkey(self.backward, 'Down')
        self.sc.onkey(self.left, left_key)
        self.sc.onkey(self.right, right_key)
        #self.sc.listen()

        #self.showturtle()

    def forward(self):
        while True:
            self.head.forward(self.distance)
            if self.head.xcor()>290 or self.head.xcor()<-290 or self.head.ycor()>290 or self.head.ycor()<-290:
            
            #time.sleep(1)
            #self.head.color('black')
                self.head.goto(0,0)
            
                self.head.direction = 'stop'

                self.score = 0
                self.pen.clear()
                self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
 
            self.random = random
            if self.head.distance(self.food) < 20:
                
                self.score += 10 
                self.pen.clear()
                
                y = self.random.randint(-290, 290)
                x = self.random.randint(-290, 290)
                self.food.goto(x,y)

                self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
                
                if self.score > 25:
                    #self.pen.clear()
                    self.pen.goto(0,0)
                    self.pen.color('black')
                    self.pen.write('Player {}  is the winner!'.format(self.player), align='center', font=('courier', 30, 'bold'))
                    wn.mainloop()

    def backward(self):
        self.head.backward(self.distance)

    def left(self):
        self.head.left(self.turn)

    def right(self):
        self.head.right(self.turn)

    #def border_c(self):
        
    #def test_m(self):
        #x = self.head.xcor()
        #self.head.setx(self.head.xcor() + 100)

    #def change(self):
        #self.head.color('red')

        
        #self.food.goto(0,0)
        
    
    #def scores(self):
        #self.color = ['red', 'yellow', 'blue', 'black']
        #self.player = player
        
        #self.pen = Turtle()
        
        #self.score = 0
        

        #pen.clear()
        #pen.write('{} Score:  0'.format(self.player), align='center', font=('courier', 24, 'normal'))
       
            #self.pen.clear()
    #def main(self):
        #self.sc.mainloop()
yellow = Snake((-20,20), 'yellow', '1', -150, 260, (100, 0))

blue = Snake((20,20), 'blue', '2', 150, 260, (-100, 0))



while True:
    yellow.move('s', 'a', 'd')
        
    
    blue.move('k', 'j', 'l')
    wn.update()
    yellow.forward()
    blue.forward()
#yellow.border_c()
    #red = Snake((20, -20), 'red', 'w', 's', 'a', 'd')
    
    #blue.change()
    #blue.test_m()
    #blue.border_c()
    #yellow.scores()
    #blue.scores()
    #yellow.food_c()
    #blue.food_c()
    #blue.border_c()

    #blue.border_c()
    #d = Snake((40,40), 'red', 'Left')
    #d.main()
    #t = Snake((40,40), 'red')
    #draw.main()
    
wn.mainloop()
    #draw.main()



    


