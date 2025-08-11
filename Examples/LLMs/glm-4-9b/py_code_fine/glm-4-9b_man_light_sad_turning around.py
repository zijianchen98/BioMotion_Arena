
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15
duration = 200  # frames
center = np.array([100, 100])  # center of the figure

# Generate initial positions for the point-lights
# Distribute the points in a circle to represent the human body
theta = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
radius = 50
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)
positions = np.column_stack((x, y))

# Function to update the positions of the points over time
def update(frame):
    global positions
    angle = 2 * np.pi * frame / duration
    x = center[0] + radius * np.cos(theta + angle)
    y = center[1] + radius * np.sin(theta + angle)
    positions = np.column_stack((x, y))
    return positions,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(center[0] - 100, center[0] + 100)
ax.set_ylim(center[1] - 100, center[1] + 100)
ax.set_facecolor('black')
ax.set_aspect('equal')
scat = ax.scatter([], [], s=50, color='white')

# Animation function
ani = FuncAnimation(fig, update, frames=duration, blit=True, repeat=True)

# Show the animation
plt.show()
