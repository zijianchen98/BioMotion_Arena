
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Set the axis aspect ratio to be equal
ax.set_aspect('equal')

# Create a solid black background
ax.set_facecolor('black')

# Define the points for the happy woman
points = np.array([
    [-0.5, -0.8],  # Left foot
    [-0.3, -0.8],  # Left ankle
    [-0.2, -0.7],  # Left knee
    [-0.2, -0.4],  # Left hip
    [0.2, -0.4],   # Right hip
    [0.2, -0.7],   # Right knee
    [0.3, -0.8],   # Right ankle
    [0.5, -0.8],   # Right foot
    [0, -0.6],     # Left hand
    [0, -0.3],     # Left shoulder
    [0, 0.3],      # Right shoulder
    [0, 0.6],      # Right hand
    [-0.4, 0.4],   # Left elbow
    [0.4, 0.4],    # Right elbow
    [0, 0.8]       # Head
])

# Define the point lights
point_lights = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Define the joints
joints = ax.scatter(points[:, 0], points[:, 1], s=50, color='red')

# Define the axes
ax.axhline(0, color='white')
ax.axvline(0, color='white')

# Function to update the animation
def update(frame):
    # Update the points for the happy woman
    points[:, 0] = np.sin(frame / 10 + np.linspace(0, 2 * np.pi, 15)) * 0.3
    points[:, 1] = np.sin(frame / 10 + np.linspace(0, 2 * np.pi, 15)) * 0.3 + np.sin(frame / 5 + np.linspace(0, 2 * np.pi, 15)) * 0.2
    point_lights.set_offsets(points)
    
    # Update the joints
    joints.set_offsets(points)
    
    # Return the updated points
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20, blit=True)

# Show the animation
plt.show()
