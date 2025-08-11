
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the point lights
num_lights = 15
lights = [plt.Circle((0, 0), 0.1, color='white') for _ in range(num_lights)]
for light in lights:
    ax.add_artist(light)

# Define the initial positions and velocities
initial_positions = np.random.uniform(-8, 8, size=(num_lights, 2))
velocities = np.zeros_like(initial_positions)
velocities[:, 0] = np.random.normal(0, 0.1, size=num_lights)

# Define the acceleration due to gravity
gravity = np.array([0, -0.1])

def update(frame):
    global initial_positions, velocities
    
    # Update the positions based on velocity and acceleration
    initial_positions += velocities + 0.5 * gravity
    
    # Apply boundary conditions
    initial_positions[:, 0] = np.clip(initial_positions[:, 0], -9, 9)
    initial_positions[:, 1] = np.clip(initial_positions[:, 1], -9, 9)
    
    # Update the velocities based on acceleration
    velocities += gravity
    
    # Update the positions of the point lights
    for i, light in enumerate(lights):
        light.center = initial_positions[i]
    
    return lights

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
