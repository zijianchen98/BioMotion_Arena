
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 point-lights
point_lights = np.array([
    [0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.4],
    [0.9, 0.5], [0.5, 0.6], [0.6, 0.7], [0.7, 0.8],
    [0.8, 0.7], [0.9, 0.6], [0.5, 0.7], [0.6, 0.8],
    [0.7, 0.9], [0.8, 0.8], [0.9, 0.7]
])

# Define the walking motion parameters
steps = 100
speed = 0.05
angle = 0.1

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the point-lights
ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)

# Animate the point-lights
for t in range(steps):
    # Calculate the new positions based on the walking motion
    x = np.cos(angle * t) * speed
    y = np.sin(angle * t) * speed
    
    # Update the position of each point-light
    for i in range(len(point_lights)):
        point_lights[i] += np.array([x, y])
    
    # Clip the point-lights within the bounds of the plot
    point_lights[point_lights[:, 0] > 1] = [1, 1]
    point_lights[point_lights[:, 0] < -1] = [-1, -1]
    point_lights[point_lights[:, 1] > 1] = [1, 1]
    point_lights[point_lights[:, 1] < -1] = [-1, -1]

    # Clear the previous frame
    ax.clear()
    
    # Plot the updated point-lights
    ax.plot(point_lights[:, 0], point_lights[:, 1], 'w.', markersize=5)
    
    # Update the plot
    fig.canvas.draw()

plt.show()
