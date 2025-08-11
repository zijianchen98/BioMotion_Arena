
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
positions = np.array([
    [0.5, 0.0], [0.25, 0.5], [0.5, 0.5], [0.75, 0.5],
    [0.1, 1.0], [0.35, 1.0], [0.65, 1.0], [0.9, 1.0],
    [0.05, 1.5], [0.2, 1.5], [0.35, 1.5], [0.65, 1.5], [0.8, 1.5],
    [0.1, 2.0], [0.7, 2.0]
])

# Define the trajectory for the movement
def trajectory(t):
    amp = 0.05
    freq = 0.5
    shift = 0.05 * np.sin(2 * np.pi * freq * t)
    new_positions = positions.copy()
    new_positions[:, 1] += shift
    return new_positions

# Function to update the plot
def update(frame):
    point_lights.set_data(trajectory(frame)[:, 0], trajectory(frame)[:, 1])
    return point_lights,

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')
point_lights, = ax.plot([], [], 'wo', markersize=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2, 200), interval=50, blit=True)

# Show the animation
plt.show()
