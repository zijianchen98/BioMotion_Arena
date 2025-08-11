
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights for the sadman
point_lights = [
    {'x': 0, 'y': 10, 'dx': 0, 'dy': -0.5},  # head
    {'x': -2, 'y': 8, 'dx': 0.2, 'dy': -0.4},  # left shoulder
    {'x': 2, 'y': 8, 'dx': -0.2, 'dy': -0.4},  # right shoulder
    {'x': -4, 'y': 6, 'dx': 0.4, 'dy': -0.3},  # left elbow
    {'x': 4, 'y': 6, 'dx': -0.4, 'dy': -0.3},  # right elbow
    {'x': -6, 'y': 4, 'dx': 0.6, 'dy': -0.2},  # left hand
    {'x': 6, 'y': 4, 'dx': -0.6, 'dy': -0.2},  # right hand
    {'x': -1, 'y': 8, 'dx': 0.1, 'dy': -0.4},  # left hip
    {'x': 1, 'y': 8, 'dx': -0.1, 'dy': -0.4},  # right hip
    {'x': -3, 'y': 6, 'dx': 0.3, 'dy': -0.3},  # left knee
    {'x': 3, 'y': 6, 'dx': -0.3, 'dy': -0.3},  # right knee
    {'x': -5, 'y': 4, 'dx': 0.5, 'dy': -0.2},  # left foot
    {'x': 5, 'y': 4, 'dx': -0.5, 'dy': -0.2},  # right foot
    {'x': 0, 'y': 2, 'dx': 0, 'dy': 0.1},  # torso
    {'x': 0, 'y': 0, 'dx': 0, 'dy': 0.2}  # sad face
]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    ax.set_facecolor('black')
    for point in point_lights:
        point['x'] += point['dx']
        point['y'] += point['dy']
        # update movement based on the jumping action
        if point['y'] < 0:
            point['dy'] = -point['dy'] * 0.8
        ax.plot(point['x'], point['y'], 'o', markersize=5, color='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
