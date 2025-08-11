
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames
num_frames = 100
num_lights = 15

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.5, 0.0], [0.4, 0.2], [0.6, 0.2],
    [0.35, 0.4], [0.65, 0.4], [0.45, 0.5],
    [0.55, 0.5], [0.3, 0.6], [0.7, 0.6],
    [0.25, 0.8], [0.75, 0.8], [0.4, 0.9],
    [0.6, 0.9], [0.5, 1.0], [0.5, 1.1]
])

# Define the angles for rotation
angles = np.linspace(0, 2 * np.pi, num_frames)

# Define the transformation matrix for rotation around the vertical axis
def rotation_matrix(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

# Define the function to update the positions of the point-lights
def update(frame):
    angle = angles[frame]
    R = rotation_matrix(angle)
    new_positions = np.dot(initial_positions, R.T)
    scatter.set_offsets(new_positions)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
