
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-1, 0)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create white point-lights
points = ax.scatter([], [], color='white', s=50)

# Coordinates of point-lights for a lying man (example coordinates)
coordinates = {
    0:  [(0.5, 0), (0.45, 0.05), (0.55, 0.05), (0.4, 0.15), (0.45, 0.15), 
          (0.5, 0.15), (0.55, 0.15), (0.6, 0.15), (0.4, 0.1), (0.45, 0.1), 
          (0.5, 0.1), (0.55, 0.1), (0.6, 0.1), (0.5, 0.1), (0.5, -0.1)],
    1:  [(0.5, -0.1), (0.45, -0.05), (0.55, -0.05), (0.4, -0.15), (0.45, -0.15), 
          (0.5, -0.15), (0.55, -0.15), (0.6, -0.15), (0.4, -0.1), (0.45, -0.1), 
          (0.5, -0.1), (0.55, -0.1), (0.6, -0.1), (0.5, 0.1), (0.5, 0.1)]
}

def init():
    points.set_offsets([])
    return points,

def update(frame):
    xy = coordinates[frame]  # Get coordinates for this frame
    points.set_offsets(xy)   # Set new positions for point-lights
    return points,

ani = animation.FuncAnimation(fig, update, frames=2, init_func=init, blit=True, repeat=True)
plt.show()
