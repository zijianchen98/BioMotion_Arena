
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

# Define the body parts and their positions (simplified for a waving hand)
body_parts = {
    'head': np.array([0, 0.7]),
    'torso': np.array([0, 0.3]),
    'left_hand': np.array([0.3, 0.1]),
    'right_hand': np.array([-0.3, 0.1]),
    'left_elbow': np.array([0.2, 0.3]),
    'right_elbow': np.array([-0.2, 0.3]),
    'left_wrist': np.array([0.3, 0.2]),
    'right_wrist': np.array([-0.3, 0.2]),
    'left_shoulder': np.array([0.3, 0.5]),
    'right_shoulder': np.array([-0.3, 0.5]),
    'left_hip': np.array([0.2, -0.3]),
    'right_hip': np.array([-0.2, -0.3]),
    'left_knee': np.array([0.2, -0.5]),
    'right_knee': np.array([-0.2, -0.5]),
    'left_ankle': np.array([0.2, -0.7]),
    'right_ankle': np.array([-0.2, -0.7]),
}

# Define a function to simulate realistic motion for a waving hand
def animate_hand(t):
    # Waving motion: hand moves back and forth
    hand_x = 0.3 * np.sin(2 * np.pi * t / 2)
    hand_y = 0.1 + 0.05 * np.sin(2 * np.pi * t / 1)
    elbow_x = 0.2 * np.sin(2 * np.pi * t / 3)
    elbow_y = 0.3 + 0.05 * np.sin(2 * np.pi * t / 2)
    wrist_x = hand_x + 0.1 * np.sin(2 * np.pi * t / 4)
    wrist_y = hand_y + 0.05 * np.sin(2 * np.pi * t / 3)
    shoulder_x = 0.3 + 0.05 * np.sin(2 * np.pi * t / 5)
    shoulder_y = 0.5 + 0.05 * np.sin(2 * np.pi * t / 4)
    return hand_x, hand_y, elbow_x, elbow_y, wrist_x, wrist_y, shoulder_x, shoulder_y

# Create a list of point lights
point_lights = []
for part in body_parts:
    x, y = body_parts[part]
    light = Circle((x, y), 0.02, color='white')
    ax.add_patch(light)
    point_lights.append(light)

# Animation function
def update(frame):
    t = frame / 60.0  # Normalize time
    hand_x, hand_y, elbow_x, elbow_y, wrist_x, wrist_y, shoulder_x, shoulder_y = animate_hand(t)

    # Update positions of the hand and related joints
    body_parts['left_hand'][0] = hand_x
    body_parts['left_hand'][1] = hand_y
    body_parts['left_elbow'][0] = elbow_x
    body_parts['left_elbow'][1] = elbow_y
    body_parts['left_wrist'][0] = wrist_x
    body_parts['left_wrist'][1] = wrist_y
    body_parts['left_shoulder'][0] = shoulder_x
    body_parts['left_shoulder'][1] = shoulder_y

    # Update all point lights
    for i, part in enumerate(body_parts):
        x, y = body_parts[part]
        point_lights[i].center = (x, y)

    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
