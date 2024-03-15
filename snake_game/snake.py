from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.init_snake()
        self.snake_head = self.snake_segments[0]

    def init_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for segment_num in range(len(self.snake_segments)-1, 0, -1): #start, stop, step
            previous_segment = self.snake_segments[segment_num - 1]
            self.snake_segments[segment_num].setposition(previous_segment.xcor(), previous_segment.ycor()) #set the current segment's position to its previous one
        self.snake_head.forward(STEP_SIZE) #move the snake head 20px forward (one square)

    def add_segment(self, position_par):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(position_par)
        self.snake_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position()) 
        #overlaps to the last segment of the snake, so it stays at the same spot after the next move but the previous segment moves to its previous segment's spot

    def up(self):
        if not self.snake_head.heading() == DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if not self.snake_head.heading() == UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if not self.snake_head.heading() == LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if not self.snake_head.heading() == RIGHT:
            self.snake_head.setheading(LEFT)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear() #deletes all the segments added
        self.init_snake()
        self.snake_head = self.snake_segments[0]