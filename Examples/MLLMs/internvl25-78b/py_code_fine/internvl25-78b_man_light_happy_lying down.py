
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

points, = ax.plot([], [], 'wo', markersize=8)  # white points

# Initial happyman lying down coordinates
initial_coords = np.array([
    [5, 9], [4, 8], [6, 8],
    [3, 7], [7, 7],
    [4, 7], [6, 7],
    [4, 6], [5, 6], [6, 6],
    [4, 5], [6, 5],
    [4.5, 4], [5.5, 4],
    [5, 3]
])

def init():
    points.set_data([], [])
    return points,

def update(frame):
    new_coords = initial_coords.copy()
    # Simulate lying down motion by adjusting y-coordinates
    move_factor = 0.1 if frame < 15 else -0.1
    new_coords[:, 1] += move_factor
    
    points.set_data(new_coords[:, 0], new_coords[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=30, init_func=init, blit=True, repeat=False)

plt.axis('off')
plt.show()
