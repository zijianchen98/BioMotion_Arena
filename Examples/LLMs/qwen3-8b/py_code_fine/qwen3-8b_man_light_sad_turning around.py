
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions
body_parts = {
    'head': (0, 0.5),
    'neck': (0, 0.3),
    'torso': (0, 0),
    'left_shoulder': (-0.2, 0),
    'right_shoulder': (0.2, 0),
    'left_elbow': (-0.4, 0.2),
    'right_elbow': (0.4, 0.2),
    'left_hand': (-0.6, 0.4),
    'right_hand': (0.6, 0.4),
    'left_hip': (-0.2, -0.4),
    'right_hip': (0.2, -0.4),
    'left_knee': (-0.4, -0.6),
    'right_knee': (0.4, -0.6),
    'left_foot': (-0.6, -0.8),
    'right_foot': (0.6, -0.8)
}

# Define the initial positions of the point lights
point_lights = [Circle(body_parts[part], 0.02, color='white') for part in body_parts]
for light in point_lights:
    ax.add_patch(light)

# Define a function to animate the motion
def animate(frame):
    # Define a simple turning motion around the y-axis
    angle = np.radians(frame * 3)
    for part in body_parts:
        x, y = body_parts[part]
        new_x = x * np.cos(angle) - y * np.sin(angle)
        new_y = x * np.sin(angle) + y * np.cos(angle)
        body_parts[part] = (new_x, new_y)

    # Update positions of point lights
    for light, (x, y) in zip(point_lights, body_parts.values()):
        light.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=False)

# Show the animation
plt.show()
