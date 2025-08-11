
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
initial_positions = np.array([
    [0, 0.5],  # Head
    [-0.1, 0], [0.1, 0],  # Shoulders
    [-0.3, 0], [0.3, 0],  # Elbows
    [-0.15, -0.05], [0.15, -0.05],  # Hands
    [0, -0.1],  # Waist
    [-0.3, -0.5], [0.3, -0.5],  # Hips
    [-0.4, -0.9], [0.4, -0.9],  # Knees
    [-0.3, -1.3], [0.3, -1.3],  # Ankles
    [-0.2, -1.5], [0.2, -1.5]  # Feet
])

def update_positions(positions, frame):
    # Adjust positions to simulate turning around
    angle = frame * np.pi / 360  # Rotate by a small angle each frame
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    positions[1:] = positions[1:] @ rotation_matrix
    return positions

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
points, = ax.plot([], [], 'w.')

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    new_positions = update_positions(initial_positions.copy(), frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=range(1440), init_func=init, blit=True)
plt.axis('off')
plt.show()
