
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions (simplified human figure)
body_parts = {
    'head': (0, 1.2),
    'neck': (0, 1.0),
    'torso': (0, 0.5),
    'waist': (0, 0.3),
    'left_shoulder': (-0.5, 0.7),
    'left_elbow': (-0.8, 0.4),
    'left_hand': (-1.0, 0.1),
    'right_shoulder': (0.5, 0.7),
    'right_elbow': (0.8, 0.4),
    'right_hand': (1.0, 0.1),
    'left_hip': (-0.3, 0.1),
    'left_knee': (-0.5, -0.2),
    'left_ankle': (-0.7, -0.5),
    'right_hip': (0.3, 0.1),
    'right_knee': (0.5, -0.2),
    'right_ankle': (0.7, -0.5)
}

# Create circles for each point-light
point_lights = {}
for part, (x, y) in body_parts.items():
    circle = Circle((x, y), 0.02, color='white')
    ax.add_patch(circle)
    point_lights[part] = circle

# Define a function to update the positions of the point-lights
def update(frame):
    # Define a smooth turning motion around the y-axis
    angle = frame * 0.05  # Adjust speed as needed

    # Define a base rotation matrix
    cos_theta = np.cos(angle)
    sin_theta = np.sin(angle)

    # Apply rotation to each point-light
    for part, (x, y) in body_parts.items():
        new_x = x * cos_theta - y * sin_theta
        new_y = x * sin_theta + y * cos_theta
        point_lights[part].center = (new_x, new_y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=False)

plt.show()
