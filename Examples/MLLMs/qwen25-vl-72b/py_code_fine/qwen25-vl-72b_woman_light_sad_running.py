
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.8, 0.4], [-0.6, 0.4], [-0.4, 0.4], [-0.2, 0.4], [0, 0.4], [0.2, 0.4], [0.4, 0.4], [0.6, 0.4], [0.8, 0.4],
    [-0.3, 0.1], [0.3, 0.1]
])

# Define the movement parameters for each point
movement_params = [
    {'speed': [0.01, -0.02], 'amplitude': [0.05, 0.1], 'frequency': [0.5, 0.3]},
    {'speed': [0.02, -0.01], 'amplitude': [0.04, 0.08], 'frequency': [0.4, 0.2]},
    {'speed': [0.015, -0.015], 'amplitude': [0.03, 0.09], 'frequency': [0.3, 0.4]},
    {'speed': [0.01, -0.02], 'amplitude': [0.05, 0.1], 'frequency': [0.5, 0.3]},
    {'speed': [0.02, -0.01], 'amplitude': [0.04, 0.08], 'frequency': [0.4, 0.2]},
    {'speed': [0.015, -0.015], 'amplitude': [0.03, 0.09], 'frequency': [0.3, 0.4]},
    {'speed': [0.01, -0.02], 'amplitude': [0.05, 0.1], 'frequency': [0.5, 0.3]},
    {'speed': [0.02, -0.01], 'amplitude': [0.04, 0.08], 'frequency': [0.4, 0.2]},
    {'speed': [0.015, -0.015], 'amplitude': [0.03, 0.09], 'frequency': [0.3, 0.4]},
    {'speed': [0.01, -0.02], 'amplitude': [0.05, 0.1], 'frequency': [0.5, 0.3]},
    {'speed': [0.02, -0.01], 'amplitude': [0.04, 0.08], 'frequency': [0.4, 0.2]},
    {'speed': [0.015, -0.015], 'amplitude': [0.03, 0.09], 'frequency': [0.3, 0.4]},
    {'speed': [0.01, -0.02], 'amplitude': [0.05, 0.1], 'frequency': [0.5, 0.3]},
    {'speed': [0.02, -0.01], 'amplitude': [0.04, 0.08], 'frequency': [0.4, 0.2]},
    {'speed': [0.015, -0.015], 'amplitude': [0.03, 0.09], 'frequency': [0.3, 0.4]}
]

fig, ax = plt.subplots()
points = []
for i in range(15):
    point, = ax.plot([], [], 'wo', markersize=10)
    points.append(point)

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    ax.set_facecolor('black')
    return points

def update(frame):
    for i, point in enumerate(points):
        x = initial_positions[i][0] + movement_params[i]['speed'][0] * frame + \
            movement_params[i]['amplitude'][0] * np.sin(movement_params[i]['frequency'][0] * frame)
        y = initial_positions[i][1] + movement_params[i]['speed'][1] * frame + \
            movement_params[i]['amplitude'][1] * np.cos(movement_params[i]['frequency'][1] * frame)
        point.set_data(x, y)
    return points

ani = animation.FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True, interval=50)
plt.show()
