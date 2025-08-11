
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for a heavy man in a forward roll
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Wrists
    [-1, 1], [1, 1],  # Hips
    [-2, 2], [2, 2],  # Knees
    [-3, 3], [3, 3]   # Ankles
])

# Add three more points to reach a total of 15 points
additional_points = np.array([
    [0, -1],  # Mid-back
    [0, 1],   # Lower back
    [0, 2]    # Upper back
])
initial_positions = np.vstack([initial_positions, additional_points])

# Define the forward roll motion as a series of transformations
def forward_roll(t):
    angle = t * np.pi / 2  # Rotate 90 degrees over the duration of the animation
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(initial_positions, rotation_matrix.T) + np.array([t * 2, 0])

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)

# Animation update function
def update(frame):
    new_positions = forward_roll(frame / 100)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=20, blit=True)

plt.show()
