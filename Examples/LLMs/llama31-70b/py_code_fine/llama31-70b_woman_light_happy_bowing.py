
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
n_points = 15
n_frames = 100

# Define the point-light positions at each frame
# These positions are based on a simplified model of a person bowing
# Each point-light is assigned to a specific joint or body part
points = np.zeros((n_points, 2, n_frames))

# Head
points[0, :, :] = np.array([0, 10]) + np.array([0, -0.1]) * np.arange(n_frames)[:, np.newaxis]

# Shoulders
points[1, :, :] = np.array([-3, 8]) + np.array([-0.05, -0.1]) * np.arange(n_frames)[:, np.newaxis]
points[2, :, :] = np.array([3, 8]) + np.array([0.05, -0.1]) * np.arange(n_frames)[:, np.newaxis]

# Elbows
points[3, :, :] = np.array([-5, 5]) + np.array([-0.1, -0.2]) * np.arange(n_frames)[:, np.newaxis]
points[4, :, :] = np.array([5, 5]) + np.array([0.1, -0.2]) * np.arange(n_frames)[:, np.newaxis]

# Hands
points[5, :, :] = np.array([-7, 0]) + np.array([-0.1, -0.3]) * np.arange(n_frames)[:, np.newaxis]
points[6, :, :] = np.array([7, 0]) + np.array([0.1, -0.3]) * np.arange(n_frames)[:, np.newaxis]

# Hips
points[7, :, :] = np.array([-2, 0]) + np.array([-0.05, 0.1]) * np.arange(n_frames)[:, np.newaxis]
points[8, :, :] = np.array([2, 0]) + np.array([0.05, 0.1]) * np.arange(n_frames)[:, np.newaxis]

# Knees
points[9, :, :] = np.array([-2, -5]) + np.array([-0.05, 0.2]) * np.arange(n_frames)[:, np.newaxis]
points[10, :, :] = np.array([2, -5]) + np.array([0.05, 0.2]) * np.arange(n_frames)[:, np.newaxis]

# Ankles
points[11, :, :] = np.array([-2, -10]) + np.array([-0.05, 0.3]) * np.arange(n_frames)[:, np.newaxis]
points[12, :, :] = np.array([2, -10]) + np.array([0.05, 0.3]) * np.arange(n_frames)[:, np.newaxis]

# Additional points to create a more realistic motion
points[13, :, :] = np.array([0, 5]) + np.array([0, -0.2]) * np.arange(n_frames)[:, np.newaxis]
points[14, :, :] = np.array([0, -5]) + np.array([0, 0.2]) * np.arange(n_frames)[:, np.newaxis]

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the first frame
ax.scatter(points[:, 0, 0], points[:, 1, 0], s=50, c='w')
ax.set_facecolor('k')
ax.set_xlim(-10, 10)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')
ax.axis('off')

# Animation function
def animate(frame):
    ax.clear()
    ax.scatter(points[:, 0, frame], points[:, 1, frame], s=50, c='w')
    ax.set_facecolor('k')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')
    ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

plt.show()
