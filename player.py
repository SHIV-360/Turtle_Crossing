from turtle import Turtle

class player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(0, -230)
        
    def up(self):
        self.setheading(90)
        self.forward(15)

    def down(self):
        self.setheading(270)
        self.forward(15)
