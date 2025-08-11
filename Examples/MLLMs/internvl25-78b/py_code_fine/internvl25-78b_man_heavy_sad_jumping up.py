
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
fig.set_facecolor('black')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_xlim(-1, 1)
ax.set_ylim(-1.5, 0.5)

# Initial positions of point-lights
init_positions = np.array([
    [0, -0.5],  # Head
    [-0.1, -0.6], [0.1, -0.6],  # Shoulders
    [-0.2, -0.8], [0.2, -0.8],  # Elbows
    [-0.3, -1], [0.3, -1],  # Hands
    [0, -0.6],  # Neck
    [-0.1, -0.7], [0.1, -0.7],  # Hips
    [-0.2, -1], [0.2, -1],  # Knees
    [-0.3, -1.2], [0.3, -1.2],  # Feet
    [0, -0.2],  # Body center
])

points, = ax.plot([], [], 'wo', markersize=4)

def init():
    points.set_data([], [])
    return points,

def update(frame):
    amplitude = 0.3 * np.sin(0.1 * frame)
    positions = init_positions.copy()
    positions[:, 1] += amplitude
    
    x, y = zip(*positions)
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, update, frames=range(200), init_func=init, blit=True)
plt.show()
