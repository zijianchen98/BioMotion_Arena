
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

# Define the 15 body joints (simplified human skeleton)
# Positions are relative to the center of the body
body_joints = np.array([
    [0, 0],        # Hip center
    [0.2, 0],      # Right hip
    [0.3, 0.1],    # Right knee
    [0.2, 0.2],    # Right ankle
    [-0.2, 0],     # Left hip
    [-0.3, 0.1],   # Left knee
    [-0.2, 0.2],   # Left ankle
    [0, 0.4],      # Torso
    [0.1, 0.6],    # Right shoulder
    [0.15, 0.8],   # Right elbow
    [0.1, 0.95],   # Right wrist
    [-0.1, 0.6],   # Left shoulder
    [-0.15, 0.8],  # Left elbow
    [-0.1, 0.95],  # Left wrist
    [0, 0.95]      # Head
])

# Define a function to simulate the motion of a sitting down action
def animate(i):
    # Scale down the motion over time
    t = i / 100.0
    # Simulate the sitting down motion by lowering the body and bending legs
    # and moving the head down
    body_joints[:, 1] -= 0.05 * t
    body_joints[1:4, 1] += 0.05 * t
    body_joints[5:8, 1] += 0.05 * t
    body_joints[13:16, 1] -= 0.05 * t

    # Clear the previous points
    for circle in circles:
        circle.remove()

    # Create new points
    circles = [Circle((body_joints[i][0], body_joints[i][1]), 0.02, color='white') for i in range(15)]
    for circle in circles:
        ax.add_patch(circle)

    return circles

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

plt.show()
