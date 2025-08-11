
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for the happyman lying down
points = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.3, 0.7],  # Left elbow
    [0.7, 0.7],  # Right elbow
    [0.2, 0.6],  # Left hand
    [0.8, 0.6],  # Right hand
    [0.4, 0.5],  # Left hip
    [0.6, 0.5],  # Right hip
    [0.3, 0.4],  # Left knee
    [0.7, 0.4],  # Right knee
    [0.2, 0.3],  # Left foot
    [0.8, 0.3],  # Right foot
    [0.5, 0.4],  # Waist
    [0.5, 0.2]   # Center of gravity
])

# Normalize points to fit in the plot
points[:, 0] *= 10
points[:, 1] *= 10

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    # Apply a small random perturbation to simulate breathing or slight movements
    perturbation = np.random.normal(0, 0.1, points.shape)
    new_points = points + perturbation
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
