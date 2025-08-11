
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point-lights
point_lights = [
    (0.1, 0.1, 0.1),  # 1
    (0.2, 0.2, 0.2),  # 2
    (0.3, 0.3, 0.3),  # 3
    (0.4, 0.4, 0.4),  # 4
    (0.5, 0.5, 0.5),  # 5
    (0.6, 0.6, 0.6),  # 6
    (0.7, 0.7, 0.7),  # 7
    (0.8, 0.8, 0.8),  # 8
    (0.9, 0.9, 0.9),  # 9
    (1.0, 1.0, 1.0),  # 10
    (1.1, 1.1, 1.1),  # 11
    (1.2, 1.2, 1.2),  # 12
    (1.3, 1.3, 1.3),  # 13
    (1.4, 1.4, 1.4),  # 14
    (1.5, 1.5, 1.5),  # 15
]

# Define the action (bowing)
def bowing(x):
    # Move the point-lights in a smooth, natural motion
    for i in range(len(point_lights)):
        point_lights[i] = (x + i * 0.01, 0.7, 0.1)
    return point_lights

# Create the animation
def animate(i):
    ax.clear()
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Bowing')
    point_lights = bowing(i)
    for light in point_lights:
        ax.scatter(light[0], light[1], color='white', s=10)

ani = animation.FuncAnimation(fig, animate, frames=range(100), interval=50)

plt.show()
