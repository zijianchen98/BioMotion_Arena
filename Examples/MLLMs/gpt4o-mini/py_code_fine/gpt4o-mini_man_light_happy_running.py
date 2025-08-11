
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Define the positions of the point lights for a running motion
points = np.array([
    [0.0, 0.5],   # Head
    [-0.1, 0.3],  # Left shoulder
    [0.1, 0.3],   # Right shoulder
    [-0.2, 0.2],  # Left elbow
    [0.2, 0.2],   # Right elbow
    [-0.1, 0.1],  # Left wrist
    [0.1, 0.1],   # Right wrist
    [0.0, 0.0],   # Body (torso)
    [-0.1, -0.5], # Left hip
    [0.1, -0.5],  # Right hip
    [-0.2, -0.8], # Left knee
    [0.2, -0.8],  # Right knee
    [-0.1, -1.0], # Left ankle
    [0.1, -1.0],  # Right ankle
])

# Function to initialize the points
def init():
    scatter.set_offsets(points)
    return scatter,

# Function to update point position for each frame
def update(frame):
    # Simulate running motion
    dz = 0.05 * np.sin(np.pi * frame / 20)  # Vertical displacement simulating leg movement
    dx = 0.05 * np.cos(np.pi * frame / 20)  # Horizontal displacement simulating forward motion

    # Modify points based on running motion
    updated_points = points.copy()
    updated_points[:, 0] += dz  # Apply vertical movement
    updated_points[:, 1] += dx  # Apply horizontal movement

    scatter.set_offsets(updated_points)
    return scatter,

# Create a scatter plot for the point lights
scatter = ax.scatter(points[:, 0], points[:, 1], c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 40), init_func=init, blit=True, interval=50)

# Show plot
plt.axis('off')
plt.show()
