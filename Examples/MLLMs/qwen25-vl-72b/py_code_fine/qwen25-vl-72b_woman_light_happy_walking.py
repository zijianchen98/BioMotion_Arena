
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [0.2, 0.8], [0.4, 0.8], [0.6, 0.8],
    [0.2, 0.6], [0.4, 0.6], [0.6, 0.6], [0.8, 0.6],
    [0.1, 0.4], [0.3, 0.4], [0.5, 0.4], [0.7, 0.4], [0.9, 0.4],
    [0.4, 0.2], [0.6, 0.2]
])

# Define the walking motion as a series of transformations
def walk_motion(t):
    x_shift = 0.1 * np.sin(2 * np.pi * t)
    y_shift = 0.05 * np.cos(2 * np.pi * t)
    rotation = 0.1 * np.sin(2 * np.pi * t)
    
    transformation_matrix = np.array([
        [np.cos(rotation), -np.sin(rotation)],
        [np.sin(rotation), np.cos(rotation)]
    ])
    
    new_positions = []
    for pos in initial_positions:
        new_pos = np.dot(transformation_matrix, pos) + [x_shift, y_shift]
        new_positions.append(new_pos)
    
    return np.array(new_positions)

# Create the figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)

# Update function for the animation
def update(frame):
    new_positions = walk_motion(frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 1, 100), interval=50, blit=True)

plt.show()
