
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 100

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Initial positions of the points
points = np.random.rand(num_points, 2)

# Scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], c='white', s=10)

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    global points
    
    # Update positions based on sitting down motion
    t = 2 * np.pi * frame / frames
    amplitude = 0.05
    frequency = 0.5
    phase_shift = np.linspace(0, 2 * np.pi, num_points)
    
    for i in range(num_points):
        if i < 5:
            # Head and shoulders
            points[i, 1] += amplitude * np.sin(frequency * t + phase_shift[i])
        elif i < 10:
            # Upper body
            points[i, 1] -= amplitude * np.sin(frequency * t + phase_shift[i])
        else:
            # Legs
            points[i, 1] += amplitude * np.sin(frequency * t + phase_shift[i])
            points[i, 0] += amplitude * np.cos(frequency * t + phase_shift[i])
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

plt.show()
