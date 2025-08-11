
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the animation
num_lights = 15
time_steps = 200
duration = 5  # Duration in seconds
fps = 30
dt = 1 / fps  # Time step size

# Define the positions of the lights over time
# For simplicity, we use a sinusoidal motion to simulate jumping forward
def light_positions(t):
    x = np.sin(2 * np.pi * t * 2 / duration) * 0.8 + 0.5  # Horizontal position (normalized between 0.2 and 0.8)
    y = np.sin(2 * np.pi * t * 4 / duration) * 0.3 + 0.5  # Vertical position (normalized between 0.2 and 0.8)
    z = np.sin(2 * np.pi * t * 2 / duration) * 0.5  # Depth position (normalized between 0.0 and 0.5)
    return x, y, z

# Generate the positions for all time steps
t = np.linspace(0, duration, time_steps)
x_pos, y_pos, z_pos = light_positions(t)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize the point-lights plot
lights, = ax.plot([], [], 'o', color='white', markersize=5)

# Animation update function
def update(frame):
    # Get the positions for the current frame
    x = x_pos[frame]
    y = y_pos[frame]
    z = z_pos[frame]
    
    # Update the positions of the lights
    lights.set_data(np.array(x) * np.sin(z) + 0.5, np.array(y) * np.cos(z) + 0.5)
    return lights,

# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, blit=True, interval=dt*1000)

plt.show()
