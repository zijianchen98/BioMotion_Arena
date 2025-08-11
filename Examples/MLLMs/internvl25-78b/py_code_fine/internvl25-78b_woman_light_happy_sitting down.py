
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Initial positions of point-lights
initial_points = np.array([
    [0, 0.8], [0.2, 0.6], [-0.2, 0.6],
    [0.4, 0.4], [-0.4, 0.4], [0, 0.2],
    [0.6, 0], [-0.6, 0], [0.2, -0.2], [-0.2, -0.2],
    [0.4, -0.4], [-0.4, -0.4], [0, -0.6],
    [0.2, -0.8], [-0.2, -0.8], [0, -1]
])

# Initialize scatter plot
point_lights, = ax.plot([], [], 'wo')

def init():
    point_lights.set_data([], [])
    return point_lights,

def animate(t):
    # Create a smooth sitting down motion
    amplitude = 0.5 * np.sin(0.1 * t)
    
    points = initial_points.copy()
    points[:, 1] -= amplitude
    
    x, y = points[:, 0], points[:, 1]
    point_lights.set_data(x, y)
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=200, init_func=init, blit=True, interval=30)

plt.show()
