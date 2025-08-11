
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
point_lights = np.array([
    [-0.2, 0.5, 0.0],  # Head
    [-0.1, 0.4, 0.0],  # Left shoulder
    [0.1, 0.4, 0.0],   # Right shoulder
    [-0.2, 0.3, 0.0],  # Left elbow
    [0.2, 0.3, 0.0],   # Right elbow
    [-0.2, 0.2, 0.0],  # Left wrist
    [0.2, 0.2, 0.0],   # Right wrist
    [-0.1, 0.1, 0.0],  # Left hip
    [0.1, 0.1, 0.0],   # Right hip
    [-0.2, 0.0, 0.0],  # Left knee
    [0.2, 0.0, 0.0],   # Right knee
    [-0.2, -0.1, 0.0], # Left ankle
    [0.2, -0.1, 0.0],  # Right ankle
    [0.0, 0.0, 0.0],   # Torso
    [0.0, -0.2, 0.0]   # Weight
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(-0.5, 0.6)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')

    # Update point-light positions
    updated_point_lights = point_lights.copy()

    # Simulate jumping motion
    jump_height = 0.1 * np.sin(2 * np.pi * frame / 100)
    updated_point_lights[:, 1] += jump_height

    # Simulate arm and leg movement
    arm_angle = np.pi / 4 * np.sin(2 * np.pi * frame / 50)
    leg_angle = np.pi / 4 * np.sin(2 * np.pi * frame / 50 + np.pi)
    updated_point_lights[1, 0] = -0.1 + 0.1 * np.cos(arm_angle)
    updated_point_lights[2, 0] = 0.1 - 0.1 * np.cos(arm_angle)
    updated_point_lights[7, 0] = -0.1 + 0.1 * np.cos(leg_angle)
    updated_point_lights[8, 0] = 0.1 - 0.1 * np.cos(leg_angle)

    # Plot point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
