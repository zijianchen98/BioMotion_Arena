
from itertools import cycle
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Set the parameters
nframes = 100
n_points = 15
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_aspect('equal')

# Initialization
x_data, y_data = [], []

# Point-light stimulus positions
def init_points():
    radius = 0.3
    positions = np.array([
        [0, 0],  # Center of the body
        [radius, 0], [-radius, 0],  # Feet
        [radius, 0.5*radius], [-radius, 0.5*radius],  # Ankles
        [radius, radius], [-radius, radius],  # Knees
        [radius, 1.5*radius], [-radius, 1.5*radius],  # Hips
        [0, 2*radius],  # Base of the spine
        [0.3*radius, 3*radius], [-0.3*radius, 3*radius],  # Shoulders
        [0.3*radius, 3.5*radius], [-0.3*radius, 3.5*radius],  # Elbows
        [0.3*radius, 4.5*radius], [-0.3*radius, 4.5*radius],  # Hands
    ])
    return positions

points = init_points()

def update(frame):
    # Clear plots
    ax.clear()
    ax.set_xlim(-radius*2, radius*2)
    ax.set_ylim(-radius*2, radius*2)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    for x_pos, y_pos in points:
        ax.plot(x_pos, y_pos, 'wo')  # white circles for point-lights

    # Rotate points around the center
    angle = 2 * np.pi * frame / nframes
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    global points
    points = np.dot(points, rotation_matrix.T)

# Creating the animation
ani = FuncAnimation(fig, update, frames=nframes, interval=50, repeat=True, blit=False)

plt.show()
