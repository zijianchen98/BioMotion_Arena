
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Initialize positions and velocities
positions = np.random.rand(num_lights, 2) * 2 - 1  # Random positions between -1 and 1
velocities = np.zeros((num_lights, 2))

# Set initial conditions for sadman sitting down
for i in range(num_lights):
    if i % 3 == 0:
        positions[i] = [-0.9, -0.8 + i / num_lights]
        velocities[i] = [0.01, 0.01]

fig, ax = plt.subplots()
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', 'box')

def update(frame):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities
    
    # Apply boundary conditions
    positions[positions > 1] -= 2
    positions[positions < -1] += 2
    
    # Update scatter plot
    scat.set_offsets(positions)
    
    # Apply gravity-like force
    velocities[:, 1] += 0.001
    
    return scat,

ani = FuncAnimation(fig, update, frames=range(200), interval=50, blit=True)
plt.show()
