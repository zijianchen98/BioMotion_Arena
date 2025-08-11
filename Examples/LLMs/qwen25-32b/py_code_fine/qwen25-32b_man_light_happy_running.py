
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
fps = 30
duration_seconds = 10
frames = duration_seconds * fps
fig, ax = plt.subplots()
line, = ax.plot([], [], 'wo', markersize=5)

# Set up the figure
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Initialize positions
positions = np.zeros((num_points, 2))
velocities = np.random.rand(num_points, 2) - 0.5

def init():
    line.set_data([], [])
    return line,

def update(frame):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities
    
    # Apply periodic boundary conditions
    positions[positions[:, 0] > 10, 0] -= 20
    positions[positions[:, 0] < -10, 0] += 20
    positions[positions[:, 1] > 10, 1] -= 20
    positions[positions[:, 1] < -10, 1] += 20
    
    # Update velocities to simulate running motion
    for i in range(num_points):
        if i % 3 == 0:
            velocities[i] = [np.sin(frame / 10), np.cos(frame / 10)]
        else:
            velocities[i] = [-np.sin(frame / 10), np.cos(frame / 10)]
    
    line.set_data(positions[:, 0], positions[:, 1])
    return line,

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000/fps)

plt.show()
