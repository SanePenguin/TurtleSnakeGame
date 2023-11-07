from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, height) -> None:
        super().__init__(visible=False)
        self.score = 0
        self.sety(height)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=('Courier', 20))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Courier', 20))