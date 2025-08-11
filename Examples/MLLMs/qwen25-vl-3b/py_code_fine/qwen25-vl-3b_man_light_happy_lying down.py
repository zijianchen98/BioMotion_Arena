
import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the 15 white point-lights
light_coords = np.array([
    [0.1, 0.1], [0.2, 0.2], [0.3, 0.3], [0.4, 0.4],
    [0.5, 0.5], [0.6, 0.6], [0.7, 0.7], [0.8, 0.8],
    [0.9, 0.9], [0.1, 0.9], [0.2, 0.8], [0.3, 0.7],
    [0.4, 0.6], [0.5, 0.5], [0.6, 0.4]
])

# Define the action parameters
action_speed = 0.05  # Speed at which the lights move
action_angle = 0.1   # Angle at which the lights move

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')

# Plot the lights
for x, y in light_coords:
    ax.plot(x, y, 'w', markersize=10)

# Animate the lights
def animate(i):
    for x, y in light_coords:
        ax.plot(x + action_speed * np.sin(action_angle * i), y + action_speed * np.cos(action_angle * i), 'w', markersize=10)
    fig.canvas.draw()

# Animate the plot
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
