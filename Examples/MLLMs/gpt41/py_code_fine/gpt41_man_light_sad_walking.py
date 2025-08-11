
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definitions for the 15 keypoints (standard biological motion)
# [name, index]
JOINT_NAMES = [
    'Head',             # 0
    'Right Shoulder',   # 1
    'Left Shoulder',    # 2
    'Right Elbow',      # 3
    'Left Elbow',       # 4
    'Right Wrist',      # 5
    'Left Wrist',       # 6
    'Pelvis',           # 7
    'Right Hip',        # 8
    'Left Hip',         # 9
    'Right Knee',       #10
    'Left Knee',        #11
    'Right Ankle',      #12
    'Left Ankle',       #13
    'Weight Box',       #14 (in this case, a small box carried in right hand)
]

# Body structure: each joint with parent for kinematic chain, and segment lengths (approx head, limb, torso lengths)
BODY_STRUCTURE = {
    # parent: (index, length in normalized units, base angle)
    'Head':             (7,    0.12,  np.pi/2),  # parent: pelvis, up
    'Right Shoulder':   (7,    0.18,  np.pi/2 + np.pi/11),   # parent: pelvis, up/right
    'Left Shoulder':    (7,    0.18,  np.pi/2 - np.pi/11),   # parent: pelvis, up/left
    'Right Elbow':      (1,    0.21,  3*np.pi/2),  # parent: RSh, down
    'Left Elbow':       (2,    0.21,  3*np.pi/2),  # parent: LSh, down
    'Right Wrist':      (3,    0.20,  3*np.pi/2),  # parent: REl, down
    'Left Wrist':       (4,    0.20,  3*np.pi/2),  # parent: LEl, down
    'Pelvis':           (None, 0,     0),  # Pelvis origin
    'Right Hip':        (7,    0.14,  3*np.pi/2 + np.pi/16),    # parent: pelvis, down/right
    'Left Hip':         (7,    0.14,  3*np.pi/2 - np.pi/16),    # parent: pelvis, down/left
    'Right Knee':       (8,    0.27,  3*np.pi/2),        # parent: RHip, down
    'Left Knee':        (9,    0.27,  3*np.pi/2),        # parent: LHip, down
    'Right Ankle':      (10,   0.27,  3*np.pi/2),        # parent: RKnee, down
    'Left Ankle':       (11,   0.27,  3*np.pi/2),        # parent: LKnee, down
    'Weight Box':       (5,    0.04,  np.pi/2),   # Small (weight) carried at wrist right
}

# Points for rendering (X, Y order)
N_JOINTS = 15

# Kinematic order for forward computation
KIN_CHAIN_ORDER = [
    7,  # Pelvis (origin/root)
    0,  # Head
    1, 2,  # Shoulders
    3, 5,  # R upper arm, wrist
    4, 6,  # L upper arm, wrist
    8, 10, 12, # R leg: hip, knee, ankle
    9, 11, 13, # L leg: hip, knee, ankle
    14 # Weight box
]

def get_joint_positions(t):
    """Return (N,2) joint positions at time t (walking cycle)."""
    # Walking parameters
    stride = 0.30            # step length (horizontal)
    hip_shift = 0.035        # sideways hip swaying
    shoulder_shift = 0.036   # shoulder swing
    step_period = 1.0        # seconds per step
    cycle = 2 * np.pi * (t % step_period) / step_period
    
    # Movement amplitudes
    arm_swing = np.deg2rad(40)
    leg_swing = np.deg2rad(35)
    elbow_swing = np.deg2rad(14)
    head_bounce = 0.015

    joints = np.zeros((N_JOINTS, 2))  # 2D for display (X, Y), (origin pelvis at (0,0))
    pelvis_y = 0.0
    pelvis_x = 0.0

    # Pelvis vertical oscillation
    pelvis_y = 0.0 + 0.03*np.sin(cycle)
    # Pelvis horizontal translation (walks rightward slowly)
    walk_speed = stride / step_period / 60  # px/frame
    pelvis_x = t * walk_speed
    
    joints[7,:] = [pelvis_x, pelvis_y]  # Pelvis

    # Head vertical movement (slightly lags pelvis)
    head_angle = np.pi/2
    head_y = BODY_STRUCTURE['Head'][1] + head_bounce*np.sin(cycle + np.pi/5)
    joints[0,:] = (joints[7,:] + [0, head_y])

    # Shoulders (relative to pelvis, with lateral shift)
    shoulder_offset = BODY_STRUCTURE['Right Shoulder'][1]
    shoulders_y = joints[7,1] + 0.10
    shoulders_x_shift = shoulder_shift*np.sin(cycle + np.pi)
    joints[1,:] = joints[7,:] + [shoulder_offset+shoulders_x_shift, 0.10]   # RShoulder
    joints[2,:] = joints[7,:] + [-shoulder_offset-shoulders_x_shift, 0.10]  # LShoulder

    # Arms swing: each arm swings opposite to leg
    r_arm_angle = np.pi/2 - arm_swing*np.sin(cycle)
    l_arm_angle = np.pi/2 + arm_swing*np.sin(cycle)

    # Elbows:
    r_elbow_len = BODY_STRUCTURE['Right Elbow'][1]
    joints[3,:] = joints[1,:] + r_elbow_len*np.array([np.cos(r_arm_angle), np.sin(r_arm_angle)])
    l_elbow_len = BODY_STRUCTURE['Left Elbow'][1]
    joints[4,:] = joints[2,:] + l_elbow_len*np.array([np.cos(l_arm_angle), np.sin(l_arm_angle)])

    # Wrists: swing at elbow + some flex (elbow_swing)
    r_wrist_angle = r_arm_angle - 0.35 + elbow_swing*np.sin(cycle)
    l_wrist_angle = l_arm_angle + 0.35 - elbow_swing*np.sin(cycle)
    r_wrist_len = BODY_STRUCTURE['Right Wrist'][1]
    l_wrist_len = BODY_STRUCTURE['Left Wrist'][1]
    joints[5,:] = joints[3,:] + r_wrist_len*np.array([np.cos(r_wrist_angle), np.sin(r_wrist_angle)])
    joints[6,:] = joints[4,:] + l_wrist_len*np.array([np.cos(l_wrist_angle), np.sin(l_wrist_angle)])

    # Weight box: just below right wrist (moved consistently as if carried)
    box_angle = BODY_STRUCTURE['Weight Box'][2]
    box_len = BODY_STRUCTURE['Weight Box'][1]
    joints[14,:] = joints[5,:] + box_len*np.array([np.cos(box_angle), np.sin(box_angle)])

    # Hips: swing side-to-side with walking motion
    hip_offset = BODY_STRUCTURE['Right Hip'][1]
    hips_x_shift = hip_shift*np.sin(cycle)
    joints[8,:] = joints[7,:] + [hip_offset+hips_x_shift, -0.08]
    joints[9,:] = joints[7,:] + [-hip_offset-hips_x_shift, -0.08]

    # Legs: swing opposite to arms
    r_leg_angle = 3*np.pi/2 + leg_swing*np.sin(cycle)
    l_leg_angle = 3*np.pi/2 - leg_swing*np.sin(cycle)

    # Knees
    r_knee_len = BODY_STRUCTURE['Right Knee'][1]
    l_knee_len = BODY_STRUCTURE['Left Knee'][1]
    joints[10,:] = joints[8,:] + r_knee_len*np.array([np.cos(r_leg_angle), np.sin(r_leg_angle)])
    joints[11,:] = joints[9,:] + l_knee_len*np.array([np.cos(l_leg_angle), np.sin(l_leg_angle)])

    # Ankles (floor contact)
    # Add some flexion for realism
    r_ankle_angle = r_leg_angle + 0.06*np.sin(cycle)
    l_ankle_angle = l_leg_angle - 0.06*np.sin(cycle)
    r_ankle_len = BODY_STRUCTURE['Right Ankle'][1]
    l_ankle_len = BODY_STRUCTURE['Left Ankle'][1]
    joints[12,:] = joints[10,:] + r_ankle_len*np.array([np.cos(r_ankle_angle), np.sin(r_ankle_angle)])
    joints[13,:] = joints[11,:] + l_ankle_len*np.array([np.cos(l_ankle_angle), np.sin(l_ankle_angle)])

    # Optionally, you may add tiny vertical jitter to the whole body for "sadness/fatigue"
    # e.g. less bounce than a happy walker
    joints[:,1] -= 0.02   # lower all for a "sad" posture (slump)

    # Sag shoulders and arms for "sad" effect
    joints[1,1] -= 0.02; joints[2,1] -= 0.02
    joints[3,1] -= 0.023; joints[4,1] -= 0.023
    joints[5,1] -= 0.013; joints[6,1] -= 0.013
    joints[14,1] -= 0.01  # weight hangs lower

    # Slight lean forward (sad posture)
    joints[:,0] += -0.04 * (joints[:,1]-joints[7,1])

    return joints

# --- Visualization ---

fig, ax = plt.subplots(figsize=(3,6))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax.set_facecolor('black')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.75, 0.25)
ax.axis('off')

# Plot only the point-lights (no lines or skeleton connections)
dot_size = 70   # diameter of the points

points, = ax.plot([], [], 'o', color='white', ms=dot_size/10)

def init():
    points.set_data([], [])
    return (points,)

def animate(i):
    t = (i/60.0)          # 60 FPS
    joints = get_joint_positions(t)
    x, y = joints[:,0], joints[:,1]
    points.set_data(x, y)
    return (points,)

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=240, interval=1000/60, blit=True)

plt.show()
