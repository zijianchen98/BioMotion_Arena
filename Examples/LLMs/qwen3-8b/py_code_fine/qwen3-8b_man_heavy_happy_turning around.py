
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

# Define the 15 point-light positions (representing joints)
# These are approximate positions for a human body during a turning motion
# Positions are relative to the center of the body (origin)

# Define joint names and their approximate positions
joint_positions = {
    'head': (0, 0.6),
    'neck': (0, 0.4),
    'shoulder': (0.3, 0.2),
    'elbow': (0.3, 0.05),
    'wrist': (0.3, -0.1),
    'hand': (0.3, -0.2),
    'hip': (0, -0.3),
    'knee': (0, -0.5),
    'ankle': (0, -0.7),
    'foot': (0, -0.9),
    'spine': (0, 0.2),
    'upper_back': (0, 0.3),
    'lower_back': (0, 0.1),
    'shoulder_left': (-0.3, 0.2),
    'shoulder_right': (0.3, 0.2)
}

# Convert to a list of positions
light_positions = list(joint_positions.values())

# Create circles for the point-lights
points = [Circle((x, y), 0.02, color='white') for x, y in light_positions]
for point in points:
    ax.add_patch(point)

# Define the turning motion using a sine wave for smooth rotation
def update(frame):
    angle = frame * 0.05  # Control the speed of rotation
    for i, (x, y) in enumerate(light_positions):
        # Apply rotation around the origin
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        points[i].center = (new_x, new_y)
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
