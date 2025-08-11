
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program creates a point-light animation of a person performing a forward roll.
# The animation is defined by a series of keyframes, and the motion between
# keyframes is generated using linear interpolation.

# --- Keyframe Data ---
# The data represents the 2D coordinates of 15 body joints over 9 keyframes.
# Joint indices:
# 0: Head          8: Pelvis
# 1: Neck          9: Right Hip
# 2: Right Shoulder 10: Left Hip
# 3: Left Shoulder  11: Right Knee
# 4: Right Elbow    12: Left Knee
# 5: Left Elbow     13: Right Ankle
# 6: Right Wrist    14: Left Ankle
# 7: Left Wrist
# The 'Right' and 'Left' are from the actor's perspective, who is facing to the right.

keyframes = np.array([
    # KF 0: Start in a low squat, preparing to roll.
    [(-40, 15), (-40, 10), (-38, 10), (-42, 10), (-30, 5), (-50, 5), (-25, 0), (-55, 0), (-40, -10), (-38, -10), (-42, -10), (-35, -20), (-45, -20), (-40, -30), (-40, -30)],
    # KF 1: Hands placed on the ground, head tucked in.
    [(-33, -3), (-35, 2), (-33, 2), (-37, 2), (-28, -5), (-42, -5), (-25, -15), (-45, -15), (-40, 0), (-38, 0), (-42, 0), (-45, -10), (-50, -10), (-50, -20), (-55, -20)],
    # KF 2: Pushing off with feet, hips rising.
    [(-25, -10), (-25, -5), (-23, -5), (-27, -5), (-18, -10), (-32, -10), (-15, -15), (-35, -15), (-30, 10), (-28, 10), (-32, 10), (-35, 5), (-40, 5), (-45, -5), (-50, -5)],
    # KF 3: Rolling onto shoulders, body tightly tucked, legs overhead.
    [(-12, -12), (-15, -8), (-13, -8), (-17, -8), (-8, -15), (-22, -15), (-5, -15), (-25, -15), (-10, 15), (-8, 15), (-12, 15), (-15, 10), (-20, 10), (-20, 5), (-25, 5)],
    # KF 4: Mid-roll, center of mass is at its highest point.
    [(5, -5), (0, -5), (2, -5), (-2, -5), (8, -8), (-8, -8), (8, -8), (-8, -8), (0, 20), (2, 20), (-2, 20), (0, 15), (0, 15), (5, 5), (-5, 5)],
    # KF 5: Rolling onto the lower back, preparing to land.
    [(18, 5), (15, 8), (17, 8), (13, 8), (22, 5), (8, 5), (22, 5), (8, 5), (10, 15), (12, 15), (8, 15), (15, 15), (5, 15), (20, 10), (0, 10)],
    # KF 6: Feet coming down to land on the ground, body uncurling.
    [(25, 10), (25, 5), (27, 5), (23, 5), (32, 8), (18, 8), (35, 5), (15, 5), (20, 0), (22, 0), (18, 0), (25, -10), (15, -10), (25, -20), (15, -20)],
    # KF 7: Landed in a low squat, arms forward for balance.
    [(40, 15), (40, 10), (42, 10), (38, 10), (50, 5), (30, 5), (55, 0), (25, 0), (40, -10), (42, -10), (38, -10), (45, -20), (35, -20), (40, -30), (40, -30)],
    # KF 8: Holding the final squat position briefly.
    [(40, 15), (40, 10), (42, 10), (38, 10), (50, 5), (30, 5), (55, 0), (25, 0), (40, -10), (42, -10), (38, -10), (45, -20), (35, -20), (40, -30), (40, -30)]
])

# --- Animation Configuration ---
TOTAL_FRAMES = 150
FRAME_INTERVAL = 40  # in milliseconds

# --- Plot Setup ---
fig, ax = plt.subplots(figsize=(8, 5))
fig.set_facecolor('black')
ax.set_facecolor('black')

# Set axes limits and aspect ratio
ax.set_xlim(-70, 70)
ax.set_ylim(-45, 45)
ax.set_aspect('equal', adjustable='box')

# Hide axes, ticks, and spines for a clean look
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Initialize the scatter plot for the 15 points
scatter = ax.scatter([], [], c='white', marker='o', s=60)

# --- Animation Logic ---
def get_interpolated_frame(frame_num):
    """
    Calculates point positions for a given frame by interpolating between keyframes.
    """
    num_keyframes = len(keyframes)
    # Calculate a float position in the keyframe sequence
    pos = (frame_num / TOTAL_FRAMES) * (num_keyframes - 1)
    
    # Find the two keyframes to interpolate between
    kf1_index = int(pos)
    kf2_index = kf1_index + 1
    
    # If it's the last frame, return the last keyframe without interpolating
    if kf2_index >= num_keyframes:
        return keyframes[-1]
        
    # Calculate the interpolation factor 't' (from 0.0 to 1.0)
    t = pos - kf1_index
    
    kf1 = keyframes[kf1_index]
    kf2 = keyframes[kf2_index]
    
    # Perform linear interpolation for all points
    current_pos = (1 - t) * kf1 + t * kf2
    return current_pos

def update(frame_num):
    """
    This function is called for each frame of the animation.
    It calculates and updates the positions of the points.
    """
    points_data = get_interpolated_frame(frame_num)
    scatter.set_offsets(points_data)
    return scatter,

# --- Create and run the animation ---
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES,
                    interval=FRAME_INTERVAL, blit=True)

plt.show()
