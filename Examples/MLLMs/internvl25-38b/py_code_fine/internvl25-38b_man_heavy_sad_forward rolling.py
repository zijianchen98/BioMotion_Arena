
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 0],     # Head
    [-1, 0],    # Shoulder Left
    [1, 0],     # Shoulder Right
    [-2, -1],   # Elbow Left
    [2, -1],    # Elbow Right
    [-3, -2],   # Wrist Left
    [3, -2],    # Wrist Right
    [0, -2],    # Hip
    [-1, -3],   # Knee Left
    [1, -3],    # Knee Right
    [-2, -4],   # Ankle Left
    [2, -4],    # Ankle Right
    [-1, 0.5],  # Weight Left
    [1, 0.5],   # Weight Right
    [0, -0.5]   # Center of weight
])

# Define the movement function for the forward rolling motion
def forward_roll(t):
    angle = 0.1 * t
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions = initial_positions @ rotation_matrix
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 0)
ax.axis('off')
points, = ax.plot([], [], 'wo', markersize=10)

# Animation function to update the point-light positions
def animate(t):
    positions = forward_roll(t)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = FuncAnimation(fig, animate, frames=np.arange(0, 300, 1), interval=20, blit=True)
plt.show()
