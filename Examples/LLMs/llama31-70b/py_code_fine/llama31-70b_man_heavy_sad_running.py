
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the point-light locations for the sad man with heavy weight
point_lights = np.array([
    [0.5, 0.5],  # head
    [0.5, 0.6],  # left shoulder
    [0.5, 0.4],  # right shoulder
    [0.4, 0.7],  # left elbow
    [0.6, 0.7],  # right elbow
    [0.3, 0.8],  # left hand
    [0.7, 0.8],  # right hand
    [0.5, 0.3],  # left hip
    [0.5, 0.2],  # right hip
    [0.4, 0.1],  # left knee
    [0.6, 0.1],  # right knee
    [0.3, 0.0],  # left foot
    [0.7, 0.0],  # right foot
    [0.45, 0.55],  # torso top
    [0.55, 0.55],  # torso bottom
])

# Define the animation function
def animate(frame):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Update the point-light locations based on the running motion
    updated_point_lights = point_lights.copy()
    updated_point_lights[:, 1] += np.sin(frame / 10.0) * 0.05

    # Draw the point-lights
    ax.scatter(updated_point_lights[:, 0], updated_point_lights[:, 1], s=10, c='white')

    # Draw the lines connecting the point-lights
    ax.plot([updated_point_lights[0, 0], updated_point_lights[1, 0]], [updated_point_lights[0, 1], updated_point_lights[1, 1]], c='white')
    ax.plot([updated_point_lights[0, 0], updated_point_lights[2, 0]], [updated_point_lights[0, 1], updated_point_lights[2, 1]], c='white')
    ax.plot([updated_point_lights[1, 0], updated_point_lights[3, 0]], [updated_point_lights[1, 1], updated_point_lights[3, 1]], c='white')
    ax.plot([updated_point_lights[2, 0], updated_point_lights[4, 0]], [updated_point_lights[2, 1], updated_point_lights[4, 1]], c='white')
    ax.plot([updated_point_lights[3, 0], updated_point_lights[5, 0]], [updated_point_lights[3, 1], updated_point_lights[5, 1]], c='white')
    ax.plot([updated_point_lights[4, 0], updated_point_lights[6, 0]], [updated_point_lights[4, 1], updated_point_lights[6, 1]], c='white')
    ax.plot([updated_point_lights[7, 0], updated_point_lights[8, 0]], [updated_point_lights[7, 1], updated_point_lights[8, 1]], c='white')
    ax.plot([updated_point_lights[7, 0], updated_point_lights[9, 0]], [updated_point_lights[7, 1], updated_point_lights[9, 1]], c='white')
    ax.plot([updated_point_lights[8, 0], updated_point_lights[10, 0]], [updated_point_lights[8, 1], updated_point_lights[10, 1]], c='white')
    ax.plot([updated_point_lights[9, 0], updated_point_lights[11, 0]], [updated_point_lights[9, 1], updated_point_lights[11, 1]], c='white')
    ax.plot([updated_point_lights[10, 0], updated_point_lights[12, 0]], [updated_point_lights[10, 1], updated_point_lights[12, 1]], c='white')
    ax.plot([updated_point_lights[0, 0], updated_point_lights[13, 0]], [updated_point_lights[0, 1], updated_point_lights[13, 1]], c='white')
    ax.plot([updated_point_lights[13, 0], updated_point_lights[14, 0]], [updated_point_lights[13, 1], updated_point_lights[14, 1]], c='white')

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
