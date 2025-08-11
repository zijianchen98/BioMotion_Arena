
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a sad woman forward rolling
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Wrists
    [0, -2],  # Torso
    [-1, -3], [1, -3],  # Hips
    [-2, -4], [2, -4],  # Knees
    [-3, -5], [3, -5]   # Ankles
])

# Define the rotation matrix for forward rolling
def rotation_matrix(theta):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]])

# Create a function to update the positions of the points for each frame
def update(frame):
    global initial_positions
    theta = frame * np.pi / 60  # Adjust the speed of the roll
    rotated_positions = np.dot(initial_positions, rotation_matrix(theta))
    scat.set_offsets(rotated_positions)
    return scat,

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=120, interval=50, blit=True)

plt.show()
