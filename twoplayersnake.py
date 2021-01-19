import turtle
from turtle import Screen, Turtle



#t = turtle.Turtle()
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)

class MyTurtle(Turtle):
    def __init__(self, shape, color, goto):
        super().__init__(shape)
        self.color(color)
        self.penup()
        self.goto(goto)
        self.shape('square') = head
        self.head = heads
        #self.shape = head
        #self.pensize(pensize)
        #self.speed(speed)   

    #def go_forward(self):
    
    def head(self):
        pass

        #head = turtle.Turtle()
        #turtle.shape(self)
        

                #head.shape('square')
        #head.color('black')
        #head.penup()
    #stops it from drawing
        #head.goto(0,0)
#starts head in centre of the screen
        #head.direction = 'stop' 

    def go_forward(self):
        x = shape.xcor()
        shape.setx(x + 2000)   
        
    #wn.listen()
    #wn.onkey(go_forward, 'd')

    #go_forward()

    def change(self):
        self.color('red')




    
#while True: 
    
yertle = MyTurtle('square', 'blue', (20,100))
nertle = MyTurtle('square', 'black', (-20,-100))   
yertle.change()   
wn.update()


#yertle.turtle()

wn.mainloop()