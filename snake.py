from turtle import Turtle

class Snake:
    def __init__(self, color="green", starting_segments=3) -> None:
        self.segments = [Turtle("square") for _ in range(starting_segments)]
        for index, segment in enumerate(self.segments):
            segment.color(color)
            segment.penup()
            segment.goto((index * -20, 0))

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            #Coordinates of the segment in front
            new_x, new_y = self.segments[index-1].xcor(), self.segments[index-1].ycor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)
