
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

points = [ax.plot([], [], 'wo', markersize=5)[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def update(frame):
    t = frame / 100
    x = [
        0.5, 0.4, 0.6, 0.35, 0.65, 0.45, 0.55, 
        0.4, 0.6, 0.4, 0.6, 0.35, 0.65, 0.45, 0.55
    ]
    y = [
        0.2 + 0.1 * np.sin(t), 0.25 + 0.15 * np.sin(t - np.pi/2), 
        0.25 + 0.15 * np.sin(t - np.pi/2), 0.3 + 0.2 * np.sin(t), 
        0.3 + 0.2 * np.sin(t), 0.35 + 0.25 * np.sin(t - np.pi/2), 
        0.35 + 0.25 * np.sin(t - np.pi/2), 0.4 + 0.3 * np.sin(t), 
        0.4 + 0.3 * np.sin(t), 0.5 + 0.4 * np.sin(t - np.pi/2), 
        0.5 + 0.4 * np.sin(t - np.pi/2), 0.55 + 0.45 * np.sin(t), 
        0.55 + 0.45 * np.sin(t), 0.5 + 0.45 * np.sin(t - np.pi), 
        0.5 + 0.45 * np.sin(t - np.pi)
    ]
    
    for i, point in enumerate(points):
        point.set_data(x[i], y[i])
    
    return points

ani = animation.FuncAnimation(fig, update, frames=range(0, 400, 10), init_func=init, blit=True)

plt.show()
