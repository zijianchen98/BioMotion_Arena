
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point lights
num_points = 15

# Initialize the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 1])  # Set x-axis limits
ax.set_ylim([0, 1])  # Set y-axis limits
ax.set_aspect('equal')  # Ensure equal aspect ratio
ax.set_xticks([])  # Remove x-axis ticks
ax.set_yticks([])  # Remove y-axis ticks
ax.set_facecolor('black') # Set background color to black


# Initialize point lights with random positions
points = np.random.rand(num_points, 2)

# Create scatter plot for the point lights
scat = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')


def animate(i):
    # Update point light positions based on rolling motion pattern

    # Example rolling motion (replace with your desired rolling logic)
    angle = i * 0.05  # Adjust animation speed
    center_x = 0.5 + 0.2 * np.sin(angle)
    center_y = 0.5 + 0.2 * np.cos(angle)
    radius = 0.1

    angles = np.linspace(0, 2 * np.pi, num_points, endpoint=False)
    x = center_x + radius * np.cos(angles) + 0.1 * np.sin(angle * 5)  # Add some wobble
    y = center_y + radius * np.sin(angles) + 0.1 * np.cos(angle * 3) # Add some wobble

    points[:, 0] = x + np.random.normal(0, 0.01, num_points) # introduce noise
    points[:, 1] = y + np.random.normal(0, 0.01, num_points) # introduce noise


    # Update the scatter plot data
    scat.set_offsets(points)

    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=range(200), interval=50, blit=True)

# Show the plot. Note that 'inline' may not work consistently across environments. Consider saving as mp4 for broader usability.
plt.show()

# Save the animation (optional)
# ani.save('rolling_point_lights.mp4', writer='ffmpeg')


