from turtle import Turtle

MOVE_DISTANCE = 20
DIRECTIONS = {"UP": 90, "LEFT": 180, "RIGHT": 0, "DOWN":270}

class Snake:
    def __init__(self, color="green", starting_segments=3) -> None:
        self.segments = []
        self.create_snake(color=color, starting_segments=starting_segments)
        self.color = color
        self.head = self.segments[0]
    
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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == DIRECTIONS["DOWN"]: return
        self.head.setheading(DIRECTIONS["UP"])
    
    def left(self):
        if self.head.heading() == DIRECTIONS["RIGHT"]: return
        self.head.setheading(DIRECTIONS["LEFT"])

    def down(self):
        if self.head.heading() == DIRECTIONS["UP"]: return
        self.head.setheading(DIRECTIONS["DOWN"])

    def right(self):
        if self.head.heading() == DIRECTIONS["LEFT"]: return
        self.head.setheading(DIRECTIONS["RIGHT"])

    def grow(self):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.setx(self.segments[-1].xcor())
        new_segment.sety(self.segments[-1].ycor())
        self.segments.append(new_segment)