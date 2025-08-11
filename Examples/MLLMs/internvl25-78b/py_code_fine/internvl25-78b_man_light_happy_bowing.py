
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define the initial positions of the points
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.3, 0.7],  # Shoulder left
    [0.7, 0.7],  # Shoulder right
    [0.3, 0.6],  # Elbow left
    [0.7, 0.6],  # Elbow right
    [0.3, 0.5],  # Hand left
    [0.7, 0.5],  # Hand right
    [0.4, 0.6],  # Hip left
    [0.6, 0.6],  # Hip right
    [0.4, 0.5],  # Knee left
    [0.6, 0.5],  # Knee right
    [0.4, 0.4],  # Foot left
    [0.6, 0.4],  # Foot right
    [0.45, 0.7],  # Mid-spine
    [0.55, 0.7]   # Mid-spine
])

# Define the points
points, = ax.plot([], [], 'wo', ms=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    pos = initial_positions.copy()
    
    angle = np.sin(2 * np.pi * i / 30) * 0.1  # Sine wave for bowing motion
    
    # Rotate hips for bowing
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation to upper body parts
    for j in range(1, 8):
        pos[j] = np.dot(rotation_matrix, pos[j] - pos[0]) + pos[0]
    
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=50, blit=True, init_func=init)

plt.show()
