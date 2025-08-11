
"""
Point-light stimulus – 15 white dots against a black background
depicting a happy, heavy man waving his right hand.

The script creates a smooth, biomechanically-plausible animation
(approx. 6 s) and stores it as “point_light_waving.mp4”.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter

# ------------------------------------------------------------------
# 1. Skeleton description (15 points)
#    0  head
#    1  neck
#    2  R-shoulder
#    3  R-elbow
#    4  R-wrist
#    5  L-shoulder
#    6  L-elbow
#    7  L-wrist
#    8  pelvis / hip-center
#    9  R-hip
#   10  R-knee
#   11  R-ankle
#   12  L-hip
#   13  L-knee
#   14  L-ankle
# ------------------------------------------------------------------

# Fixed bone lengths (in arbitrary units ≈ metres)
BONES = dict(
    head      = .20,
    neck      = .15,
    torso     = .35,
    shoulderW = .40,
    hipW      = .30,
    uArm      = .30,
    lArm      = .30,
    uLeg      = .50,
    lLeg      = .50,
)

# Animation timing --------------------------------------------------
FPS          = 30                 # frames per second
T_TOTAL      = 6                  # total duration (s)
FRAMES       = int(FPS * T_TOTAL) # total frames
t            = np.linspace(0, T_TOTAL, FRAMES)

# Movement parameters ----------------------------------------------
bounce_amp   = .05    # vertical bounce (heavy / happy vibe)
bounce_freq  = 2.0    # Hz

wave_freq    = 2.0    # hand-wave (Hz)
wave_amp     = .35    # elbow swing amplitude (rad)

# ------------------------------------------------------------------
# Helper: compute joint positions for one animation frame
# ------------------------------------------------------------------
def skeleton_at(time):
    """
    Returns an (N=15,2) array with x,y coordinates of all joints
    for the given moment `time` (in seconds).
    """
    # Pelvis (origin, with bounce)
    pelvis_y = bounce_amp * np.sin(2 * np.pi * bounce_freq * time)
    pelvis   = np.array([0.0, pelvis_y])
    
    # Torso & head ---------------------------------------------------
    neck  = pelvis + np.array([0.0, BONES['torso']])
    head  = neck   + np.array([0.0, BONES['head']])
    
    # Shoulders (left negative x, right positive x)
    half_shW = BONES['shoulderW'] / 2
    R_sh = neck + np.array([ half_shW, 0.0])
    L_sh = neck + np.array([-half_shW, 0.0])
    
    # ----------------------------------------------------------------
    # Right arm – waving
    # ----------------------------------------------------------------
    # Shoulder elevation (arm raised ~70° from horizontal)
    shoulder_angle = np.deg2rad(70)       # fixed elevation
    # Base direction (from shoulder) in polar coords:
    dir_sh = np.array([np.cos(shoulder_angle), np.sin(shoulder_angle)])
    R_el  = R_sh + BONES['uArm'] * dir_sh  # elbow
    
    # Elbow oscillation – waving around forearm
    # Swing forearm by ±wave_amp about elbow
    swing = wave_amp * np.sin(2*np.pi*wave_freq*time)
    forearm_angle = shoulder_angle + np.pi - swing
    dir_el = np.array([np.cos(forearm_angle), np.sin(forearm_angle)])
    R_wr  = R_el + BONES['lArm'] * dir_el  # wrist
    
    # ----------------------------------------------------------------
    # Left arm – relaxed beside body
    # ----------------------------------------------------------------
    L_el_angle = -np.pi/2 + 0.1*np.sin(2*np.pi*1.2*time)  # small sway
    dir_Lu = np.array([np.cos(L_el_angle), np.sin(L_el_angle)])
    L_el  = L_sh + BONES['uArm'] * dir_Lu
    
    L_fr_angle = -np.pi/2 + 0.05*np.sin(2*np.pi*1.2*time + np.pi/4)
    dir_Ll = np.array([np.cos(L_fr_angle), np.sin(L_fr_angle)])
    L_wr  = L_el + BONES['lArm'] * dir_Ll
    
    # ----------------------------------------------------------------
    # Hips
    # ----------------------------------------------------------------
    half_hipW = BONES['hipW'] / 2
    R_hip = pelvis + np.array([ half_hipW, 0.0])
    L_hip = pelvis + np.array([-half_hipW, 0.0])
    
    # Legs (standing, slight knee bob)
    knee_bend = 0.08 * np.sin(2*np.pi*1.5*time)  # subtle
    R_knee = R_hip + np.array([0.0, -(BONES['uLeg'] - knee_bend)])
    R_ank  = R_knee + np.array([0.0, -BONES['lLeg']])
    
    L_knee = L_hip + np.array([0.0, -(BONES['uLeg'] + knee_bend)])
    L_ank  = L_knee + np.array([0.0, -BONES['lLeg']])
    
    # Assemble in correct order
    joints = np.vstack([
        head, neck,
        R_sh, R_el, R_wr,
        L_sh, L_el, L_wr,
        pelvis,
        R_hip, R_knee, R_ank,
        L_hip, L_knee, L_ank
    ])
    return joints

# Pre-compute trajectories (Fast rendering) -------------------------
traj = np.stack([skeleton_at(tt) for tt in t])  # shape (frames, 15, 2)

# ------------------------------------------------------------------
# Matplotlib animation setup
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(4,7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# White dots
scat = ax.scatter([], [], s=50, c='white')

# Plot aesthetics
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.6, 1.6)
ax.set_aspect('equal')
ax.axis('off')

def init():
    scat.set_offsets([])
    return scat,

def update(frame):
    scat.set_offsets(traj[frame])
    return scat,

anim = FuncAnimation(fig, update, frames=FRAMES, init_func=init,
                     interval=1000/FPS, blit=True)

# ------------------------------------------------------------------
# Save animation (mp4 if FFmpeg exists, else fallback to GIF)
# ------------------------------------------------------------------
try:
    writer = FFMpegWriter(fps=FPS, bitrate=1800)
    anim.save("point_light_waving.mp4", writer=writer)
except Exception:
    writer = PillowWriter(fps=FPS)
    anim.save("point_light_waving.gif", writer=writer)

# Uncomment the next line if you want to display interactively
# plt.show()
