
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the body parts and their positions (simplified human skeleton)
body_parts = {
    'head': (0, 1.2),
    'neck': (0, 0.9),
    'torso': (0, 0.6),
    'pelvis': (0, 0.3),
    'left_shoulder': (-0.3, 0.6),
    'left_elbow': (-0.6, 0.3),
    'left_wrist': (-0.9, 0.0),
    'right_shoulder': (0.3, 0.6),
    'right_elbow': (0.6, 0.3),
    'right_wrist': (0.9, 0.0),
    'left_hip': (-0.3, 0.3),
    'left_knee': (-0.6, 0.0),
    'left_ankle': (-0.9, -0.3),
    'right_hip': (0.3, 0.3),
    'right_knee': (0.6, 0.0),
    'right_ankle': (0.9, -0.3)
}

# Initialize point lights
lights = {}
for part, (x, y) in body_parts.items():
    light = patches.Circle((x, y), 0.02, color='white', zorder=5)
    ax.add_patch(light)
    lights[part] = light

# Define motion parameters for a lying down action
def update(frame):
    # Simulate a smooth transition to lying down
    t = frame / 100.0
    if t < 1.0:
        # Rising from sitting to lying down
        head_y = 1.2 - (1.2 - 0.6) * t
        neck_y = 0.9 - (0.9 - 0.6) * t
        torso_y = 0.6 - (0.6 - 0.3) * t
        pelvis_y = 0.3 - (0.3 - 0.0) * t
        left_shoulder_y = 0.6 - (0.6 - 0.3) * t
        left_elbow_y = 0.3 - (0.3 - 0.0) * t
        left_wrist_y = 0.0 - (0.0 - (-0.3)) * t
        right_shoulder_y = 0.6 - (0.6 - 0.3) * t
        right_elbow_y = 0.3 - (0.3 - 0.0) * t
        right_wrist_y = 0.0 - (0.0 - (-0.3)) * t
        left_hip_y = 0.3 - (0.3 - 0.0) * t
        left_knee_y = 0.0 - (0.0 - (-0.3)) * t
        left_ankle_y = -0.3 - (-0.3 - (-0.6)) * t
        right_hip_y = 0.3 - (0.3 - 0.0) * t
        right_knee_y = 0.0 - (0.0 - (-0.3)) * t
        right_ankle_y = -0.3 - (-0.3 - (-0.6)) * t
    else:
        # Lying down
        head_y = 0.6
        neck_y = 0.6
        torso_y = 0.3
        pelvis_y = 0.0
        left_shoulder_y = 0.3
        left_elbow_y = 0.0
        left_wrist_y = -0.3
        right_shoulder_y = 0.3
        right_elbow_y = 0.0
        right_wrist_y = -0.3
        left_hip_y = 0.0
        left_knee_y = -0.3
        left_ankle_y = -0.6
        right_hip_y = 0.0
        right_knee_y = -0.3
        right_ankle_y = -0.6

    # Update positions
    lights['head'].set_center((0, head_y))
    lights['neck'].set_center((0, neck_y))
    lights['torso'].set_center((0, torso_y))
    lights['pelvis'].set_center((0, pelvis_y))
    lights['left_shoulder'].set_center((-0.3, left_shoulder_y))
    lights['left_elbow'].set_center((-0.6, left_elbow_y))
    lights['left_wrist'].set_center((-0.9, left_wrist_y))
    lights['right_shoulder'].set_center((0.3, right_shoulder_y))
    lights['right_elbow'].set_center((0.6, right_elbow_y))
    lights['right_wrist'].set_center((0.9, right_wrist_y))
    lights['left_hip'].set_center((-0.3, left_hip_y))
    lights['left_knee'].set_center((-0.6, left_knee_y))
    lights['left_ankle'].set_center((-0.9, left_ankle_y))
    lights['right_hip'].set_center((0.3, right_hip_y))
    lights['right_knee'].set_center((0.6, right_knee_y))
    lights['right_ankle'].set_center((0.9, right_ankle_y))

# Create the animation
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

plt.show()
