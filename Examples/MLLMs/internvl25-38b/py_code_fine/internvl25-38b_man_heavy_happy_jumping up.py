
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
fps = 30
duration = 2  # seconds

# Time array
t = np.linspace(0, duration, fps * duration)

# Point-light positions for jumping up
def get_positions(t):
    amplitude = 0.1
    frequency = 1  # Hz
    phase_shift = np.pi / 4

    x = np.array([
        0, 0, 0, -0.1, 0.1, -0.1, 0.1, -0.1, 0.1, -0.1, 0.1, 0, 0, 0, 0
    ])
    y = np.array([
        0, 0.2, 0.4, 0.3, 0.3, 0.1, 0.1, -0.1, -0.1, -0.3, -0.3, -0.3, -0.3, -0.3, -0.3
    ])

    y += amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)

    return x, y

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.set_axis_off()
points, = ax.plot([], [], 'wo', markersize=10)

# Animation function
def animate(i):
    x, y = get_positions(t[i])
    points.set_data(x, y)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=1000/fps, blit=True)

# Show plot
plt.show()
