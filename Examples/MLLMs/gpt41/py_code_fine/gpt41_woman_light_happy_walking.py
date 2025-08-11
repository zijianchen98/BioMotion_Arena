
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Indices for the 15 points
# 0: Head
# 1: Right Shoulder
# 2: Left Shoulder
# 3: Right Elbow
# 4: Left Elbow
# 5: Right Hand
# 6: Left Hand
# 7: Hip Center
# 8: Right Hip
# 9: Left Hip
#10: Right Knee
#11: Left Knee
#12: Right Foot
#13: Left Foot
#14: Spine (chest center)

# Body proportions for a woman (relative, "happy/light" style: soft curves)
POSE_DEF = {
    "HEAD_TO_SHOULDER": 0.13,
    "SHOULDER_WIDTH": 0.25,
    "SHOULDER_TO_HIP": 0.33,
    "HIP_WIDTH": 0.20,
    "HIP_TO_KNEE": 0.33,
    "KNEE_TO_FOOT": 0.29,
    "ARM": 0.31,
    "FOREARM": 0.26,
}

# Marker order for 15 points
def walker_pose(phase, step_length=0.17):
    """
    Returns the 2D coordinates of the 15 points at a given phase of walking.
    phase : float in [0, 2*pi], where 0 is one midstance, pi is the other.
    """

    # Pelvis center (origin), place in center
    hip_x, hip_y = 0.0, 0.0

    # Parameters
    shw = POSE_DEF["SHOULDER_WIDTH"]
    chw = POSE_DEF["HIP_WIDTH"]
    neck_y = hip_y + POSE_DEF["SHOULDER_TO_HIP"]
    sh_y = neck_y
    head_y = sh_y + POSE_DEF["HEAD_TO_SHOULDER"]
    chest_y = sh_y - 0.07  # intermediate for spine

    # Shoulders
    rs_x = hip_x + shw/2
    ls_x = hip_x - shw/2
    rs_y, ls_y = sh_y, sh_y

    # Hips
    rh_x = hip_x + chw/2
    lh_x = hip_x - chw/2
    rh_y, lh_y = hip_y, hip_y

    # Intermediate marker: chest center
    chest_x = hip_x
    chest_y = sh_y - 0.07

    # Head
    head_x, head_y = hip_x, sh_y + POSE_DEF["HEAD_TO_SHOULDER"]

    # Arm swing (phase offset from legs, ~pi)
    arm_phase = phase + np.pi

    arm_swing_amp = 0.18
    arm_lift = 0.06
    elbow_bend = 0.6  # natural bend for a light happy walk

    # Right arm
    # Shoulder -> elbow
    ra_theta = arm_swing_amp * np.sin(arm_phase) + np.deg2rad(7)
    re_x = rs_x + POSE_DEF["ARM"] * np.sin(ra_theta)
    re_y = rs_y - POSE_DEF["ARM"] * np.cos(ra_theta) + arm_lift
    # Elbow -> hand
    rh_theta = ra_theta + (np.pi/3 + elbow_bend*np.sin(arm_phase)/2)
    rhand_x = re_x + POSE_DEF["FOREARM"] * np.sin(rh_theta)
    rhand_y = re_y - POSE_DEF["FOREARM"] * np.cos(rh_theta)

    # Left arm
    la_theta = arm_swing_amp * np.sin(arm_phase + np.pi) - np.deg2rad(7)
    le_x = ls_x + POSE_DEF["ARM"] * np.sin(la_theta)
    le_y = ls_y - POSE_DEF["ARM"] * np.cos(la_theta) + arm_lift
    lh_theta = la_theta + (np.pi/3 + elbow_bend*np.sin(arm_phase + np.pi)/2)
    lhand_x = le_x + POSE_DEF["FOREARM"] * np.sin(lh_theta)
    lhand_y = le_y - POSE_DEF["FOREARM"] * np.cos(lh_theta)

    # Spine
    spine_x = hip_x
    spine_y = chest_y

    # Leg phase; "light happy" walk = slightly higher knee lift, lively
    leg_swing = 0.22
    knee_lift_amp = 0.16  # higher than neutral b/c light/happy
    foot_lift_amp = 0.10

    # Right leg
    rleg_theta = leg_swing * np.sin(phase)
    rknee_x = rh_x + POSE_DEF["HIP_TO_KNEE"] * np.sin(rleg_theta)
    rknee_y = rh_y - POSE_DEF["HIP_TO_KNEE"] * np.cos(rleg_theta) + knee_lift_amp*np.maximum(0, np.sin(phase))
    rfoot_theta = rleg_theta + (np.pi/6) + 0.10*np.sin(phase)  # slightly bent
    rfoot_x = rknee_x + POSE_DEF["KNEE_TO_FOOT"] * np.sin(rfoot_theta)
    rfoot_y = rknee_y - POSE_DEF["KNEE_TO_FOOT"] * np.cos(rfoot_theta) + foot_lift_amp*np.maximum(0, np.sin(phase))

    # Left leg (180 degrees out of phase)
    lleg_theta = leg_swing * np.sin(phase + np.pi)
    lknee_x = lh_x + POSE_DEF["HIP_TO_KNEE"] * np.sin(lleg_theta)
    lknee_y = lh_y - POSE_DEF["HIP_TO_KNEE"] * np.cos(lleg_theta) + knee_lift_amp*np.maximum(0, np.sin(phase + np.pi))
    lfoot_theta = lleg_theta + (np.pi/6) + 0.10*np.sin(phase + np.pi)
    lfoot_x = lknee_x + POSE_DEF["KNEE_TO_FOOT"] * np.sin(lfoot_theta)
    lfoot_y = lknee_y - POSE_DEF["KNEE_TO_FOOT"] * np.cos(lfoot_theta) + foot_lift_amp*np.maximum(0, np.sin(phase + np.pi))

    # Offset all points along +X to "walk"
    com_offset = step_length * phase/(2*np.pi)
    all_xs = np.array([
        head_x + com_offset,      # 0 head
        rs_x  + com_offset,       # 1 right shoulder
        ls_x  + com_offset,       # 2 left shoulder
        re_x  + com_offset,       # 3 right elbow
        le_x  + com_offset,       # 4 left elbow
        rhand_x + com_offset,     # 5 right hand
        lhand_x + com_offset,     # 6 left hand
        hip_x + com_offset,       # 7 hip center
        rh_x + com_offset,        # 8 right hip
        lh_x + com_offset,        # 9 left hip
        rknee_x + com_offset,     #10 right knee
        lknee_x + com_offset,     #11 left knee
        rfoot_x + com_offset,     #12 right foot
        lfoot_x + com_offset,     #13 left foot
        spine_x + com_offset      #14 chest mid (spine)
    ])
    all_ys = np.array([
        head_y,   # 0
        rs_y,     # 1
        ls_y,     # 2
        re_y,     # 3
        le_y,     # 4
        rhand_y,  # 5
        lhand_y,  # 6
        hip_y,    # 7
        rh_y,     # 8
        lh_y,     # 9
        rknee_y,  #10
        lknee_y,  #11
        rfoot_y,  #12
        lfoot_y,  #13
        spine_y   #14
    ])
    return all_xs, all_ys

# ---- Animation setup ----

fig, ax = plt.subplots(figsize=(4.5, 8))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

pointsize = 92 # radius squared, for dot size

# Fix axis for consistent size
ax.set_xlim(-0.4, 0.7)
ax.set_ylim(-0.1, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# Draw initial points (scatter)
init_x, init_y = walker_pose(0)
points = ax.scatter(init_x, init_y, s=pointsize, c='white', edgecolors='none')

# For showing coherent movement, optional lines (commented out, as style is dots only)
# To add lines, supply pairs of indices to connect
# skeleton_pairs = [
#     (0, 14), (14, 1), (14, 2), # head-chest-shoulder
#     (1, 3), (3, 5), # right arm
#     (2, 4), (4, 6), # left arm
#     (14, 7), # spine
#     (7, 8), (7, 9), # hips
#     (8, 10), (10, 12), # right leg
#     (9, 11), (11, 13) # left leg
# ]
# lines = [ax.plot([], [], c='white', lw=1.1)[0] for _ in skeleton_pairs]

def animate(frame):
    total_frames = 60
    walk_cycles = 2
    # Map frame to phase
    phase = 2 * np.pi * walk_cycles * (frame / total_frames)
    xs, ys = walker_pose(phase)
    points.set_offsets(np.column_stack([xs, ys]))
    # # If you want to add lines (see above)
    # for i, (a, b) in enumerate(skeleton_pairs):
    #     lines[i].set_data([xs[a], xs[b]], [ys[a], ys[b]])
    return points, # for blitting

ani = animation.FuncAnimation(
    fig, animate, frames=60, interval=1000/30, blit=True
)

plt.show()
