
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the point lights
num_lights = 15
initial_positions = np.random.rand(num_lights, 2) * 8 - 4  # Random positions between -4 and 4

# Define the target positions for jumping forward
target_positions = np.array([
    [0, -4],
    [-0.5, -3.5],
    [-1, -3],
    [-1.5, -2.5],
    [-2, -2],
    [-2.5, -1.5],
    [-3, -1],
    [-3.5, -0.5],
    [-4, 0],
    [-3.5, 0.5],
    [-3, 1],
    [-2.5, 1.5],
    [-2, 2],
    [-1.5, 2.5],
    [-1, 3]
])

# Define the time steps for the animation
time_steps = np.linspace(0, 1, len(target_positions))

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Create the point lights
point_lights = []
for _ in range(num_lights):
    point_light, = ax.plot([], [], 'wo', markersize=10)
    point_lights.append(point_light)

def update(frame):
    for i, point_light in enumerate(point_lights):
        x = initial_positions[i, 0] + (target_positions[i, 0] - initial_positions[i, 0]) * time_steps[frame]
        y = initial_positions[i, 1] + (target_positions[i, 1] - initial_positions[i, 1]) * time_steps[frame]
        point_light.set_data(x, y)
    return point_lights

ani = FuncAnimation(fig, update, frames=len(time_steps), interval=100, blit=True)

plt.show()
