
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE_COLOR = (1, 1, 1)
BLACK_COLOR = (0, 0, 0)

# Define point light parameters
POINT_LIGHTS = 15
LIGHT_COLOR = WHITE_COLOR
LIGHT_RADIUS = 0.1
LIGHT_SPEED = 2

# Define action parameters
ACTION_STEPS = 100
ACTION_SPEED = 0.1

# Initialize figure and axis
fig, ax = plt.subplots()

# Initialize point light positions
point_lights = []
for i in range(POINT_LIGHTS):
    angle = np.radians(i * 10)  # Convert angle to radians
    x = WIDTH / 2 + np.cos(angle) * 300
    y = HEIGHT / 2 + np.sin(angle) * 300
    point_lights.append((x, y))

# Initialize axis limits
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)

# Initialize figure size
fig.set_size_inches(10, 8)

# Function to update point light positions
def update(frame):
    for i in range(POINT_LIGHTS):
        x, y = point_lights[i]
        angle = np.radians(i * 10)  # Convert angle to radians
        x += np.cos(angle) * LIGHT_SPEED * frame
        y += np.sin(angle) * LIGHT_SPEED * frame
        point_lights[i] = (x, y)
    ax.clear()
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_aspect('equal')
    ax.set_axis_off()
    ax.plot(*zip(*point_lights), color=WHITE_COLOR, lw=1)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=ACTION_STEPS, interval=16, repeat=False)

# Show animation
plt.show()
