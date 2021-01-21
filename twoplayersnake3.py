from turtle import Turtle, Screen
import turtle
import time
import random




delay = 0.1


#score = 0
high_score = 0

wn = Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
#wn.tracer(0)

segments = []
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
        self.head.color('white')
        
        #self.head._outlinewidth(2)
        self.head.fillcolor(color)
        self.head.shape('square')
        self.head.penup()
        self.head.pensize(10)
        #self.head.shapesize(2,2,2)
        self.head.speed(0)
        self.head.goto(goto)
        self.distance = 10
        self.head.direction = 'stop'
        #self.turn = 90

        self.food = turtle.Turtle()
        self.food.penup()

        self.food.goto(foodgoto)
        self.food.speed(0)
        self.food.shape('circle')
        self.food.color('white')
        self.food.fillcolor(color)

        self.new_food = Turtle()
        self.new_food.speed(0)
        self.new_food.penup()
        self.new_food.goto(400,400)
        self.new_food.shape('circle')
        self.new_food.color(color)
        

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
        #self.segments = []
        

        self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))

    
    
    def move(self, left_key, right_key, up_key, down_key):
        #self.head.speed()
        #self.head.forward(10)
        self.sc = Screen()
        self.sc.listen()

        self.sc.onkey(self.up, up_key)
        self.sc.onkey(self.down, down_key)
        ####self.sc.onkey(self.backward, 'Down')
        self.sc.onkey(self.left, left_key)
        self.sc.onkey(self.right, right_key)
        #self.sc.listen()

        #self.showturtle()

    def turn(self):
        if self.head.direction == 'left':
            l = self.head.xcor()
            self.head.setx(l - 10)

        if self.head.direction == 'right':
            r = self.head.xcor()
            self.head.setx(r + 10)

        if self.head.direction == 'up':
            u = self.head.ycor()
            self.head.sety(u + 10)

        if self.head.direction == 'down':
            d = self.head.ycor()
            self.head.sety(d - 10)
    #def forward(self):
        #self.head.forward(self.distance)

    #def backward(self):
        #self.head.forward(self.distance * 5)

    def left(self):
        self.head.direction = 'left'
        #self.head.setx(xx-20)
        #self.head.left(self.turn)

    def right(self):
        self.head.direction = 'right'
        #self.head.setx(xx+20)
       # self.head.right(self.turn)

    def up(self):
        self.head.direction = 'up'

    def down(self):
        self.head.direction = 'down'

    def border_c(self):
        if self.head.xcor()>290 or self.head.xcor()<-290 or self.head.ycor()>290 or self.head.ycor()<-290:
            
            

            #self.head.speed(0)
            #self.head.color('black')
            self.head.goto(0,0)
            #self.head.direction = 'stop'
            #time.sleep(1)
            self.score = 0
            self.pen.clear()
            self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
 
    #def test_m(self):
        #x = self.head.xcor()
        #self.head.setx(self.head.xcor() + 100)

    #def change(self):
        #self.head.color('red')

        
        #self.food.goto(0,0)
        
    
    def scores(self):
        #self.color = ['red', 'yellow', 'blue', 'black']
        #self.player = player
        
        #self.pen = Turtle()
        
        #self.score = 0
        self.seg = [] 

        #pen.clear()
        #pen.write('{} Score:  0'.format(self.player), align='center', font=('courier', 24, 'normal'))
        self.random = random
        #self.food = food
        if self.head.distance(self.food) < 20 or self.head.distance(self.new_food) < 20:
             
            self.score += 10 
            self.pen.clear()
            #self.head.speed(self.head.speed-1)

            y = self.random.randint(-290, 290)
            x = self.random.randint(-290, 290)

            self.food.goto(x,y)

            
            #self.new_food = Turtle()
            
            #self.new_food.goto(i, j)
            #self.seg.append(self.new_food)



            self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
            
            if self.score > 45:
                #self.pen.clear()
                self.pen.goto(0,0)
                self.pen.color('black')
                self.pen.write('Player {}  is the winner!'.format(self.player), align='center', font=('courier', 30, 'bold'))
                wn.mainloop()
            #self.pen.clear()
            # 
    
        #self.sc.mainloop()
yellow = Snake((-30,30), 'red', '1', -150, 260, (100, 0))

blue = Snake((30,30), 'blue', '2', 150, 260, (-100, 0))

while True:

    wn.update()

    #red = Snake((20, -20), 'red', 'w', 's', 'a', 'd')
    yellow.move('a', 'd', 'w', 's')
    
    yellow.border_c()
    blue.move('j', 'l', 'i', 'k')
    yellow.turn()
    blue.turn()
    #blue.change()
    #blue.test_m()
    blue.border_c()
    yellow.scores()
    blue.scores()
    ##yellow.forw()

   # blue.forw()
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



    


