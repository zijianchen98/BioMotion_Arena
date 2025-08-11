
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize coordinates of the point-lights representing the sadman
coordinates = np.array([
    [0, 5], [1, 4], [2, 3], [3, 2], [4, 1],
    [5, 0], [6, 1], [7, 2], [8, 3], [9, 4],
    [2, 6], [4, 7], [6, 7], [8, 6], [5, 5]
])

def init():
    scat.set_offsets(coordinates)
    return scat,

def animate(frame):
    global coordinates
    new_coords = coordinates.copy()
    
    # Simulate movement
    amplitude = 0.5 * (np.sin(frame / 10.0) + 1)
    new_coords[:, 1] = coordinates[:, 1] - 2 * amplitude ** 2
    new_coords[:, 0] += 0.1 * amplitude

    scat.set_offsets(new_coords)
    coordinates = new_coords
    return scat,

# Create figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_facecolor('black')
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 8)

# Create point lights
scat = ax.scatter([], [], s=50, c='white')

# Animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.axis('off')
plt.show()
