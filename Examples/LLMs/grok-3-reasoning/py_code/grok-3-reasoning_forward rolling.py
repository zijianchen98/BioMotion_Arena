

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from scipy.interpolate import interp1d

# Define key times

t_key = np.array([0,1,2,3,4,5])

# Define positions at key frames

points_t0 = np.array([[0, 0.7], [0, 0.5], [-0.2, 0.5], [0.2, 0.5], [-0.2, 0.2], [0.2, 0.2], [-0.2, -0.1], [0.2, -0.1], [0, 0], [-0.1, 0], [0.1, 0], [-0.1, -0.4], [0.1, -0.4], [-0.1, -0.8], [0.1, -0.8]])

points_t1 = np.array([[0.3, 0.2], [0.2, 0.1], [0.1, 0.1], [0.3, 0.1], [0.3, -0.1], [0.5, -0.1], [0.5, -0.8], [0.7, -0.8], [0.2, -0.3], [0.1, -0.3], [0.3, -0.3], [0.0, -0.5], [0.4, -0.5], [-0.1, -0.8], [0.5, -0.8]])

points_t2 = np.array([[1.0, -0.4], [1.0, -0.3], [0.9, -0.3], [1.1, -0.3], [0.8, -0.4], [1.2, -0.4], [0.9, -0.5], [1.1, -0.5], [1.0, -0.5], [0.9, -0.6], [1.1, -0.6], [1.0, -0.7], [1.0, -0.7], [1.0, -0.8], [1.0, -0.8]])

points_t3 = np.array([[1.5, -0.1], [1.5, -0.3], [1.4, -0.4], [1.6, -0.4], [1.3, -0.5], [1.7, -0.5], [1.4, -0.6], [1.6, -0.6], [1.5, -0.8], [1.4, -0.7], [1.6, -0.7], [1.5, -0.6], [1.5, -0.6], [1.5, -0.5], [1.5, -0.5]])

points_t4 = np.array([[2.0, 0.2], [2.0, 0.0], [1.9, 0.0], [2.1, 0.0], [1.8, -0.2], [2.2, -0.2], [1.9, -0.4], [2.1, -0.4], [2.0, -0.4], [1.9, -0.4], [2.1, -0.4], [1.8, -0.6], [2.2, -0.6], [1.7, -0.8], [2.3, -0.8]])

points_t5 = np.array([[2.0, 0.7], [2.0, 0.5], [1.8, 0.5], [2.2, 0.5], [1.8, 0.2], [2.2, 0.2], [1.8, -0.1], [2.2, -0.1], [2.0, 0], [1.9, 0], [2.1, 0], [1.9, -0.4], [2.1, -0.4], [1.9, -0.8], [2.1, -0.8]])

positions = np.array([points_t0, points_t1, points_t2, points_t3, points_t4, points_t5])

# Create interpolation functions

x_interp = [interp1d(t_key, positions[:, i, 0], kind='cubic') for i in range(15)]

y_interp = [interp1d(t_key, positions[:, i, 1], kind='cubic') for i in range(15)]

# Set up figure and axis

fig, ax = plt.subplots()

ax.set_facecolor('black')

fig.patch.set_facecolor('black')

ax.set_xlim(-1, 3)

ax.set_ylim(-1, 1)

ax.set_aspect('equal')

# Create scatter plot

scatter = ax.scatter([], [], c='white', s=50)

# Update function

def update(frame):

    t = frame / 99 * 5  # for frame=0 to 99, t=0 to 5

    xs = [x_interp[i](t) for i in range(15)]

    ys = [y_interp[i](t) for i in range(15)]

    scatter.set_offsets(np.c_[xs, ys])

    return scatter,

# Create animation

ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()

