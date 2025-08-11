
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
n_points = 15

# Define the duration of the animation
duration = 4  # seconds

# Define the frame rate
fps = 60

# Define the number of frames
n_frames = int(duration * fps)

# Define the angle of the waving hand
angle = np.linspace(0, 2 * np.pi, n_frames)

# Define the position of the point-lights
points = np.zeros((n_points, 2, n_frames))

# Define the position of the points on the body
points[0, :, :] = np.array([0, 0])[:, np.newaxis]  # head
points[1, :, :] = np.array([-0.5, 0.5])[:, np.newaxis]  # left shoulder
points[2, :, :] = np.array([0.5, 0.5])[:, np.newaxis]  # right shoulder
points[3, :, :] = np.array([0, 1])[:, np.newaxis]  # left elbow
points[4, :, :] = np.array([0, 1])[:, np.newaxis]  # right elbow
points[5, :, :] = np.array([-0.5, 1.5])[:, np.newaxis]  # left hand
points[6, :, :] = np.array([0.5, 1.5])[:, np.newaxis]  # right hand
points[7, :, :] = np.array([0, -0.5])[:, np.newaxis]  # left hip
points[8, :, :] = np.array([0, -0.5])[:, np.newaxis]  # right hip
points[9, :, :] = np.array([-0.5, -1])[:, np.newaxis]  # left knee
points[10, :, :] = np.array([0.5, -1])[:, np.newaxis]  # right knee
points[11, :, :] = np.array([-0.5, -1.5])[:, np.newaxis]  # left foot
points[12, :, :] = np.array([0.5, -1.5])[:, np.newaxis]  # right foot
points[13, :, :] = np.array([-0.25, 0.75])[:, np.newaxis]  # left upper arm
points[14, :, :] = np.array([0.25, 0.75])[:, np.newaxis]  # right upper arm

# Animate the waving hand
for i in range(n_frames):
    points[6, 0, i] = 0.5 + 0.25 * np.cos(angle[i])  # right hand
    points[6, 1, i] = 1.5 + 0.25 * np.sin(angle[i])  # right hand
    points[14, 0, i] = 0.25 + 0.25 * np.cos(angle[i])  # right upper arm
    points[14, 1, i] = 0.75 + 0.25 * np.sin(angle[i])  # right upper arm

# Create a new figure
fig, ax = plt.subplots()

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Set the background color to black
ax.set_facecolor('black')

# Set the axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)

# Initialize the plot with the first frame
scatter = ax.scatter(points[:, 0, 0], points[:, 1, 0], c='w')

# Animation function
def animate(i):
    scatter.set_offsets(points[:, :, i])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=1000//fps)

plt.show()
