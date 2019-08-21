from time import sleep
import turtle as t

caterpillar = t.Turtle()
caterpillar.speed(1)
caterpillar.penup()
caterpillar.showturtle()

def start_game():
    while True:
        caterpillar.forward(1)
        sleep(.1)

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90) 

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 0 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def move_right():
    if caterpillar.heading() == 0 or caterpillar.heading() == 270:
        caterpillar.setheading(180) 

t.onkey(start_game, "space")
t.onkey(move_up, "Up")
t.onkey(move_right, "Right")
t.onkey(move_down, "Down")
t.onkey(move_left, "Left")
t.listen()
t.mainloop()


