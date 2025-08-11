
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights
num_lights = 15

# Define the time step and duration
dt = 0.1
duration = 10

# Define the radius of the turning circle and speed
radius = 1
speed = 0.5

# Define initial positions (assuming a simple distribution)
initial_positions = [
    [radius * np.cos(np.deg2rad(360 / num_lights * i)), radius * np.sin(np.deg2rad(360 / num_lights * i))]
    for i in range(num_lights)
]

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for cleaner look

# Create scatter plot for the lights
scat = ax.scatter(*zip(*initial_positions), color='white')

def update(frame):
    angles = np.linspace(0, 2*np.pi, num_lights, endpoint=False) + frame * speed
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, int(duration/dt)), interval=int(dt*1000), blit=True)

plt.show()
