
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
point_lights = np.array([
    [-0.3, 0.6, 0.0],  # Head
    [-0.2, 0.5, 0.0],  # Neck
    [-0.1, 0.4, 0.0],  # Right shoulder
    [0.1, 0.4, 0.0],   # Left shoulder
    [-0.2, 0.3, 0.0],  # Right elbow
    [0.2, 0.3, 0.0],   # Left elbow
    [-0.3, 0.2, 0.0],  # Right wrist
    [0.3, 0.2, 0.0],   # Left wrist
    [-0.1, 0.1, 0.0],  # Right hip
    [0.1, 0.1, 0.0],   # Left hip
    [-0.2, 0.0, 0.0],  # Right knee
    [0.2, 0.0, 0.0],   # Left knee
    [-0.3, -0.1, 0.0], # Right ankle
    [0.3, -0.1, 0.0],  # Left ankle
    [0.0, -0.2, 0.0]   # Spine
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.7)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    # Update point-light positions based on the sitting down action
    updated_point_lights = point_lights.copy()
    if frame < 30:
        # Start sitting down
        updated_point_lights[:, 1] -= frame * 0.01
    elif frame < 60:
        # Continue sitting down
        updated_point_lights[:, 1] -= 0.3
        updated_point_lights[9:, 1] -= (frame - 30) * 0.01  # Move legs down
    else:
        # End sitting down
        updated_point_lights[:, 1] -= 0.3
        updated_point_lights[9:, 1] -= 0.3  # Keep legs down

    # Plot the updated point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=90, interval=50)

plt.show()
