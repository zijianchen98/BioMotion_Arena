
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_human_figure():
    # Define the positions of the points representing a human figure
    # Head, Torso, Left Arm, Right Arm, Left Leg, Right Leg
    points = np.array([
        [0, 0],   # Head
        [0, -1], # Torso
        [-1, -2],  # Left Arm
        [1, -2],  # Right Arm
        [-2, -3],  # Left Leg
        [2, -3]    # Right Leg
    ])
    return points

def animate(frame):
    global points, x, y
    angle = frame / 10 * 2 * np.pi  # Calculate the rotation angle
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    rotated_points = np.dot(points, rotation_matrix)
    x = rotated_points[:, 0]
    y = rotated_points[:, 1]

def initialize():
    global x, y
    x = np.zeros(()
    y = np.zeros(())
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.plot(x, y, 'ro')

fig, ax = plt.subplots()
points = create_human_figure()
initialize()

ani = FuncAnimation(fig, animate, frames=np.arange((), init_func=initialize,
                    interval=50, blit=False)

plt.show()
