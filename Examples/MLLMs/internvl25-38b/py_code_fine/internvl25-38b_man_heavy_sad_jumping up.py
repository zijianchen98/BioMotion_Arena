
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
points, = ax.plot([], [], 'wo', markersize=10)

# Number of points
n_points = 15

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    theta = np.linspace(0, 2 * np.pi, n_points)
    r = 5 + 3 * np.sin(frame / 10)
    x = r * np.cos(theta) + 5
    y = r * np.sin(theta) + 5
    
    # Adjust for jumping motion
    t = np.linspace(0, 2 * np.pi, n_points)
    y += 4 * np.sin(frame / 5)
    
    points.set_data(x, y)
    return points,

# Create animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.show()
