
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-lights for the running man
point_lights = np.array([
    [0.0, 0.5],  # Head
    [-0.2, 0.4],  # Left shoulder
    [0.2, 0.4],  # Right shoulder
    [-0.3, 0.2],  # Left elbow
    [0.3, 0.2],  # Right elbow
    [-0.4, 0.1],  # Left wrist
    [0.4, 0.1],  # Right wrist
    [0.0, 0.0],  # Hip
    [-0.2, -0.2],  # Left knee
    [0.2, -0.2],  # Right knee
    [-0.3, -0.4],  # Left ankle
    [0.3, -0.4],  # Right ankle
    [-0.1, -0.5],  # Left foot
    [0.1, -0.5],  # Right foot
    [0.0, -0.6]  # Body center
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')
    ax.set_aspect('equal')

    # Update point-light positions based on the running motion
    updated_point_lights = point_lights.copy()
    updated_point_lights[1, 0] = -0.2 + 0.1 * np.sin(frame / 10.0)  # Left shoulder
    updated_point_lights[2, 0] = 0.2 - 0.1 * np.sin(frame / 10.0)  # Right shoulder
    updated_point_lights[3, 0] = -0.3 + 0.2 * np.sin(frame / 5.0)  # Left elbow
    updated_point_lights[4, 0] = 0.3 - 0.2 * np.sin(frame / 5.0)  # Right elbow
    updated_point_lights[5, 0] = -0.4 + 0.3 * np.sin(frame / 2.5)  # Left wrist
    updated_point_lights[6, 0] = 0.4 - 0.3 * np.sin(frame / 2.5)  # Right wrist
    updated_point_lights[8, 1] = -0.2 + 0.1 * np.sin(frame / 5.0)  # Left knee
    updated_point_lights[9, 1] = -0.2 - 0.1 * np.sin(frame / 5.0)  # Right knee
    updated_point_lights[10, 1] = -0.4 + 0.2 * np.sin(frame / 2.5)  # Left ankle
    updated_point_lights[11, 1] = -0.4 - 0.2 * np.sin(frame / 2.5)  # Right ankle
    updated_point_lights[12, 1] = -0.5 + 0.1 * np.sin(frame / 2.5)  # Left foot
    updated_point_lights[13, 1] = -0.5 - 0.1 * np.sin(frame / 2.5)  # Right foot

    # Plot the updated point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='white', s=10)

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
