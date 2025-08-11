
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the point-lights
n_points = 15
points = np.zeros((n_points, 2))

# Define the movement of the point-lights
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Define the movement of the point-lights
    # The point-lights are arranged to represent a sad woman waving her hand
    points[0] = [0, 0.5]  # head
    points[1] = [-0.2, 0.3]  # left shoulder
    points[2] = [0.2, 0.3]  # right shoulder
    points[3] = [-0.4, 0.1]  # left elbow
    points[4] = [0.4, 0.1]  # right elbow
    points[5] = [-0.6, -0.1]  # left wrist
    points[6] = [0.6, -0.1]  # right wrist
    points[7] = [-0.2, -0.3]  # left hip
    points[8] = [0.2, -0.3]  # right hip
    points[9] = [-0.4, -0.5]  # left knee
    points[10] = [0.4, -0.5]  # right knee
    points[11] = [-0.6, -0.7]  # left ankle
    points[12] = [0.6, -0.7]  # right ankle
    points[13] = [-0.3, 0.2]  # left hand
    points[14] = [0.3, 0.2]  # right hand
    
    # Waving motion
    points[5][0] = -0.6 + 0.1 * np.sin(2 * np.pi * frame / 100)
    points[5][1] = -0.1 + 0.1 * np.cos(2 * np.pi * frame / 100)
    
    # Plot the point-lights
    ax.scatter(points[:, 0], points[:, 1], c='white', s=10)

ani = animation.FuncAnimation(fig, update, frames=range(100), interval=20)

plt.show()
