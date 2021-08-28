from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=400, height=400)
screen.title('Tdaycode Snake Game')

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle(shape='square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

snake_move = True

while snake_move:
    for segment in segments:
      segment.forward(20)
      break















screen.exitonclick()