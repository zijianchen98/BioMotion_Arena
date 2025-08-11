
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
point_lights = [
    # Head
    {'x': 0, 'y': 10, 'vx': 0, 'vy': -0.1},
    # Torso
    {'x': -2, 'y': 5, 'vx': 0, 'vy': -0.2},
    {'x': 2, 'y': 5, 'vx': 0, 'vy': -0.2},
    # Left arm
    {'x': -4, 'y': 8, 'vx': 0.1, 'vy': -0.1},
    {'x': -6, 'y': 6, 'vx': 0.2, 'vy': -0.1},
    # Right arm
    {'x': 4, 'y': 8, 'vx': -0.1, 'vy': -0.1},
    {'x': 6, 'y': 6, 'vx': -0.2, 'vy': -0.1},
    # Left leg
    {'x': -3, 'y': 0, 'vx': 0.1, 'vy': -0.2},
    {'x': -5, 'y': -2, 'vx': 0.2, 'vy': -0.2},
    # Right leg
    {'x': 3, 'y': 0, 'vx': -0.1, 'vy': -0.2},
    {'x': 5, 'y': -2, 'vx': -0.2, 'vy': -0.2},
    # Left hand
    {'x': -7, 'y': 4, 'vx': 0.2, 'vy': -0.1},
    # Right hand
    {'x': 7, 'y': 4, 'vx': -0.2, 'vy': -0.1},
    # Left foot
    {'x': -6, 'y': -4, 'vx': 0.2, 'vy': -0.1},
    # Right foot
    {'x': 6, 'y': -4, 'vx': -0.2, 'vy': -0.1}
]

# Create a new figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Initialize the plot
def init():
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

# Update the plot
def update(frame):
    ax.clear()
    init()
    for point_light in point_lights:
        point_light['x'] += point_light['vx']
        point_light['y'] += point_light['vy']
        ax.plot(point_light['x'], point_light['y'], 'o', markersize=5, color='white')
        
        # Sitting down motion
        if point_light['y'] < -5:
            point_light['vy'] = 0.1
        elif point_light['y'] > 10:
            point_light['vy'] = -0.1

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, interval=50)

plt.show()
