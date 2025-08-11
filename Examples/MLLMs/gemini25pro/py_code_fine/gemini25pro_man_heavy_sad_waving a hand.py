
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Main Configuration ---
# Set the total number of frames for one full animation loop
NUM_FRAMES = 240
# Specify which hand should perform the waving action ('right' or 'left')
WAVE_HAND = 'right'

# --- Skeleton Structure Definition ---
# The skeleton is represented by 15 points (joints).
# These constants are used as indices for easy access to specific joints.
HEAD, NECK, PELVIS = 0, 1, 2
L_SHOULDER, R_SHOULDER = 3, 4
L_ELBOW, R_ELBOW = 5, 6
L_WRIST, R_WRIST = 7, 8
L_HIP, R_HIP = 9, 10
L_KNEE, R_KNEE = 11, 12
L_ANKLE, R_ANKLE = 13, 14

# --- Base Pose: "Sad Man with Heavy Weight" ---
# This dictionary holds the initial coordinates for the slumped, tired posture
# and will be used to calculate limb lengths.
skeleton_base = {
    'positions': np.zeros((15, 2)),
    'limb_lengths': {}
}

# Define the coordinates for the core body points to create a slumped posture.
# The figure is slightly hunched forward.
skeleton_base['positions'][PELVIS] = [0.0, 0.8]
skeleton_base['positions'][NECK]   = [0.05, 2.2]
skeleton_base['positions'][HEAD]   = [0.1, 2.7]

# Define leg positions with slightly bent knees.
hip_width = 0.4
skeleton_base['positions'][L_HIP] = [-hip_width, 0.8]
skeleton_base['positions'][R_HIP] = [hip_width, 0.8]
skeleton_base['positions'][L_KNEE] = [-hip_width - 0.05, 0.0]
skeleton_base['positions'][R_KNEE] = [hip_width + 0.05, 0.0]
skeleton_base['positions'][L_ANKLE] = [-hip_width, -0.8]
skeleton_base['positions'][R_ANKLE] = [hip_width, -0.8]

# Define arm positions with drooped shoulders.
shoulder_width = 0.55
skeleton_base['positions'][L_SHOULDER] = [-shoulder_width, 2.1]
skeleton_base['positions'][R_SHOULDER] = [shoulder_width, 2.1]
skeleton_base['positions'][L_ELBOW] = [-shoulder_width - 0.1, 1.4]
skeleton_base['positions'][R_ELBOW] = [shoulder_width + 0.1, 1.4]
skeleton_base['positions'][L_WRIST] = [-shoulder_width - 0.05, 0.8]
skeleton_base['positions'][R_WRIST] = [shoulder_width + 0.05, 0.8]

# Calculate and store limb lengths based on the initial pose.
def get_len(p1, p2):
    return np.linalg.norm(skeleton_base['positions'][p1] - skeleton_base['positions'][p2])

skeleton_base['limb_lengths']['upper_arm'] = get_len(L_SHOULDER, L_ELBOW)
skeleton_base['limb_lengths']['lower_arm'] = get_len(L_ELBOW, L_WRIST)

# --- Animation Core Logic ---
def animate(frame):
    """
    Calculates the position of each of the 15 points for a given frame.
    """
    points = np.copy(skeleton_base['positions'])
    t = frame / NUM_FRAMES  # Normalized time (progress from 0.0 to 1.0)

    # 1. Breathing/Swaying Motion: A subtle, slow sine wave applied to the
    #    torso to simulate breathing and fatigue.
    sway_amp = 0.02
    sway_freq = 2 * np.pi
    sway_dy = sway_amp * np.sin(sway_freq * t)
    head_sway_dy = 1.5 * sway_amp * np.sin(sway_freq * t - 0.5)

    torso_indices = [PELVIS, NECK, HEAD, L_SHOULDER, R_SHOULDER, L_HIP, R_HIP]
    points[torso_indices, 1] += sway_dy
    points[HEAD, 1] += head_sway_dy

    # 2. Hand Waving Motion: A multi-phase animation for the waving arm.
    lift_duration = 0.25
    wave_duration = 0.50
    lower_duration = 0.25

    if WAVE_HAND == 'right':
        sh, el, wr = R_SHOULDER, R_ELBOW, R_WRIST
        other_sh = L_SHOULDER
        sign = 1
    else:
        sh, el, wr = L_SHOULDER, L_ELBOW, L_WRIST
        other_sh = R_SHOULDER
        sign = -1

    # Keep the non-waving arm in its initial relative position to the swaying shoulder.
    non_waving_indices = (L_SHOULDER, L_ELBOW, L_WRIST) if WAVE_HAND == 'right' else (R_SHOULDER, R_ELBOW, R_WRIST)
    points[non_waving_indices[1]] = points[non_waving_indices[0]] + (skeleton_base['positions'][non_waving_indices[1]] - skeleton_base['positions'][non_waving_indices[0]])
    points[non_waving_indices[2]] = points[non_waving_indices[1]] + (skeleton_base['positions'][non_waving_indices[2]] - skeleton_base['positions'][non_waving_indices[1]])


    # Define angles for the arm at rest (drooped) and when raised for waving.
    base_shoulder_angle = np.deg2rad(-100) * sign
    base_elbow_angle_rel = np.deg2rad(-15) * sign
    lift_shoulder_angle = np.deg2rad(-45) * sign
    lift_elbow_angle_rel = np.deg2rad(-60) * sign

    # Interpolate angles based on the current phase of the animation.
    if 0 <= t < lift_duration:
        # Phase 1: Lifting the arm.
        p = t / lift_duration
        p_eased = 0.5 * (1 - np.cos(np.pi * p))  # Ease-in-out for smooth start/end.
        shoulder_angle = base_shoulder_angle + p_eased * (lift_shoulder_angle - base_shoulder_angle)
        elbow_angle_rel = base_elbow_angle_rel + p_eased * (lift_elbow_angle_rel - base_elbow_angle_rel)

    elif lift_duration <= t < lift_duration + wave_duration:
        # Phase 2: Waving the hand.
        p = (t - lift_duration) / wave_duration
        shoulder_angle = lift_shoulder_angle
        wave_amp = np.deg2rad(25) * sign
        wave_freq = 2 * np.pi * 2  # Two wave cycles.
        elbow_angle_rel = lift_elbow_angle_rel + wave_amp * np.sin(wave_freq * p)

    else:
        # Phase 3: Lowering the arm.
        p = (t - lift_duration - wave_duration) / lower_duration
        p_eased = 0.5 * (1 - np.cos(np.pi * p))
        shoulder_angle = lift_shoulder_angle + p_eased * (base_shoulder_angle - lift_shoulder_angle)
        elbow_angle_rel = lift_elbow_angle_rel + p_eased * (base_elbow_angle_rel - lift_elbow_angle_rel)

    # Add a subtle dip to the opposite shoulder to convey the weight of the lifted arm.
    arm_lift_ratio = (shoulder_angle - base_shoulder_angle) / (lift_shoulder_angle - base_shoulder_angle)
    arm_lift_ratio = np.clip(arm_lift_ratio, 0, 1)
    points[other_sh, 1] -= arm_lift_ratio * 0.08

    # Apply the calculated angles to find the new positions of the elbow and wrist.
    shoulder_pos = points[sh]
    upper_arm_len = skeleton_base['limb_lengths']['upper_arm']
    lower_arm_len = skeleton_base['limb_lengths']['lower_arm']

    points[el, 0] = shoulder_pos[0] + upper_arm_len * np.cos(shoulder_angle)
    points[el, 1] = shoulder_pos[1] + upper_arm_len * np.sin(shoulder_angle)

    total_elbow_angle = shoulder_angle + elbow_angle_rel
    points[wr, 0] = points[el, 0] + lower_arm_len * np.cos(total_elbow_angle)
    points[wr, 1] = points[el, 1] + lower_arm_len * np.sin(total_elbow_angle)

    # 3. Legs: Keep legs in their base pose relative to the swaying hips.
    for side_indices in [(L_HIP, L_KNEE, L_ANKLE), (R_HIP, R_KNEE, R_ANKLE)]:
        hip, knee, ankle = side_indices
        points[knee] = points[hip] + (skeleton_base['positions'][knee] - skeleton_base['positions'][hip])
        points[ankle] = points[knee] + (skeleton_base['positions'][ankle] - skeleton_base['positions'][knee])

    # Update the positions of the points in the scatter plot.
    scatter.set_offsets(points)
    return scatter,

# --- Matplotlib Visualization Setup ---
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_facecolor('black')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.5, 3.5)
ax.set_aspect('equal', adjustable='box')
plt.axis('off')
fig.tight_layout(pad=0)

# Create the initial scatter plot object with white points.
scatter = ax.scatter([], [], c='white', s=70)

def init():
    """Initializes the animation."""
    scatter.set_offsets(np.empty((15, 2)))
    return scatter,

# Create the animation object.
ani = animation.FuncAnimation(fig, animate, frames=NUM_FRAMES,
                              init_func=init, blit=True, interval=33)

# Display the animation.
plt.show()
