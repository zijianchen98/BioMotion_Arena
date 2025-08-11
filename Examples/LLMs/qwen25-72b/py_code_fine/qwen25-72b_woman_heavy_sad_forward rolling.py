
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Define the initial positions of the point-lights
initial_positions = [
    [0, 0],  # Center of mass
    [-2, -3], [2, -3],  # Feet
    [-1, -2], [1, -2],  # Knees
    [-3, -1], [3, -1],  # Hips
    [-4, 0], [4, 0],  # Shoulders
    [-5, 1], [5, 1],  # Elbows
    [-6, 2], [6, 2],  # Hands
    [-3, 3], [3, 3],  # Head
]

# Convert initial positions to a NumPy array
positions = np.array(initial_positions)

# Define the number of frames
num_frames = 100

# Define the forward roll motion
def forward_roll(t):
    angle = t * 2 * np.pi / num_frames
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(positions, rotation_matrix.T)

# Initialize the scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Update function for the animation
def update(frame):
    new_positions = forward_roll(frame)
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
