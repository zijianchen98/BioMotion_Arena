
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

num_points = 15
points = np.zeros((num_points, 2))

# Define the initial positions of the points to resemble a walking figure
# These coordinates represent a basic configuration for a walking motion
initial_positions = np.array([
    [0, 0.5],   # Head
    [-0.1, 0.4],  # Left shoulder
    [0.1, 0.4],   # Right shoulder
    [-0.3, 0.2],  # Left elbow
    [0.3, 0.2],   # Right elbow
    [-0.5, 0],  # Left hand
    [0.5, 0],   # Right hand
    [0, 0.2],  # Body
    [-0.2, -0.5], # Left hip
    [0.2, -0.5],  # Right hip
    [-0.2, -1],  # Left knee
    [0.2, -1],   # Right knee
    [-0.1, -1.2], # Left foot
    [0.1, -1.2],  # Right foot
    [0, -1.5]    # Central point (for stability)
])

# Create the points on the plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def update(frame):
    global points
    # Update positions to create a walking motion
    offset = 0.02 * np.sin(frame * 0.1)
    points[:, 0] = initial_positions[:, 0] + offset * np.sin(np.linspace(0, 2 * np.pi, num_points) + frame * 0.2)
    points[:, 1] = initial_positions[:, 1] + offset * np.cos(np.linspace(0, 2 * np.pi, num_points) + frame * 0.2)
    
    scat.set_offsets(points)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
