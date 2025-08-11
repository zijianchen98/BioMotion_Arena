
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the point-lights
positions = np.array([
    [0 for _ in range(4) ],   # Head
    [ 3, 4, 5, 6, 7 ],          # Upper body
    [ 8, 9, 10, 12, 13 ],     # Lower body
    [ 14, 15, 16, 17 ]        # Legs
])

# Define the movement patterns for each each point-light
movements = {
    'head': lambda t: np.array([2 * np.sin(t), 0 * np.cos(t)]),
    'upper_body': lambda t: np.array([2 * np.sin(t + np.pi / 2), 2 * np.cos(t + np.pi / 2)]),
    'lower_body': lambda t: np.array([2 * np.sin(t - np.pi / 2), 2 * np.cos(t - np.pi / 2)]),
    'legs': lambda t: np.array([2 * np.sin(t + np.pi), 2 * np.cos(t + np.pi)])
}

def update_points(num):
    for i, part in enumerate(positions):
        x, y = movements[list(movements.keys())[i]](num * 0)
        part[0] += y
        part[1] += x
    return positions

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ay.set_ylim(-10, 10)
ax.set_aspect('equal')

points, = ax.plot([], [], 'o', color='white')

def init():
    points.set_data([], [])
    return points,

ani = animation.FuncAnimation(fig, update_points, init_func=init, frames=200, interval=50, blit=True)

plt.show()
