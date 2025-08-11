
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of lights and frames
num_lights = 15
frames = 100

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axes

# Initialize the scatter plot for the point-lights
scat = ax.scatter([], [], color='white')

# Define the trajectory for each light
def get_light_trajectory(light_idx):
    t = np.linspace(0, 1, frames)
    if light_idx < 5:
        x = 0.5 + 0.1 * np.sin(t * 2 * np.pi * 2)
        y = 0.5 - 0.1 * np.cos(t * 2 * np.pi * 2) + 0.1 * t
    elif light_idx < 10:
        x = 0.5 + 0.1 * np.cos(t * 2 * np.pi * 2)
        y = 0.5 - 0.1 * np.sin(t * 2 * np.pi * 2) - 0.1 * t
    else:
        x = 0.5 + 0.1 * np.sin(t * 2 * np.pi * 2 + np.pi / 2)
        y = 0.5 - 0.1 * np.cos(t * 2 * np.pi * 2 + np.pi / 2) - 0.1 * t
    return x, y

# Precompute the trajectories
trajectories = [get_light_trajectory(i) for i in range(num_lights)]

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    offsets = []
    for i in range(num_lights):
        x, y = trajectories[i]
        offsets.append([x[frame], y[frame]])
    scat.set_offsets(offsets)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

plt.show()
