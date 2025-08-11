
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 50

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0.5, 0.8],
    [0.4, 0.6],
    [0.6, 0.6],
    [0.45, 0.5],
    [0.55, 0.5],
    [0.4, 0.4],
    [0.45, 0.3],
    [0.55, 0.3],
    [0.6, 0.4],
    [0.3, 0.2],
    [0.7, 0.2],
    [0.35, 0.1],
    [0.45, 0.1],
    [0.55, 0.1],
    [0.65, 0.1]
])

# Define the function to update the positions of the point-lights
def update_positions(frame, points, positions):
    t = 2 * np.pi * frame / num_frames
    y_shift = 0.2 * np.sin(t)
    for i in range(len(positions)):
        if i < 5:
            positions[i, 1] = initial_positions[i, 1] + y_shift
        else:
            positions[i, 1] = initial_positions[i, 1] + 0.1 * np.sin(t + 0.6)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot for point-lights
points = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white')

# Create the animation
positions = initial_positions.copy()
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, fargs=[points, positions], interval=100, blit=True)

# Show the animation
plt.show()
