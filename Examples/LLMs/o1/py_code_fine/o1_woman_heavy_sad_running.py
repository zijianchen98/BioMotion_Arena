#!/usr/bin/env python3
"""
This Python program creates a point-light animation of a "sad, heavy-weight woman"
running. It displays exactly 15 white points against a solid black background,
using a simplified kinematic model to produce a biomechanically plausible gait cycle.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# CONFIGURATION AND PARAMETERS
# -----------------------------
FPS = 30              # frames per second
CYCLE_FRAMES = 60     # how many frames per running gait cycle
TOTAL_FRAMES = 180    # total frames in the animation
DOT_SIZE = 50         # size of the plotted points
WHITE = (1, 1, 1)     # color of the points
BLACK = (0, 0, 0)     # background color

# Body segment lengths (somewhat exaggerated to resemble a "heavy-weight" figure)
HEAD_HEIGHT = 0.15
NECK_LENGTH = 0.05
TORSO_LENGTH = 0.35
SHOULDER_WIDTH = 0.25
UPPER_ARM_LENGTH = 0.20
FOREARM_LENGTH = 0.20
HIP_WIDTH = 0.25
UPPER_LEG_LENGTH = 0.35
LOWER_LEG_LENGTH = 0.35

# A simple side-view skeleton labeling 15 points:
#  1  Head
#  2  Neck
#  3  Left Shoulder
#  4  Right Shoulder
#  5  Left Elbow
#  6  Right Elbow
#  7  Left Wrist
#  8  Right Wrist
#  9  Mid-Spine (torso midpoint)
#  10 Left Hip
#  11 Right Hip
#  12 Left Knee
#  13 Right Knee
#  14 Left Ankle
#  15 Right Ankle

# --------------------
# HELPER FUNCTIONS
# --------------------
def lerp(a, b, t):
    """Linear interpolation: value at fraction t between a and b."""
    return a + (b - a)*t

def sad_posture_tilt(t):
    """
    Returns a small forward tilt offset for the torso to give a "sad / heavy" look.
    t is a normalized time fraction within one gait cycle (0..1).
    We'll just keep it roughly constant, or gently vary it.
    """
    # Add a small variation so it doesn't look too static
    # E.g. tilt forward by ~10 degrees, plus a little sway
    base_tilt = np.deg2rad(10)
    sway = np.deg2rad(2) * np.sin(2 * np.pi * 1.0 * t)
    return base_tilt + sway

def running_motion(t):
    """
    Given a normalized time t within one gait cycle [0..1],
    compute the angles (in radians) for arms and legs and a slight vertical bounce.
    We'll produce a side-view running cycle with arms, legs out of phase.
    """
    # Leg angles: one leg leads, the other trails out of phase
    # We'll use sine for left leg, and shifted sine for right leg
    # A heavier runner might have slower leg turnover and deeper knee lift
    left_leg_phase = 2 * np.pi * t
    right_leg_phase = left_leg_phase + np.pi  # out of phase by 180 degrees

    # For arms, do likewise, but out of phase with legs
    left_arm_phase = left_leg_phase + np.pi
    right_arm_phase = right_leg_phase + np.pi

    # Angles around the hip/shoulder (basic pivot)
    leg_amp = np.deg2rad(35)   # amplitude of leg swing
    arm_amp = np.deg2rad(25)   # amplitude of arm swing

    left_hip_angle = leg_amp * np.sin(left_leg_phase)
    right_hip_angle = leg_amp * np.sin(right_leg_phase)

    left_shoulder_angle = arm_amp * np.sin(left_arm_phase)
    right_shoulder_angle = arm_amp * np.sin(right_arm_phase)

    # Bending at the knee and elbow
    # We can approximate with a double-frequency sine for some natural flex
    knee_amp = np.deg2rad(40)
    left_knee_angle = knee_amp * (1 - np.cos(2 * left_leg_phase))  # 0..80 deg
    right_knee_angle = knee_amp * (1 - np.cos(2 * right_leg_phase))

    elbow_amp = np.deg2rad(20)
    left_elbow_angle = elbow_amp * (1 - np.cos(2 * left_arm_phase))
    right_elbow_angle = elbow_amp * (1 - np.cos(2 * right_arm_phase))

    # Vertical bounce of torso: heavier runner might have more bounce
    vertical_bounce = 0.03 * np.sin(2 * np.pi * 2 * t)

    return (left_hip_angle, right_hip_angle,
            left_knee_angle, right_knee_angle,
            left_shoulder_angle, right_shoulder_angle,
            left_elbow_angle, right_elbow_angle,
            vertical_bounce)

def get_skeleton_points(t):
    """
    Compute (x, y) positions (side-view) of the 15 skeleton points at time fraction t.
    t goes from 0..1 for one gait cycle.
    """
    # We get angles from our running motion model
    (left_hip_angle, right_hip_angle,
     left_knee_angle, right_knee_angle,
     left_shoulder_angle, right_shoulder_angle,
     left_elbow_angle, right_elbow_angle,
     vertical_bounce) = running_motion(t)

    # Torso tilt (sad posture)
    torso_tilt = sad_posture_tilt(t)

    # Horizontal translation to simulate forward running
    # Let's move ~0.8 units horizontally per cycle
    # So at t=0..1, move from x=0..0.8
    base_x_torso = 0.8 * t
    base_y_torso = 0.5 + vertical_bounce  # baseline ~0.5

    # We'll treat the spine "pivot" (Mid-Spine) as reference
    # and position everything around it in 2D:
    # We'll define the direction "forward" as +x, and "up" as +y.
    # Tilt the torso as sad_posture_tilt.
    # We can rotate segments around that angle.

    def rotate(ax, ay, theta):
        """Rotate point (ax, ay) by angle theta about origin (0,0)."""
        rx = ax*np.cos(theta) - ay*np.sin(theta)
        ry = ax*np.sin(theta) + ay*np.cos(theta)
        return rx, ry

    # 9: Mid-Spine (the center of the torso)
    # We'll store points in a list of (x, y).
    points = [None]*15  # placeholders for each of the 15 points

    # Mid-spine is the pivot of the torso
    mid_torso_x = base_x_torso
    mid_torso_y = base_y_torso
    points[8] = (mid_torso_x, mid_torso_y)  # index 8 = #9 in 1-based list

    # 2: Neck is TORSO_LENGTH above mid-spine after rotation by torso tilt
    neck_local = (0, TORSO_LENGTH * 0.5)
    neck_gx, neck_gy = rotate(*neck_local, torso_tilt)
    neck_gx += mid_torso_x
    neck_gy += mid_torso_y
    points[1] = (neck_gx, neck_gy)

    # 1: Head is NECK_LENGTH + HEAD_HEIGHT above the neck
    head_local = (0, NECK_LENGTH + HEAD_HEIGHT)
    head_rot_x, head_rot_y = rotate(*head_local, torso_tilt)
    head_rot_x += neck_gx
    head_rot_y += neck_gy
    points[0] = (head_rot_x, head_rot_y)

    # Hips: we assume mid-spine is halfway between shoulders and hips
    # so hips are TORSO_LENGTH/2 below the mid-spine
    hip_local = (0, -TORSO_LENGTH*0.5)
    hip_gx, hip_gy = rotate(*hip_local, torso_tilt)
    hip_gx += mid_torso_x
    hip_gy += mid_torso_y

    # Left hip (#10) and right hip (#11) are offset horizontally by half HIP_WIDTH
    # We'll define left as negative x offset, right as + offset, then rotate about torso pivot
    left_hip_offset = (-HIP_WIDTH*0.5, -TORSO_LENGTH*0.5)
    right_hip_offset = ( HIP_WIDTH*0.5, -TORSO_LENGTH*0.5)
    # Rotate about (0,0), then translate by (mid_torso_x, mid_torso_y)
    lhx, lhy = rotate(*left_hip_offset, torso_tilt)
    lhx += mid_torso_x
    lhy += mid_torso_y
    points[9] = (lhx, lhy)  # left hip
    rhx, rhy = rotate(*right_hip_offset, torso_tilt)
    rhx += mid_torso_x
    rhy += mid_torso_y
    points[10] = (rhx, rhy)  # right hip

    # Shoulder positions: near the neck, slightly outward
    left_shoulder_offset = (-SHOULDER_WIDTH*0.5, TORSO_LENGTH*0.5*0.8)
    right_shoulder_offset = ( SHOULDER_WIDTH*0.5, TORSO_LENGTH*0.5*0.8)
    lsx, lsy = rotate(*left_shoulder_offset, torso_tilt)
    lsx += mid_torso_x
    lsy += mid_torso_y
    points[2] = (lsx, lsy)  # left shoulder (#3)
    rsx, rsy = rotate(*right_shoulder_offset, torso_tilt)
    rsx += mid_torso_x
    rsy += mid_torso_y
    points[3] = (rsx, rsy)  # right shoulder (#4)

    # ARMS:
    # We treat shoulder angles as rotation about the shoulder
    #   left_shoulder_angle for left arm
    # Then elbow is a further bend.
    # We'll do 2D forward/back.

    def limb2D(base_x, base_y, base_angle, seg1_len, seg2_len, joint_angle):
        """
        Return the elbow (joint) and wrist (end) positions for a 2-segment limb
        in 2D. base_angle is rotation from the torso plane,
        joint_angle is the bend for the second segment.
        """
        # Elbow:
        ex = base_x + seg1_len*np.cos(base_angle)
        ey = base_y + seg1_len*np.sin(base_angle)
        # Then from elbow to wrist, we add seg2 rotated by (base_angle + joint_angle)
        wx = ex + seg2_len*np.cos(base_angle + joint_angle)
        wy = ey + seg2_len*np.sin(base_angle + joint_angle)
        return (ex, ey, wx, wy)

    # Left arm (#3->#5->#7):
    l_elbow_x, l_elbow_y, l_wrist_x, l_wrist_y = limb2D(
        lsx, lsy,
        torso_tilt + left_shoulder_angle,
        UPPER_ARM_LENGTH,
        FOREARM_LENGTH,
        left_elbow_angle
    )
    points[4] = (l_elbow_x, l_elbow_y)  # #5
    points[6] = (l_wrist_x, l_wrist_y)  # #7

    # Right arm (#4->#6->#8):
    r_elbow_x, r_elbow_y, r_wrist_x, r_wrist_y = limb2D(
        rsx, rsy,
        torso_tilt + right_shoulder_angle,
        UPPER_ARM_LENGTH,
        FOREARM_LENGTH,
        right_elbow_angle
    )
    points[5] = (r_elbow_x, r_elbow_y)  # #6
    points[7] = (r_wrist_x, r_wrist_y)  # #8

    # LEGS:
    # Use limb2D: base x, y = left hip for left leg, then right hip
    # base_angle = torso_tilt + left_hip_angle
    # joint_angle = left_knee_angle
    # seg1_len = UPPER_LEG_LENGTH, seg2_len = LOWER_LEG_LENGTH

    # Left leg (#10->#12->#14):
    l_knee_x, l_knee_y, l_ankle_x, l_ankle_y = limb2D(
        lhx, lhy,
        torso_tilt + left_hip_angle,
        UPPER_LEG_LENGTH,
        LOWER_LEG_LENGTH,
        left_knee_angle
    )
    points[11] = (l_knee_x, l_knee_y)  # #12
    points[13] = (l_ankle_x, l_ankle_y)  # #14

    # Right leg (#11->#13->#15):
    r_knee_x, r_knee_y, r_ankle_x, r_ankle_y = limb2D(
        rhx, rhy,
        torso_tilt + right_hip_angle,
        UPPER_LEG_LENGTH,
        LOWER_LEG_LENGTH,
        right_knee_angle
    )
    points[12] = (r_knee_x, r_knee_y)  # #13
    points[14] = (r_ankle_x, r_ankle_y)  # #15

    return np.array(points)

# --------------------
# ANIMATION SETUP
# --------------------
fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor(BLACK)  # black background
ax.set_facecolor(BLACK)

# We'll plot 15 dots:
scatter_plot = ax.scatter([], [], s=DOT_SIZE, c=[WHITE]*15)

# Set axis limits so the figure remains stable
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(0.0, 1.2)
ax.set_aspect('equal')
plt.axis('off')  # hide axes for clean display


def init():
    """Initialize the scatter with no data."""
    scatter_plot.set_offsets([])
    return scatter_plot,

def update(frame):
    """Update function for the animation."""
    # Normalize the frame into [0..1] cycle
    cycle_t = (frame % CYCLE_FRAMES) / float(CYCLE_FRAMES)
    points = get_skeleton_points(cycle_t)
    scatter_plot.set_offsets(points)
    return scatter_plot,

# Create animation
ani = FuncAnimation(
    fig, update,
    frames=TOTAL_FRAMES,
    init_func=init,
    blit=True,
    interval=1000/FPS
)

# Show the animation window
plt.show()