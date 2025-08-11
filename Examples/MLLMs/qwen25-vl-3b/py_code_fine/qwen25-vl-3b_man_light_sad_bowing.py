
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point lights
lights = np.array([
    [0.4, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7],
    [0.4, 0.4], [0.5, 0.5], [0.6, 0.6],
    [0.7, 0.7], [0.8, 0.8], [0.9, 0.9],
    [0.4, 0.2], [0.5, 0.3], [0.6, 0.4]
])

# Define the direction of the bowing motion
direction = np.array([0.05, -0.05])  # Move slightly forward and downward

# Define the time step for the animation
dt = 0.01

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Plot the lights
for x, y in lights:
    ax.plot(x, y, 'o', markersize=10, color='white')

# Animate the bowing motion
for t in np.arange(0, 1, dt):
    lights[:, 0] += direction[0] * dt
    lights[:, 1] += direction[1] * dt
    ax.clear()
    for x, y in lights:
        ax.plot(x, y, 'o', markersize=10, color='white')
    fig.canvas.draw()

plt.show()
