
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Number and order of points: 
# 0: Head         1-2: Shoulders        3-4: Elbows
# 5-6: Wrists     7: Hip center         8-9: Hips (L/R)
# 10-11: Knees    12-13: Ankles        14: Weight (object)
#
# We'll define a skeleton to ensure consistent, plausible motion.

# Body segment lengths (relative, can rescale for size)
L_head = 0.12
L_neck = 0.06
L_trunk = 0.28
L_pelvis = 0.14
L_upper_arm = 0.14
L_forearm = 0.13
L_thigh = 0.21
L_shank = 0.22
L_foot = 0.06
L_weight = 0.12  # Position of lightweight held

# Joint connectivities for consistency, not used for drawing
# (just for ordering and segment hierarchy)
# We'll simulate rolling: squat, arm down, curl into ball, rotate over, uncurl

def rollover_pose(t, Nframes):
    """Return 15 point positions (x, y) simulating a forward roll for frame t."""
    # The subject starts upright, squats, tucks, rotates forward, untucks, stands up.
    # t in [0, Nframes)
    # We'll normalize phase to [0,1) for cyclic motion
    phase = (t % Nframes) / Nframes

    # Subject center (hip) 'travels' to the right as they roll
    # and follows a small arc (for realism)
    x_center = 0.5 + 0.3 * phase
    y_center = 0.32 + 0.10 * np.sin(np.pi * phase)

    # The rolling motion: angle theta over time (0 to 2pi over roll)
    roll_angle = 2 * np.pi * phase

    # "Squash" and "unsquash" body to simulate tucking in the roll
    # Tuck: max at phase in [0.12, 0.7], untucked at endpoints
    if phase < 0.15:
        tuck = np.interp(phase, [0.0, 0.15], [0.0, 1.0])
    elif phase > 0.75:
        tuck = np.interp(phase, [0.75, 1.0], [1.0, 0.0])
    else:
        tuck = 1.0
    # Tucking shortens arms, legs, trunk; moves all limbs closer to pelvis
    tlimb = 1.0 - 0.45 * tuck  # limb proportion (shorten to ~55% when fully tucked)
    ttrunk = 1.0 - 0.38 * tuck

    # Pelvis base
    hip = np.array([x_center, y_center])

    # For tucking, trunk curls forward & upward
    trunk_dir = np.array([0, 1])  # points up when standing
    if phase < 0.15:  # squatting
        # Hip drops, knees bend
        squat = np.interp(phase, [0, 0.15], [0., 1.])
    elif phase > 0.9:  # rising
        squat = np.interp(phase, [0.9, 1.0], [1., 0.])
    else:
        squat = 1.0
    trunk_angle = -np.pi / 2 * squat  # from up to 90 deg forward bend

    # During roll, trunk follows roll theta (rotates over hip)
    if phase > 0.18 and phase < 0.90:
        # Tucked rolling!
        trunk_angle = -np.pi / 2 + roll_angle

    # Neck & head
    shoulder_pos = hip + (L_trunk * ttrunk) * np.array(
        [np.sin(trunk_angle), np.cos(trunk_angle)])
    neck_pos = shoulder_pos + L_neck * np.array(
        [np.sin(trunk_angle), np.cos(trunk_angle)])
    head_pos = neck_pos + L_head * np.array(
        [np.sin(trunk_angle), np.cos(trunk_angle)])

    # Shoulders (width apart, perpendicular to trunk)
    s_offset = 0.16
    dx_s, dy_s = s_offset * np.cos(trunk_angle), -s_offset * np.sin(trunk_angle)
    sh_L = shoulder_pos + np.array([dx_s, dy_s])
    sh_R = shoulder_pos - np.array([dx_s, dy_s])

    # Arms: When squatting/rolling, arms go toward/above head to hold "weight"
    # Natural swing to animate
    # Forward roll: arms move in arc from sides to over head, then back
    if phase < 0.18:
        upness = np.interp(phase, [0.0, 0.15, 0.18], [0.0, 1.0, 1.0])
    elif phase > 0.85:
        upness = np.interp(phase, [0.85, 1.0], [1.0, 0.0])
    else:
        upness = 1.0

    base_angle = trunk_angle - np.pi / 3  # start at arms-down
    arm_angle = base_angle + upness * (np.pi / 2 + np.pi / 6)  # swing up

    # Add a "curl-in" during tucking in the roll
    if tuck > 0.9:
        fore_angle_delta = 0.85
    else:
        fore_angle_delta = 0.35

    # Left arm (shoulder, elbow, wrist)
    el_L = sh_L + (L_upper_arm * tlimb) * np.array(
        [np.sin(arm_angle), np.cos(arm_angle)])
    wr_L = el_L + (L_forearm * tlimb) * np.array(
        [np.sin(arm_angle - fore_angle_delta), np.cos(arm_angle - fore_angle_delta)])
    # Right arm
    el_R = sh_R + (L_upper_arm * tlimb) * np.array(
        [np.sin(arm_angle), np.cos(arm_angle)])
    wr_R = el_R + (L_forearm * tlimb) * np.array(
        [np.sin(arm_angle - fore_angle_delta), np.cos(arm_angle - fore_angle_delta)])

    # "Object": a weight/lightweight held in both hands, average between wrists, projected further ahead (so it goes over head in the roll)
    ob_avg = 0.5 * (wr_L + wr_R)
    obj_vec = np.array([np.sin(arm_angle-0.3), np.cos(arm_angle-0.3)])
    ob_pos = ob_avg + (L_weight * tlimb) * obj_vec

    # Hips (width apart)
    h_offset = L_pelvis / 2
    dx_h, dy_h = h_offset * np.cos(trunk_angle), -h_offset * np.sin(trunk_angle)
    hip_L = hip + np.array([dx_h, dy_h])
    hip_R = hip - np.array([dx_h, dy_h])

    # Legs: As standing/squatting, knees bend forward, ankles below
    # During roll, knees draw up
    # Standing: straight down (angle = trunk_angle), squatting: forward
    # tucking: knees more toward body
    knee_angle = trunk_angle + np.pi/2 * squat + 0.6 * tuck
    ankle_angle = knee_angle + 0.8 + 0.7 * tuck

    # Left leg
    kn_L = hip_L + (L_thigh * tlimb) * np.array(
        [np.sin(knee_angle), np.cos(knee_angle)])
    an_L = kn_L + (L_shank * tlimb) * np.array(
        [np.sin(ankle_angle), np.cos(ankle_angle)])
    # Right leg
    kn_R = hip_R + (L_thigh * tlimb) * np.array(
        [np.sin(knee_angle), np.cos(knee_angle)])
    an_R = kn_R + (L_shank * tlimb) * np.array(
        [np.sin(ankle_angle), np.cos(ankle_angle)])

    # Return all points in the correct order
    points = np.stack([
        head_pos,           # 0 head
        sh_L, sh_R,         # 1-2 shoulders
        el_L, el_R,         # 3-4 elbows
        wr_L, wr_R,         # 5-6 wrists
        hip,                # 7 hip center
        hip_L, hip_R,       # 8-9 hips
        kn_L, kn_R,         # 10-11 knees
        an_L, an_R,         # 12-13 ankles
        ob_pos,             # 14 object (weight)
    ])
    return points

# Animation setup
fig, ax = plt.subplots(figsize=(3, 6))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

Npoints = 15
Nframes = 120

scat = ax.scatter([], [], s=34, c='white', edgecolors='none')

# Set up the background
ax.set_facecolor('black')
ax.set_xlim(0.15, 1.0)
ax.set_ylim(0.08, 1.17)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
for sp in ax.spines.values():
    sp.set_visible(False)

def init():
    scat.set_offsets(np.zeros((Npoints,2)))
    return scat,

def animate(i):
    arr = rollover_pose(i, Nframes)
    scat.set_offsets(arr)
    # Intensity = more faded for weight (point 14)
    colors = ['white']*14 + ['#AAAAAA']
    scat.set_color(colors)
    return scat,

ani = FuncAnimation(fig, animate, frames=Nframes, interval=1000/40, blit=True, init_func=init)

plt.show()
