
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
dots, = ax.plot([], [], 'wo', markersize=6)

# Coordinates of the points for the bowing motion
initial_positions = np.array([
    [0.5, 0.9],
    [0.3, 0.8],
    [0.7, 0.8],
    [0.2, 0.7],
    [0.8, 0.7],
    [0.3, 0.6],
    [0.7, 0.6],
    [0.4, 0.5],
    [0.6, 0.5],
    [0.1, 0.4],
    [0.9, 0.4],
    [0.3, 0.3],
    [0.7, 0.3],
    [0.2, 0.2],
    [0.8, 0.2]
])

def init():
    dots.set_data([], [])
    return dots,

def update(frame):
    positions = initial_positions.copy()
    amplitude = 0.05
    bowing_motion = np.sin(frame / 10) * amplitude
    positions[:, 1] -= bowing_motion
    
    x, y = positions[:, 0], positions[:, 1]
    dots.set_data(x, y)
    return dots,

ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
plt.axis('off')
plt.show()
