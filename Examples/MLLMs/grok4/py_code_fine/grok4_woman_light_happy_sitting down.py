
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)

# Define the point-light positions for the sitting down motion
# The positions can be adjusted for a more realistic action
num_points = 15
points = np.array([
    [0, 8],    # Head
    [-1, 7],   # Left Shoulder
    [1, 7],    # Right Shoulder
    [-1, 5.5], # Left Elbow
    [1, 5.5],  # Right Elbow
    [-1, 4.5], # Left Hand
    [1, 4.5],  # Right Hand
    [0, 6],    # Torso
    [-1, 4],   # Left Hip
    [1, 4],    # Right Hip
    [-1, 2],   # Left Knee
    [1, 2],    # Right Knee
    [-1, 0],   # Left Foot
    [1, 0],    # Right Foot
])

# Initial state
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Change the y-coordinates to simulate sitting down
    new_y = points[:, 1] - 0.1  # Move downwards
    scat.set_offsets(points[:, 0], new_y)
    
    # If the figure goes below a certain y limit, stop the motion
    if new_y[0] < 0:
        new_y[:] = 0  # Normalize back to ground level
    points[:, 1] = new_y  # Update points position
    return scat,

# Animation creation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

# Show the animation
plt.show()
