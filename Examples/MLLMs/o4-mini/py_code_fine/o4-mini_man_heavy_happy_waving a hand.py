
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation parameters
fps = 30                       # frames per second
duration = 2.0                 # duration of one running cycle in seconds
frames = int(fps * duration)   # total frames
omega = 2 * np.pi / duration   # angular speed

# Body segment lengths
spine_len      = 0.5
head_len       = 0.2
shoulder_off   = 0.15
upper_arm_len  = 0.2
lower_arm_len  = 0.2
hip_off        = 0.1
thigh_len      = 0.3
shin_len       = 0.3

# Postural parameters
trunk_lean     = 0.1   # slight forward lean for "sad" posture
bob_amp        = 0.02  # small vertical bob of the pelvis

# Set up plot
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(-1.0, 1.0)
ax.axis('off')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# A single scatter artist for the 15 points
pts, = ax.plot([], [], 'o', color='white', markersize=6)

def init():
    pts.set_data([], [])
    return (pts,)

def animate(frame):
    t = frame / fps
    # Pelvis position (with slight vertical bob)
    pel_x = 0.0
    pel_y = bob_amp * np.sin(2 * omega * t)
    pelvis = np.array([pel_x, pel_y])
    
    # Rotation matrix for trunk lean
    c, s = np.cos(trunk_lean), np.sin(trunk_lean)
    R_trunk = np.array([[c, -s],
                        [s,  c]])
    
    # Neck and head
    neck = pelvis + R_trunk.dot(np.array([0, spine_len]))
    head = neck + R_trunk.dot(np.array([0, head_len]))
    
    # Shoulders
    left_sh  = neck + R_trunk.dot(np.array([-shoulder_off, 0]))
    right_sh = neck + R_trunk.dot(np.array([ shoulder_off, 0]))
    
    # Hips
    left_hp  = pelvis + np.array([-hip_off, -0.1])
    right_hp = pelvis + np.array([ hip_off, -0.1])
    
    # Gait-derived joint angles
    hip_amp      = 0.8
    hip_ang_L    = hip_amp * np.sin(omega * t)
    hip_ang_R    = -hip_ang_L
    
    knee_amp     = 1.2
    knee_ang_L   = np.clip(knee_amp * np.sin(omega * t + np.pi/2), 0, None)
    knee_ang_R   = np.clip(knee_amp * np.sin(omega * t + 3*np.pi/2), 0, None)
    
    shoulder_amp = 0.5
    sh_ang_L     = -shoulder_amp * np.sin(omega * t)
    sh_ang_R     = -sh_ang_L
    
    elbow_amp    = 0.7
    el_ang_L     = elbow_amp * (1 - np.cos(omega * t)) / 2
    el_ang_R     = elbow_amp * (1 - np.cos(omega * t + np.pi)) / 2
    
    # Compute arm joints
    def compute_arm(j_sh, sh_ang, el_ang):
        # upper arm angle: default down (−90°) plus trunk lean plus shoulder swing
        ua_ang = trunk_lean - np.pi/2 + sh_ang
        elbow = j_sh + upper_arm_len * np.array([np.cos(ua_ang), np.sin(ua_ang)])
        la_ang = ua_ang + el_ang
        wrist = elbow + lower_arm_len * np.array([np.cos(la_ang), np.sin(la_ang)])
        return elbow, wrist
    
    L_elbow, L_wrist = compute_arm(left_sh,  sh_ang_L, el_ang_L)
    R_elbow, R_wrist = compute_arm(right_sh, sh_ang_R, el_ang_R)
    
    # Compute leg joints
    def compute_leg(j_hp, hip_ang, knee_ang):
        # thigh angle: default down (−90°) plus trunk lean plus hip swing
        th_ang = trunk_lean - np.pi/2 + hip_ang
        knee = j_hp + thigh_len * np.array([np.cos(th_ang), np.sin(th_ang)])
        sh_ang = th_ang - knee_ang
        ankle = knee + shin_len * np.array([np.cos(sh_ang), np.sin(sh_ang)])
        return knee, ankle
    
    L_knee, L_ankle = compute_leg(left_hp, hip_ang_L, knee_ang_L)
    R_knee, R_ankle = compute_leg(right_hp, hip_ang_R, knee_ang_R)
    
    # Collect all 15 points in a fixed order
    points = np.vstack([
        head,
        neck,
        left_sh,  right_sh,
        L_elbow,  R_elbow,
        L_wrist,  R_wrist,
        pelvis,
        left_hp,  right_hp,
        L_knee,   R_knee,
        L_ankle,  R_ankle
    ])
    
    pts.set_data(points[:,0], points[:,1])
    return (pts,)

anim = FuncAnimation(fig, animate, frames=frames,
                     init_func=init, blit=True, interval=1000/fps)

plt.show()
