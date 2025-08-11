
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_points = 15
frames = 60
time_step = 0.1
weight_factor = 0.5

# Initial positions and velocities
positions = np.random.rand(num_points, 2) * 8 - 4
velocities = np.zeros((num_points, 2))

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')

points, = ax.plot([], [], 'o', markersize=10, color='white')

def init():
    points.set_data([], [])
    return points,

def update(frame):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities * time_step
    
    # Apply boundary conditions
    positions[:, 0] = np.clip(positions[:, 0], -5, 5)
    positions[:, 1] = np.clip(positions[:, 1], -5, 5)
    
    # Calculate new velocities for realistic motion
    for i in range(num_points):
        if i == 0:
            # Head follows the center of mass
            com = np.mean(positions, axis=0)
            velocities[i] = (com - positions[i]) / np.linalg.norm(com - positions[i])
        else:
            # Remaining points follow the previous point
            velocities[i] = (positions[i-1] - positions[i]) / np.linalg.norm(positions[i-1] - positions[i])
    
    # Scale down velocity for realism
    velocities *= weight_factor
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=int(time_step*1000))
plt.show()
