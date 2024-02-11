from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []

    def spawn_car(self):
        rand = random.randint(0, 2)
        if rand == 2:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=0.75)
            car.penup()
            car.goto(400, random.randrange(-200, 200, 15))
            car.color(random.choice(["yellow", "blue", "lightgreen", "red", "orange", "purple", "pink", "brown", "cyan"])) 
            car.setheading(180)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(20)
        
    def delete_them(self):
        for car in self.all_cars:
            if car.xcor() <= -410:
                car.hideturtle()
                self.all_cars.remove(car)
                del car
