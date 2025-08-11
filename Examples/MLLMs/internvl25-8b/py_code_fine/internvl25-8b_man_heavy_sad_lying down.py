
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_points(lx, ly, rx, ry, anim_list):
    # Create points at given coordinates and add to animation list
    points, = plt.plot(lx, ly, 'o', color='white', markersize=7, markeredgewidth=0.5)
    anim_list.append(points)
    return points

def init():
    # Initialize animation
    return [points for points in circles]

def animate(i):
    # Update the positions of points
    for points in circles:
        points.set_data(lx[i], ly[i])
    return circles

# Parameters
num_points = 15
lx = np.linspace(-0.5, 0.2, num_points)
ly = np.linspace(-0.5 + 0.4 * (np.linspace(0, 1, num_points) ** 2), 0.5, num_points)
rx = np.linspace(0.2, 0.5, num_points)
ry = np.linspace(-0.5, 0.2, num_points)

# Create figure and animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
circles = [create_points(lx[i], ly[i], rx[i], ry[i], []) for i in range(num_points)]
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=range(num_points), interval=100, blit=True, repeat=False)

plt.show()
