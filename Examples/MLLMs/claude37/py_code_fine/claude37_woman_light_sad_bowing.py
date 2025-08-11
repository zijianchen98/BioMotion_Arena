
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
points, = ax.plot([], [], 'bo', markersize=10)

# Define initial positions of the 15 points (body parts)
body_parts = np.array([
    [0, 3],   # Head
    [-1, 2],  # Left shoulder
    [1, 2],   # Right shoulder
    [-1, 1],  # Left elbow
    [1, 1],   # Right elbow
    [-1, 0],  # Left wrist
    [1, 0],   # Right wrist
    [-2, 1],  # Left hip
    [2, 1],   # Right hip
    [-2, -2], # Left knee
    [2, -2],  # Right knee
    [-1.5, -3], # Left ankle
    [1.5, -3],  # Right ankle
    [0, -1],   # Torso
    [0, 0]     # Center of the body
])

# Bowing motion (downward motion)
def update(frame):
    # Compute the new positions based on a simple bowing motion
    bow = np.sin(frame / 10) * np.array([0, -1])  # downward bowing motion
    points.set_data(body_parts[:, 0] + bow[0], body_parts[:, 1] + bow[1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True, interval=100)

# Display the animation
plt.show()
