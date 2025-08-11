
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define parameters
SUBJECT_SIZE = 100
ACTION_SIZE = 100
LIGHT_COUNT = 15
LIGHT_SPEED = 2
ACTION_SPEED = 0.5

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize point lights
points = []
for i in range(LIGHT_COUNT):
    angle = i * np.pi / LIGHT_COUNT
    x = WIDTH / 2 + 50 * np.cos(angle)
    y = HEIGHT / 2 + 50 * np.sin(angle)
    points.append((x, y))

# Define the action
def action(x, y):
    return np.array([x + ACTION_SPEED * np.cos(x * 0.1), y + ACTION_SPEED * np.sin(x * 0.1)])

# Initialize plot
for i, point in enumerate(points):
    ax.scatter(point[0], point[1], s=SUBJECT_SIZE, color=WHITE)

# Function to update the plot
def update(frame):
    global ax
    ax.clear()
    ax.scatter(points[frame % LIGHT_COUNT][0], points[frame % LIGHT_COUNT][1], s=SUBJECT_SIZE, color=WHITE)
    action_x = action(points[frame % LIGHT_COUNT][0], points[frame % LIGHT_COUNT][1])
    ax.scatter(action_x[0], action_x[1], s=ACTION_SIZE, color=BLACK)
    ax.set_xlim(-50, 50)
    ax.set_ylim(-50, 50)
    ax.set_aspect('equal')
    plt.draw()

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(LIGHT_COUNT), interval=50)

plt.show()
