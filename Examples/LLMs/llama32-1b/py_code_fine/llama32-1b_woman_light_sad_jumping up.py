
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the subject and action
subject = {'name': 'woman', 'action': 'jumping up'}

# Define the parameters for the animation
params = {
   'subject': subject,
    'action': 'jumping up',
    'points': 15,
    'light_weight': 0.1,
    'background_color': 'black',
    'light_color': 'white',
    'light_speed': 0.1,
    'light_distance': 0.5,
    'frame_rate': 60,
    'time_step': 0.02
}

# Create a figure and axis object
fig, ax = plt.subplots()

# Initialize the positions of the points
x, y = 0, 0

# Initialize the light positions
light_positions = []

# Create the point-lights
for i in range(params['points']):
    light_angle = np.linspace(0, 2*np.pi, 100)
    light_x = x + params['light_distance'] * np.cos(light_angle)
    light_y = y + params['light_distance'] * np.sin(light_angle)
    light_positions.append((light_x, light_y))
    ax.add_patch(plt.Line2D([light_x], [light_y], color=params['light_color'], lw=params['light_weight']))

# Update the positions of the points
def update(frame):
    global x, y, light_positions
    x += params['light_speed'] * params['light_distance'] * np.cos(frame)
    y += params['light_speed'] * params['light_distance'] * np.sin(frame)
    light_positions = [(x + params['light_distance'] * np.cos(frame), y + params['light_distance'] * np.sin(frame)) for x, y in light_positions]
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    for light_x, light_y in light_positions:
        ax.add_patch(plt.Line2D([light_x], [light_y], color=params['light_color'], lw=params['light_weight']))
    plt.draw()
    plt.pause(params['time_step'])

# Set the limits and callback for the animation
plt.ion()
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
ax.set_aspect('equal')
plt.show(block=False)
update(0)

# Keep the plot open
plt.ion()
plt.show()
