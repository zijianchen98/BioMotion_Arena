
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

# Define the body parts and their positions relative to the center
body_parts = {
    'head': (0, 0.6),
    'torso': (0, 0),
    'left_shoulder': (-0.2, 0.3),
    'right_shoulder': (0.2, 0.3),
    'left_hip': (-0.3, -0.3),
    'right_hip': (0.3, -0.3),
    'left_knee': (-0.3, -0.6),
    'right_knee': (0.3, -0.6),
    'left_ankle': (-0.3, -0.9),
    'right_ankle': (0.3, -0.9),
    'left_elbow': (-0.4, 0.0),
    'right_elbow': (0.4, 0.0),
    'left_wrist': (-0.4, -0.2),
    'right_wrist': (0.4, -0.2)
}

# Create circles for each point-light
point_lights = {}
for part, (x, y) in body_parts.items():
    circle = Circle((x, y), 0.02, color='white')
    ax.add_patch(circle)
    point_lights[part] = circle

# Define a function to update the position of each point-light
def update(frame):
    # Simulate a running motion with sine waves for smooth movement
    t = frame / 10.0
    for part, (x, y) in body_parts.items():
        if part == 'head':
            x = np.sin(t * 2) * 0.1 + 0.0
            y = np.cos(t * 2) * 0.1 + 0.6
        elif part == 'torso':
            x = np.sin(t * 2) * 0.1 + 0.0
            y = np.cos(t * 2) * 0.1 + 0.0
        elif part in ['left_shoulder', 'right_shoulder']:
            x = np.sin(t * 2 + (np.pi if part == 'left_shoulder' else 0)) * 0.1 + (part[0] == 'l') * -0.2
            y = np.cos(t * 2) * 0.1 + 0.3
        elif part in ['left_hip', 'right_hip']:
            x = np.sin(t * 2 + (np.pi if part == 'left_hip' else 0)) * 0.1 + (part[0] == 'l') * -0.3
            y = np.cos(t * 2) * 0.1 - 0.3
        elif part in ['left_knee', 'right_knee']:
            x = np.sin(t * 2 + (np.pi if part == 'left_knee' else 0)) * 0.1 + (part[0] == 'l') * -0.3
            y = np.cos(t * 2) * 0.1 - 0.6
        elif part in ['left_ankle', 'right_ankle']:
            x = np.sin(t * 2 + (np.pi if part == 'left_ankle' else 0)) * 0.1 + (part[0] == 'l') * -0.3
            y = np.cos(t * 2) * 0.1 - 0.9
        elif part in ['left_elbow', 'right_elbow']:
            x = np.sin(t * 2 + (np.pi if part == 'left_elbow' else 0)) * 0.1 + (part[0] == 'l') * -0.4
            y = np.cos(t * 2) * 0.1 + 0.0
        elif part in ['left_wrist', 'right_wrist']:
            x = np.sin(t * 2 + (np.pi if part == 'left_wrist' else 0)) * 0.1 + (part[0] == 'l') * -0.4
            y = np.cos(t * 2) * 0.1 - 0.2

        point_lights[part].set_center((x, y))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
