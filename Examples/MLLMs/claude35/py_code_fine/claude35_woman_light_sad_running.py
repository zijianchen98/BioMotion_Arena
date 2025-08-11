
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number of point-lights
num_points = 15

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Initialize point lights data
point_lights = ax.plot([], [], 'wo', markersize=10)[0]

# Running motion data (x, y coordinates at different time steps)
# These values can be adjusted to create a more realistic running motion
time_steps = np.linspace(0, 2 * np.pi, 100)
x_data = np.sin(3 * time_steps)  # X position changes
y_data = np.cos(3 * time_steps) - 1  # Y positions to simulate running

# Create initial position for point lights
positions = np.zeros((num_points, 2))

for i in range(num_points):
    positions[i, 0] = x_data[i * (len(x_data) // num_points)]
    positions[i, 1] = y_data[i * (len(y_data) // num_points)]

# Update function for animation
def update(frame):
    # Calculate new positions for the point lights
    for i in range(num_points):
        positions[i, 0] = x_data[(frame + i) % len(x_data)]  # X position
        positions[i, 1] = y_data[(frame + i) % len(y_data)]  # Y position
    point_lights.set_data(positions[:, 0], positions[:, 1])
    return point_lights,

# Create Animation
ani = FuncAnimation(fig, update, frames=len(x_data), interval=50, blit=True)

# Show animation
plt.axis('off')  # Hide axes
plt.show()
