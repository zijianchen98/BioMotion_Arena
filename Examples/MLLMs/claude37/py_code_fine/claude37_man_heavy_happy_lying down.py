
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.set_xticks([])  # Remove x ticks
ax.set_yticks([])  # Remove y ticks

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Function to initialize the positions of the points
def init():
    # Initial positions mimicking a happy person lying down
    points[:, 0] = np.random.uniform(-1.5, 1.5, num_points)  # X coordinates
    points[:, 1] = np.random.uniform(-2, -1, num_points)  # Y coordinates
    return points

# Create point lights on the plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

def update(frame):
    # Define motion for the points to simulate lying down with slight movements
    # Adding small random movements in y to mimic natural motion
    points[:, 1] += np.random.uniform(-0.05, 0.05, num_points)
    points[:, 1] = np.clip(points[:, 1], -2, -1)  # Keep y within limits
    scat.set_offsets(points)
    return scat,

# Initialize points' positions
init()

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
