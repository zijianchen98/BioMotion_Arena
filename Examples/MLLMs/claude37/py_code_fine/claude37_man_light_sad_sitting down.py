
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')

# Number of point-lights
num_points = 15

# Define initial positions of point-lights for 'sitting down'
# Arranging points roughly in a figure of a person sitting
points = np.array([
    [0, 1],    # head
    [-0.2, 0.8], [0.2, 0.8],  # shoulders
    [-0.3, 0.6], [0.3, 0.6],  # elbows
    [-0.4, 0.4], [0.4, 0.4],  # hands
    [-0.3, 0.5], [0.3, 0.5],  # torso
    [-0.1, 0.2], [0.1, 0.2],  # thighs
    [-0.2, 0.0], [0.2, 0.0],  # knees
    [0, -0.2]   # feet
])

# Create point-light objects
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function to update the positions of the points
def update(frame):
    # Simulate the motion of sitting down
    new_points = points.copy()
    
    # Update y-coordinates to depict downward sitting motion
    new_points[:, 1] -= frame * 0.02  # Adjust the 0.02 for speed of motion

    # Ensure points don't go below certain y value to keep in view
    new_points[new_points[:, 1] < -0.2, 1] = -0.2

    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
