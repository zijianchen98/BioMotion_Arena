
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and frames
num_points = 15
frames = 60

# Initialize positions
positions = np.zeros((frames, num_points, 2))

# Happy woman walking motion parameters
walk_speed = 0.1
walk_amplitude = 0.1
walk_frequency = 0.1

# Generate walk motion
for t in range(frames):
    for i in range(num_points):
        angle = 2 * np.pi * i / num_points
        radius = 0.5 + 0.2 * np.sin(walk_frequency * t + angle)
        x = radius * np.cos(walk_speed * t + angle)
        y = radius * np.sin(walk_speed * t + angle)
        positions[t, i] = [x, y]

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Plot the points
points, = ax.plot([], [], 'o', color='white')

def update(frame):
    points.set_data(positions[frame].T)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
