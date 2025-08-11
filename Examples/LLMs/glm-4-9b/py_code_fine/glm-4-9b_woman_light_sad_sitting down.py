
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up the parameters
num_points = 15
duration = 100  # frames
fig, ax = plt.subplots()

# Create a black background
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Position of the lights for a person sitting down (example trajectory)
# These coordinates would need to be adjusted to actually represent a person sitting down
# For simplicity, we're using a circular motion that is gradually descending
def update(frame):
    ax.clear()
    ax.set_facecolor('black')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    theta = np.linspace(0, 2*np.pi, num_points)
    radius = 5 - 0.05*frame  # Decreasing radius to simulate sitting down
    x = 5 + radius * np.cos(theta)
    y = 5 + radius * np.sin(theta)

    # Plotting the point-lights
    ax.scatter(x, y, color='white', s=10)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=duration, interval=50)
plt.show()
