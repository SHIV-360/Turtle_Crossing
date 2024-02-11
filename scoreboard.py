from turtle import Turtle 

class scorebod(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-300, 200)
        self.write(f"your level: {self.p1}", align= "center", font= ("Courier", 20, "normal"))

    def score1(self):
        self.p1 += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= ("Courier", 50, "normal"))
