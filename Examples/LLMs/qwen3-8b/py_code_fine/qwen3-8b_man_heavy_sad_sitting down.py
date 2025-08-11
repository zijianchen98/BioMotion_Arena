
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 points representing the body parts of a person sitting down
# Positions are relative to the center of the screen
body_points = np.array([
    [0, 0],          # Hip center
    [0.2, 0.1],      # Right hip
    [-0.2, 0.1],     # Left hip
    [0.2, -0.2],     # Right knee
    [-0.2, -0.2],    # Left knee
    [0.2, -0.4],     # Right ankle
    [-0.2, -0.4],    # Left ankle
    [0, 0.2],        # Torso
    [0.1, 0.3],      # Right shoulder
    [-0.1, 0.3],     # Left shoulder
    [0.1, 0.5],      # Right elbow
    [-0.1, 0.5],     # Left elbow
    [0.1, 0.7],      # Right wrist
    [-0.1, 0.7],     # Left wrist
    [0, 0.8]         # Head
])

# Define a function to simulate the sitting motion over time
def animate(t):
    # Time-based parameters for motion
    t_norm = t / 10.0  # Normalize to 0-1
    t_cycle = t_norm * 2 * np.pi  # Cycle through motion

    # Define motion for each body part
    # Hip and torso move down and forward
    body_points[:, 1] = 0.1 * (1 - np.cos(t_cycle)) - 0.2 * np.sin(t_cycle)
    body_points[:, 0] = 0.05 * np.sin(t_cycle)

    # Knees and ankles move down and back
    body_points[3:5, 1] = -0.2 * (1 - np.cos(t_cycle)) - 0.2 * np.sin(t_cycle)
    body_points[3:5, 0] = -0.05 * np.sin(t_cycle)
    body_points[5:7, 1] = -0.4 * (1 - np.cos(t_cycle)) - 0.2 * np.sin(t_cycle)
    body_points[5:7, 0] = -0.1 * np.sin(t_cycle)

    # Elbows and wrists move down and forward
    body_points[10:12, 1] = 0.5 * (1 - np.cos(t_cycle)) - 0.2 * np.sin(t_cycle)
    body_points[10:12, 0] = 0.05 * np.sin(t_cycle)
    body_points[12:14, 1] = 0.7 * (1 - np.cos(t_cycle)) - 0.2 * np.sin(t_cycle)
    body_points[12:14, 0] = 0.05 * np.sin(t_cycle)

    # Head moves slightly forward
    body_points[14, 0] = 0.1 * np.sin(t_cycle)

    # Clear previous points
    for circle in circles:
        circle.remove()

    # Draw new points
    circles = [ax.add_patch(Circle((x, y), 0.02, color='white')) for x, y in body_points]

    return circles

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
