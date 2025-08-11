import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up parameters for the running motion
fps = 30          # frames per second
duration = 1.0    # duration (seconds) of one running cycle (one full set of leg swings)
frames = int(fps * duration)

# Lengths for body segments
torso_length = 0.3
neck_to_head = 0.07
shoulder_offset = 0.12
hip_offset = 0.09
upper_arm_len = 0.18
lower_arm_len = 0.18
upper_leg_len = 0.26
lower_leg_len = 0.26

# Base angles (in degrees) and amplitudes for arms/legs
torso_tilt_deg = 5.0
arm_base_deg = -20.0
leg_base_deg = -10.0
arm_amp_deg = 30.0
leg_amp_deg = 35.0

# A small bounce effect
bounce_amp = 0.02

# Convert degrees to radians
deg2rad = np.pi / 180.0
torso_tilt = torso_tilt_deg * deg2rad

def rotate(x, y, theta):
    """Rotate (x, y) by theta around origin."""
    xr = x * np.cos(theta) - y * np.sin(theta)
    yr = x * np.sin(theta) + y * np.cos(theta)
    return xr, yr

def get_joints(t):
    """
    Compute (x, y) coordinates of 15 joint center points for a running man
    at time t (from 0 to 1, inclusive) in one cycle.
    Order of returned points:
    1) head
    2) neck
    3) right_shoulder
    4) right_elbow
    5) right_wrist
    6) left_shoulder
    7) left_elbow
    8) left_wrist
    9) center_hip (pelvis)
    10) right_hip
    11) right_knee
    12) right_ankle
    13) left_hip
    14) left_knee
    15) left_ankle
    """

    # Frequency for the leg and arm swings (two steps per cycle for "running")
    freq = 2.0
   
    # Angular motion for right/left arms/legs:
    # Right arm (RA), left arm (LA), right leg (RL), left leg (LL)
    # The arms are out of phase with each other by pi, likewise for legs.
    # We'll add some offset angles for a more natural posture.
    RA = (arm_base_deg + arm_amp_deg * np.sin(2.0 * np.pi * freq * t)) * deg2rad
    LA = (-arm_base_deg + arm_amp_deg * np.sin(2.0 * np.pi * freq * t + np.pi)) * deg2rad
    RL = (leg_base_deg + leg_amp_deg * np.sin(2.0 * np.pi * freq * t + np.pi)) * deg2rad
    LL = (leg_base_deg + leg_amp_deg * np.sin(2.0 * np.pi * freq * t)) * deg2rad

    # Elbow and knee bending: approximate them as half of shoulder/hip angle variation
    # so that arms and legs bend more when they're behind the body.
    RE = 0.5 * RA
    LE = 0.5 * LA
    RK = 0.5 * RL
    LK = 0.5 * LL

    # Vertical bounce
    pelvis_y = bounce_amp * np.cos(2.0 * np.pi * freq * t)

    # Pelvis (center_hip)
    pelvis = np.array([0.0, pelvis_y])

    # Torso top (near neck) by rotating (0, torso_length) around pelvis
    dx_torso, dy_torso = rotate(0.0, torso_length, torso_tilt)
    neck = pelvis + np.array([dx_torso, dy_torso])

    # Head from neck
    head = neck + np.array([0, neck_to_head])

    # Shoulders from neck (right and left)
    # We'll ignore torso tilt for left-right offset and just apply horizontal shift
    right_shoulder = neck + np.array([+shoulder_offset, 0])
    left_shoulder  = neck + np.array([-shoulder_offset, 0])

    # Hips from pelvis (right and left)
    # Similarly ignoring small tilt for basic horizontal offset
    right_hip = pelvis + np.array([+hip_offset, 0])
    left_hip  = pelvis + np.array([-hip_offset, 0])

    # Right arm chain: shoulder -> elbow -> wrist
    # Shoulder->Elbow rotates RA around shoulder downward
    re_dx, re_dy = rotate(0, -upper_arm_len, RA)
    right_elbow = right_shoulder + np.array([re_dx, re_dy])
    # Elbow->Wrist rotates RE around the elbow downward
    rw_dx, rw_dy = rotate(0, -lower_arm_len, RE)
    right_wrist = right_elbow + np.array([rw_dx, rw_dy])

    # Left arm chain
    le_dx, le_dy = rotate(0, -upper_arm_len, LA)
    left_elbow = left_shoulder + np.array([le_dx, le_dy])
    lw_dx, lw_dy = rotate(0, -lower_arm_len, LE)
    left_wrist = left_elbow + np.array([lw_dx, lw_dy])

    # Right leg chain: hip -> knee -> ankle
    rk_dx, rk_dy = rotate(0, -upper_leg_len, RL)
    right_knee = right_hip + np.array([rk_dx, rk_dy])
    ra_dx, ra_dy = rotate(0, -lower_leg_len, RK)
    right_ankle = right_knee + np.array([ra_dx, ra_dy])

    # Left leg chain
    lk_dx, lk_dy = rotate(0, -upper_leg_len, LL)
    left_knee = left_hip + np.array([lk_dx, lk_dy])
    la_dx, la_dy = rotate(0, -lower_leg_len, LK)
    left_ankle = left_knee + np.array([la_dx, la_dy])

    # Combine all 15 points
    points = np.vstack([
        head,
        neck,
        right_shoulder,
        right_elbow,
        right_wrist,
        left_shoulder,
        left_elbow,
        left_wrist,
        pelvis,
        right_hip,
        right_knee,
        right_ankle,
        left_hip,
        left_knee,
        left_ankle
    ])
    return points

# Set up the figure and plot
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111, facecolor='black')
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.4, 0.8)
ax.set_aspect('equal')
ax.axis('off')

scatter = ax.scatter([], [], c='white', s=30)

def init():
    scatter.set_offsets([])
    return (scatter,)

def update(frame):
    # Convert frame to time t in [0, 1) for one running cycle
    t = (frame % frames) / float(frames)
    pts = get_joints(t)
    scatter.set_offsets(pts)
    return (scatter,)

ani = animation.FuncAnimation(
    fig, update, frames=frames, init_func=init, interval=1000/fps, blit=True, repeat=True
)

plt.show()