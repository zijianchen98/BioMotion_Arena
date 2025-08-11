
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
IMAGE_SIZE = 250

# Create a figure
fig, ax = plt.subplots(figsize=(IMAGE_SIZE / 100, IMAGE_SIZE / 100))
ax.set_xlim(0, IMAGE_SIZE / 100)
ax.set_ylim(0, IMAGE_SIZE / 100)
ax.axis('off')

# Initialize the white dots
points, = ax.plot([], [], 'o', c='white', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    # Define the points' positions based on the animation frame
    x = np.linspace(0, 1, NUM_POINTS)
    if i == 0:
        y = np.linspace(0.2, 0.5 + 0.3 * np.sin(np.pi * x), NUM_POINTS)
    elif 0 < i < 30:
        y = np.sin(np.pi * x) + 0.5
    else:
        y = np.sin(np.pi * x) * 0.7 + 0.1
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=30, init_func=init, blit=True)

plt.close(fig)
