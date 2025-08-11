
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create point lights
num_lights = 15
lights = [plt.Circle((np.random.uniform(-10, 10), np.random.uniform(-10, 10)), 0.2, color='white') for _ in range(num_lights)]
for light in lights:
    ax.add_artist(light)

# Initial positions
initial_positions = np.array([light.center for light in lights])

# Define motion parameters
def update(frame):
    global initial_positions
    # Update positions based on jumping motion
    current_positions = initial_positions + np.sin(np.linspace(0, 2 * np.pi, num_lights)) * frame / 10
    for i, light in enumerate(lights):
        light.center = tuple(current_positions[i])
    return lights

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 0.1), blit=True)

# Show animation
plt.show()
