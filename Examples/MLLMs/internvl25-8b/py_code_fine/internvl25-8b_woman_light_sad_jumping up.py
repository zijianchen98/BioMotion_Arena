
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15  # Number of points in the stimulus
CYCLE_TIME = 100  # Time for one complete cycle in milliseconds

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_aspect('equal')
ax.set_axis_off()

# Initialize points
points, = ax.plot([], [], 'o', color='white', markersize=1)

# Define points' initial positions and movement parameters
points_location = np.linspace(-10, 10, NUM_POINTS)
y_offset = np.linspace(-5, 5, NUM_POINTS)
movement_pattern = [
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
    lambda x, a, b: a + (b - a) * math.sin(2 * np.pi * x),  # up
    lambda x, a, b: b + (a - b) * math.sin(2 * np.pi * x),  # down
]

# Animation function
def update(frame):
    ax.set_xlim(points_location)
    ax.set_ylim(y_offset)
    new_y = np.array([points_location[j] for j in range(NUM_POINTS)])
    for i in range(NUM_POINTS):
        new_y[i] = movement_pattern[i](points_location[i], points_location[0], points_location[NUM_POINTS - 1])
    points.set_data(points_location, new_y)
    return points,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, CYCLE_TIME * 2, CYCLE_TIME / 10), blit=True)

# Show plot
plt.show()
