
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- Points Map ----
# 0: Head
# 1: Right shoulder
# 2: Left shoulder
# 3: Right elbow
# 4: Left elbow
# 5: Right hand
# 6: Left hand
# 7: Chest
# 8: Pelvis
# 9: Right hip
# 10: Left hip
# 11: Right knee
# 12: Left knee
# 13: Right foot
# 14: Left foot

# The body is "lying down" horizontally, head to the right. 
# The "heavy weight" can be represented as hands pushing an imaginary object above (i.e., hands pressed together and bobbing gently).

# All coordinates in (x, y), unit = relative to a 1x1 square. We'll scale for display.

def body_pose(t):
    """
    Return a (15,2) array of the 2d coordinates for each point-light.
    The basic pose is lying flat, head to the right, feet to the left.
    Args:
        t: time (float)
    Returns:
        coords: np.array shape (15, 2)
    """
    # Body segment lengths (in canvas units)
    # Lying along x, y is vertical tight spread
    head_radius = 0.06
    neck_to_chest = 0.07
    shoulder_span = 0.18
    upper_arm = 0.12
    lower_arm = 0.13
    hand_size = 0.08
    torso_length = 0.22
    pelvis_span = 0.14
    thigh = 0.16
    shank = 0.15
    foot_size = 0.09

    # Body center
    cx = 0.5
    cy = 0.5

    # Shoulder and hips y (vertical placement)
    shoulder_y = cy + 0.04
    chest_y    = cy + 0.02
    pelvis_y   = cy - 0.01
    hip_y      = pelvis_y - 0.01

    # Head
    head_x = cx + torso_length/2 + head_radius
    head_y = shoulder_y

    # Chest and pelvis
    chest_x = cx
    chest_y = chest_y
    pelvis_x = cx - torso_length/2
    pelvis_y = pelvis_y

    # Shoulders
    r_shoulder_x = cx + shoulder_span/2
    l_shoulder_x = cx - shoulder_span/2
    r_shoulder_y = shoulder_y
    l_shoulder_y = shoulder_y

    # Hips
    r_hip_x = pelvis_x + pelvis_span/2
    l_hip_x = pelvis_x - pelvis_span/2
    r_hip_y = hip_y
    l_hip_y = hip_y

    # Arms: both arms raised above chest, close together to push "heavy weight"
    # The hands are above the chest, slightly apart, and they move up/down to simulate weight pressing.
    # Sinusoidal up/down of hand/wrists/elbows

    # Animation: Hand motion amplitude
    weight_amp = 0.04
    weight_freq = 1.1  # times per second
    weight_phase = np.sin(2*np.pi*weight_freq*t)
    vertical_shift = weight_amp * weight_phase

    # Both hands above chest, almost touching (heavy weight)
    hands_base_x = cx + 0.04
    hands_base_y = shoulder_y + 0.13 + vertical_shift

    hands_sep = 0.045  # their apart spacing

    # Right arm chain (from shoulder)
    r_elbow_angle = np.deg2rad(-18 + 7*np.sin(2*np.pi*weight_freq*t + 1.4))  # angle relative to arm axis
    r_elbow_x = r_shoulder_x + upper_arm * np.cos(np.pi/10 + 0.04*weight_phase)
    r_elbow_y = r_shoulder_y + upper_arm * np.sin(np.pi/10 + 0.04*weight_phase)
    r_hand_x = hands_base_x + hands_sep/2
    r_hand_y = hands_base_y

    # Left arm chain
    l_elbow_angle = np.deg2rad(18 - 7*np.sin(2*np.pi*weight_freq*t - 1.7))
    l_elbow_x = l_shoulder_x + upper_arm * np.cos(-np.pi/10 + 0.03*weight_phase)
    l_elbow_y = l_shoulder_y + upper_arm * np.sin(-np.pi/10 + 0.03*weight_phase)
    l_hand_x = hands_base_x - hands_sep/2
    l_hand_y = hands_base_y

    # Legs: both flat lying, smallest vertical offset (ankle/knee bounce due to weight)
    leg_amp = 0.01
    leg_bounce = leg_amp * np.sin(2*np.pi*weight_freq*t + 0.7)

    # Right leg
    r_knee_x = r_hip_x - thigh * 0.93
    r_knee_y = r_hip_y - thigh * 0.08 + leg_bounce
    r_foot_x = r_knee_x - shank * 0.89
    r_foot_y = r_knee_y - shank * 0.09 + 0.75*leg_bounce

    # Left leg
    l_knee_x = l_hip_x - thigh * 0.89
    l_knee_y = l_hip_y - thigh * 0.07 - leg_bounce*0.85
    l_foot_x = l_knee_x - shank * 0.91
    l_foot_y = l_knee_y - shank * 0.11 - 0.73*leg_bounce

    # All points as per the kinematic chain above
    coords = np.array([
        [head_x, head_y],                        # 0: Head
        [r_shoulder_x, r_shoulder_y],            # 1: Right shoulder
        [l_shoulder_x, l_shoulder_y],            # 2: Left shoulder
        [r_elbow_x, r_elbow_y],                  # 3: Right elbow
        [l_elbow_x, l_elbow_y],                  # 4: Left elbow
        [r_hand_x, r_hand_y],                    # 5: Right hand
        [l_hand_x, l_hand_y],                    # 6: Left hand
        [chest_x, chest_y],                      # 7: Chest
        [pelvis_x, pelvis_y],                    # 8: Pelvis
        [r_hip_x, r_hip_y],                      # 9: Right hip
        [l_hip_x, l_hip_y],                      # 10: Left hip
        [r_knee_x, r_knee_y],                    # 11: Right knee
        [l_knee_x, l_knee_y],                    # 12: Left knee
        [r_foot_x, r_foot_y],                    # 13: Right foot
        [l_foot_x, l_foot_y],                    # 14: Left foot
    ])
    return coords

# ---- Animation set-up ----
fig, ax = plt.subplots(figsize=(4,8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

scat = ax.scatter([], [], s=70, color='white', linewidths=0)

def init():
    scat.set_offsets(np.zeros((15,2)))
    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.15, 0.85)
    ax.axis('off')
    return scat,

def animate(frame):
    t = frame/40.0
    coords = body_pose(t)
    scat.set_offsets(coords)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=400, interval=25, blit=True, init_func=init)

plt.show()
