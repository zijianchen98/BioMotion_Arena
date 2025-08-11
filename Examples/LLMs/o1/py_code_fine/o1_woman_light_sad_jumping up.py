#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program displays 15 white point-lights (joints) on a black background,
# depicting a "sad woman" performing a lightweight jump in a biomechanically
# plausible manner.

# Global parameters
FPS = 50              # frames per second
DURATION = 2.0        # total animation duration in seconds
N_FRAMES = int(FPS * DURATION)

# Define a function that smoothly transitions between two values
def smooth_transition(t, t_start, t_end, start_val, end_val):
    """Returns a smoothed value from start_val to end_val over [t_start, t_end]."""
    if t <= t_start:
        return start_val
    elif t >= t_end:
        return end_val
    else:
        # Use a simple smooth step (sin-based) interpolation
        alpha = (t - t_start) / (t_end - t_start)
        alpha_smooth = 0.5 - 0.5 * np.cos(np.pi * alpha)  # smoothstep
        return start_val + (end_val - start_val) * alpha_smooth

def get_joint_positions(t):
    """
    Returns an array of shape (15, 2) with (x,y) for each of 15 joints
    representing a sad woman jumping. Time t is in [0, DURATION].
    """

    # PHASES (example):
    #  0.0 - 0.3s  : slight crouch
    #  0.3 - 0.55s : jump up (pelvis rises)
    #  0.55- 0.80s : come down to initial
    #  0.80- 2.0s  : stand (rest) at initial position

    # Pelvis base position (x=0, y=0.4) in default stance
    pelvis_y_rest = 0.40
    # We'll define pelvis_y as a piecewise function that moves from 0.40 to about 0.35,
    # then up to ~0.70, then back down to 0.40, then stays there.
    pelvis_y = pelvis_y_rest
    pelvis_y = smooth_transition(t, 0.0, 0.3, 0.40, 0.35)   # crouch
    pelvis_y = smooth_transition(t, 0.3, 0.55, pelvis_y, 0.70)  # jump up
    pelvis_y = smooth_transition(t, 0.55, 0.80, pelvis_y, 0.40) # land

    # Let's define a forward-lean factor for a "sad" posture
    # We'll just tilt the upper body forward slightly at all times
    # and maybe exaggerate it a bit during the crouch.
    base_tilt = 0.1  # base forward tilt
    tilt = base_tilt + 0.1 * (0.35 - pelvis_y)  # tilt more when pelvis is lower

    # We'll define some proportions for body segments (rough skeleton in 2D)
    head_offset = 0.15
    torso_length = 0.25
    upper_arm_length = 0.18
    lower_arm_length = 0.18
    upper_leg_length = 0.25
    lower_leg_length = 0.25

    # We place the pelvis at (0, pelvis_y).
    pelvis = np.array([0.0, pelvis_y])

    # We'll define the torso line from pelvis to neck with a forward tilt
    neck = pelvis + np.array([tilt, torso_length])  # small x shift + y up
    # The head is above the neck, continuing the same tilt
    head = neck + np.array([tilt, head_offset])

    # Shoulders: near the neck, offset sideways for left and right
    # We'll shift them horizontally from the neck
    shoulder_offset = 0.08
    right_shoulder = neck + np.array([+shoulder_offset, 0.0])
    left_shoulder  = neck + np.array([-shoulder_offset, 0.0])

    # For a jump, arms swing up a bit in mid-air. We'll define a simple piecewise raise.
    # We'll define an "arm_raise" factor from 0 (down) to ~0.5 (up).
    arm_raise = 0.0
    arm_raise = smooth_transition(t, 0.0, 0.3, 0.0, 0.1)    # prepping
    arm_raise = smooth_transition(t, 0.3, 0.55, arm_raise, 0.5)  # upward swing
    arm_raise = smooth_transition(t, 0.55, 0.80, arm_raise, 0.0) # back down

    # We'll define the elbows and wrists using arm_raise as a vertical offset from shoulders
    # plus a small forward tilt if arms come up.
    # Right arm
    right_elbow = right_shoulder + np.array([0.02 * arm_raise, -upper_arm_length * 0.8 * (1 - arm_raise)])
    right_wrist = right_elbow + np.array([0.02 * arm_raise, -lower_arm_length * 0.8 * (1 - arm_raise)])

    # Left arm
    left_elbow = left_shoulder + np.array([-0.02 * arm_raise, -upper_arm_length * 0.8 * (1 - arm_raise)])
    left_wrist = left_elbow + np.array([-0.02 * arm_raise, -lower_arm_length * 0.8 * (1 - arm_raise)])

    # Hips: The pelvis is in the middle, so define left_hip and right_hip
    hip_offset = 0.07
    right_hip = pelvis + np.array([+hip_offset, 0.0])
    left_hip  = pelvis + np.array([-hip_offset, 0.0])

    # Knees: They come up slightly when jumping, otherwise near ground. We'll define a factor
    # based on how high the pelvis is from the rest.
    # We'll define the fraction for knee bend
    crouch_factor = 1.0 if pelvis[1] < pelvis_y_rest else 0.5
    # Right knee
    right_knee = right_hip + np.array([0.0, -upper_leg_length * crouch_factor])
    # Left knee
    left_knee  = left_hip  + np.array([0.0, -upper_leg_length * crouch_factor])

    # Ankles: If pelvis is going up, the ankles also come up but remain lower than knees.
    # We'll assume the ankles might leave the ground only if pelvis is definitely above ~0.45.
    ankle_elev = max(0.0, pelvis[1] - 0.45) * 0.7  # ankles rise fraction
    # Right ankle
    right_ankle = right_knee + np.array([0.0, -lower_leg_length + ankle_elev])
    # Left ankle
    left_ankle  = left_knee  + np.array([0.0, -lower_leg_length + ankle_elev])

    # One extra joint (15th) for a "chest" or mid-torso point
    chest = pelvis + np.array([tilt * 0.5, torso_length * 0.6])

    # Collect all 15 points in order:
    # 0: Head
    # 1: Neck
    # 2: Right Shoulder
    # 3: Right Elbow
    # 4: Right Wrist
    # 5: Left Shoulder
    # 6: Left Elbow
    # 7: Left Wrist
    # 8: Right Hip
    # 9: Right Knee
    # 10: Right Ankle
    # 11: Left Hip
    # 12: Left Knee
    # 13: Left Ankle
    # 14: Chest
    points = np.array([
        head,
        neck,
        right_shoulder,
        right_elbow,
        right_wrist,
        left_shoulder,
        left_elbow,
        left_wrist,
        right_hip,
        right_knee,
        right_ankle,
        left_hip,
        left_knee,
        left_ankle,
        chest
    ])
    return points

# Set up the figure and animation
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')  # black background
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0.0, 1.0)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter with 15 points
scatter = ax.scatter([0]*15, [0]*15, s=40, c='white')

def update(frame):
    t = (frame / N_FRAMES) * DURATION
    pts = get_joint_positions(t)
    scatter.set_offsets(pts)
    return (scatter,)

ani = FuncAnimation(
    fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True, repeat=True
)

plt.show()