
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')

# Define point-light locations for a running figure
# The coordinates can be modified to create a better running motion
points = np.array([[4, 1], [5, 1], [4, 3], [5, 3], [4, 5], 
                   [5, 5], [4, 7], [5, 7], [4, 9], [5, 9], 
                   [3.5, 6], [5.5, 6], [3.5, 4], [5.5, 4], 
                   [3.5, 2], [5.5, 2]])

# Initialize point lights on the plot
lights = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def animate(frame):
    # Update positions to simulate running
    phase = np.sin(np.radians(frame * 10))
    changed_points = points.copy()
    changed_points[:, 0] += phase * 0.05  # Change x position for running effect

    # Clear previous points and update with new positions
    lights.set_offsets(changed_points)

    return lights,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 360, 1), interval=50, blit=True)

# Show the animation
plt.show()
