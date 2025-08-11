
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()

# Define the positions and movements of the 15 point-lights
lights = {
    'left_hand': {'x': 0.2, 'y': 0.5, 'vx': 0.05, 'vy': -0.05},
    'right_hand': {'x': 0.8, 'y': 0.5, 'vx': -0.05, 'vy': -0.05},
    'left_foot': {'x': 0.2, 'y': 0.8, 'vx': 0.01, 'vy': 0.01},
    'right_foot': {'x': 0.8, 'y': 0.8, 'vx': -0.01, 'vy': 0.01},
    'left_knee': {'x': 0.2, 'y': 0.7, 'vx': 0.01, 'vy': 0.01},
    'right_knee': {'x': 0.8, 'y': 0.7, 'vx': -0.01, 'vy': 0.01},
    'left_hip': {'x': 0.2, 'y': 0.9, 'vx': 0.01, 'vy': 0.01},
    'right_hip': {'x': 0.8, 'y': 0.9, 'vx': -0.01, 'vy': 0.01},
    'left_elbow': {'x': 0.2, 'y': 0.6, 'vx': 0.01, 'vy': -0.01},
    'right_elbow': {'x': 0.8, 'y': 0.6, 'vx': -0.01, 'vy': -0.01},
    'left_shoulder': {'x': 0.2, 'y': 0.4, 'vx': 0.01, 'vy': 0.01},
    'right_shoulder': {'x': 0.8, 'y': 0.4, 'vx': -0.01, 'vy': 0.01},
    'head': {'x': 0.5, 'y': 0.2, 'vx': 0.01, 'vy': 0.01},
    'left_eye': {'x': 0.45, 'y': 0.1, 'vx': 0.01, 'vy': 0.01},
    'right_eye': {'x': 0.55, 'y': 0.1, 'vx': -0.01, 'vy': 0.01}
}

# Initialize the point-light positions
light_positions = {key: [lights[key]['x'], lights[key]['y']] for key in lights}

# Function to update the point-light positions
def update(frame):
    for key in lights:
        light_positions[key][0] += lights[key]['vx']
        light_positions[key][1] += lights[key]['vy']
        if light_positions[key][0] < 0 or light_positions[key][0] > 1:
            lights[key]['vx'] *= -1
        if light_positions[key][1] < 0 or light_positions[key][1] > 1:
            lights[key]['vy'] *= -1
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor('black')
    for key in lights:
        ax.plot(light_positions[key][0], light_positions[key][1], 'o', color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, interval=16, blit=False)

# Show the animation
plt.show()
