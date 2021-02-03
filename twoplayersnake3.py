from turtle import Turtle, Screen
import turtle
import random


#Setting up the interface
wn = Screen()
wn.title('Snake Game')
wn.setup(width=800, height=800)
wn.bgcolor('green')

#Creating the class 'Snake', this is the class from which the two player instances will be made from
class Snake:
    #the parameters in __init__ are the parameters that allow the player instances to be called, e.g. 'color' allows the instances to be called with different colors so the players know who is who
    def __init__(self, goto, color, player, setx, sety, foodgoto):
        self.sc = Screen()

        #setting up the 'head' of the player, this is the square the player will move. 
        self.head = Turtle()
        self.head.color(color)
        self.head.fillcolor('white')
        self.head.shapesize(outline=10)
        self.head.shape('square')
        self.head.penup()
        self.head.pensize(1)
        self.head.speed(0)
        self.head.goto(goto)
        self.head.direction = 'stop'
        
        #creating the food the player will move over to score points
        self.food = turtle.Turtle()
        self.food.penup()
        self.food.goto(foodgoto)
        self.food.speed(0)
        self.food.shape('circle')
        self.food.color('white')
        self.food.fillcolor(color)


        
        
        
        #setting up the point system and player graphics
        self.score = 0
        self.player = player
        
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape('square')
        self.pen.color('white')
        self.pen.pensize()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(setx, sety)
        self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
        
        #This will be increased every time a player moves over food to increase the speed, or reset if they hit an edge. 
        self.di = 12
        
    # creating the move function
    def move(self, left_key, right_key, up_key, down_key):
        self.sc.listen()
        self.sc.onkey(self.up, up_key)
        self.sc.onkey(self.down, down_key)
        self.sc.onkey(self.left, left_key)
        self.sc.onkey(self.right, right_key)
     
     #creating the turn functions
    def turn(self):
    
        if self.head.direction == 'left':
            l = self.head.xcor()
            self.head.setx(l - self.di)

        if self.head.direction == 'right':
            r = self.head.xcor()
            self.head.setx(r + self.di)

        if self.head.direction == 'up':
            u = self.head.ycor()
            self.head.sety(u + self.di)

        if self.head.direction == 'down':
            d = self.head.ycor()
            self.head.sety(d - self.di)


    def left(self):
        self.head.direction = 'left'

    def right(self):
        self.head.direction = 'right'

    def up(self):
        self.head.direction = 'up'

    def down(self):
        self.head.direction = 'down'

    #This function resets the player position and speed if they get too close the edge of the screen. 
    def border_c(self):
        if self.head.xcor()>390 or self.head.xcor()<-390 or self.head.ycor()>390 or self.head.ycor()<-390:
            self.head.pensize(1)
            self.head.goto(0,0)
            self.di = 12
            self.score = 0
            self.pen.clear()
            self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
    
    #This function increases the score and speed if the player moves over food, and resets the position of the food. 
    def scores(self):
        self.seg = [] 
        self.random = random
        if self.head.distance(self.food) < 20:
            
            self.di += 3
            p = self.head.pensize()
            new = p + 3
            self.head.pensize(new)
            self.score += 10 
            self.pen.clear()

            y = self.random.randint(-390, 390)
            x = self.random.randint(-390, 390)
            self.food.goto(x,y)

          



            self.pen.write('Player {}  Score: {}'.format(self.player, self.score), align='center', font=('courier', 24, 'normal'))
            
            #This ends the game when a player has a score of 100, and announces the winner. 
            if self.score > 95:
                self.pen.goto(0,0)
                self.pen.color('white')
                self.pen.fillcolor('black')
                self.pen.shapesize(outline=20)
                self.pen.write('Player {}  is the winner!'.format(self.player), align='center', font=('courier', 40, 'bold'))
                wn.mainloop()
          
#Creates two player instances
player1 = Snake((-30,30), 'red', '1', -150, 360, (100, 0))
player2 = Snake((30,30), 'blue', '2', 150, 360, (-100, 0))

#creates the game loop that calls the functions on the instances. 
while True:
    player1.move('a', 'd', 'w', 's')
    player1.border_c()
    player1.turn()
    player1.scores()

    player2.move('j', 'l', 'i', 'k')
    player2.turn()
    player2.border_c()
    player2.scores()

    wn.update()

wn.mainloop()


    


