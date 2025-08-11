
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters
WIDTH, HEIGHT = 800, 600
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)

# Define the parameters for the subject and action
SUBJECT_SIZE = 50
ACTION_SIZE = 50

# Define the parameters for the point lights
POINT_LIGHTS = 15
POINT_LIGHT_COLOR = WHITE
POINT_LIGHT_RADIUS = 10

# Define the parameters for the animation
ANIMATION_SPEED = 0.05

# Create a figure and axis object
fig, ax = plt.subplots()

# Function to draw a point light
def draw_point_light(x, y, color):
    theta = np.linspace(0, 2 * np.pi, 100)
    r = np.sqrt(x**2 + y**2)
    ax.plot([x, x + r * np.cos(theta)], [y, y + r * np.sin(theta)], color=color, lw=POINT_LIGHT_RADIUS)

# Function to update the point lights
def update(frame):
    ax.clear()
    for i in range(POINT_LIGHTS):
        x = WIDTH / 2 + i * (WIDTH / POINT_LIGHTS)
        y = HEIGHT / 2 + i * (HEIGHT / POINT_LIGHTS)
        draw_point_light(x, y, WHITE)
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(ANIMATION_SPEED * 100), interval=20)

# Show the animation
plt.show()
