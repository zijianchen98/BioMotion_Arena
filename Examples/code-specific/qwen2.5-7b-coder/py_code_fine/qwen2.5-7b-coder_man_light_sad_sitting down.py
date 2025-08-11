
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of point lights
num_lights = 15

# Initialize positions and velocities
positions = np.random.rand(num_lights, 2)
velocities = np.random.randn(num_lights, 2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create point lights
point_lights = [plt.Circle((x, y), 0.02, color='white') for x, y in positions]
for light in point_lights:
    ax.add_artist(light)

def update(frame):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities
    
    # Apply boundary conditions
    positions[:, 0] = np.clip(positions[:, 0], 0, 1)
    positions[:, 1] = np.clip(positions[:, 1], 0, 1)
    
    # Update velocities randomly
    velocities += np.random.randn(num_lights, 2) * 0.01
    
    # Update point light positions
    for i, light in enumerate(point_lights):
        light.center = positions[i]

# Create animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=50, blit=True)

# Show animation
plt.show()
