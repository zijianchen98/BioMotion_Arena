
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 point-lights: Head, Neck, L/R Shoulders, L/R Elbows, L/R Wrists,
# Pelvis, L/R Hips, L/R Knees, L/R Ankles, ~L/R Toes
# Indices: 0:Head, 1:Neck, 2:RS, 3:LS, 4:RE, 5:LE, 6:RW, 7:LW, 8:Pelvis,
# 9:RH, 10:LH, 11:RK, 12:LK, 13:RA, 14:LA

# Skeleton segment lengths (arbitrary units):
L_NECK = 0.18   # Neck to head
L_SHOULDER = 0.17
L_UPPER_ARM = 0.20
L_LOWER_ARM = 0.20
L_TORSO = 0.26
L_PELVIS_TO_HIP = 0.08
L_UPPER_LEG = 0.28
L_LOWER_LEG = 0.25
L_ANKLE_TO_TOE = 0.10

# Joint pairs as (parent_index, child_index)
JOINTS = [
    (1, 0),   # neck-head
    (1, 2),   # neck-rshoulder
    (1, 3),   # neck-lshoulder
    (2, 4),   # rshoulder-relbow
    (3, 5),   # lshoulder-lelbow
    (4, 6),   # relbow-rwrist
    (5, 7),   # lelbow-lwrist
    (1, 8),   # neck-pelvis
    (8, 9),   # pelvis-rhip
    (8,10),   # pelvis-lhip
    (9,11),   # rhip-rknee
    (10,12),  # lhip-lknee
    (11,13),  # rknee-rankle
    (12,14),  # lknee-lankle,
    (13,13),  # could use as toes
    (14,14)
]

def get_body_pose(t, jump_phase, is_ascending):
    # t is from 0 to 1 (normalized phase in jump cycle)
    # jump_phase: 0 to 1 full cycle
    # Return 15 (x, y) joint positions
    #
    # Animation parameters
    hip_x, hip_y = 0, 0
    stance_width = 0.20
    shoulder_width = 0.30
    #
    # Vertical jump arc (global Y offset for whole body, simple ballistic trajectory)
    Y_JUMP = 0.6  # meters, max jump height
    g = 2*Y_JUMP  # determines flight-time, normalized so peak at t=0.35--0.65
    # smooth jump curve: t=0 to t=1. 0 at start, peak at t=0.5, 0 at end.
    t0 = 0.40; t1 = 0.60  # frames spent airborne
    if t < t0:
        y_off = 0
        v_body = (Y_JUMP/(t1-t0))*np.sin(np.pi*(t-t0)/(t1-t0)) if t > t0-0.15 else 0
    elif t > t1:
        y_off = 0
        v_body = 0
    else:
        dy = t - t0
        jump_air = (t1-t0)
        y_off = Y_JUMP * np.sin(np.pi * dy/jump_air)
        v_body = Y_JUMP*np.pi/(t1-t0)*np.cos(np.pi * dy/jump_air) * (1/60)
    # Use y_off as the vertical root/pelvis offset
    #
    # Pelvis
    pelvis = np.array([0, hip_y + y_off])
    # Neck (above pelvis by L_TORSO)
    neck = pelvis + np.array([0, L_TORSO])
    # Head (above neck)
    head = neck + np.array([0, L_NECK])
    #
    # Shoulders (from neck at shoulder width)
    r_shoulder = neck + np.array([+shoulder_width/2, 0])
    l_shoulder = neck + np.array([-shoulder_width/2, 0])
    # Elbows and Wrists
    # Arm swing: during descend, arms forward; during takeoff, arms upward
    # Swing as: angle = base +/- swing, swing varies with phase
    # Up phase: 90 deg (vertical) at t~0, forward (horizontal, 30 deg) at peak
    arm_up_base = np.deg2rad(70)
    arm_swing = 0.5 if t < t0 else (0 if t > t1 else
                                    0.5*np.cos(np.pi*(t-t0)/(t1-t0)))  # reduced at apex
    r_arm_angle = -np.pi/2 + arm_up_base*arm_swing
    l_arm_angle = -np.pi/2 - arm_up_base*arm_swing
    # Elbows
    r_elbow = r_shoulder + L_UPPER_ARM * np.array([np.cos(r_arm_angle), np.sin(r_arm_angle)])
    l_elbow = l_shoulder + L_UPPER_ARM * np.array([np.cos(l_arm_angle), np.sin(l_arm_angle)])
    # Wrists
    r_wrist = r_elbow + L_LOWER_ARM * np.array([np.cos(r_arm_angle), np.sin(r_arm_angle)])
    l_wrist = l_elbow + L_LOWER_ARM * np.array([np.cos(l_arm_angle), np.sin(l_arm_angle)])
    #
    # Hips
    r_hip = pelvis + np.array([+stance_width/2, 0])
    l_hip = pelvis + np.array([-stance_width/2, 0])
    # Knees: when jumping, legs extend on takeoff, flex on land (t<0.15 or t>0.85)
    if t < t0 or t > t1:
        knee_bend = np.deg2rad(50)
        leg_ang = np.pi/2 - knee_bend  # bent
    else:
        leg_ang = np.pi/2  # extended, vertical
    r_knee = r_hip + L_UPPER_LEG * np.array([0, -np.cos(leg_ang)])
    l_knee = l_hip + L_UPPER_LEG * np.array([0, -np.cos(leg_ang)])
    r_ankle = r_knee + L_LOWER_LEG * np.array([0, -np.cos(leg_ang)])  # same angle
    l_ankle = l_knee + L_LOWER_LEG * np.array([0, -np.cos(leg_ang)])
    # Toes: ahead in jump; slightly behind on takeoff ("push-off" pose)
    if t < t0:
        toe_offset = 0.04  # behind ankle on ground
    elif t > t1:
        toe_offset = 0.04
    else:
        toe_offset = 0.10  # ahead (airborne "float" positioning)
    r_toe = r_ankle + np.array([toe_offset, -L_ANKLE_TO_TOE])
    l_toe = l_ankle + np.array([-toe_offset, -L_ANKLE_TO_TOE])
    # All joints in order
    pts = np.stack([
        head, neck, r_shoulder, l_shoulder, r_elbow, l_elbow,
        r_wrist, l_wrist, pelvis, r_hip, l_hip, r_knee, l_knee, r_ankle, l_ankle
    ])
    # Toes are not in the canonical 15; optionally replace ankles with toes below
    foot_pts = np.stack([r_toe, l_toe])
    return pts, foot_pts

# --- Animation loop ---

fig, ax = plt.subplots(figsize=(3.5, 5.6))
ax.set_facecolor("black")
plt.axis('off')
ax.set_xlim([-0.5, 0.5])
ax.set_ylim([-0.15, 1.3])

num_frames = 80             # smoothness
frames_per_jump = num_frames
jump_duration = 1.3         # seconds (total time for jump cycle)
dt = jump_duration / frames_per_jump

# Animation: observers see a continuously looped jump
def animate(i):
    ax.cla()
    ax.set_facecolor("black")
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.15, 1.3])
    plt.axis('off')
    #
    t = i / frames_per_jump
    # t: [0,1); remap to [0,1]
    is_ascending = t < 0.5
    # Generate body-pose
    pts, foot_pts = get_body_pose(t, t, is_ascending)
    # Draw 15 white dots
    ax.scatter(pts[:,0], pts[:,1], s=36, color="white")
    # Add toes (using color or size, optional):
    # ax.scatter(foot_pts[:,0], foot_pts[:,1], s=24, color="white")
    # option: connect with faded lines for debugging skeleton
    # for (p,c) in JOINTS:
    #     ax.plot([pts[p,0], pts[c,0]], [pts[p,1], pts[c,1]], lw=0.8, color="gray", alpha=0.2)

ani = animation.FuncAnimation(fig, animate, frames=frames_per_jump, interval=dt*1000, blit=False, repeat=True)
plt.show()
