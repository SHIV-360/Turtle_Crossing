import time
from turtle import Screen
from car_manager import CarManager
from player import player
from scoreboard import scorebod

user = player()
car = CarManager()
screen = Screen()
sco = scorebod()
screen.setup(width=1000, height=500)
screen.tracer(0)

screen.listen()
screen.onkey(user.up, "w")
screen.onkey(user.down, "s")

speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    car.move()
    car.delete_them()
    time.sleep(speed)
    car.spawn_car()
    for x in car.all_cars:
        if user.distance(x) <= 14:
            game_is_on = False
            sco.game_over()
    if user.ycor() >= 210:
        sco.score1()
        sco.update_score()
        user.goto(0, -230)
        speed /= 1.2


screen.mainloop()
