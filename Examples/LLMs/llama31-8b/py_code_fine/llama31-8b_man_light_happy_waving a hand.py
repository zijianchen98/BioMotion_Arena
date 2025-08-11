
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Define the figure and axis
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Create a black background
ax.set_facecolor('black')

# Define the point-light stimulus
lights = []

# Function to generate the point-light stimulus
def generate_stimulus():
    # Define the positions of the point-lights
    positions = [
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9),
        (2, 1), (2, 3), (2, 5), (2, 7), (2, 9)
    ]

    # Define the movements of the point-lights
    movements = [
        {'x': 0, 'y': 0},
        {'x': 0, 'y': 0.1},
        {'x': 0, 'y': 0.2},
        {'x': 0, 'y': 0.3},
        {'x': 0, 'y': 0.4},
        {'x': 0, 'y': 0.5},
        {'x': 0, 'y': 0.6},
        {'x': 0, 'y': 0.7},
        {'x': 0, 'y': 0.8},
        {'x': 0.1, 'y': 0},
        {'x': 0, 'y': 0.2},
        {'x': -0.1, 'y': 0.2},
        {'x': 0, 'y': 0.4},
        {'x': 0.1, 'y': 0.4},
        {'x': 0, 'y': 0.6}
    ]

    # Create the point-lights
    for i, (x, y) in enumerate(positions):
        light = patches.Circle((x, y), 0.05, color='white', alpha=0.5)
        ax.add_patch(light)
        lights.append({'patch': light,'movement': movements[i]})

# Generate the point-light stimulus
generate_stimulus()

# Function to update the animation
def update(frame):
    for light in lights:
        light['patch'].center = (light['patch'].center[0] + light['movement']['x'], light['patch'].center[1] + light['movement']['y'])
        if light['patch'].center[0] > 10 or light['patch'].center[0] < 0:
            light['movement']['x'] = -light['movement']['x']
        if light['patch'].center[1] > 10 or light['patch'].center[1] < 0:
            light['movement']['y'] = -light['movement']['y']

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, blit=False, interval=20)

# Show the animation
plt.show()
