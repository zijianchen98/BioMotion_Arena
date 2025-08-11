
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
positions = np.array([
    [0.5, 1.5], [0.4, 1.0], [0.6, 1.0],
    [0.3, 0.5], [0.7, 0.5], [0.2, 0.0], [0.8, 0.0],
    [0.15, -0.5], [0.85, -0.5], [0.25, -1.0], [0.75, -1.0],
    [0.4, -1.5], [0.6, -1.5], [0.3, -2.0], [0.7, -2.0]
])

# Define the walking motion parameters
num_frames = 100
amplitude = 0.1
frequency = 0.1
phase_offset = np.linspace(0, np.pi, positions.shape[0])

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')
points = ax.scatter([], [])

def init():
    points.set_offsets([])
    return points,

def update(frame):
    x = positions[:, 0] + amplitude * np.sin(2 * np.pi * frequency * frame + phase_offset)
    y = positions[:, 1] + amplitude * np.sin(2 * np.pi * frequency * frame + phase_offset + np.pi / 2)
    points.set_offsets(np.column_stack((x, y)))
    return points,

ani = animation.FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True)

plt.show()
