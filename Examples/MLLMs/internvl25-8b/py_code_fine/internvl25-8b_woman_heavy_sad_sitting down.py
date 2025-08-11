
import turtle

# Constants for screen and movement
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DOT_RADIUS = 5
MOVE_DISTANCE = 30
MOVE_PAUSE = 0.05  # seconds

# Create the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

# Create the turtle representing the dot
dot = turtle.Turtle()
dot.shape("circle")
dot.shapesize(stretch_wid=DOT_RADIUS, stretch_len=DOT_RADIUS, dyn=1000)
dot.color("white")
dot.speed(0)
dot.hideturtle()

# List of positions for the dots
positions = [
    [-50, -55], [-40, -65], [-30, -75], [-20, -85], [-10, -95],
    [10, -65], [20, -75], [30, -85], [40, -100],
    [50, -65], [60, -75], [70, -85], [80, -95], [90, -100]
]

# Function to move the turtle to a specific position
def move_turtle(x, y):
    dot.penup()
    dot.goto(x, y)
    dot.pendown()

# Move the dot to the starting position
move_turtle(-50, -55)

# Animation loop
turtle.hideturtle()
for i, pos in enumerate(positions):
    move_turtle(pos[0], pos[1])
    dot.circle(25)
    dot.left(20)
    dot.right(140)
    dot.circle(25)
    dot.left(160)
    dot.right(0)
    dot.done(timeout=MOVE_PAUSE)

# Hide turtle and finish
wn.mainloop()
dot.hideturtle()
wn.exitonclick()
