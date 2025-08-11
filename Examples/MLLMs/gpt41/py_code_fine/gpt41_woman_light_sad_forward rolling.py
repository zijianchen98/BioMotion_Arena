
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- Body Model: 15 Points ----
# Indices:      Names:
# 0             Head
# 1,2           Shoulders (L,R)
# 3,4           Elbows (L,R)
# 5,6           Wrists (L,R)
# 7             spine/hip center
# 8,9           Hips (L,R)
# 10,11         Knees (L,R)
# 12,13         Ankles (L,R)
# 14            Sternum (chest, above hip center)

# BODY SKELETON: approximate 2D graph.
# The skeleton is defined so when upright it's in a "sad" weak stance
# and when rolling, all 15 points roll as a loose chain.

# Simulated with forward roll (somersault).

# Key parameters
n_points = 15
frames = 64  # One roll cycle
fps = 30

# Stick figure model: lengths in arbitrary units
L_head = 0.32
L_neck = 0.18
L_torso = 0.53
L_pelvis = 0.26
L_upper_arm = 0.28
L_forearm = 0.26
L_upper_leg = 0.41
L_lower_leg = 0.36

# Neutral pose (upright, slightly stooped posture)
def neutral_pose():
    # y-axis up
    y0 = 0
    x0 = 0
    # Hip center (spine base)
    p7 = np.array([x0, y0])
    # Sternum: up from hip
    p14 = p7 + np.array([0, L_torso])
    # Head: up from sternum + neck + half head height
    head_ctr = p14 + np.array([0, L_neck + L_head/2])
    # Shoulders: out from sternum
    sh_offset = 0.18
    p1 = p14 + np.array([-sh_offset, 0.01])
    p2 = p14 + np.array([sh_offset, 0.01])
    # Elbows: forward/down from shoulders
    p3 = p1 + np.array([-0.07, -L_upper_arm])
    p4 = p2 + np.array([0.07, -L_upper_arm])
    # Wrists: further out and down from elbows
    p5 = p3 + np.array([-0.09, -L_forearm])
    p6 = p4 + np.array([0.09, -L_forearm])
    # Hips: out from hip center
    hip_offset = 0.12
    p8 = p7 + np.array([-hip_offset, 0])
    p9 = p7 + np.array([hip_offset, 0])
    # Knees: down from hips + slight inward
    p10 = p8 + np.array([0.02, -L_upper_leg])
    p11 = p9 + np.array([-0.02, -L_upper_leg])
    # Ankles: down from knees + slight inward
    p12 = p10 + np.array([0.03, -L_lower_leg])
    p13 = p11 + np.array([-0.03, -L_lower_leg])
    # Head as a point
    p0 = head_ctr
    pts = np.stack([p0, p1, p2, p3, p4, p5, p6,
                    p7, p8, p9, p10, p11, p12, p13, p14])
    return pts

# Forward Roll Trajectory
def roll_pose(t, sad_angle=20, sad_head_dip=8):
    """
    t: phase in [0,1)
    sad_angle: deg, how stooped/curved (for 'sad' style)
    sad_head_dip: deg, extra downward head orientation (sad look)
    Returns array (15,2) of xy
    """
    # Rotate the whole stick figure about the hand/shoulders
    theta = 2*np.pi * t
    neutral = neutral_pose()
    center = neutral[14]  # Use sternum as local 'center' of rotation
    
    # Curvature: For 'sad' and for 'rolling', we add more curl as subject is upside down
    # from upright (theta=0), min curve, to max at upside-down
    curvature = np.deg2rad(sad_angle) + 0.50*np.abs(np.sin(theta))  # more curve upside-down
    
    # Forward position: move horizontally as roll progresses, as in a real forward roll
    x_disp = 0.5 * np.sin(theta)
    y_disp = 0.1 * np.cos(theta)

    # Animation: Apply curve along body
    pts = np.zeros_like(neutral)
    # Chain model: pelvis to head
    chain_lengths = [
        0,         # head: start at neck
        L_neck,    # neck (sternum to head base)
        L_torso,   # torso (spine)
    ]
    # For simplicity, build a "spine curve" with head, sternum, and hip, happy-sad forward curl
    n_spine = 5
    spine = []
    for i in range(n_spine):
        frac = i / (n_spine-1)
        angle = curvature * (frac-0.1)  # more curve at top
        r = L_torso * frac
        p = center + np.array([r*np.sin(angle), r*np.cos(angle)])
        spine.append(p)
    spine = np.array(spine)
    # Place the major points
    p14 = spine[2]    # sternum
    p7  = spine[0]    # hip
    p0  = spine[-1]   # head

    # Shoulders: sternum +/- outwards, rotated and slightly slouched
    sh_angle = curvature*0.2
    sh_offset = 0.18
    sh_vec = np.array([[np.cos(sh_angle), -np.sin(sh_angle)],
                       [np.cos(-sh_angle), -np.sin(-sh_angle)]])
    p1 = p14 + sh_offset*sh_vec[0]  # left
    p2 = p14 + sh_offset*sh_vec[1]  # right

    # Elbows: down/forward from shoulder, bent (sad: arms more down)
    elb_angle = -curvature*0.7 - 0.6
    elb_off = np.array([np.sin(elb_angle), -np.cos(elb_angle)]) * L_upper_arm
    p3 = p1 + elb_off
    p4 = p2 + elb_off
    # Wrists: further in that direction
    wr_angle = elb_angle - 0.2
    wr_off = np.array([np.sin(wr_angle), -np.cos(wr_angle)]) * L_forearm
    p5 = p3 + wr_off
    p6 = p4 + wr_off

    # Hips: from hip center out to sides, more knees together (sad)
    hip_offset = 0.11
    hip_vec = np.array([[np.cos(0.0), -np.sin(0.0)],
                        [np.cos(0.0),  np.sin(0.0)]])
    p8 = p7 + hip_offset*hip_vec[0]
    p9 = p7 + hip_offset*hip_vec[1]
    # Knees: forward/down, inward
    knee_angle = -curvature*0.7 - 0.8
    knee_off = np.array([np.sin(knee_angle), -np.cos(knee_angle)]) * L_upper_leg
    p10 = p8 + 0.02 + knee_off
    p11 = p9 - 0.02 + knee_off
    # Ankles: down/inward
    ankle_angle = knee_angle - 0.13
    ankle_off = np.array([np.sin(ankle_angle), -np.cos(ankle_angle)]) * L_lower_leg
    p12 = p10 + 0.03 + ankle_off
    p13 = p11 - 0.03 + ankle_off

    # Slightly tip head downward (sad expression)
    sad_head_theta = -np.deg2rad(sad_head_dip)
    p0 = p14 + np.array([0, L_neck]) \
         + np.array([np.sin(sad_head_theta), np.cos(sad_head_theta)]) * (L_head/2)

    # Stack them up (head, shoulders, elbows, wrists, hip, etc)
    pts[0] = p0
    pts[1] = p1
    pts[2] = p2
    pts[3] = p3
    pts[4] = p4
    pts[5] = p5
    pts[6] = p6
    pts[7] = p7
    pts[8] = p8
    pts[9] = p9
    pts[10] = p10
    pts[11] = p11
    pts[12] = p12
    pts[13] = p13
    pts[14] = p14

    # Rotate whole body for rolling
    # Pivot about shoulder midpoint
    shoulder_mid = 0.5*(p1+p2)
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    pts_centered = pts - shoulder_mid
    pts_rot = pts_centered @ R.T
    # Move cyclically forward as the rolling progresses
    pts_disp = pts_rot + np.array([x_disp, 1.4 + y_disp])

    # Add subtle offsets/perturbations to simulate soft joints (biomechanical plausibility/movement)
    # (optional, for style; can be omitted)
    # For 'sad', animate wrists droop downward and head droops more at the bottom
    droop = 0.14*np.sin(theta + 0.8)
    pts[5] = pts[5] + np.array([0, -droop])
    pts[6] = pts[6] + np.array([0, -droop])
    # head lower when upside down (sad head droop)
    if np.abs(np.sin(theta)) > 0.9:
        pts[0] = pts[0] + np.array([0, -0.04])

    return pts_disp

# ----- Animation -----
fig, ax = plt.subplots(figsize=(5,8))
plt.style.use('dark_background')
ax.set_facecolor('black')
ax.set_xlim(-1.3,1.3)
ax.set_ylim(0,2.5)
ax.set_aspect('equal')
ax.axis('off')

# Scatter plot for the 15 points
scat = ax.scatter(np.zeros(n_points), np.zeros(n_points), s=60, c='white')

# Animation update function
def animate(i):
    t = (i % frames) / frames
    pts = roll_pose(t)
    scat.set_offsets(pts)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=frames, interval=1000/fps, blit=True
)

plt.show()
