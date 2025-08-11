
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

# Define the body parts and their positions (simplified for a waving hand)
body_parts = {
    'torso': (0, 0),
    'left_shoulder': (-0.3, 0.2),
    'right_shoulder': (0.3, 0.2),
    'left_elbow': (-0.2, 0.1),
    'right_elbow': (0.2, 0.1),
    'left_hand': (-0.1, 0.05),
    'right_hand': (0.1, 0.05),
    'left_wrist': (-0.15, 0.02),
    'right_wrist': (0.15, 0.02),
    'left_knee': (-0.2, -0.2),
    'right_knee': (0.2, -0.2),
    'left_ankle': (-0.15, -0.3),
    'right_ankle': (0.15, -0.3),
    'head': (0, 0.3)
}

# Create points for the light sources
points = [patches.Circle(body_parts[part], 0.02, color='white') for part in body_parts]
for point in points:
    ax.add_patch(point)

# Define a function to animate the motion
def animate(frame):
    # Define a simple waving motion for the hand
    hand_angle = np.sin(frame * 0.05)
    hand_x = np.cos(hand_angle) * 0.05
    hand_y = np.sin(hand_angle) * 0.05

    # Update the positions of the points
    for i, part in enumerate(body_parts):
        if part == 'left_hand':
            body_parts[part] = (-0.1 + hand_x, 0.05 + hand_y)
        elif part == 'right_hand':
            body_parts[part] = (0.1 + hand_x, 0.05 + hand_y)
        elif part == 'left_wrist':
            body_parts[part] = (-0.15 + hand_x, 0.02 + hand_y)
        elif part == 'right_wrist':
            body_parts[part] = (0.15 + hand_x, 0.02 + hand_y)
        elif part == 'left_elbow':
            body_parts[part] = (-0.2 + hand_x, 0.1 + hand_y)
        elif part == 'right_elbow':
            body_parts[part] = (0.2 + hand_x, 0.1 + hand_y)
        elif part == 'left_knee':
            body_parts[part] = (-0.2, -0.2)
        elif part == 'right_knee':
            body_parts[part] = (0.2, -0.2)
        elif part == 'left_ankle':
            body_parts[part] = (-0.15, -0.3)
        elif part == 'right_ankle':
            body_parts[part] = (0.15, -0.3)
        elif part == 'head':
            body_parts[part] = (0, 0.3)
        elif part == 'torso':
            body_parts[part] = (0, 0)
        elif part == 'left_shoulder':
            body_parts[part] = (-0.3, 0.2)
        elif part == 'right_shoulder':
            body_parts[part] = (0.3, 0.2)

    # Update the positions of the points
    for i, point in enumerate(points):
        point.set_center(body_parts[list(body_parts.keys())[i]])

# Create the animation
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

# Show the animation
plt.show()
