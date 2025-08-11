
"""
Point-light stimulus animation showing a sad, heavy woman jumping forward.
The animation depicts a 15‐point representation of a human figure (head, neck, torso,
shoulders, elbows, hands, hips, knees and feet) against a black background.
The motion simulates a single heavy–weight jump forward with biomechanically plausible, smooth motion.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the body joints relative offsets (in “body‐center” coordinates)
# The torso (or “body center”) is taken as (0,0); all others are defined relative to it.
# For a "sad" posture we lower the head a bit.
joints_offsets = {
    "head":         (0.0, 0.12),    # slightly drooped head for a sad expression
    "neck":         (0.0, 0.10),
    "torso":        (0.0, 0.0),
    "left_shoulder":(-0.05, 0.08),
    "right_shoulder":(0.05, 0.08),
    "left_elbow":   (-0.11, 0.05),
    "right_elbow":  (0.11, 0.05),
    "left_hand":    (-0.14, 0.0),
    "right_hand":   (0.14, 0.0),
    "left_hip":     (-0.04, -0.1),
    "right_hip":    (0.04, -0.1),
    "left_knee":    (-0.04, -0.25),
    "right_knee":   (0.04, -0.25),
    "left_foot":    (-0.04, -0.4),
    "right_foot":   (0.04, -0.4),
}

# Order of joints (to have exactly 15 points)
joint_names = ["head", "neck", "torso",
               "left_shoulder", "right_shoulder",
               "left_elbow", "right_elbow",
               "left_hand", "right_hand",
               "left_hip", "right_hip",
               "left_knee", "right_knee",
               "left_foot", "right_foot"]

# Animation parameters
n_frames = 100          # number of animation frames for one jump cycle
interval = 30           # milliseconds between frames
duration = 1.0          # normalized duration (t from 0 to 1) for the jump cycle

# Global jump parameters
horizontal_distance = 1.0    # total forward distance of the jump
jump_peak = 0.3              # maximum vertical jump height (additional to baseline)
baseline_center_y = 0.5      # baseline vertical position of the torso center
# For a heavy, weighted jump the movement is not exaggerated

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor('black')
ax.axis('equal')
ax.set_xlim(-0.1, horizontal_distance + 0.3)
ax.set_ylim(-0.6, 1.2)
ax.axis('off')  # Hide axes for stimulus view

# Initialize scatter plot for 15 point-lights (white markers)
scatter = ax.scatter([], [], c='white', s=80)

def update(frame):
    # Normalize time t in [0, 1]
    t = (frame % n_frames) / (n_frames - 1)
    
    # Global movement of the subject's center (torso)
    # Horizontal: constant forward displacement; Vertical: parabolic (jump arc)
    center_x = horizontal_distance * t
    # A simple parabolic jump: 4A*t*(1-t)
    center_y = baseline_center_y + jump_peak * 4 * t * (1 - t)
    center = np.array([center_x, center_y])
    
    # For additional natural movement we add slight arm and leg oscillations.
    # (These modulations are subtle and help simulate biomechanically plausible motion.)
    
    # Prepare list for updated joint positions.
    points = []
    for name in joint_names:
        base_offset = np.array(joints_offsets[name])
        # Start with no modulation.
        mod = np.array([0.0, 0.0])
        # For the arms, simulate a small vertical swing (as if counterbalancing the jump)
        if name in ["left_hand", "right_hand"]:
            mod[1] = 0.02 * np.sin(2*np.pi*t)
        elif name in ["left_elbow", "right_elbow"]:
            mod[1] = 0.01 * np.sin(2*np.pi*t)
        # For the feet, add a slight horizontal shift to simulate a push-off and landing effect.
        elif name == "left_foot":
            mod[0] = 0.01 * np.cos(2*np.pi*t)
        elif name == "right_foot":
            mod[0] = 0.01 * np.cos(2*np.pi*t + np.pi)
        # For shoulders, a tiny vertical modulation.
        elif name in ["left_shoulder", "right_shoulder"]:
            mod[1] = 0.005 * np.sin(2*np.pi*t + np.pi/4)
        
        # Compute the absolute joint position.
        joint_position = center + base_offset + mod
        points.append(joint_position)
    
    # Update scatter plot positions
    scatter.set_offsets(np.array(points))
    return scatter,

# Create animation
anim = FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=True)

plt.show()