
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the happy woman
point_lights = np.array([
    [0.5, 0.5],  # Head
    [0.4, 0.6],  # Left shoulder
    [0.6, 0.6],  # Right shoulder
    [0.4, 0.4],  # Left elbow
    [0.6, 0.4],  # Right elbow
    [0.4, 0.3],  # Left hand
    [0.6, 0.3],  # Right hand
    [0.5, 0.8],  # Hip
    [0.4, 0.7],  # Left knee
    [0.6, 0.7],  # Right knee
    [0.4, 0.6],  # Left ankle
    [0.6, 0.6],  # Right ankle
    [0.5, 0.9],  # Torso
    [0.45, 0.55],  # Left breast
    [0.55, 0.55],  # Right breast
])

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Simulate the sitting down motion
    if i < 30:
        # Initial position
        ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)
    elif i < 60:
        # Start sitting down
        hip_y = 0.8 - (i - 30) / 30 * 0.1
        knee_y = 0.7 - (i - 30) / 30 * 0.1
        ankle_y = 0.6 - (i - 30) / 30 * 0.1
        point_lights[7, 1] = hip_y
        point_lights[8, 1] = knee_y
        point_lights[9, 1] = ankle_y
        point_lights[10, 1] = knee_y
        point_lights[11, 1] = ankle_y
        ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)
    elif i < 90:
        # Continue sitting down
        hip_y = 0.7 - (i - 60) / 30 * 0.1
        knee_y = 0.6 - (i - 60) / 30 * 0.1
        ankle_y = 0.5 - (i - 60) / 30 * 0.1
        point_lights[7, 1] = hip_y
        point_lights[8, 1] = knee_y
        point_lights[9, 1] = ankle_y
        point_lights[10, 1] = knee_y
        point_lights[11, 1] = ankle_y
        ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)
    else:
        # Final position
        ax.scatter(point_lights[:, 0], point_lights[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=120, interval=50)

plt.show()
