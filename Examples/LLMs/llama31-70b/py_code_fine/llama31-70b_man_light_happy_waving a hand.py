
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights and frames
n_points = 15
n_frames = 100

# Define the point-light positions at each frame
def get_positions(frame):
    # Define the positions of the point-lights at the initial frame
    positions = np.array([
        [0.5, 0.5],  # head
        [0.4, 0.6],  # left shoulder
        [0.6, 0.6],  # right shoulder
        [0.4, 0.7],  # left elbow
        [0.6, 0.7],  # right elbow
        [0.4, 0.8],  # left wrist
        [0.6, 0.8],  # right wrist
        [0.5, 0.4],  # torso
        [0.5, 0.3],  # abdomen
        [0.5, 0.2],  # hip
        [0.4, 0.1],  # left knee
        [0.6, 0.1],  # right knee
        [0.4, 0.0],  # left ankle
        [0.6, 0.0],  # right ankle
        [0.5, 0.9],  # waving hand
    ])

    # Define the movement of the point-lights
    # Waving hand
    positions[-1, 1] = 0.9 + 0.1 * np.sin(frame / 10.0)
    # Moving arm
    positions[4, 1] = 0.7 + 0.1 * np.sin(frame / 10.0)
    positions[6, 1] = 0.8 + 0.1 * np.sin(frame / 10.0)

    return positions

# Create a new figure
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Initialize the point-lights
points = ax.scatter([], [], s=10, c='white')

# Animation function
def animate(frame):
    positions = get_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=50)

plt.show()
