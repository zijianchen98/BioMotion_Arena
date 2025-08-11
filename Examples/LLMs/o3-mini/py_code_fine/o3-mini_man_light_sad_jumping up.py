
"""
This program shows an animation of a “sad man” jumping up using 15 white point‐lights
on a solid black background. The 15 points represent key anatomical locations of the body:
   1. Head
   2. Neck
   3. Spine
   4. Right Shoulder
   5. Left Shoulder
   6. Right Elbow
   7. Left Elbow
   8. Right Wrist
   9. Left Wrist
  10. Right Hip
  11. Left Hip
  12. Right Knee
  13. Left Knee
  14. Right Ankle
  15. Left Ankle

The animation simulates a jump by applying a smooth vertical offset (following a sine curve)
to all joints and by adding modest oscillatory rotations to the arms and legs for biomechanically
plausible motions.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Convenience rotation function (rotates a 2D vector by angle radians)
def rotate(vec, angle):
    """Rotate a 2D vector by 'angle' radians."""
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
    return rot @ np.array(vec)

# Animation parameters
num_frames = 120          # total frames per jump cycle
fps = 30                  # frames per second for animation
jump_height = 2.0         # maximum vertical jump offset

# Joint base positions (standing pose) in 2D (x,y)
# We use a simple quasi-skeletal setup.
# The coordinates here are chosen so that higher y means higher on the screen.
base_points = {
    "head": np.array([0, 8]),
    "neck": np.array([0, 7]),
    "spine": np.array([0, 6]),
    "Rshoulder": np.array([1, 7]),
    "Lshoulder": np.array([-1, 7]),
    # Arms: the following segments are defined relative to the shoulder.
    # For the right arm, the vector from shoulder to elbow is (0.5, -1) and from elbow to wrist is (0, -1).
    # Similarly for the left arm (reflected horizontally).
    # Legs: from hip to knee is (0, -2) and from knee to ankle is (0, -2).
    "Rhip": np.array([0.5, 5]),
    "Lhip": np.array([-0.5, 5]),
}

def compute_frame_positions(frame):
    """
    Given a frame index, compute the positions for all 15 joints.
    Returns a list of (x,y) coordinates.
    """
    # Compute a normalized time variable in [0, 1] for this jump cycle.
    t = frame / num_frames

    # Vertical jump offset: using sine so that t=0 and t=1 are on the ground, with a peak at t=0.5.
    y_offset = jump_height * np.sin(np.pi * t)
    base_offset = np.array([0, y_offset])
    
    # For biomechanical motion, let the arms and legs swing gently:
    # Arms: swing amplitude ~10° (in radians)
    arm_amp = np.deg2rad(10)
    angle_arm = arm_amp * np.sin(2 * np.pi * t)
    # For left arm, reverse the swing so that arms move in opposite directions:
    angle_arm_left = -angle_arm

    # Legs: swing amplitude ~15° (in radians).
    leg_amp = np.deg2rad(15)
    # To simulate alternating leg movement during jump, let right and left legs move out-of-phase.
    angle_leg_right = leg_amp * np.sin(2 * np.pi * t)
    angle_leg_left  = -leg_amp * np.sin(2 * np.pi * t)

    joints = {}

    # Static vertical body (head, neck, spine, shoulders)
    joints["head"]      = base_points["head"] + base_offset
    joints["neck"]      = base_points["neck"] + base_offset
    joints["spine"]     = base_points["spine"] + base_offset
    joints["Rshoulder"] = base_points["Rshoulder"] + base_offset
    joints["Lshoulder"] = base_points["Lshoulder"] + base_offset

    # Right Arm
    # Base vector from shoulder to elbow.
    r_shoulder = joints["Rshoulder"]
    vec_SE = np.array([0.5, -1])
    r_elbow = r_shoulder + rotate(vec_SE, angle_arm)
    # Vector from elbow to wrist.
    vec_EW = np.array([0, -1])
    r_wrist = r_elbow + rotate(vec_EW, angle_arm)
    joints["Relbow"] = r_elbow
    joints["Rwrist"] = r_wrist

    # Left Arm
    l_shoulder = joints["Lshoulder"]
    # For left arm, use the mirror image vector and the opposite arm swing.
    vec_SE_left = np.array([-0.5, -1])
    l_elbow = l_shoulder + rotate(vec_SE_left, angle_arm_left)
    vec_EW_left = np.array([0, -1])
    l_wrist = l_elbow + rotate(vec_EW_left, angle_arm_left)
    joints["Lelbow"] = l_elbow
    joints["Lwrist"] = l_wrist

    # Right Leg
    # Hip position (taken from base_points and adding vertical offset)
    r_hip = base_points["Rhip"] + base_offset
    # Knee: from hip use a vertical segment of length 2 rotated by angle.
    vec_HK = np.array([0, -2])
    r_knee = r_hip + rotate(vec_HK, angle_leg_right)
    # Ankle: from knee similarly
    r_ankle = r_knee + rotate(vec_HK, angle_leg_right)
    joints["Rhip"] = r_hip   # update with vertical offset already
    joints["Rknee"] = r_knee
    joints["Rankle"] = r_ankle

    # Left Leg
    l_hip = base_points["Lhip"] + base_offset
    vec_HK_left = np.array([0, -2])
    l_knee = l_hip + rotate(vec_HK_left, angle_leg_left)
    l_ankle = l_knee + rotate(vec_HK_left, angle_leg_left)
    joints["Lhip"] = l_hip
    joints["Lknee"] = l_knee
    joints["Lankle"] = l_ankle

    # Order the joints in the specified order:
    # 1. Head
    # 2. Neck
    # 3. Spine
    # 4. Right Shoulder
    # 5. Left Shoulder
    # 6. Right Elbow
    # 7. Left Elbow
    # 8. Right Wrist
    # 9. Left Wrist
    # 10. Right Hip
    # 11. Left Hip
    # 12. Right Knee
    # 13. Left Knee
    # 14. Right Ankle
    # 15. Left Ankle
    ordered_joints = [
        joints["head"],
        joints["neck"],
        joints["spine"],
        joints["Rshoulder"],
        joints["Lshoulder"],
        joints["Relbow"],
        joints["Lelbow"],
        joints["Rwrist"],
        joints["Lwrist"],
        joints["Rhip"],
        joints["Lhip"],
        joints["Rknee"],
        joints["Lknee"],
        joints["Rankle"],
        joints["Lankle"]
    ]
    return np.array(ordered_joints)

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
# Determine suitable limits (padding added for jump and limb excursions)
ax.set_xlim(-3, 3)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for the 15 point-lights (drawn as white circles)
scatter = ax.scatter([], [], s=80, c='white')

def init():
    scatter.set_offsets([])
    return scatter,

def animate(frame):
    points = compute_frame_positions(frame % num_frames)
    scatter.set_offsets(points)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, init_func=init,
                              interval=1000/fps, blit=True)

plt.show()