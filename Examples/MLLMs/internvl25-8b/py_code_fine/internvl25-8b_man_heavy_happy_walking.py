
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and interval between frames
frames = 100
interval = 20

# Define the dimensions and positions of the points for the animation
fig, ax = plt.subplots()
points = [plt.Circle([0.4 * i, 0.0], 0.03, color='white') for i in range(15)]
ax.set_xlim(-0.1, 1.0)
ax.set_ylim(-0.1, 1.0)
ax.set_aspect('equal')

def update(frame):
    for i, point in enumerate(points):
        point.center = [0.4 * i, 0.0 + 0.03 * np.sin(2 * np.pi * frame / 10)]
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

plt.show()
