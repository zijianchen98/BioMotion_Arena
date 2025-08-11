
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define 15 points: ['Head', 'Neck', 'Right Shoulder', 'Left Shoulder',
# 'Right Elbow', 'Left Elbow', 'Right Wrist', 'Left Wrist',
# 'Right Hip', 'Left Hip', 'Right Knee', 'Left Knee',
# 'Right Ankle', 'Left Ankle', 'Pelvis']

POINT_NAMES = [
    'Head', 'Neck', 'Right Shoulder', 'Left Shoulder',
    'Right Elbow', 'Left Elbow', 'Right Wrist', 'Left Wrist',
    'Right Hip', 'Left Hip', 'Right Knee', 'Left Knee',
    'Right Ankle', 'Left Ankle', 'Pelvis'
]

# Skeleton segment definitions (for calculation, not for drawing lines)
UPPER_BODY = {
    'Head': ('Neck', 0.14, 90),  # origin at Neck, up
    'Neck': ('Pelvis', 0.28, 90),
    'Right Shoulder':  ('Neck', 0.12, -30),
    'Left Shoulder':   ('Neck', 0.12,  30),
    'Right Elbow':     ('Right Shoulder', 0.15, -60),
    'Left Elbow':      ('Left Shoulder',  0.15,  60),
    'Right Wrist':     ('Right Elbow',    0.13, -80),
    'Left Wrist':      ('Left Elbow',     0.13,  80),
    'Pelvis':          ('Origin', 0, 0), # root joint at (0,0)
    'Right Hip':       ('Pelvis', 0.10, -15),
    'Left Hip':        ('Pelvis', 0.10,  15),
    'Right Knee':      ('Right Hip', 0.22, 0),
    'Left Knee':       ('Left Hip',  0.22, 0),
    'Right Ankle':     ('Right Knee', 0.22, 0),
    'Left Ankle':      ('Left Knee',  0.22, 0)
}

# Walking gait params
STEP_PERIOD = 1.0       # seconds per full gait cycle
FPS = 60                # frames per second
N_FRAMES = int(STEP_PERIOD * FPS)
N_CYCLES = 3            # how many cycles to show

def deg2rad(deg):
    return deg * np.pi / 180

def shoulder_swing(phase):
    # Arms anti-phase with legs, about ±35 degrees at shoulder
    return 35 * np.sin(2 * np.pi * phase + np.pi)

def hip_swing(phase):
    # Hips oscillate ±20 deg
    return 20 * np.sin(2 * np.pi * phase)

def elbow_swing(phase):
    # Elbow slightly flexes -> 20±25 deg
    return 25 * np.sin(2 * np.pi * phase + np.pi) + 20

def knee_swing(phase):
    # Knees flex: max extension at stance, max flexion at swing
    k = 40 * np.maximum(0, np.sin(2 * np.pi * phase))
    return k

def ankle_swing(phase):
    # Dorsiflexion/plantar: ±15 deg
    return 15 * np.sin(2 * np.pi * phase)

def pelvis_y(phase):
    # Pelvis rises and falls with step: ±.03 m
    return 0.03 * np.sin(4 * np.pi * phase)

def make_frame_params(t):
    # t: time in seconds
    phase_R = (t / STEP_PERIOD) % 1          # right leg phase
    phase_L = (phase_R + 0.5) % 1            # left leg ~opposite phase

    params = {
        'Right Shoulder': shoulder_swing(phase_R),
        'Left Shoulder':  shoulder_swing(phase_L),
        'Right Elbow': elbow_swing(phase_R),
        'Left Elbow': elbow_swing(phase_L),
        'Right Hip': hip_swing(phase_R),
        'Left Hip': hip_swing(phase_L),
        'Right Knee': knee_swing(phase_R),
        'Left Knee': knee_swing(phase_L),
        'Right Ankle': ankle_swing(phase_R),
        'Left Ankle': ankle_swing(phase_L),
        'Pelvis_y': pelvis_y(phase_R)
    }
    return params

def get_joint_coords(params, base_x=0, base_y=0):
    # Calculate global coordinates for all 15 points
    coords = {}
    # First, pelvis
    pelvis = np.array([base_x, base_y + params['Pelvis_y']])
    coords['Pelvis'] = pelvis

    # Torso
    # Neck
    neck = pelvis + np.array([0, UPPER_BODY['Neck'][1]])
    coords['Neck'] = neck
    # Head
    head = neck + np.array([0, UPPER_BODY['Head'][1]])
    coords['Head'] = head

    # Shoulders
    for side in ['Right', 'Left']:
        offset = UPPER_BODY[f'{side} Shoulder'][1]
        angle = deg2rad(UPPER_BODY[f'{side} Shoulder'][2])
        sval = -1 if side == 'Right' else 1
        shoulder = neck + offset * np.array([np.sin(angle) * sval, -np.cos(angle)])
        coords[f'{side} Shoulder'] = shoulder

        # Elbow
        sh_angle = deg2rad(params[f'{side} Shoulder'])
        upperarm = UPPER_BODY[f'{side} Elbow'][1]
        elbow = shoulder + upperarm * np.array([np.sin(sh_angle) * sval, -np.cos(sh_angle)])
        coords[f'{side} Elbow'] = elbow

        # Wrist
        el_angle = deg2rad(params[f'{side} Elbow'])
        el_abs_angle = sh_angle + el_angle * 0.6 * sval
        forearm = UPPER_BODY[f'{side} Wrist'][1]
        wrist = elbow + forearm * np.array([np.sin(el_abs_angle) * sval, -np.cos(el_abs_angle)])
        coords[f'{side} Wrist'] = wrist

    # Hips & legs
    for side in ['Right', 'Left']:
        hip_offset = UPPER_BODY[f'{side} Hip'][1]
        hip_angle = deg2rad(UPPER_BODY[f'{side} Hip'][2])
        sval = -1 if side == 'Right' else 1
        hip_theta = deg2rad(params[f'{side} Hip'])
        hip = pelvis + hip_offset * np.array([np.sin(hip_angle) * sval, -np.cos(hip_angle)])
        coords[f'{side} Hip'] = hip

        # Knee relative to hip
        thigh_len = UPPER_BODY[f'{side} Knee'][1]
        knee_angle = hip_theta
        knee = hip + thigh_len * np.array([np.sin(knee_angle) * sval, -np.cos(knee_angle)])
        # Add knee flexion
        k_swing = deg2rad(params[f'{side} Knee'])
        knee += thigh_len * 0.04 * np.array([np.sin(k_swing) * sval, -np.cos(k_swing)])

        coords[f'{side} Knee'] = knee

        # Ankle: knee to ankle
        shank_len = UPPER_BODY[f'{side} Ankle'][1]
        ankle_angle = knee_angle + deg2rad(params[f'{side} Knee']) / 3
        ankle = knee + shank_len * np.array([np.sin(ankle_angle) * sval, -np.cos(ankle_angle)])
        # Ankle flex
        a_swing = deg2rad(params[f'{side} Ankle'])
        ankle += shank_len * 0.04 * np.array([np.sin(a_swing) * sval, -np.cos(a_swing)])
        coords[f'{side} Ankle'] = ankle

    return coords

def points_for_time(t, x_walk=0.5):
    # Returns np.array of (x, y) for all 15 points, with X translation
    params = make_frame_params(t)
    walk_speed = 2.0 # m/s, real walk speed, converted to image coordinates later
    walk_progress = walk_speed * t * x_walk
    coords = get_joint_coords(params, base_x=walk_progress)
    arr = np.array([coords[name] for name in POINT_NAMES])
    return arr

# Animation setup
fig, ax = plt.subplots(figsize=(4, 7))
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-0.4, 1.2)
ax.set_ylim(-0.1, 1.7)

dots, = ax.plot([], [], 'wo', markersize=8)

def init():
    dots.set_data([], [])
    return (dots,)

def animate(frame):
    t = (frame / FPS) % STEP_PERIOD
    # Move the entire walker horizontally for the "walking" effect
    total_walker_shift = (frame / (N_FRAMES * N_CYCLES)) * 0.75
    points = points_for_time(t, x_walk=total_walker_shift)
    x, y = points[:, 0], points[:, 1]
    # Fix to center on screen
    x = x - np.mean(x) + 0.5
    y = y - np.min(y)
    dots.set_data(x, y)
    return (dots,)

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES*N_CYCLES,
    interval=1000/FPS, blit=True, init_func=init
)

plt.show()
