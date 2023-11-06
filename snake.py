from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self, color="green", starting_segments=3) -> None:
        self.segments = []
        self.create_snake(color=color, starting_segments=starting_segments)
    
    def create_snake(self, color="green", starting_segments=3):
        for index in range(starting_segments):
            segment = Turtle("square")
            segment.color(color)
            segment.penup()
            segment.goto((index * -20, 0))
            self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            #Coordinates of the segment in front
            new_x, new_y = self.segments[index-1].xcor(), self.segments[index-1].ycor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
    
    def left(self):
        self.segments[0].setheading(180)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)
