
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sad man with heavy weight
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.4, 0.6],  # left shoulder
    [0.6, 0.6],  # right shoulder
    [0.4, 0.4],  # left elbow
    [0.6, 0.4],  # right elbow
    [0.4, 0.2],  # left hand
    [0.6, 0.2],  # right hand
    [0.5, 0.7],  # neck
    [0.5, 0.8],  # torso top
    [0.5, 0.9],  # torso middle
    [0.5, 1.0],  # torso bottom
    [0.4, 0.9],  # left hip
    [0.6, 0.9],  # right hip
    [0.4, 1.1],  # left knee
    [0.6, 1.1],  # right knee
])

# Define the animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.2)
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Update point-light locations based on the jumping motion
    updated_point_lights = point_lights.copy()
    updated_point_lights[:, 1] += np.sin(frame / 10.0) * 0.1  # vertical motion
    updated_point_lights[2:4, 1] += np.sin(frame / 10.0 + np.pi / 2) * 0.05  # arm motion
    updated_point_lights[4:6, 1] += np.sin(frame / 10.0 + np.pi) * 0.05  # hand motion
    updated_point_lights[8:, 1] += np.sin(frame / 10.0 + np.pi / 4) * 0.05  # leg motion

    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], c='w', s=5)

# Create the animation
fig, ax = plt.subplots(figsize=(5, 6), facecolor='k')
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
