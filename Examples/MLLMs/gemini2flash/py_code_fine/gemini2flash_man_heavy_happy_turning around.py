
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
plt.axis('off')

# Initialize the points
points, = ax.plot([], [], 'wo', markersize=6)

# Define the initial positions of the points
initial_positions = np.array([
    [0, 4],       # Head
    [-1, 3],      # Left Shoulder
    [1, 3],       # Right Shoulder
    [-2, 2],      # Left Elbow
    [2, 2],       # Right Elbow
    [-2, 1],      # Left Wrist
    [2, 1],       # Right Wrist
    [-0.5, 1],     # Torso 1
    [0.5, 1],      # Torso 2
    [0, 0],      # Hip
    [-1, -1],     # Left Knee
    [1, -1],      # Right Knee
    [-0.5, -2.5],   # Left Ankle
    [0.5, -2.5],   # Right Ankle
    [0, -4],         # Foot
])

# Define the animation function
def animate(i):
    # Define the angle of rotation
    angle = np.sin(i / 20) * np.pi / 4

    # Define the rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    # Rotate the points around the origin
    rotated_positions = np.dot(initial_positions, rotation_matrix)

    # Update the positions of the points
    x = rotated_positions[:, 0]
    y = rotated_positions[:, 1]
    points.set_data(x, y)

    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20, blit=True, repeat=True)

# Show the animation
plt.show()
