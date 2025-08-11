
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Initialize point lights
points, = ax.plot([], [], 'wo', ms=10)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    # Coordinates for each frame
    t = frame / 10.0
    x_coords = np.array([
        5 + 1 * np.sin(t),
        5 + 1.5 * np.sin(t),
        5 + 1 * np.cos(t),
        5 + 1.5 * np.cos(t),
        5 + 0.5 * np.sin(t),
        5 + 0.5 * np.cos(t),
        5 + 2 * np.sin(t),
        5 + 2 * np.cos(t),
        5 + 3 * np.sin(t),
        5 + 3 * np.cos(t),
        5 + 4 * np.sin(t),
        5 + 4 * np.cos(t),
        5 + 0.75 * np.sin(t),
        5 + 0.75 * np.cos(t),
        5 + 0.25 * np.sin(t)
    ])
    y_coords = np.array([
        5 + 1 * np.cos(t),
        5 + 1.5 * np.cos(t),
        5 + 1 * np.sin(t),
        5 + 1.5 * np.sin(t),
        5 + 0.5 * np.cos(t),
        5 + 0.5 * np.sin(t),
        5 + 2 * np.cos(t),
        5 + 2 * np.sin(t),
        5 + 3 * np.cos(t),
        5 + 3 * np.sin(t),
        5 + 4 * np.cos(t),
        5 + 4 * np.sin(t),
        5 + 0.75 * np.cos(t),
        5 + 0.75 * np.sin(t),
        5 + 0.25 * np.cos(t)
    ])
    
    points.set_data(x_coords, y_coords)
    return points,

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

plt.show()
