
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the duration of the animation
num_points = 15
duration = 10 # seconds

# Define the time steps for the animation
t = np.linspace(0, 1, 10 * 30, endpoint=False)

# Define the positions of the points
positions = np.zeros((len(t), num_points, 2))

# Create a list of angles to simulate the bowing motion
angles = np.linspace(0, -np.pi / 4, num_points // 3)
angles += np.linspace(0, np.pi / 4, num_points // 3)
angles += np.linspace(-np.pi / 4, -3 * np.pi / 4, num_points // 3)

# Assign the angles to the positions
for i in range(num_points):
    positions[:, i, 0] = 20 + 3 * np.cos(angles[i] * t)
    positions[:, i, 1] = 20 + 3 * np.sin(angles[i] * t)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
axset(ax, xlim=(-25, 25), ylim=(-25, 25), aspect='equal', facecolor='k')

# Initialize the scatter plot
scat = ax.scatter(positions[0, :, 0], positions[0, :, 1], color='w')

def update(frame):
    scat.set_offsets(positions[frame, :, :])
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), interval=30, blit=True)

# Show the animation
plt.show()
