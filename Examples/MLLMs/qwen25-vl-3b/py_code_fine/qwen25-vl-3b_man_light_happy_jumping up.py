
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
light_coords = np.array([
    [0.1, 0.9], [0.2, 0.8], [0.3, 0.7],
    [0.4, 0.6], [0.5, 0.5], [0.6, 0.4],
    [0.7, 0.3], [0.8, 0.2], [0.9, 0.1],
    [0.1, 0.2], [0.2, 0.3], [0.3, 0.4],
    [0.4, 0.5], [0.5, 0.6], [0.6, 0.7]
])

# Define the jump action
def jump(action):
    # Jump up
    return np.array([0.5, 0.5]) + np.array([0.1, -0.2]) * action

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the lights
ax.scatter(light_coords[:, 0], light_coords[:, 1], color='white', s=100)

# Define the action
action = 0

# Update the lights based on the action
for _ in range(10):  # Number of frames
    light_coords[:, 1] = jump(action)
    ax.scatter(light_coords[:, 0], light_coords[:, 1], color='white', s=100)
    fig.canvas.draw()
    plt.pause(0.01)
    action += 0.1  # Increment the action value

plt.show()
