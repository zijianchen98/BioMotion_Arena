
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- Biological Kinematics Parameters ---
FPS = 60
DURATION = 6      # seconds
N_FRAMES = DURATION * FPS

# --- Human body: 15 point-lights (x, y) order ---
JOINT_NAMES = [
    'Head',
    'RShoulder', 'Neck', 'LShoulder',
    'RElbow', 'MidBack', 'LElbow',
    'RWrist', 'LHip', 'LWrist', 'RHip',
    'RKnee', 'LKnee',
    'RAnkle', 'LAnkle'
]

# 2D skeleton static pose, normalized (origin at pelvis center)
BASE = {
    'Head':      (0,   2.0),
    'Neck':      (0,   1.6),
    'RShoulder': (-0.27, 1.6),
    'LShoulder': (0.27,  1.6),
    'MidBack':   (0,   1.26),
    'RElbow':    (-0.44, 1.22),
    'LElbow':    (0.44,  1.22),
    'RWrist':    (-0.52, 0.8),
    'LWrist':    (0.52,  0.8),
    'RHip':      (-0.15, 0.98),
    'LHip':      (0.15,  0.98),
    'RKnee':     (-0.18, 0.48),
    'LKnee':     (0.18,  0.48),
    'RAnkle':    (-0.22, 0.0),
    'LAnkle':    (0.22,  0.00),
}

# Mapping rendering order (indices match above)
ORDER = [
    'Head',
    'RShoulder', 'Neck', 'LShoulder',
    'RElbow', 'MidBack', 'LElbow',
    'RWrist', 'LHip', 'LWrist', 'RHip',
    'RKnee', 'LKnee',
    'RAnkle', 'LAnkle',
]

# --- Running Motion Generators ---
def generate_running_pose(phase, sad_mod=1.0, heavy_mod=1.0):
    """
    Returns dict of joint positions at the given running phase [0, 1)
    phase: normalized gait phase
    sad_mod: [0-1] sadness: lower head/shoulders, less bounce, arms close to body
    heavy_mod: [0-1] heavy weight: less vertical oscillation, slower swing, arms low
    """
    # Amplitudes & Timings
    stride = 0.80                # stride length
    vertical_amp = 0.13 * (0.6*heavy_mod+0.4)
    vertical_amp *= 1-0.25*sad_mod
    head_drop = 0.25 * sad_mod   # head preset lower for sad
    arm_amp = 0.21 * (0.45*heavy_mod+0.55)
    arm_amp *= 1-0.40*sad_mod
    arm_swing = 96/180*np.pi     # maximum swing angle

    # Gait phase (two steps per cycle)
    global_phase = phase*2*np.pi
    # Right leg phase: 0 running step, 1 swing step, 2 full gait
    legR_phase = global_phase
    legL_phase = global_phase + np.pi

    # Symmetry: index 0=right, 1=left
    legs_y_base = BASE['RHip'][1]
    arms_y_base = BASE['RShoulder'][1]

    # Torso
    # Slight vertical oscillation for CoM (lower, less bounce for sad & heavy weight)
    rootY = 1.02 + vertical_amp * np.sin(global_phase) * 0.75
    rootY -= 0.12*heavy_mod + 0.10*sad_mod
    # Head slumped for sadness
    headY = BASE['Head'][1] + 0.21*vertical_amp*np.sin(global_phase)
    headY -= head_drop
    headY += rootY - 1.0
    # Shoulders slump forward for sadness
    shouldersY = arms_y_base + 0.09*vertical_amp*np.sin(global_phase)
    shouldersY -= 0.10*head_drop
    shouldersY += rootY - 1.0

    # Horizontal move of body (translation for running)
    translation = stride * phase

    # --- Joint positions (x, y) ---
    pts = {}
    # Head
    pts['Head'] = (0.0 + translation, headY)
    # Neck
    pts['Neck'] = (0.0 + translation, shouldersY - 0.23)
    # Shoulders
    pts['RShoulder'] = (-0.27 + translation, shouldersY)
    pts['LShoulder'] = (0.27 + translation, shouldersY)

    # Torso mid-back
    pts['MidBack'] = (0.0 + translation, shouldersY - 0.33)

    # Hips (pelvis)
    pts['RHip'] = (-0.15 + translation, rootY)
    pts['LHip'] = (0.15 + translation, rootY)

    # Legs (sinusoidal swing and vertical bounce)
    # Right leg
    hipR_x, hipR_y = pts['RHip']
    thetaR = np.pi/8 + 0.9 * np.sin(legR_phase)
    kneeR_x = hipR_x + 0.36 * np.sin(thetaR)
    kneeR_y = hipR_y - 0.50 * np.cos(thetaR)
    ankleR_x = kneeR_x + 0.22 * np.sin(thetaR+ np.pi/6)
    ankleR_y = kneeR_y - 0.46 * np.cos(thetaR+ np.pi/6)
    pts['RKnee'] = (kneeR_x, kneeR_y)
    pts['RAnkle'] = (ankleR_x, ankleR_y)

    # Left leg
    hipL_x, hipL_y = pts['LHip']
    thetaL = np.pi/8 + 0.9 * np.sin(legL_phase)
    kneeL_x = hipL_x + 0.36 * np.sin(thetaL)
    kneeL_y = hipL_y - 0.50 * np.cos(thetaL)
    ankleL_x = kneeL_x + 0.22 * np.sin(thetaL+ np.pi/6)
    ankleL_y = kneeL_y - 0.46 * np.cos(thetaL+ np.pi/6)
    pts['LKnee'] = (kneeL_x, kneeL_y)
    pts['LAnkle'] = (ankleL_x, ankleL_y)

    # Arms
    # Right arm (back-swing with gait)
    elbowR_angle = -arm_swing * np.sin(global_phase) * 0.8 * (1-heavy_mod*0.1)
    elbowR_y = shouldersY - 0.32 - 0.13*heavy_mod
    elbowR_x = pts['RShoulder'][0] + arm_amp*np.cos(elbowR_angle)
    elbowR_y += arm_amp*np.sin(elbowR_angle)
    wristR_angle = elbowR_angle - 0.75*arm_swing * (0.75+0.25*heavy_mod)
    wristR_x = elbowR_x + 0.23*np.cos(wristR_angle)
    wristR_y = elbowR_y + 0.12*np.sin(wristR_angle)

    pts['RElbow'] = (elbowR_x, elbowR_y)
    pts['RWrist'] = (wristR_x, wristR_y)

    # Left arm (opposite phase)
    elbowL_angle = arm_swing * np.sin(global_phase) * 0.8 * (1-heavy_mod*0.1)
    elbowL_y = shouldersY - 0.32 - 0.13*heavy_mod
    elbowL_x = pts['LShoulder'][0] + arm_amp*np.cos(elbowL_angle)
    elbowL_y += arm_amp*np.sin(elbowL_angle)
    wristL_angle = elbowL_angle + 0.75*arm_swing * (0.75+0.25*heavy_mod)
    wristL_x = elbowL_x + 0.23*np.cos(wristL_angle)
    wristL_y = elbowL_y + 0.12*np.sin(wristL_angle)

    pts['LElbow'] = (elbowL_x, elbowL_y)
    pts['LWrist'] = (wristL_x, wristL_y)

    return [pts[k] for k in ORDER]

# -- Sad woman, heavy weight: sadness and heaviness modulation --
SADNESS = 1.0    # max = 1, min = 0
HEAVY = 1.0      # max = 1, min = 0

# --- Animation Setup ---
fig, ax = plt.subplots(figsize=(4, 8))   # Tall portrait
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.axis('off')
scatter = ax.scatter([], [], s=80, color='white', edgecolors='none')

# Set X and Y lim for central framing
ax.set_xlim(-1, 2)
ax.set_ylim(-0.3, 2.4)

# --- Animation function ---
def animate(frame):
    phase = (frame / N_FRAMES) % 1.0
    pts = generate_running_pose(phase, sad_mod=SADNESS, heavy_mod=HEAVY)
    xs = [x for (x, y) in pts]
    ys = [y for (x, y) in pts]
    scatter.set_offsets(np.c_[xs, ys])
    return scatter,

# --- Run animation ---
ani = FuncAnimation(fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True)
plt.show()
