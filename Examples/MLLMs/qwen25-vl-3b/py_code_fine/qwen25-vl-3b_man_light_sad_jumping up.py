
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
    if action == 'up':
        # Jump up
        return np.array([0.5, 0.5]) + np.array([-0.1, -0.1])
    elif action == 'down':
        # Jump down
        return np.array([0.5, 0.5]) + np.array([0.1, 0.1])
    else:
        raise ValueError("Action must be 'up' or 'down'")

# Apply the jump action
action = 'up'
jumped_lights = jump(action)

# Plot the lights
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

for x, y in lights:
    ax.plot(x, y, 'w.', markersize=10)

for x, y in jumped_lights:
    ax.plot(x, y, 'w.', markersize=10)

plt.show()
