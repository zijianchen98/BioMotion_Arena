import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program displays a 15-point biological motion stimulus of a running figure
# against a black background, with white point-lights.

# -----------------------------
# 1) Parameter definitions
# -----------------------------
num_frames = 60   # Number of frames per run cycle
fps = 30          # Animation frames per second
duration = 4      # Total seconds to loop the running cycle
total_frames = num_frames * duration

# Biomechanical parameters (tuned to mimic a light, happy running style):
leg_amplitude = 0.5
arm_amplitude = 0.4
leg_offset = 0.7
arm_offset = 0.5
bounce_height = 0.05
stride_length = 0.08
body_height = 1.0

# Indices of the 15 points in our skeleton model:
# 0: head
# 1: neck
# 2: right_shoulder
# 3: right_elbow
# 4: right_wrist
# 5: left_shoulder
# 6: left_elbow
# 7: left_wrist
# 8: spine
# 9: right_hip
# 10: right_knee
# 11: right_ankle
# 12: left_hip
# 13: left_knee
# 14: left_ankle

def get_points(phase):
    """
    Returns a (15, 2) numpy array of 2D coordinates for the skeleton
    at a given phase of the running cycle, where phase in [0, 2*pi).
    """
    # Horizontal translation and vertical bounce of the body center
    center_x = stride_length * phase / (2 * np.pi)
    center_y = body_height + bounce_height * np.sin(2 * phase)

    # Leg angles (right leg and left leg are out of phase by pi)
    right_leg_angle = leg_amplitude * np.sin(phase * 2) - leg_offset
    left_leg_angle = leg_amplitude * np.sin(phase * 2 + np.pi) - leg_offset

    # Arm angles (slightly out of phase with legs and smaller amplitude)
    right_arm_angle = arm_amplitude * np.sin(phase * 2 + np.pi) - arm_offset
    left_arm_angle  = arm_amplitude * np.sin(phase * 2) - arm_offset

    # Build the skeleton in a local coordinate system:
    # We'll anchor the "spine" as (0, 0) in local coords, then add center offset.
    # Simple approximate offsets for each point in local coordinates:
    local = np.zeros((15, 2))

    # Spine, Neck, Head
    local[8] = [0, 0]         # spine
    local[1] = [0, 0.2]       # neck
    local[0] = [0, 0.4]       # head

    # Shoulders
    shoulder_width = 0.15
    local[2] = [ shoulder_width,  0.2]  # right_shoulder
    local[5] = [-shoulder_width,  0.2]  # left_shoulder

    # Hips
    hip_width = 0.12
    local[9]  = [ hip_width,  0]  # right_hip
    local[12] = [-hip_width,  0]  # left_hip

    # Arms (elbow and wrist)
    arm_length_upper = 0.18
    arm_length_lower = 0.18
    # Right arm
    local[3] = local[2] + [
        np.cos(right_arm_angle) * arm_length_upper,
        np.sin(right_arm_angle) * arm_length_upper
    ]
    local[4] = local[3] + [
        np.cos(right_arm_angle) * arm_length_lower,
        np.sin(right_arm_angle) * arm_length_lower
    ]
    # Left arm
    local[6] = local[5] + [
        np.cos(left_arm_angle) * arm_length_upper,
        np.sin(left_arm_angle) * arm_length_upper
    ]
    local[7] = local[6] + [
        np.cos(left_arm_angle) * arm_length_lower,
        np.sin(left_arm_angle) * arm_length_lower
    ]

    # Legs (knee and ankle)
    leg_length_upper = 0.25
    leg_length_lower = 0.25
    # Right leg
    local[10] = local[9] + [
        np.sin(right_leg_angle) * leg_length_upper,
        -np.cos(right_leg_angle) * leg_length_upper
    ]
    local[11] = local[10] + [
        np.sin(right_leg_angle) * leg_length_lower,
        -np.cos(right_leg_angle) * leg_length_lower
    ]
    # Left leg
    local[13] = local[12] + [
        np.sin(left_leg_angle) * leg_length_upper,
        -np.cos(left_leg_angle) * leg_length_upper
    ]
    local[14] = local[13] + [
        np.sin(left_leg_angle) * leg_length_lower,
        -np.cos(left_leg_angle) * leg_length_lower
    ]

    # Translate entire skeleton by (center_x, center_y)
    global_pos = local + np.array([center_x, center_y])
    return global_pos

# -----------------------------
# 2) Build initial figure
# -----------------------------
fig, ax = plt.subplots(figsize=(5, 5))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.2, 2.0)  # Adjust as needed for the running figure
ax.set_ylim(0.0, 2.0)
ax.axis('off')

# Scatter plot for the 15 white points
scatter = ax.scatter([], [], c='white', s=40)

# -----------------------------
# 3) Animation update function
# -----------------------------
def update(frame):
    # Phase goes from 0 to 2*pi over one "run cycle"
    cycle_fraction = (frame % num_frames) / float(num_frames)
    phase = 2 * np.pi * cycle_fraction

    points = get_points(phase)
    scatter.set_offsets(points)
    return scatter,

# -----------------------------
# 4) Create animation
# -----------------------------
ani = FuncAnimation(
    fig, update, frames=total_frames, interval=1000 // fps, blit=True
)

plt.show()