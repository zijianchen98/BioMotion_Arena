
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

# Define the jump action
def jump(action):
    if action == 'forward':
        # Jump forward
        lights[:, 0] += 0.1
        lights[:, 1] -= 0.1
    elif action == 'backward':
        # Jump backward
        lights[:, 0] -= 0.1
        lights[:, 1] += 0.1
    else:
        # Default to no action
        pass

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Plot the lights
for x, y in lights:
    ax.plot(x, y, 'o', markersize=10, color='white')

# Animate the jump
jump('forward')
plt.show()

