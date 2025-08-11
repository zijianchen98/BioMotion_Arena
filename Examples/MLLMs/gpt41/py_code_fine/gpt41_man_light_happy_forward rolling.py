
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 keypoints for the 'happyman' stick figure: (in head to foot order)
# head, neck, R shoulder, L shoulder, R elbow, L elbow, R wrist, L wrist,
# pelvis, R hip, L hip, R knee, L knee, R ankle, L ankle

POINT_ORDER = [
    'Head',      # 0
    'Neck',      # 1
    'RShoulder', # 2
    'LShoulder', # 3
    'RElbow',    # 4
    'LElbow',    # 5
    'RWrist',    # 6
    'LWrist',    # 7
    'Pelvis',    # 8
    'RHip',      # 9
    'LHip',      #10
    'RKnee',     #11
    'LKnee',     #12
    'RAnkle',    #13
    'LAnkle'     #14
]

# Body segment connections (not plotted, but useful for structure)
SEGMENTS = [
    (0,1),    # Head-Neck
    (1,2),    # Neck-RShoulder
    (1,3),    # Neck-LShoulder
    (2,4),    # RShoulder-RElbow
    (3,5),    # LShoulder-LElbow
    (4,6),    # RElbow-RWrist
    (5,7),    # LElbow-LWrist
    (1,8),    # Neck-Pelvis
    (8,9),    # Pelvis-RHip
    (8,10),   # Pelvis-LHip
    (9,11),   # RHip-RKnee
    (11,13),  # RKnee-RAnkle
    (10,12),  # LHip-LKnee
    (12,14)   # LKnee-LAnkle
]

# Key segment lengths (rough proportions, arbitrary units)
LEN = {
    'Head-Neck':      0.11,
    'Neck-Pelvis':    0.32,
    'RShoulder-Neck': 0.14,
    'LShoulder-Neck': 0.14,
    'UpperArm':       0.16, # Shoulder->Elbow
    'Forearm':        0.13, # Elbow->Wrist
    'Pelvis-Hip':     0.09, 
    'Hip-Knee':       0.22,
    'Knee-Ankle':     0.22
}

# Animation parameters
N_FRAMES = 90    # duration of rolling
FPS = 30
BODY_HEIGHT = 1.0  # overall "height" in unitless screen coordinates

def get_pose_params(t, total_time):
    """
    Returns angles for the rolling pose at normalized time 0-1.
    Returns a dict of segment angles (radians), all relative to "horizontal"
    for the roll cycle.
    """
    # The body behaves like a rolling stick-man, rotating and curling
    # As subject rolls forwards (e.g. do a somersault), body rotates+limbs move cyclically.
    # t is between 0 (start) and 1 (end)
    roll_angle = 2 * np.pi * t  # roll one full circle in cycle
    # phase offsets for limbs to achieve the rolling motion
    # 'curl' is more at upside-down, extended at upright
    curl = 0.45 + 0.35 * np.cos(roll_angle)
    
    params = dict()
    params['trunk_angle'] = roll_angle               # body axis rotation (horizontal = 0)
    params['head_angle'] = 0.0                       # head vertical vs neck (constant)
    params['neck_angle'] = -0.09 * np.cos(roll_angle)
    params['shoulder_angle'] = np.pi/2 + 0.38*np.sin(roll_angle) * (1-curl)
    
    # Arm phase: alternating curling - symmetric but out of phase for each pair
    # Elbows and wrists cycle as a function of roll phase
    params['r_shoulder_abd'] = 0.61 * np.sin(roll_angle + np.pi) * curl
    params['l_shoulder_abd'] = 0.61 * np.sin(roll_angle) * curl
    params['r_elbow_flex'] = 0.9 - 1.2 * (np.cos(roll_angle + np.pi) + 1)/2 * curl # flexion
    params['l_elbow_flex'] = 0.9 - 1.2 * (np.cos(roll_angle) + 1)/2 * curl
  
    # Hip joint
    params['r_hip_flex'] = 0.28 * np.sin(roll_angle + np.pi) * curl
    params['l_hip_flex'] = 0.28 * np.sin(roll_angle) * curl
    # Knee joint
    params['r_knee_flex'] = 0.96 - 1.1 * (np.cos(roll_angle + np.pi) + 1)/2 * curl
    params['l_knee_flex'] = 0.96 - 1.1 * (np.cos(roll_angle) + 1)/2 * curl

    params['curl'] = curl  # for debug/adjustments

    # Forward translation (rolling forward)
    stride_len = 1.16 # screen units total
    params['x_offset'] = stride_len * t
    params['y_offset'] = 0.0

    return params

def get_body_points(params, base_xy):
    """
    Given pose params and initial base (pelvis) x,y position,
    compute the XY coordinates of each of 15 joints.
    Returns an (15,2) array of (x,y).
    """
    x0, y0 = base_xy
    ang_trunk = params['trunk_angle']
    # Pelvis
    pelvis = np.array([x0, y0])

    # Neck: up trunk
    neck = pelvis + [
        LEN['Neck-Pelvis'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi/2),
        LEN['Neck-Pelvis'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi/2)
    ]

    # Head: up from neck
    head = neck + [
        LEN['Head-Neck'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi/2 + params['neck_angle']),
        LEN['Head-Neck'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi/2 + params['neck_angle'])
    ]

    # Shoulders
    r_shoulder = neck + [
        LEN['RShoulder-Neck'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi),
        LEN['RShoulder-Neck'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi)
    ]
    l_shoulder = neck + [
        LEN['LShoulder-Neck'] * BODY_HEIGHT * np.cos(ang_trunk),
        LEN['LShoulder-Neck'] * BODY_HEIGHT * np.sin(ang_trunk)
    ]

    # Arms: right (from shoulder to wrist)
    r_elbow = r_shoulder + [
        LEN['UpperArm'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi + params['r_shoulder_abd']),
        LEN['UpperArm'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi + params['r_shoulder_abd'])
    ]
    r_wrist = r_elbow + [
        LEN['Forearm'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi + params['r_shoulder_abd'] + params['r_elbow_flex']),
        LEN['Forearm'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi + params['r_shoulder_abd'] + params['r_elbow_flex'])
    ]
    # left
    l_elbow = l_shoulder + [
        LEN['UpperArm'] * BODY_HEIGHT * np.cos(ang_trunk + params['l_shoulder_abd']),
        LEN['UpperArm'] * BODY_HEIGHT * np.sin(ang_trunk + params['l_shoulder_abd'])
    ]
    l_wrist = l_elbow + [
        LEN['Forearm'] * BODY_HEIGHT * np.cos(ang_trunk + params['l_shoulder_abd'] + params['l_elbow_flex']),
        LEN['Forearm'] * BODY_HEIGHT * np.sin(ang_trunk + params['l_shoulder_abd'] + params['l_elbow_flex'])
    ]

    # Hips
    r_hip = pelvis + [
        LEN['Pelvis-Hip'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*5/4),
        LEN['Pelvis-Hip'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*5/4)
    ]
    l_hip = pelvis + [
        LEN['Pelvis-Hip'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*3/4),
        LEN['Pelvis-Hip'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*3/4)
    ]

    # Legs
    r_knee = r_hip + [
        LEN['Hip-Knee'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*5/4 + params['r_hip_flex']),
        LEN['Hip-Knee'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*5/4 + params['r_hip_flex'])
    ]
    r_ankle = r_knee + [
        LEN['Knee-Ankle'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*5/4 + params['r_hip_flex'] + params['r_knee_flex']),
        LEN['Knee-Ankle'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*5/4 + params['r_hip_flex'] + params['r_knee_flex'])
    ]
    l_knee = l_hip + [
        LEN['Hip-Knee'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*3/4 + params['l_hip_flex']),
        LEN['Hip-Knee'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*3/4 + params['l_hip_flex'])
    ]
    l_ankle = l_knee + [
        LEN['Knee-Ankle'] * BODY_HEIGHT * np.cos(ang_trunk + np.pi*3/4 + params['l_hip_flex'] + params['l_knee_flex']),
        LEN['Knee-Ankle'] * BODY_HEIGHT * np.sin(ang_trunk + np.pi*3/4 + params['l_hip_flex'] + params['l_knee_flex'])
    ]

    # Compose into 15-point array
    pts = np.stack([
        head, neck,
        r_shoulder, l_shoulder,
        r_elbow, l_elbow,
        r_wrist, l_wrist,
        pelvis, r_hip, l_hip,
        r_knee, l_knee,
        r_ankle, l_ankle
    ], axis=0)
    # Move all points by translation
    pts[:,0] += params['x_offset']
    pts[:,1] += params['y_offset']
    return pts

# Set up the figure
fig, ax = plt.subplots(figsize=(4, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-0.5, 2.0)
ax.set_ylim(-0.12, 1.12)

# Prepare line artist for 15 points
scatter = ax.scatter([], [], c='white', s=30, edgecolor='none')

def init():
    scatter.set_offsets(np.zeros((15,2)))
    return (scatter,)

def animate(frame):
    t = frame / N_FRAMES
    params = get_pose_params(t, 1.0)
    base_xy = (0.25, 0.24)
    pts = get_body_points(params, base_xy)
    scatter.set_offsets(pts)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True, init_func=init
)

plt.show()
