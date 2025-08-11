
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights representing the happy woman
# Each point-light is defined by its x and y coordinates
# We'll use a simple stick figure representation
point_lights = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.4, 0.6],  # Left elbow
    [0.6, 0.6],  # Right elbow
    [0.4, 0.4],  # Left wrist
    [0.6, 0.4],  # Right wrist
    [0.5, 0.7],  # Neck
    [0.5, 0.5],  # Torso
    [0.5, 0.3],  # Hip
    [0.4, 0.2],  # Left knee
    [0.6, 0.2],  # Right knee
    [0.4, 0.1],  # Left ankle
    [0.6, 0.1],  # Right ankle
    [0.5, 0.0]   # Feet
])

# Define the animation frames
# We'll use a simple jumping motion
def animate(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_facecolor('black')
    ax.set_aspect('equal')

    # Move the point-lights to create the jumping motion
    # We'll use a simple sine wave to create a smooth motion
    t = frame / 30.0  # 30 frames per second
    motion = np.array([
        [0, 0],  # Head
        [-0.05, 0.1],  # Left shoulder
        [0.05, 0.1],  # Right shoulder
        [-0.1, 0.2],  # Left elbow
        [0.1, 0.2],  # Right elbow
        [-0.15, 0.3],  # Left wrist
        [0.15, 0.3],  # Right wrist
        [0, 0.1],  # Neck
        [0, 0.2],  # Torso
        [0, 0.3],  # Hip
        [-0.1, 0.4],  # Left knee
        [0.1, 0.4],  # Right knee
        [-0.15, 0.5],  # Left ankle
        [0.15, 0.5],  # Right ankle
        [0, 0.6]  # Feet
    ]) * np.sin(t * 2 * np.pi)

    # Update the point-lights
    updated_point_lights = point_lights + motion

    # Plot the point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='white', s=10)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=range(30), interval=33)
plt.show()
