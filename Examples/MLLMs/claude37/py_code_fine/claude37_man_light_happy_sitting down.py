
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_points = 15
duration = 10  # Duration of the animation in seconds
fps = 30  # Frames per second
total_frames = duration * fps

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Initialize points for a happy man sitting down
# Point locations based on a rough skeleton for sitting down
# (x, y) coordinates
points = np.array([
    [0, 0.7],  # Head
    [-0.2, 0.5], [0.2, 0.5],  # Shoulders
    [-0.4, 0.2], [0.4, 0.2],  # Elbows
    [-0.25, 0], [0.25, 0],    # Hips
    [-0.5, -0.5], [0.5, -0.5], # Knees
    [-0.5, -1], [0.5, -1],    # Feet
    [0, -0.5],                # Center of the body (sitting)
    [-0.1, 0], [0.1, 0],      # Additional points for detail
    [0.35, -0.1], [-0.35, -0.1]
])

# Plot the initial points
point_lights, = ax.plot([], [], 'o', color='white', markersize=10)

def init():
    """Initialize the background of the animation."""
    point_lights.set_data([], [])
    return point_lights,

def update(frame):
    """Update the points for each frame to simulate motion."""
    # Define a simple motion pattern
    if frame < total_frames // 2:
        # Transition to a sitting position 
        y_offset = -0.5 + (frame / (total_frames // 2)) * 0.5
    else:
        # Sway slightly while sitting
        y_offset = -0.5 + (0.5 * np.sin((frame - (total_frames // 2)) / (total_frames // 2) * np.pi))

    # Set new positions with the y offset
    new_points = points.copy()
    new_points[:, 1] += y_offset
    point_lights.set_data(new_points[:, 0], new_points[:, 1])
    return point_lights,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True)
plt.show()
