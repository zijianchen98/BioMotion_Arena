
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 points (white lights)
initial_positions = np.array([
    [0.5, 0.1], [0.3, 0.2], [0.7, 0.2], [0.3, 0.3], [0.7, 0.3],
    [0.4, 0.4], [0.6, 0.4], [0.35, 0.5], [0.65, 0.5], [0.2, 0.6],
    [0.8, 0.6], [0.45, 0.7], [0.55, 0.7], [0.5, 0.8], [0.5, 0.9]
])

# Define the frames of the animation
frames = 100

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create a scatter plot for the points
points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Define the amplitude and frequency of the oscillation
    amplitude = 0.05
    frequency = 0.1

    # Update the positions of the points
    positions = initial_positions.copy()
    for i in range(positions.shape[0]):
        positions[i, 1] += amplitude * np.sin(2 * np.pi * frequency * frame + i * np.pi / 8)

    # Adjust the position of the "feet" to simulate running motion
    if frame % 2 == 0:
        positions[0, 0] += 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[1, 0] -= 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[2, 0] -= 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[3, 0] += 0.02 * np.sin(2 * np.pi * frequency * frame)
    else:
        positions[0, 0] -= 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[1, 0] += 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[2, 0] += 0.02 * np.sin(2 * np.pi * frequency * frame)
        positions[3, 0] -= 0.02 * np.sin(2 * np.pi * frequency * frame)

    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
