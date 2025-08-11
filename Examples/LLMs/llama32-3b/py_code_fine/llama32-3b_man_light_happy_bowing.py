
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()

# Define the point-lights
lights = []
for i in range(15):
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 1)
    lights.append(ax.plot(x, y, 'w', lw=0.5)[0])

# Define the initial positions of the lights
initial_positions = np.array([[0.3, 0.3], [0.2, 0.6], [0.6, 0.6], [0.8, 0.2], [0.4, 0.1], [0.1, 0.9], [0.7, 0.9], [0.5, 0.5], [0.9, 0.5], [0.1, 0.1], [0.3, 0.7], [0.7, 0.3], [0.5, 0.8], [0.2, 0.4], [0.8, 0.4]])

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    for j in range(15):
        x = initial_positions[j, 0] + (i / 60) * (0.2 - initial_positions[j, 0])
        y = initial_positions[j, 1] + (i / 60) * (0.2 - initial_positions[j, 1])
        lights[j].set_data(x, y)
        lights[j].set_color('white')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=20, repeat=False)

plt.show()
