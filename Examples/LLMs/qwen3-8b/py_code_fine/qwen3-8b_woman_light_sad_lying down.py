
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Define the body parts and their positions (approximate for a sad woman lying down)
body_parts = {
    'head': (0, 0.5),
    'neck': (0, 0.3),
    'torso': (0, 0.1),
    'right_shoulder': (0.2, 0.1),
    'right_elbow': (0.3, 0.05),
    'right_hand': (0.4, 0.02),
    'left_shoulder': (-0.2, 0.1),
    'left_elbow': (-0.3, 0.05),
    'left_hand': (-0.4, 0.02),
    'right_hip': (0.1, -0.2),
    'right_knee': (0.2, -0.3),
    'right_ankle': (0.3, -0.4),
    'left_hip': (-0.1, -0.2),
    'left_knee': (-0.2, -0.3),
    'left_ankle': (-0.3, -0.4)
}

# Create point-light circles
points = []
for part in body_parts:
    circle = Circle(body_parts[part], 0.02, color='white')
    ax.add_patch(circle)
    points.append(circle)

# Define a function to animate the motion
def animate(frame):
    # Define smooth motion for each body part (simulating a sad woman lying down)
    for part in body_parts:
        x, y = body_parts[part]
        if part == 'head':
            new_x = x + 0.02 * np.sin(frame * 0.05)
            new_y = y + 0.01 * np.sin(frame * 0.05)
        elif part == 'neck':
            new_x = x + 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.01 * np.sin(frame * 0.05)
        elif part == 'torso':
            new_x = x + 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.02 * np.sin(frame * 0.05)
        elif part == 'right_shoulder':
            new_x = x + 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.02 * np.sin(frame * 0.05)
        elif part == 'right_elbow':
            new_x = x + 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.03 * np.sin(frame * 0.05)
        elif part == 'right_hand':
            new_x = x + 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.04 * np.sin(frame * 0.05)
        elif part == 'left_shoulder':
            new_x = x - 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.02 * np.sin(frame * 0.05)
        elif part == 'left_elbow':
            new_x = x - 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.03 * np.sin(frame * 0.05)
        elif part == 'left_hand':
            new_x = x - 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.04 * np.sin(frame * 0.05)
        elif part == 'right_hip':
            new_x = x + 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.03 * np.sin(frame * 0.05)
        elif part == 'right_knee':
            new_x = x + 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.04 * np.sin(frame * 0.05)
        elif part == 'right_ankle':
            new_x = x + 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.05 * np.sin(frame * 0.05)
        elif part == 'left_hip':
            new_x = x - 0.01 * np.sin(frame * 0.05)
            new_y = y + 0.03 * np.sin(frame * 0.05)
        elif part == 'left_knee':
            new_x = x - 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.04 * np.sin(frame * 0.05)
        elif part == 'left_ankle':
            new_x = x - 0.005 * np.sin(frame * 0.05)
            new_y = y + 0.05 * np.sin(frame * 0.05)
        else:
            new_x, new_y = x, y

        points[body_parts.index(part)].set_center((new_x, new_y))

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=False)

plt.show()
