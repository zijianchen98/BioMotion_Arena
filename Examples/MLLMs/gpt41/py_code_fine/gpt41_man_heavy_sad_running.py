
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 joint names and their mapping (based on biological marker sets):
JOINT_LABELS = [
    'head',         # 0
    'neck',         # 1
    'right_shoulder',   # 2
    'left_shoulder',    # 3
    'right_elbow',      # 4
    'left_elbow',       # 5
    'right_hand',       # 6
    'left_hand',        # 7
    'torso',            # 8
    'right_hip',        # 9
    'left_hip',         #10
    'right_knee',       #11
    'left_knee',        #12
    'right_foot',       #13
    'left_foot',        #14
]

# Body segments (for reference: not used in plotting)
LIMB_CONNECTIONS = [
    (0,1),  # head-neck
    (1,2), (2,4), (4,6),   # right side: shoulder-elbow-hand
    (1,3), (3,5), (5,7),   # left side: shoulder-elbow-hand
    (1,8),     # neck-torso
    (8,9), (9,11), (11,13), # right leg: torso-hip-knee-foot
    (8,10), (10,12), (12,14), # left leg: torso-hip-knee-foot
]

# Relative (average) coordinates for standing posture, scale and position normalized.
# Format: [x, y], where y is upwards
BODY_BASE = np.array([
    [0.,1.55],  # head
    [0.,1.4],   # neck
    [0.15,1.35], # right_shoulder
    [-0.15,1.35], # left_shoulder
    [0.23,1.15],  # right_elbow
    [-0.23,1.15], # left_elbow
    [0.32,0.95],  # right_hand
    [-0.32,0.95], # left_hand
    [0.,1.0],     # torso (base of spine)
    [0.09,0.87],  # right_hip
    [-0.09,0.87], # left_hip
    [0.18,0.5],   # right_knee
    [-0.18,0.5],  # left_knee
    [0.18,0.05],  # right_foot
    [-0.18,0.05], # left_foot
])

# Parameters for running motion, for each joint: amplitude and phase of motion
# Units: meter and radians; Tweak amplitudes for heavy/sad/run look.
RUN_PARAMS = {
    # Each joint: (amp_x, amp_y, phase_x, phase_y)
    'head'  : (0.025, 0.025, 0, np.pi),     # little vertical, heavier downward
    'neck'  : (0.032, 0.04, 0, np.pi),      # more vertical oscillation
    'right_shoulder': (0.045,  0.05, -np.pi/10, np.pi),
    'left_shoulder' : (0.045,  0.05, +np.pi/10, np.pi),
    'right_elbow'   : (0.11,   0.09, -np.pi/2, 0),
    'left_elbow'    : (0.11,   0.09, +np.pi/2, 0),
    'right_hand'    : (0.16,   0.11, -np.pi/2, -np.pi/3),
    'left_hand'     : (0.16,   0.11, +np.pi/2, -np.pi/3),
    'torso'         : (0.020,  0.048, 0, np.pi),    # heavy bobbing
    'right_hip'     : (0.045,  0.05, -np.pi/13, np.pi),
    'left_hip'      : (0.045,  0.05, np.pi/13, np.pi),
    'right_knee'    : (0.12,   0.18, -np.pi/2, -np.pi/12), # bigknee
    'left_knee'     : (0.12,   0.18, +np.pi/2, -np.pi/12),
    'right_foot'    : (0.19,   0.16, -np.pi/2, 0),   # feet up
    'left_foot'     : (0.19,   0.16, +np.pi/2, 0),
}

JOINT_PARAMS = [RUN_PARAMS[label] for label in JOINT_LABELS]

# Main animation function
def running_motion_frame(t, base_xy, params, stride_len=0.25, run_speed=1.9):
    period = 0.62  # seconds per running cycle (cadence for 'heavy' blunted style)
    omega = 2*np.pi / period
    # For 'sadman with weight', vertical motion and arm/leg swing exaggerated, with a downwards bias
    # Add offset so figure moves forward along X
    stride = stride_len * (t / period)
    offset_x = stride % 2.4   # keep within screen
    
    pts = []
    for idx, (base, (ax, ay, phx, phy)) in enumerate(zip(base_xy, params)):
        phase = omega*t
        # Use sine for arms/legs, and heavy downward bias for overall figure (sad/heavy)
        if idx == 0:  # head has a 'droop' bias
            y_down_extra = -0.05*np.abs(np.sin(phase))
        else:
            y_down_extra = 0

        # Alternating left/right
        is_left = (idx in [3,5,7,10,12,14])
        side_sign = 1 if is_left else -1
        # phase offset for right/left in gait
        px = phase + side_sign * phx
        py = phase + side_sign * phy

        # Heavy/sad: less vertical bounce for arms, more for legs+torso.
        dx = ax * np.sin(px)
        dy = ay * np.sin(py)

        p = np.copy(base)
        if idx == 8:  # torso
            # Add stronger vertical drop for torso during down-phase
            dy -= 0.05 * (1 + np.sin(phase+np.pi/12))

        if idx in [2,3,9,10]:  # hips/shoulders
            # Add a little lateral shift to hips/shoulders to mimic whole-body sway
            dx += 0.04*np.sin(phase + (side_sign*np.pi/3))

        p[0] += dx + offset_x
        p[1] += dy + y_down_extra

        pts.append(p)
    return np.array(pts)

# Set up Matplotlib animated plot
fig, ax = plt.subplots(figsize=(4,7))
ax.set_facecolor('k')
plt.axis('off')

# Animation limits
xlim = (0, 2.2)
ylim = (0, 1.8)

ax.set_xlim(xlim)
ax.set_ylim(ylim)

# White dots
dot_plots = ax.plot(
    [], [], 'wo', ms=8
)[0]

# (optional) Show limb lines for reference/debug
# lines = []
# for i0, i1 in LIMB_CONNECTIONS:
#     l, = ax.plot([], [], 'w-', lw=1.6, alpha=0.25)
#     lines.append(l)

def init():
    dot_plots.set_data([], [])
    # for l in lines:
    #     l.set_data([], [])
    return (dot_plots, ) #+ tuple(lines)

def animate(frame):
    t = frame / 50.0  # 50 fps timebase
    pts = running_motion_frame(
        t, BODY_BASE, JOINT_PARAMS, stride_len=0.22, run_speed=1.7
    )
    dot_plots.set_data(pts[:,0], pts[:,1])

    # For showing limb skeleton (optional, for debugging):
    # for (i, (j0,j1)) in enumerate(LIMB_CONNECTIONS):
    #     lines[i].set_data([pts[j0,0],pts[j1,0]], [pts[j0,1],pts[j1,1]])

    return (dot_plots,) # + tuple(lines)

ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=20, blit=True
)

plt.show()
