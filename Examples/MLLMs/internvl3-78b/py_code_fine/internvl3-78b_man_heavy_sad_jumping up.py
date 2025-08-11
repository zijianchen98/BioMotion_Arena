
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Defining the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-120, 120)
ax.set_ylim(-120, 120)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Define the initial coordinates of the 15 points
initial_points = np.array([
    [-5,-15], [-10,-15], [-35,-15], [-55,-15], [-90,-15],
    [5,7.5], [5,-7.5], [5,-22.5], [30,7.5], [30,-7.5], 
    [30,-22.5], [-10,-15], [15,-15], [60,-15], [95,-30]
])

# Create initial points
points, = ax.plot([], [], 'wo') # 'wo' means white dots

def init():
    points.set_data([], [])  # clear previous plot
    return points,

def animate(i):
    time = i % 100
    x = initial_points[:, 0] + 0.5 * np.sin(time * 0.05)
    y = initial_points[:, 1] + 5 * np.sin(time * 0.05) + 50
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=range(200), interval=50, blit=True)

plt.show()
