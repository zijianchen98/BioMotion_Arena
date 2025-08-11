
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOWING_SPEED = 0.1

# Define the subject's pose
POSE = {
    'x': 100,
    'y': 100,
    'z': 100,
    'w': 100,
    'h': 100,
    'angle_x': np.pi / 4,
    'angle_y': 0,
    'angle_z': 0,
}

# Define the action's pose
ACTION = {
    'x': 300,
    'y': 200,
    'z': 200,
    'w': 200,
    'h': 200,
    'angle_x': np.pi / 4,
    'angle_y': 0,
    'angle_z': 0,
}

# Define the point-light positions and intensities
LIGHTS = [
    {'x': 200, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 300, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 400, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 500, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 600, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 700, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
    {'x': 800, 'y': 200, 'z': 200, 'w': 0, 'h': 0, 'i': 100},
]

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize the axis with the background
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_zlim(0, HEIGHT)
ax.set_axis_off()

# Initialize the point lights
for light in LIGHTS:
    ax.add_patch(plt.Circle((light['x'], light['y']), 2, edgecolor='black', facecolor='white', lw=2))

# Function to update the plot
def update(i):
    # Update the subject's pose
    POSE['x'] += BOWING_SPEED * i
    POSE['y'] += BOWING_SPEED * i
    POSE['z'] += BOWING_SPEED * i

    # Update the action's pose
    ACTION['x'] += BOWING_SPEED * i
    ACTION['y'] += BOWING_SPEED * i
    ACTION['z'] += BOWING_SPEED * i

    # Update the point lights
    for light in LIGHTS:
        light['x'] = POSE['x'] + light['w']
        light['y'] = POSE['y'] + light['h']
        light['z'] = POSE['z'] + light['z']
        light['w'] = POSE['w']
        light['h'] = POSE['h']
        light['i'] = int(100 * (1 - (light['x'] / WIDTH) ** 2 - (light['y'] / HEIGHT) ** 2 - (light['z'] / HEIGHT) ** 2))

    # Clear the previous frame
    ax.clear()

    # Draw the axis
    ax.set_xlim(0, WIDTH)
    ax.set_ylim(0, HEIGHT)
    ax.set_zlim(0, HEIGHT)
    ax.set_axis_off()

    # Draw the point lights
    for light in LIGHTS:
        ax.add_patch(plt.Circle((light['x'], light['y']), 2, edgecolor='black', facecolor='white', lw=2))

    # Draw the subject and action
    ax.scatter(POSE['x'], POSE['y'], POSE['z'], color='red', s=50)
    ax.scatter(ACTION['x'], ACTION['y'], ACTION['z'], color='blue', s=50)

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=100, interval=10)

plt.show()
