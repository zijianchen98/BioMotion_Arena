
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint labels for 15-point stick figure (sagittal view):
# 0: head, 1: right shoulder, 2: left shoulder, 3: right elbow, 4: left elbow,
# 5: right hand, 6: left hand, 7: pelvis, 8: right hip, 9: left hip,
# 10: right knee, 11: left knee, 12: right ankle, 13: left ankle, 14: mid-pelvis

# Limb lengths, in pixels
HEAD_HEIGHT = 30
SHOULDER_Y = 20
SHOULDER_SPAN = 32
TORSO_LENGTH = 48
PELVIS_WIDTH = 24
UPPER_ARM = 28
FOREARM = 24
THIGH = 42
SHIN = 38
UPPER_BODY_OFFSET = 24

def get_pose(t, stride=90):
    """
    Returns the 2D (x, y) positions of the 15 anatomical points at time t in the motion cycle.
    - t: Progress through the jump cycle [0, 1]
    - stride: jump forward stride in pixels per cycle.
    """

    # Vertical jump parameters
    cycle_t = t % 1.0
    g = 2 * np.pi
    t_jump = cycle_t

    # Jump arc: y = a - b * (t_jump - 0.5) ** 2
    jump_height = 100
    base_y = 100
    y_traj = base_y + jump_height * (1 - 4 * (t_jump - 0.5) ** 2)  # Parabola

    # Horizontal motion: moving forward constantly
    base_x = 80 + stride * cycle_t

    # Sway (to keep figure lively)
    sway = 6 * np.sin(np.pi * t_jump)

    # Body lean (forward during takeoff, upright at top, forward on landing)
    lean = np.deg2rad(12 * np.sin(np.pi * t_jump))

    # Arms/legs coordinated with jump phase (t_jump in [0,1])
    # Arms swing: backward on crouch (0), forward at apex (0.5), backward at land (1)
    arm_swing = np.deg2rad(-60 * np.cos(np.pi * t_jump))  # from -60 (back) to +60 (forward)
    elbow_flex = np.deg2rad(20 + 15 * np.sin(np.pi * t_jump))

    # Legs fold during takeoff and apex, extend on landing and start
    thigh_angle = np.deg2rad(-50 + 80 * np.sin(np.pi * t_jump))  # crouched (-50), to upright (30)
    knee_flex = np.deg2rad(40 + 20 * np.sin(np.pi * t_jump))  # flexed at start/land, less flexed at top

    # Pelvis tilts slightly with phase
    pelvis_tilt = np.deg2rad(8 * np.sin(np.pi * t_jump))

    # Center (mid-pelvis)
    mp_x, mp_y = base_x, y_traj

    # Pelvis
    lw_pelvis = PELVIS_WIDTH / 2
    pelvis_L = np.array([
        mp_x - lw_pelvis * np.cos(pelvis_tilt),
        mp_y + lw_pelvis * np.sin(pelvis_tilt)
    ])
    pelvis_R = np.array([
        mp_x + lw_pelvis * np.cos(pelvis_tilt),
        mp_y - lw_pelvis * np.sin(pelvis_tilt)
    ])
    pelvis_M = np.array([mp_x, mp_y])

    # Shoulders (upper body offset from pelvis)
    torso_angle = lean  # lean body
    SHOULDER_YOFF = TORSO_LENGTH
    sh_x = mp_x + SHOULDER_YOFF * np.sin(torso_angle)
    sh_y = mp_y - SHOULDER_YOFF * np.cos(torso_angle)

    # Shoulders left/right
    sh_span = SHOULDER_SPAN / 2
    sh_L = np.array([
        sh_x - sh_span * np.cos(torso_angle),
        sh_y - sh_span * np.sin(torso_angle)
    ])
    sh_R = np.array([
        sh_x + sh_span * np.cos(torso_angle),
        sh_y + sh_span * np.sin(torso_angle)
    ])
    sh_M = np.array([sh_x, sh_y])

    # Head position (directly above shoulders)
    head_x = sh_x + HEAD_HEIGHT * np.sin(torso_angle)
    head_y = sh_y - HEAD_HEIGHT * np.cos(torso_angle)
    head = np.array([head_x, head_y])

    # Arms: origin at shoulders, move with shoulder_angle and arm_swing
    def arm_chain(shoulder, side):
        # side: -1 for left, +1 for right
        # Shoulder
        s_ang = torso_angle + arm_swing * side
        elbow = shoulder + UPPER_ARM * np.array([np.sin(s_ang), -np.cos(s_ang)])
        e_ang = s_ang + elbow_flex * side
        hand = elbow + FOREARM * np.array([np.sin(e_ang), -np.cos(e_ang)])
        return elbow, hand

    elb_R, hand_R = arm_chain(sh_R, +1)
    elb_L, hand_L = arm_chain(sh_L, -1)

    # Legs: hips at pelvis, move with thigh_angle
    def leg_chain(hip, side):
        # side: -1 for left, +1 for right
        thigh_ang = torso_angle + thigh_angle * side
        knee = hip + THIGH * np.array([np.sin(thigh_ang), np.cos(thigh_ang)])
        shn_ang = thigh_ang + knee_flex * side
        ankle = knee + SHIN * np.array([np.sin(shn_ang), np.cos(shn_ang)])
        return knee, ankle

    knee_R, ankle_R = leg_chain(pelvis_R, +1)
    knee_L, ankle_L = leg_chain(pelvis_L, -1)

    # Assemble: order matches example:
    # 0: head
    # 1: right shoulder, 2: left shoulder, 3: right elbow, 4: left elbow,
    # 5: right hand, 6: left hand, 7: pelvis right, 8: pelvis left, 9: pelvis mid
    # 10: right knee, 11: left knee, 12: right ankle, 13: left ankle
    keypoints = np.array([
        head,
        sh_R, sh_L,
        elb_R, elb_L,
        hand_R, hand_L,
        pelvis_R, pelvis_L, pelvis_M,
        knee_R, knee_L,
        ankle_R, ankle_L,
        pelvis_M  # 14: repeat mid-pelvis for symmetry (or use for base for ground ref)
    ])
    return keypoints

# Setup matplotlib
fig, ax = plt.subplots(figsize=(3.2, 5.6))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
plt.axis("off")
ax.set_xlim(0, 320)
ax.set_ylim(0, 450)

# Draw ground line (for reference, faded)
ground, = ax.plot([0, 320], [100, 100], color='white', lw=1, alpha=0.15, zorder=0)

# Plot the 15 points
scat = ax.scatter([], [], s=60, color='white', edgecolors='none', zorder=10)

def init():
    scat.set_offsets(np.zeros((15, 2)))
    return scat,

def animate(i):
    # Loop duration: 2 s at 60 fps
    t = (i % 120) / 120.0
    pts = get_pose(t)
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=120, init_func=init, interval=1000/60, blit=True, repeat=True
)

plt.show()
