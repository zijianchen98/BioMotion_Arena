
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.7, 0.4], [-0.3, 0.4], [0.3, 0.4], [0.7, 0.4],
    [-0.8, 0.1], [-0.4, 0.1], [0, 0.1], [0.4, 0.1], [0.8, 0.1],
    [-0.3, -0.2], [0.3, -0.2]
])

# Define the movement parameters for each point
movement_params = [
    {'speed': [0.01, 0.02], 'oscillation': [0.05, 0.05]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]},
    {'speed': [0.015, 0.015], 'oscillation': [0.03, 0.03]},
    {'speed': [0.01, 0.02], 'oscillation': [0.05, 0.05]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]},
    {'speed': [0.015, 0.015], 'oscillation': [0.03, 0.03]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]},
    {'speed': [0.015, 0.015], 'oscillation': [0.03, 0.03]},
    {'speed': [0.01, 0.02], 'oscillation': [0.05, 0.05]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]},
    {'speed': [0.015, 0.015], 'oscillation': [0.03, 0.03]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]},
    {'speed': [0.015, 0.015], 'oscillation': [0.03, 0.03]},
    {'speed': [0.01, 0.02], 'oscillation': [0.05, 0.05]},
    {'speed': [0.02, 0.01], 'oscillation': [0.04, 0.04]}
]

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
points = [ax.plot([], [], 'w.', markersize=10)[0] for _ in range(15)]

def init():
    for point in points:
        point.set_data([], [])
    return points

def animate(i):
    for j, point in enumerate(points):
        x, y = initial_positions[j]
        speed = movement_params[j]['speed']
        oscillation = movement_params[j]['oscillation']
        x += speed[0] * i + oscillation[0] * np.sin(0.1 * i)
        y += speed[1] * i + oscillation[1] * np.cos(0.1 * i)
        point.set_data(x, y)
    return points

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()
