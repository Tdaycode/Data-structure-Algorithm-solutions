from turtle import Turtle, Screen

tayo = Turtle()
screen = Screen()


def move_forward():
    tayo.forward(10)


screen.listen()
screen.onkey(move_forward, 'space')
screen.exitonclick()
