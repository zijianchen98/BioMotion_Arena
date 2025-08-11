
import turtle

def create_body(color, size):
    body = turtle.Turtle()
    body.shape("circle")
    body.color(color)
    body.shapesize(size, size)
    return body

def create_arm(color, size, angle):
    arm = turtle.Turtle()
    arm.color(color)
    arm.shapesize(size, size)
    arm.penup()
    arm.setheading(angle)
    return arm

def draw_point_light(x, y, color):
    point_light = turtle.Turtle()
    point_light.shape("circle")
    point_light.color(color)
    point_light.shapesize(0.5, 0.5)
    point_light.penup()
    point_light.goto(x, y)

def animate_character(body, arm, point_lights):
    body.shape("circle")
    body.shapesize(5,5)
    body.setheading(170)

    while True:
        body.forward(1)
        body.left(1)

        arm.setheading(body.heading() + 90)
        arm.forward(2)
        arm.left(1)

        for light in point_lights:
            light.forward(1)

        turtle.getscreen().clear()
        turtle.reset()
        draw_point_light(0, 0, "white")

# Create the main character
body = create_body("gold", 10)
arm = create_arm("gold", 10, 180)

# Add point lights
point_lights = []
for i in range(15):
    x = (i % 5) * 10
    y = (i // 5) * 10
    draw_point_light(x, y, "white")
    point_lights.append([turtle.Turtle()])
    point_lights[i][0].shape("circle")
    point_lights[i][0].color("white")
    point_lights[i][0].shapesize(0.5, 0.5)
    point_lights[i][0].penup()
    point_lights[i][0].goto(x, y)

# Run the animation
animate_character(body, arm, point_lights)
