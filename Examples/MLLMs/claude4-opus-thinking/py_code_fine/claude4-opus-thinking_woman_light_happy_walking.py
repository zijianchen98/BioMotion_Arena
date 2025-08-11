
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point lights
num_points = 15

# Define initial coordinates of point-lights in a walking pose
# Each point light represented as (x, y)
walk_pose = np.array([
    [0.2, 0.8],  # Head
    [0.2, 0.6],  # Neck
    [0.15, 0.5], # Left shoulder
    [0.25, 0.5], # Right shoulder
    [0.15, 0.4], # Left elbow
    [0.25, 0.4], # Right elbow
    [0.1, 0.3],  # Left wrist
    [0.3, 0.3],  # Right wrist
    [0.2, 0.3],  # Torso
    [0.15, 0.1], # Left hip
    [0.25, 0.1], # Right hip
    [0.1, -0.1], # Left knee
    [0.3, -0.1], # Right knee
    [0.1, -0.2], # Left ankle
    [0.3, -0.2], # Right ankle
    [0.2, -0.5], # Feet (midpoint)
])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.6, 0.9)
ax.set_facecolor('black')
ax.axis('off')

# Create scatter plot for point lights
scat = ax.scatter(walk_pose[:,0], walk_pose[:,1], color='white')

# Function to update the points for the animation
def update(frame):
    # Simulate walking motion by altering the points
    t = frame / 10.0
    # Update the position of each light to represent motion
    new_positions = walk_pose.copy()
    new_positions[:, 1] += np.sin(t + (np.arange(num_points) * np.pi / 15)) / 20  # Up and down for walking
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=100, blit=True)

# Show the animation
plt.show()
