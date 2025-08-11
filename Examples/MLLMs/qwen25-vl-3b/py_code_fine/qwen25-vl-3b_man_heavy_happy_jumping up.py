
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.4],
    [0.9, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8],
    [0.8, 0.7], [0.9, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7]
])

# Define the jump action
def jump(action):
    # Jump up
    for i in range(len(point_lights)):
        point_lights[i][0] += 0.1 * np.sin(i / 10)
        point_lights[i][1] -= 0.1 * np.cos(i / 10)

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point-lights
ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)

# Animate the jump
for _ in range(10):
    jump('jump')
    plt.pause(0.01)

plt.show()
