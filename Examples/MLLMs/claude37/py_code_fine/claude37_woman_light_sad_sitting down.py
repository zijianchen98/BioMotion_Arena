
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Number of point-lights
num_points = 15

# Initial positions of the point-lights (representing a sad woman sitting down)
# Points are set in a way to mimic the sitting position
initial_y = np.array([-0.5, -0.5, -0.5, -0.3, -0.3, -0.3, -0.2, -0.2, -0.1, 0, 0, 0.2, 0.4, 0.4, 0.4])
initial_x = np.zeros(num_points)

# Create a scatter plot for the point-lights
points, = ax.plot(initial_x, initial_y, 'o', color='white', markersize=10)

# Animation update function
def update(frame):
    # Simulate the sitting down motion by adjusting the y-coordinates
    if frame < 30:
        # Partially down
        new_y = initial_y - (frame * 0.01)
    else:
        # At rest
        new_y = initial_y - (0.3)

    points.set_data(initial_x, new_y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)

# Display the animation
plt.show()
