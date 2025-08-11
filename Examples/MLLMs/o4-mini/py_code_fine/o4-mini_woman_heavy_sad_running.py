
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters for the biomechanical model
SEG_LENGTH = {
    'head_neck': 0.15,
    'neck_shoulder': 0.20,
    'shoulder_elbow': 0.30,
    'elbow_wrist': 0.25,
    'trunk': 0.45,
    'pelvis_hip': 0.10,
    'hip_knee': 0.40,
    'knee_ankle': 0.40
}

HIP_WIDTH = 0.20      # distance between left/right hips
SHOULDER_WIDTH = 0.40 # distance between left/right shoulders

RUN_FREQ = 2.0        # cycles per second (running)
ARM_AMP = np.deg2rad(25)   # shoulder swing amplitude
LEG_AMP = np.deg2rad(35)   # hip swing amplitude
KNEE_OFFSET = np.deg2rad(15)
KNEE_AMP = np.deg2rad(60)
ELBOW_BEND = np.deg2rad(20)
HEAD_DROOP = np.deg2rad(15)

# Visualization scaling
SCALE = 200.0  # to convert meters -> screen units
FPS = 30.0

def compute_joint_positions(t):
    """
    Compute 2D positions of 15 point-lights at time t.
    Returns an array of shape (15,2) with (x,y) for each joint.
    Joint order:
      0: head
      1: neck
      2: left shoulder
      3: right shoulder
      4: left elbow
      5: right elbow
      6: left wrist
      7: right wrist
      8: pelvis
      9: left hip
     10: right hip
     11: left knee
     12: right knee
     13: left ankle
     14: right ankle
    """
    # Phase angle for running cycle
    phase = 2 * np.pi * RUN_FREQ * t

    # Pelvis fixed in space (will animate in place)
    px, py = 0.0, 0.0

    # Trunk: from pelvis to neck (vertical)
    neck_x = px
    neck_y = py + SEG_LENGTH['trunk']

    # Head: from neck, slightly drooped forward
    head_dx = SEG_LENGTH['head_neck'] * np.sin(HEAD_DROOP)
    head_dy = SEG_LENGTH['head_neck'] * np.cos(HEAD_DROOP)
    head = np.array([neck_x + head_dx, neck_y + head_dy])

    # Shoulders
    left_shoulder  = np.array([neck_x - SHOULDER_WIDTH/2, neck_y])
    right_shoulder = np.array([neck_x + SHOULDER_WIDTH/2, neck_y])

    # Arm swings opposite phase to legs
    shoulder_angle_L =  ARM_AMP * np.sin(phase + np.pi)
    shoulder_angle_R = -ARM_AMP * np.sin(phase + np.pi)

    # Elbows bent by fixed amount inward
    elbow_angle_L = shoulder_angle_L - ELBOW_BEND
    elbow_angle_R = shoulder_angle_R + ELBOW_BEND

    # Left arm joints
    L_elbow = left_shoulder + SEG_LENGTH['shoulder_elbow'] * np.array([
        np.sin(shoulder_angle_L), -np.cos(shoulder_angle_L)
    ])
    L_wrist = L_elbow + SEG_LENGTH['elbow_wrist'] * np.array([
        np.sin(elbow_angle_L), -np.cos(elbow_angle_L)
    ])

    # Right arm joints
    R_elbow = right_shoulder + SEG_LENGTH['shoulder_elbow'] * np.array([
        np.sin(shoulder_angle_R), -np.cos(shoulder_angle_R)
    ])
    R_wrist = R_elbow + SEG_LENGTH['elbow_wrist'] * np.array([
        np.sin(elbow_angle_R), -np.cos(elbow_angle_R)
    ])

    # Pelvis & hips
    pelvis = np.array([px, py])
    left_hip  = pelvis + np.array([-HIP_WIDTH/2, 0.0])
    right_hip = pelvis + np.array([ HIP_WIDTH/2, 0.0])

    # Leg swings
    hip_angle_L =  LEG_AMP * np.sin(phase)
    hip_angle_R = -LEG_AMP * np.sin(phase)

    # Knee flexion more during swing phase
    knee_angle_L = KNEE_OFFSET + KNEE_AMP * max(0.0, -np.sin(phase))
    knee_angle_R = KNEE_OFFSET + KNEE_AMP * max(0.0,  np.sin(phase))

    # Left leg joints
    L_knee = left_hip + SEG_LENGTH['hip_knee'] * np.array([
        np.sin(hip_angle_L), -np.cos(hip_angle_L)
    ])
    L_ankle = L_knee + SEG_LENGTH['knee_ankle'] * np.array([
        np.sin(hip_angle_L + knee_angle_L),
        -np.cos(hip_angle_L + knee_angle_L)
    ])

    # Right leg joints
    R_knee = right_hip + SEG_LENGTH['hip_knee'] * np.array([
        np.sin(hip_angle_R), -np.cos(hip_angle_R)
    ])
    R_ankle = R_knee + SEG_LENGTH['knee_ankle'] * np.array([
        np.sin(hip_angle_R + knee_angle_R),
        -np.cos(hip_angle_R + knee_angle_R)
    ])

    # Pack all joints into one array
    joints = np.vstack([
        head,
        np.array([neck_x, neck_y]),
        left_shoulder,
        right_shoulder,
        L_elbow,
        R_elbow,
        L_wrist,
        R_wrist,
        pelvis,
        left_hip,
        right_hip,
        L_knee,
        R_knee,
        L_ankle,
        R_ankle
    ])

    return joints

# Set up the plotting
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, c='white')
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)
ax.axis('off')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    t = frame / FPS
    joints = compute_joint_positions(t)
    # Scale to screen coords
    pts = joints * SCALE
    scat.set_offsets(pts)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=int(FPS*10),
                    init_func=init, blit=True, interval=1000/FPS, repeat=True)

plt.show()
