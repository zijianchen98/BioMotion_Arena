
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

# Define the 15 points representing the body parts of a sad man with heavy weight jumping
# Positions are relative and adjusted to simulate a realistic jumping motion

# Initial positions of the 15 points (approximate body parts)
initial_positions = np.array([
    [0.3, 0.5],   # Head
    [0.2, 0.4],   # Left eye
    [0.3, 0.4],   # Right eye
    [0.25, 0.3],  # Left eyebrow
    [0.35, 0.3],  # Right eyebrow
    [0.3, 0.2],   # Nose
    [0.2, 0.1],   # Left cheek
    [0.4, 0.1],   # Right cheek
    [0.2, 0.0],   # Left shoulder
    [0.4, 0.0],   # Right shoulder
    [0.1, -0.1],  # Left elbow
    [0.3, -0.2],  # Right elbow
    [0.0, -0.3],  # Left hand
    [0.4, -0.3],  # Right hand
    [0.2, -0.4],  # Hip
])

# Define a function to simulate jumping motion
def jump_motion(t, total_time=2.0):
    # Normalize time
    t_norm = t / total_time
    # Jump up and down
    if t_norm < 0.5:
        y = 0.5 * (1 - np.cos(np.pi * t_norm))  # Upward motion
    else:
        y = 0.5 * (1 - np.cos(np.pi * (1 - t_norm)))  # Downward motion
    return y

# Create circles for the point lights
points = [Circle((x, y), 0.02, color='white') for x, y in initial_positions]
for point in points:
    ax.add_patch(point)

# Animation function
def animate(t):
    # Compute jump height
    jump_height = jump_motion(t)
    # Apply jump to the body parts
    for i, (x, y) in enumerate(initial_positions):
        # Apply some body movement based on part
        if i == 0:  # Head
            y += jump_height * 0.6
        elif i == 8 or i == 9:  # Shoulders
            y += jump_height * 0.4
        elif i == 10 or i == 11:  # Elbows
            y += jump_height * 0.2
        elif i == 12 or i == 13:  # Hands
            y += jump_height * 0.1
        elif i == 14:  # Hip
            y += jump_height * 0.3
        # Update position
        points[i].center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

plt.show()
