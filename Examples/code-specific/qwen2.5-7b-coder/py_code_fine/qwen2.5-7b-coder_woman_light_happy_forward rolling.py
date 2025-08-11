
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Initialize positions of the points
positions = np.zeros((num_points, 2))
velocities = np.random.randn(num_points, 2)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create point lights
point_lights = [plt.Circle((0, 0), 0.1, color='white') for _ in range(num_points)]
for light in point_lights:
    ax.add_artist(light)

def update(frame):
    # Update positions based on velocities
    positions += velocities
    
    # Apply boundary conditions
    positions[:, 0] %= 20
    positions[:, 1] %= 20
    
    # Update the positions of the point lights
    for i, pos in enumerate(positions):
        point_lights[i].center = pos
    
    return point_lights

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1000), interval=50, blit=True)

# Show the animation
plt.show()
