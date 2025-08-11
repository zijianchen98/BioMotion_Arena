
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and the line that we wish to animate
fig, ax = plt.subplots()
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 8)
point, = ax.plot([], [], 'bo')  # Plot points as blue dots

# Animation configuration parameters
frames = 100  # Total number of animation frames
interval = 50  # Time between frames in milliseconds (1000ms = 1s)

# Initialize the points location matrix (2D coordinates for each point)
num_points = 15
positions = np.random.rand(num_points, 2)

def init():
    """Initialize the background of the animation."""
    point.set_data([], [])
    return point,

def update(frame):
    """Update the position of the points in the animation."""
    global positions

    # Update positions (example with simple incremental movement)
    positions[:, 0] += 0.1  # Change in x coordinates (Right)
    positions[:, 1] -= 0.1  # Change in y coordinates (Down)

    # Keep points within boundaries by resetting position if out of bounds
    out_of_bounds_x = np.where(positions[:, 0] > 10)
    positions[out_of_bounds_x, 0] = -1
    out_of_bounds_y = np.where(positions[:, 1] < -1)
    positions[out_of_bounds_y, 1] = 9

    # Set data for the points (x and y coordinates)
    point.set_data(positions[:, 0], positions[:, 1])
    return point,

# Create the animation using the update function and frame range
ani = animation.FuncAnimation(fig, update, range(frames), init_func=init, blit=True, interval=interval)

# Adjust the plot style (black background and no axis)
ax.set_facecolor('black')
ax.axis('off')

plt.show()
