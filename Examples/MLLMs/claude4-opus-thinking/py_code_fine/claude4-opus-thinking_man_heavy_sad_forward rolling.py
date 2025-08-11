
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point lights
num_lights = 15

# Initialize point light positions (x, y)
# Some initial positions to represent body parts
points = np.zeros((num_lights, 2))
points[:, 0] = np.linspace(-0.5, 0.5, num_lights)  # X positions
points[:, 1] = 0  # Initial Y positions

# Initialize scatter plot
sc = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation update function
def update(frame):
    # Compute forward rolling motion
    # Y position follows a sinusoidal path to simulate rolling
    points[:, 0] += 0.1  # Moving forward

    # Update Y positions for a rolling effect
    points[0, 1] = -1 + np.sin(frame * 0.1)  # Head light
    points[1:5, 1] = -0.5 + np.sin(frame * 0.1)  # Upper body
    points[5:10, 1] = -0.7 + np.sin(frame * 0.1)  # Lower body
    points[10:, 1] = -0.5 + np.sin(frame * 0.1)  # Legs

    sc.set_offsets(points)  # Update the scatter plot with new positions
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.show()
