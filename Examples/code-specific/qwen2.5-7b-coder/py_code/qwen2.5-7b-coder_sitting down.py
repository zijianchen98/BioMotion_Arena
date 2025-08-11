
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point lights
num_lights = 15
positions = np.random.rand(num_lights, 2)

# Define the target positions for the man sitting down
target_positions = np.array([
    [0.2, 0.8], [0.3, 0.8], [0.4, 0.8],
    [0.2, 0.7], [0.3, 0.7], [0.4, 0.7],
    [0.2, 0.6], [0.3, 0.6], [0.4, 0.6],
    [0.2, 0.5], [0.3, 0.5], [0.4, 0.5]
])

# Define the time step for the animation
dt = 0.05

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

lights, = ax.plot([], [], 'o', markersize=10, color='white')

def update(frame):
    global positions
    
    # Update the positions towards the target positions
    positions += (target_positions - positions) * dt
    
    # Ensure the positions stay within the bounds of the plot
    positions[:, 0] = np.clip(positions[:, 0], 0, 1)
    positions[:, 1] = np.clip(positions[:, 1], 0, 1)
    
    # Update the light positions
    lights.set_data(positions[:, 0], positions[:, 1])
    
    return lights,

ani = FuncAnimation(fig, update, frames=np.arange(0, 1, dt), interval=50, blit=True)
plt.show()
