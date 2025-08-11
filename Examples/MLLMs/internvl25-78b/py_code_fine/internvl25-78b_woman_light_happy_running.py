
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
points, = ax.plot([], [], 'w.', ms=10)

def init():
    points.set_data([], [])
    return points,

def animate(t):
    # Define the point lights positions for a running motion
    x = [
        3 + 2 * np.sin(t), 4 + 1.5 * np.sin(t + np.pi / 2), 
        5 + 1.5 * np.sin(t + np.pi), 6 + 2 * np.sin(t + np.pi), 
        5 + 1.5 * np.cos(t + np.pi / 2), 5 + 1.5 * np.cos(t), 
        4 + 1.5 * np.cos(t - np.pi / 2), 4.5 + 0.5 * np.sin(t), 
        5.5 + 0.5 * np.sin(t), 5 + 0.5 * np.cos(t), 
        5 + 2 * np.sin(t), 4.5 + 0.5 * np.cos(t), 
        5.5 + 0.5 * np.cos(t), 5 + 2 * np.sin(t + np.pi / 2), 
        5 + 2 * np.sin(t - np.pi / 2)
    ]
    y = [
        5 + 1 * np.cos(t), 6 + 0.5 * np.cos(t + np.pi / 2), 
        6 + 0.5 * np.cos(t + np.pi), 5 + 1 * np.cos(t + np.pi), 
        4 + 0.5 * np.sin(t + np.pi / 2), 4 + 0.5 * np.sin(t), 
        4 + 0.5 * np.sin(t - np.pi / 2), 5 + 1 * np.sin(t), 
        5 + 1 * np.sin(t), 5 + 0.5 * np.sin(t), 
        5 + 2 * np.cos(t), 5 + 0.5 * np.cos(t), 
        5 + 0.5 * np.cos(t), 6 + 0.5 * np.sin(t), 
        6 + 0.5 * np.sin(t)
    ]
    points.set_data(x, y)
    return points,

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 100),
                              init_func=init, blit=True, interval=50)

plt.axis('off')
plt.show()
