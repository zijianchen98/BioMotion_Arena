
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames and the FPS for the animation
num_frames = 100
fps = 20

# Define the initial positions of the points
initial_positions = np.array([
    [0.3, 0.8], [0.4, 0.9], [0.5, 0.8],  # Head
    [0.2, 0.6], [0.6, 0.6],             # Shoulders
    [0.15, 0.4], [0.65, 0.4],           # Elbows
    [0.1, 0.2], [0.7, 0.2],             # Wrists
    [0.15, 0.1], [0.65, 0.1],           # Hips
    [0.1, 0.0], [0.7, 0.0]              # Ankles
])

# Define the function to update the positions of the points
def update_position(frame):
    angle = frame * 2 * np.pi / num_frames
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    new_positions = np.dot(initial_positions, rotation_matrix.T)
    scat.set_offsets(new_positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Create the scatter plot for the points
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=100)

# Create the animation
ani = animation.FuncAnimation(fig, update_position, frames=num_frames, interval=1000/fps)

# Show the animation
plt.show()
