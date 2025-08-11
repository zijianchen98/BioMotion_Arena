
"""
This program creates an animated point‐light display of a “sad man with light weight” turning around.
It uses exactly 15 white dots on a black background to depict a simplified human skeleton.
The joints and limbs move with a smooth, cyclical gait and the entire body rotates in place to
simulate turning. The simulation uses biomechanically‐plausible (though simplified)
motion for the arms and legs.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define indices for each joint in our 15‐point skeleton:
# 0: Head
# 1: Left Shoulder
# 2: Right Shoulder
# 3: Left Elbow
# 4: Right Elbow
# 5: Left Wrist
# 6: Right Wrist
# 7: Neck
# 8: Left Hip
# 9: Right Hip
# 10: Left Knee
# 11: Right Knee
# 12: Left Ankle
# 13: Right Ankle
# 14: Pelvis (pivot reference)

# Base positions (in meters) in a local coordinate system.
# Vertical direction is y, horizontal is x.
base_positions = np.array([
    [0.00, 1.80],    # Head
    [-0.20,1.65],    # Left Shoulder
    [ 0.20,1.65],    # Right Shoulder
    [-0.40,1.45],    # Left Elbow
    [ 0.40,1.45],    # Right Elbow
    [-0.55,1.25],    # Left Wrist
    [ 0.55,1.25],    # Right Wrist
    [0.00,1.60],     # Neck
    [-0.20,1.00],    # Left Hip
    [ 0.20,1.00],    # Right Hip
    [-0.20,0.50],    # Left Knee
    [ 0.20,0.50],    # Right Knee
    [-0.20,0.00],    # Left Ankle
    [ 0.20,0.00],    # Right Ankle
    [0.00,0.95]      # Pelvis -- taken as the pivot for rotation
])

# Animation parameters
frames = 200           # total frames in one full turn
interval = 30          # milliseconds between frames
total_time = 2.0       # total duration in seconds (for gait cycle timing)

# Amplitudes for limb swinging (in meters)
amp_arm_elbow = 0.03
amp_arm_wrist = 0.05
amp_leg_knee  = 0.05
amp_leg_ankle = 0.08

# Frequency: one gait cycle per full turn (adjust if needed)
def gait_phase(frame):
    # phase goes from 0 to 2*pi over the whole sequence.
    return 2*np.pi * frame/frames

# Function to get joint positions for a given frame
def get_joint_positions(frame):
    # Copy the base positions
    pos = base_positions.copy()
    phase = gait_phase(frame)
    
    # Add cyclic limb swing offsets (in the local coordinate system)
    # Arms: swing in opposite directions
    pos[3, 0] += amp_arm_elbow * np.sin(phase)    # Left Elbow
    pos[5, 0] += amp_arm_wrist * np.sin(phase)      # Left Wrist
    pos[4, 0] += -amp_arm_elbow * np.sin(phase)     # Right Elbow
    pos[6, 0] += -amp_arm_wrist * np.sin(phase)     # Right Wrist

    # Legs: swing in opposite directions
    pos[10, 0] += amp_leg_knee * np.sin(phase)      # Left Knee
    pos[12, 0] += amp_leg_ankle * np.sin(phase)       # Left Ankle
    pos[11, 0] += -amp_leg_knee * np.sin(phase)       # Right Knee
    pos[13, 0] += -amp_leg_ankle * np.sin(phase)      # Right Ankle

    # The overall rotation angle of the body (simulate turning around in place)
    theta = 2*np.pi * frame/frames  # from 0 to 2*pi over the animation

    # Rotate all joints around the pelvis (index 14) to simulate turning.
    pivot = pos[14].copy()
    # Create 2D rotation matrix:
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    for i in range(len(pos)):
        pos[i] = pivot + R.dot(pos[i] - pivot)
    
    return pos

# Set up the plot: black background, no axes.
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor("black")
plt.axis("equal")
plt.xlim(-1.0, 1.0)
plt.ylim(-0.2, 2.2)
plt.axis("off")

# Initialize scatter for the 15 points.
scat = ax.scatter([], [], s=100, c='white')

# Animation update function.
def update(frame):
    positions = get_joint_positions(frame)
    # Scatter expects two arrays for x & y
    x = positions[:, 0]
    y = positions[:, 1]
    scat.set_offsets(np.column_stack((x,y)))
    return scat,

# Create animation using FuncAnimation.
anim = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)

# To display the animation, use plt.show(). 
# (Alternatively, one could save as a GIF or video file.)
if __name__ == '__main__':
    plt.show()