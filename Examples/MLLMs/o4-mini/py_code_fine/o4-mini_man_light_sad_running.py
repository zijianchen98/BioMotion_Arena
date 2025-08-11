
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simulation parameters
fps = 30
interval = 1000 / fps  # in milliseconds
cycle_duration = 1.0    # one gait cycle in seconds
frames_per_cycle = int(cycle_duration * fps)

# Body segment lengths (in arbitrary units)
torso_len = 0.6
neck_head_len = 0.3
shoulder_sep = 0.4
hip_sep = 0.3
thigh_len = 0.5
shin_len = 0.5
upper_arm_len = 0.4
forearm_len = 0.4

# Joint angle parameters (degrees)
hip_amp_deg = 30
knee_offset_deg = 150
knee_amp_deg = 30
knee_phase_off = np.pi / 2

shoulder_amp_deg = 30
elbow_offset_deg = 140
elbow_amp_deg = 40
elbow_phase_off = np.pi / 6

bob_amp = 0.05  # vertical bobbing amplitude

# Utility: degrees to radians
d2r = np.pi / 180.0

# Set up the figure
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(0.0, 2.2)
ax.axis('off')

# Initialize scatter for 15 joints
points = ax.scatter([], [], s=50, c='white')

def compute_positions(t):
    """
    Compute the 15 joint positions at normalized time t in [0,1).
    Returns a list of (x,y) tuples in a fixed order.
    Order: head, neck, L_shoulder, R_shoulder, L_elbow, R_elbow,
           L_wrist, R_wrist, pelvis, L_hip, R_hip, L_knee, R_knee,
           L_ankle, R_ankle
    """
    # Pelvis position with vertical bob
    base_y = 0.8
    bob = bob_amp * np.sin(4 * np.pi * t)
    pelvis = np.array((0.0, base_y + bob))
    
    # Neck and head
    neck = pelvis + np.array((0.0, torso_len))
    head = neck + np.array((0.0, neck_head_len))
    
    # Shoulders and hips
    L_sh = neck + np.array((-shoulder_sep/2, 0.0))
    R_sh = neck + np.array(( shoulder_sep/2, 0.0))
    L_hip = pelvis + np.array((-hip_sep/2, 0.0))
    R_hip = pelvis + np.array(( hip_sep/2, 0.0))
    
    # Phases for left/right limbs
    phase_leg_L = 0.0
    phase_leg_R = np.pi
    phase_arm_L = phase_leg_R  # arms swing opposite the legs
    phase_arm_R = phase_leg_L
    
    omega = 2 * np.pi  # angular freq for one gait cycle
    
    # Left leg joint angles
    hip_ang_L = hip_amp_deg * np.sin(omega * t + phase_leg_L) * d2r
    knee_ang_L = (knee_offset_deg + knee_amp_deg * np.sin(omega * t + phase_leg_L + knee_phase_off)) * d2r
    # Right leg joint angles
    hip_ang_R = hip_amp_deg * np.sin(omega * t + phase_leg_R) * d2r
    knee_ang_R = (knee_offset_deg + knee_amp_deg * np.sin(omega * t + phase_leg_R + knee_phase_off)) * d2r
    
    # Left arm joint angles
    sh_ang_L = shoulder_amp_deg * np.sin(omega * t + phase_arm_L) * d2r
    el_ang_L = (elbow_offset_deg + elbow_amp_deg * np.sin(omega * t + phase_arm_L + elbow_phase_off)) * d2r
    # Right arm joint angles
    sh_ang_R = shoulder_amp_deg * np.sin(omega * t + phase_arm_R) * d2r
    el_ang_R = (elbow_offset_deg + elbow_amp_deg * np.sin(omega * t + phase_arm_R + elbow_phase_off)) * d2r
    
    # Helper to compute joint chain
    def segment(pt0, length, abs_angle):
        """Compute end point from pt0 given length and absolute angle
        with 0 rad = up, positive clockwise."""
        dx = length * np.sin(abs_angle)
        dy = length * np.cos(abs_angle)
        return pt0 + np.array((dx, dy))
    
    # Legs: thigh angle measured from upward vertical, plus 180 for downward
    thigh_L_ang = np.pi + hip_ang_L
    knee_L = segment(L_hip, thigh_len, thigh_L_ang)
    shin_L_ang = thigh_L_ang + (np.pi - knee_ang_L)
    ankle_L = segment(knee_L, shin_len, shin_L_ang)
    
    thigh_R_ang = np.pi + hip_ang_R
    knee_R = segment(R_hip, thigh_len, thigh_R_ang)
    shin_R_ang = thigh_R_ang + (np.pi - knee_ang_R)
    ankle_R = segment(knee_R, shin_len, shin_R_ang)
    
    # Arms: shoulder angle measured from downward vertical
    up_arm_L_ang = np.pi + sh_ang_L
    elbow_L = segment(L_sh, upper_arm_len, up_arm_L_ang)
    forearm_L_ang = up_arm_L_ang + (np.pi - el_ang_L)
    wrist_L = segment(elbow_L, forearm_len, forearm_L_ang)
    
    up_arm_R_ang = np.pi + sh_ang_R
    elbow_R = segment(R_sh, upper_arm_len, up_arm_R_ang)
    forearm_R_ang = up_arm_R_ang + (np.pi - el_ang_R)
    wrist_R = segment(elbow_R, forearm_len, forearm_R_ang)
    
    # Collect joints in required order
    joints = [
        head, neck,
        L_sh, R_sh,
        elbow_L, elbow_R,
        wrist_L, wrist_R,
        pelvis,
        L_hip, R_hip,
        knee_L, knee_R,
        ankle_L, ankle_R
    ]
    return np.array(joints)

def init():
    points.set_offsets([])
    return (points,)

def update(frame):
    t = (frame % frames_per_cycle) / frames_per_cycle
    pts = compute_positions(t)
    points.set_offsets(pts)
    return (points,)

ani = animation.FuncAnimation(
    fig, update, init_func=init,
    frames=frames_per_cycle*10, interval=interval, blit=True
)

plt.show()
