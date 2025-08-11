
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points representing the sad woman bowing
initial_positions = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8],  # Shoulder left
    [0.6, 0.8],  # Shoulder right
    [0.3, 0.6],  # Elbow left
    [0.7, 0.6],  # Elbow right
    [0.2, 0.4],  # Hand left
    [0.8, 0.4],  # Hand right
    [0.5, 0.4],  # Chest
    [0.5, 0.2],  # Waist
    [0.4, 0.0],  # Knee left
    [0.6, 0.0],  # Knee right
    [0.3, -0.2], # Foot left
    [0.7, -0.2], # Foot right
    [0.45, 0.7], # Hip left
    [0.55, 0.7]  # Hip right
])

# Define the trajectory of the bowing motion
def bowing_motion(t):
    angle = np.pi / 4 * np.sin(2 * np.pi * t)
    displacement = np.array([0, -np.sin(angle)])
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return rotation_matrix, displacement

# Update function for the animation
def update(frame):
    rotation_matrix, displacement = bowing_motion(frame / 30)
    new_positions = np.dot(initial_positions, rotation_matrix.T) + displacement
    scat.set_offsets(new_positions)

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide the axes

scat = ax.scatter(*zip(*initial_positions), color='white')

ani = FuncAnimation(fig, update, frames=np.arange(0, 60), interval=50, repeat=True)
plt.show()
