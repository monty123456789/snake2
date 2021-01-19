import turtle
from turtle import Screen, Turtle



#t = turtle.Turtle()
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('green')
wn.setup(width=600, height=600)
wn.tracer(0)
#head = turtle.Turtle()

class MyTurtle(Turtle):
    def __init__(self, color, goto, shape, turtle):
        super().__init__(shape)

        turtle.shape('square')
        turtle.color(color)
        turtle.penup()
        turtle.goto(goto)
        turtle.shape() 
       


    
    def go_up(self):
        
        head = turtle.Turtle()
        head.penup()

        head.shape('square')
       
        y = head.ycor()
        head.sety(y+70)
    
    wn.listen()
    wn.onkey(go_up, 'w')
    
   
    def change(self):
       self.color('red')
        
    
        
        #turtle = turtle.Turtle()
                #head = turtle.Turtle()
        #turtle.shape(self)
        

                #head.shape('square')
        #head.color('black')
        #head.penup()
    #stops it from drawing
        #head.goto(0,0)
#starts head in centre of the screen
        #head.direction = 'stop' 

    #def go_forward(self):
        #x = shape.xcor()
        #shape.setx(x + 2000)   
        
        
    #wn.listen()
    #wn.onkey(go_forward, 'd')

    #go_forward()

    




    
#while True: 
    

#nertle = MyTurtle('square', 'black', (-20,-100))   
#yertle.change() 
#yertle.go_up()  

while True:
    #wn.onkey(go_up, 'w')
    wn.update()
    yertle = MyTurtle('blue', (20,100), 'square', turtle)
    #yertle.go_up()
    yertle.change()

#yertle.turtle()

wn.mainloop()