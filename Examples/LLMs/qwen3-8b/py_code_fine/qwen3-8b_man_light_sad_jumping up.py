
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the number of point lights
num_points = 15

# Define the body parts and their positions (simplified for a sad man jumping)
body_parts = {
    'head': (0, 0.5),
    'torso': (0, 0),
    'left_hip': (-0.3, -0.3),
    'right_hip': (0.3, -0.3),
    'left_knee': (-0.3, -0.5),
    'right_knee': (0.3, -0.5),
    'left_ankle': (-0.3, -0.7),
    'right_ankle': (0.3, -0.7),
    'left_shoulder': (-0.2, 0.2),
    'right_shoulder': (0.2, 0.2),
    'left_elbow': (-0.2, -0.1),
    'right_elbow': (0.2, -0.1),
    'left_wrist': (-0.2, -0.3),
    'right_wrist': (0.2, -0.3),
    'left_hand': (-0.2, -0.4),
    'right_hand': (0.2, -0.4)
}

# Create point lights
points = []
for part in body_parts:
    point, = ax.plot([], [], 'o', color='white', markersize=10)
    points.append(point)

# Define a function to update the animation
def update(frame):
    # Simulate a jumping motion with sine wave for vertical movement
    jump_amplitude = 0.2
    jump_frequency = 0.05
    jump_phase = frame * jump_frequency
    jump_y = 0.5 * np.sin(jump_phase) + 0.5  # Adjust for upward jump

    # Define a realistic motion for each body part
    for i, (part, (x, y)) in enumerate(body_parts.items()):
        # Adjust positions based on body part and jump
        if part == 'head':
            new_y = y + jump_y
        elif part in ['left_hand', 'right_hand', 'left_wrist', 'right_wrist']:
            new_y = y + jump_y
        elif part in ['left_elbow', 'right_elbow']:
            new_y = y + jump_y * 0.7
        elif part in ['left_shoulder', 'right_shoulder']:
            new_y = y + jump_y * 0.5
        elif part in ['left_knee', 'right_knee']:
            new_y = y + jump_y * 0.3
        elif part in ['left_ankle', 'right_ankle']:
            new_y = y + jump_y * 0.1
        elif part in ['left_hip', 'right_hip']:
            new_y = y + jump_y * 0.05
        elif part == 'torso':
            new_y = y + jump_y * 0.2
        else:
            new_y = y

        # Apply some slight oscillation for realism
        if part in ['left_hand', 'right_hand']:
            new_x = x + 0.05 * np.sin(frame * 0.1)
        elif part in ['left_wrist', 'right_wrist']:
            new_x = x + 0.03 * np.sin(frame * 0.1)
        elif part in ['left_elbow', 'right_elbow']:
            new_x = x + 0.02 * np.sin(frame * 0.1)
        elif part in ['left_shoulder', 'right_shoulder']:
            new_x = x + 0.01 * np.sin(frame * 0.1)
        else:
            new_x = x

        points[i].set_data(new_x, new_y)

    return points

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
