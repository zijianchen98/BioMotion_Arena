
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [0.2, 0.8], [0.4, 0.8], [0.6, 0.8],
    [0, 0.6], [0.2, 0.6], [0.4, 0.6], [0.6, 0.6],
    [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4],
    [0.2, 0.2], [0.4, 0.2], [0.3, 0]
])

# Define the wave motion parameters
amplitude = 0.1
frequency = 0.5

# Create a figure and axis with a black background
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.axis('off')

# Create the scatter plot for the points
points, = ax.plot([], [], 'wo', markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(t):
    x = initial_positions[:, 0]
    y = initial_positions[:, 1] + amplitude * np.sin(frequency * t + 2 * np.pi * initial_positions[:, 0])
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=np.linspace(0, 2*np.pi, 200), interval=50, blit=True)

plt.show()
