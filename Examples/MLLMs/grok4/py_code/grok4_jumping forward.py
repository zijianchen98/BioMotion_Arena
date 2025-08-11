
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Create a figure and axis
fig, ax = plt.subplots()

# Set background color to black
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)

# Create an array to hold the point-light positions
points = np.zeros((num_points, 2))

# Initial positions of the point-lights
# Assuming a rough jumping pose (body up, limbs out)
points[:, 0] = np.linspace(-1, 1, num_points)  # x positions
points[0:5, 1] = 8  # arms (top row)
points[5:10, 1] = 6  # body (middle row)
points[10:15, 1] = 4  # legs (bottom row)

# Create scatter plot for the point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Update y positions to simulate jumping motion
    jump_height = 2 * np.sin(frame * 0.2)  # Simple sinusoidal function for jumping
    # Update the vertical position of the points
    points[:, 1] = np.clip(points[:, 1] + jump_height, 0, 10)

    # Set the new positions
    scatter.set_offsets(points)
    
    return scatter,

# Create an animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
