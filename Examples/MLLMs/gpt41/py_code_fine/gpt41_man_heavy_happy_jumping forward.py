
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set random seed for reproducibility
np.random.seed(2)

# Number of points
N_POINTS = 15

# Joint order: head, neck, R shoulder, L shoulder, mid torso,
# R elbow, L elbow, bottom torso, R hand, L hand,
# R knee, L knee, R foot, L foot, heavy weight object

JOINT_NAMES = [
    "head", "neck", "r_shoulder", "l_shoulder", "upper_torso",
    "r_elbow", "l_elbow", "mid_torso", "r_hand", "l_hand",
    "r_knee", "l_knee", "r_foot", "l_foot", "weight"
]

# Skeleton connections (just for structure, not drawn)
SKELETON = [
    (0, 1),         # head -> neck
    (1, 2), (1, 3), # neck -> shoulders
    (1, 4),         # neck -> upper torso
    (2, 5), (3, 6), # shoulders -> elbows
    (5, 8), (6, 9), # elbows -> hands
    (4, 7),         # upper torso -> mid torso
    (7, 10), (7, 11), # mid torso -> knees
    (10, 12), (11, 13) # knees -> feet
    # weight (14) will be attached in both hands
]

def jump_trajectory(num_frames, stride=3, jump_height=1.5):
    """Generate the jump's center-of-mass trajectory (x, y) for the sequence."""
    t = np.linspace(0, 2*np.pi, num_frames)
    # x: move steadily forward, with a bit of bounce
    x = 0.16 * t * stride
    # y: parabolic jump arc (with repeated cycles if needed)
    y = 2 + jump_height * np.sin(t)**2 # Always positive, resemble vertical motion
    return x, y

def get_limb_offsets(phase, frame_prop, heavy=True):
    """Get offsets for arms/legs at jump phase, heavy = 'weighted style'"""
    # Arms swing downward and hold object
    if heavy:
        # Both elbows/hands tuck close, slightly forward
        r_shoulder = np.array([0.19, 0.23 - 0.04*np.sin(phase)])
        l_shoulder = np.array([-0.19, 0.23 - 0.04*np.sin(phase)])
        r_elbow = r_shoulder + np.array([0.09, -0.19])
        l_elbow = l_shoulder + np.array([-0.09, -0.19])
        r_hand = r_elbow + np.array([0.12, -0.08])
        l_hand = l_elbow + np.array([-0.12, -0.08])
        # Add some bounce
        handsY_bounce = 0.01*np.sin(2*phase)
        r_hand[1] += handsY_bounce
        l_hand[1] += handsY_bounce
    else:
        # Arms swing naturally
        swing = 0.28*np.sin(phase)
        r_shoulder = np.array([0.19, 0.23])
        l_shoulder = np.array([-0.19, 0.23])
        r_elbow = r_shoulder + np.array([swing, -0.18])
        l_elbow = l_shoulder + np.array([-swing, -0.18])
        r_hand = r_elbow + np.array([0.13, -0.06])
        l_hand = l_elbow + np.array([-0.13, -0.06])
    # Legs: symmetric, extend and contract; heavy jump = knees more flexed
    squat = 0.09 + 0.06*np.sin(phase + np.pi) # more flex at crouch
    # Knees move up on takeoff, then extend
    r_knee = np.array([0.08, -0.45 + squat])
    l_knee = np.array([-0.08, -0.45 + squat])
    # Feet extend down and angle out on takeoff, land "flat"
    l_foot_x = -0.125 + 0.09*(np.sin(phase+np.pi/3)**2)*np.clip(1-frame_prop*2, 0.2, 1)
    r_foot_x =  0.125 - 0.09*(np.sin(phase+np.pi/3)**2)*np.clip(1-frame_prop*2, 0.2, 1)
    # Bounce feet up during the middle of the jump
    foot_y_offset = 0.22*np.sin(phase)**2 * np.clip(2*frame_prop, 0, 1)
    r_foot = np.array([r_foot_x, -0.73 + foot_y_offset])
    l_foot = np.array([l_foot_x, -0.73 + foot_y_offset])
    return r_shoulder, l_shoulder, r_elbow, l_elbow, r_hand, l_hand, r_knee, l_knee, r_foot, l_foot

def get_frame_pose(x, y, phase, frame_prop):
    # Main vertical axis: y
    # Middle torso
    upper_torso = np.array([0, 0.14])
    mid_torso = np.array([0, -0.12])
    bottom_torso = np.array([0, -0.38])
    # Head & neck
    neck = np.array([0, 0.25])
    head = np.array([0, 0.38 + 0.01*np.sin(phase)])
    # Shoulders, arms, hands, legs, feet
    (r_shoulder, l_shoulder, r_elbow, l_elbow, 
     r_hand, l_hand, r_knee, l_knee, 
     r_foot, l_foot) = get_limb_offsets(phase, frame_prop)
    # Heavy weight object: located between hands
    weight_delta = l_hand - r_hand
    weight_pos = r_hand + 0.5 * weight_delta + np.array([0, -0.06])
    # Offset by current (x,y)
    all_points = np.stack([
        head, neck, r_shoulder, l_shoulder, upper_torso,
        r_elbow, l_elbow, mid_torso, r_hand, l_hand,
        r_knee, l_knee, r_foot, l_foot, weight_pos
    ])
    all_points[:, 0] += x
    all_points[:, 1] += y
    return all_points

# Animation parameters
FPS = 30
DUR = 2.0+1.5   # seconds (one big jump)
n_frames = int(FPS * DUR)

# Generate motion trajectory
traj_x, traj_y = jump_trajectory(n_frames)

# Build all frames' positions
frames = []
for i in range(n_frames):
    # Phase: 0 to 2pi
    frame_prop = i / n_frames
    phase = np.pi * (i / n_frames)    # Only one big jump
    p = get_frame_pose(traj_x[i], traj_y[i], phase, frame_prop)
    frames.append(p)

# Setup plot
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_facecolor('black')
plt.axis('off')

# Point marker visuals
point_kwargs = dict(marker="o", markersize=10, color="white", ls="")

# Initial scatter
scat = ax.plot([], [], **point_kwargs)[0]
ax.set_xlim(-1.0, 2.0)
ax.set_ylim(-0.5, 3.8)

def init():
    scat.set_data([], [])
    return (scat,)

def animate(i):
    pts = frames[i]
    scat.set_data(pts[:, 0], pts[:, 1])
    return (scat,)

ani = animation.FuncAnimation(fig, animate, frames=n_frames,
                              interval=1000*DUR/n_frames, blit=True, init_func=init)

plt.show()
