
"""
This program shows an animation of a happy, light‐weight man jumping forward,
represented as a point‐light stimulus. The “skeleton” is drawn using exactly 15 white
points against a black background. The joints of the figure (head, shoulders, elbows,
wrists, hips, knees, ankles and toes) move in a biomechanically plausible way as
he performs a jumping‐forward action.
  
Joints (in order):
  1: Head 
  2: Left Shoulder
  3: Right Shoulder
  4: Left Elbow
  5: Right Elbow
  6: Left Wrist
  7: Right Wrist
  8: Left Hip
  9: Right Hip
 10: Left Knee
 11: Right Knee
 12: Left Ankle
 13: Right Ankle
 14: Left Toe
 15: Right Toe
     
The animation uses matplotlib’s FuncAnimation.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Global parameters for the jump motion.
total_frames = 120
jump_distance = 3.0      # horizontal distance traveled during the jump
max_jump_height = 1.0    # maximum additional height at jump apex (above normal hip height)
base_hip_y = 1.0         # normal hip height when standing
crouch_depth = 0.2       # how much the hips lower during crouch/landing
arm_swing_amplitude = 0.1  # amplitude for arm sweep

def get_joint_positions(nt):
    """
    Compute and return the positions of the 15 joints for the current normalized time nt,
    where nt is in [0,1].
    """
    # --------------------------------------------------------------------------
    # Compute hip center trajectory
    # Horizontal: linear from 0 to jump_distance.
    hip_center_x = jump_distance * nt
    # Vertical jump trajectory: a parabolic arc that is 0 at start and end and peaks at nt=0.5.
    jump_y = 4 * max_jump_height * nt * (1 - nt)
    # Crouch adjustments in early (0-0.2) and late (0.8-1) phases.
    if nt < 0.2:
        crouch_offset = -crouch_depth * (1 - nt/0.2)
    elif nt > 0.8:
        crouch_offset = -crouch_depth * ((nt - 0.8) / 0.2)
    else:
        crouch_offset = 0.0
    hip_center_y = base_hip_y + jump_y + crouch_offset

    # Hip center point as reference.
    hip_center = np.array([hip_center_x, hip_center_y])

    # --------------------------------------------------------------------------
    # Define body segments relative to hip center in the standing posture.
    # Hips: left and right offset horizontally from the center.
    hip_offset = 0.15
    left_hip = hip_center + np.array([-hip_offset, 0])
    right_hip = hip_center + np.array([hip_offset, 0])

    # Trunk: Shoulder center above hips.
    shoulder_rise = 0.7
    shoulder_center = hip_center + np.array([0, shoulder_rise])
    # Shoulders: left and right.
    shoulder_sep = 0.2
    left_shoulder = shoulder_center + np.array([-shoulder_sep, 0])
    right_shoulder = shoulder_center + np.array([shoulder_sep, 0])
    
    # Head: Above shoulder center.
    head_offset = 0.3
    head = shoulder_center + np.array([0, head_offset])
    
    # Arms (we add a little swing modulation):
    swing = arm_swing_amplitude * np.sin(2 * np.pi * nt)
    # Left arm: elbow and wrist relative to left shoulder.
    left_elbow = left_shoulder + np.array([-0.15 + (-swing), -0.3])
    left_wrist = left_shoulder + np.array([-0.30 + (-swing), -0.6])
    # Right arm: elbow and wrist.
    right_elbow = right_shoulder + np.array([0.15 + swing, -0.3])
    right_wrist = right_shoulder + np.array([0.30 + swing, -0.6])
    
    # Legs: For a standing figure the leg segments are arranged vertically.
    # However, when crouching or landing, the knees bend.
    # Compute a knee bend offset: in crouch phases (nt<0.2 and nt>0.8) the knees drop further.
    if nt < 0.2:
        knee_offset = -crouch_depth * (1 - nt/0.2)
    elif nt > 0.8:
        knee_offset = -crouch_depth * ((nt - 0.8) / 0.2)
    else:
        knee_offset = 0.0
    thigh = 0.5
    shank = 0.5
    # Left leg:
    left_knee = left_hip + np.array([0, -thigh + knee_offset])
    left_ankle = left_knee + np.array([0, -shank])
    # Add a small toe offset (left toe: a little backward)
    toe_offset = 0.1
    left_toe = left_ankle + np.array([-toe_offset, 0])
    
    # Right leg:
    right_knee = right_hip + np.array([0, -thigh + knee_offset])
    right_ankle = right_knee + np.array([0, -shank])
    # Right toe: a little forward
    right_toe = right_ankle + np.array([toe_offset, 0])
    
    # Collect the 15 joints in the specified order:
    joints = [
        head,             # 1. Head
        left_shoulder,    # 2. Left Shoulder
        right_shoulder,   # 3. Right Shoulder
        left_elbow,       # 4. Left Elbow
        right_elbow,      # 5. Right Elbow
        left_wrist,       # 6. Left Wrist
        right_wrist,      # 7. Right Wrist
        left_hip,         # 8. Left Hip
        right_hip,        # 9. Right Hip
        left_knee,        # 10. Left Knee
        right_knee,       # 11. Right Knee
        left_ankle,       # 12. Left Ankle
        right_ankle,      # 13. Right Ankle
        left_toe,         # 14. Left Toe
        right_toe         # 15. Right Toe
    ]
    return joints

# Set up the figure.
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_facecolor('black')
plt.axis('equal')
ax.set_xlim(-0.5, jump_distance + 1.0)
ax.set_ylim(-0.2, 3.0)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Initialize scatter plot for the 15 points.
scatter = ax.scatter([], [], s=80, color='white')

def init():
    scatter.set_offsets([])
    return scatter,

def update(frame):
    # Normalize time between 0 and 1.
    nt = frame / (total_frames - 1)
    joints = get_joint_positions(nt)
    # Convert list of joints to a NumPy array of shape (15,2)
    pts = np.array(joints)
    scatter.set_offsets(pts)
    return scatter,

animation = FuncAnimation(fig, update, frames=total_frames,
                          init_func=init, blit=True, interval=30)

plt.show()