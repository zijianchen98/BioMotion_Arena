
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points for the sadman figure
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [0, -1], [1, -1],  # Shoulders
    [-2, -2], [0, -2], [2, -2],  # Elbows
    [-3, -3], [0, -3], [3, -3],  # Hands
    [0, -4],  # Waist
    [-1, -5], [0, -5], [1, -5],  # Knees
    [-2, -6], [0, -6], [2, -6]   # Feet
])

# Function to calculate new positions based on forward rolling motion
def update_positions(positions, frame):
    angle = frame * np.pi / 90  # Rolling speed
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    new_positions = np.dot(positions, rotation_matrix)
    return new_positions

# Create the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-7, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'w.', markersize=10)

# Animation update function
def animate(frame):
    new_positions = update_positions(initial_positions, frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=180, interval=20, blit=True)

plt.show()
