
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -- Point-light marker definition (joint order) --
JOINTS = [
    'head',
    'neck',
    'right_shoulder', 'left_shoulder',
    'right_elbow', 'left_elbow',
    'right_hand', 'left_hand',
    'pelvis',
    'right_hip', 'left_hip',
    'right_knee', 'left_knee',
    'right_foot', 'left_foot'
]

# Define basic body structure (distances in arbitrary units)
limbs = dict(
    head_neck=0.18,
    neck_shoulder=0.15,
    shoulder_elbow=0.21,
    elbow_hand=0.18,
    neck_pelvis=0.24,
    pelvis_hip=0.08,
    hip_knee=0.27,
    knee_foot=0.24,
    shoulder_offset=0.19,
    hip_offset=0.14
)

# Anatomical locations for heavy weight (wider, rounder body)
def get_body_pose(t, handwave=True):
    '''
    Returns 15x2 array of body positions at time t.
    - handwave: if True, left hand waves; else, right hand
    '''
    # Core joint: pelvis (origin)
    pelvis = np.array([0., 0.])
    # Pelvis is wider for heavier individual
    hip_R = pelvis + np.array([-limbs['hip_offset'], 0])
    hip_L = pelvis + np.array([ limbs['hip_offset'], 0])

    # Up to neck
    neck = pelvis + np.array([0, limbs['neck_pelvis']])

    # Head
    head = neck + np.array([0, limbs['head_neck']])

    # Shoulders: wider and slightly elevated
    sh_R = neck + np.array([-limbs['shoulder_offset'], 0.03])
    sh_L = neck + np.array([limbs['shoulder_offset'], 0.03])

    # Elbows (neutral base)
    elb_R = sh_R + np.array([-0.065, -limbs['shoulder_elbow']])
    elb_L = sh_L + np.array([0.065, -limbs['shoulder_elbow']])

    # Hands (neutral base)
    hand_R = elb_R + np.array([-0.03, -limbs['elbow_hand']])
    hand_L = elb_L + np.array([0.03, -limbs['elbow_hand']])

    # Knees
    knee_R = hip_R + np.array([-0.02, -limbs['hip_knee']])
    knee_L = hip_L + np.array([0.02, -limbs['hip_knee']])

    # Feet
    foot_R = knee_R + np.array([0, -limbs['knee_foot']])
    foot_L = knee_L + np.array([0, -limbs['knee_foot']])

    # Animate arm for waving hand
    phase = t * 2 * np.pi
    # Left hand waves by default
    wave_amp = 0.45*np.pi # (in radians)
    wave = 0.20*np.sin(phase*1.01)
    # Joint angles (shoulder, elbow for left arm)
    # Simulate a "heavy" inertia: slightly slower, bigger shoulder movement

    # Shoulder movement: rotate around shoulder
    # Start with left upper arm straight down, then oscillate leftwards
    sh_angle_L = -np.pi/2 + 0.33*wave_amp*np.sin(phase*0.88)
    elb_angle_L = -np.pi/3 + 0.30*wave_amp*np.sin(phase*0.92 + 0.4)

    # Calculate left elbow
    elb_L = sh_L + limbs['shoulder_elbow']*np.array([
        np.cos(sh_angle_L), np.sin(sh_angle_L)
    ])
    # Calculate left hand
    hand_L = elb_L + limbs['elbow_hand']*np.array([
        np.cos(sh_angle_L+elb_angle_L), np.sin(sh_angle_L+elb_angle_L)
    ])

    # Approximate a happy expression and ground truth; slightly sway whole body (biological realism)
    sway = 0.03 * np.sin(phase*0.51)

    # Optional: bounce motion (simulating the weight)
    bounce = 0.025 * np.sin(phase*0.97 + 0.5)

    for var in ['pelvis','hip_R','hip_L','neck','sh_R','sh_L','elb_R','elb_L','hand_R','hand_L','knee_R','knee_L','foot_R','foot_L']:
        eval(var)[:] += np.array([sway, bounce])

    # Head vertical bob
    head[:] += [sway, 0.012*np.sin(phase*2)]

    # Assemble all joint positions as per JOINTS
    points = np.array([
        head,         # 0 Head
        neck,         # 1 Neck
        sh_R, sh_L,   # 2,3 Shoulders
        elb_R, elb_L, # 4,5 Elbows
        hand_R, hand_L,# 6,7 Hands
        pelvis,       # 8 Pelvis
        hip_R, hip_L, # 9,10 Hips
        knee_R, knee_L, # 11,12 Knees
        foot_R, foot_L # 13,14 Feet
    ])
    return points

# --- Animation setup ---
fig, ax = plt.subplots(figsize=(4,7))

ax.set_facecolor('k')
ax.set_xlim(-0.45, 0.45)
ax.set_ylim(-0.10, 1.15)
ax.set_xticks([])
ax.set_yticks([])
plt.tight_layout()
# Store 15 point objects
points = get_body_pose(0)

scat = ax.scatter(points[:,0], points[:,1], s=70, color='w', edgecolors='none')

def animate(frame):
    t = frame / 60  # ~60 FPS
    pts = get_body_pose(t)
    scat.set_offsets(pts)
    return scat,

ani = FuncAnimation(fig, animate, frames=360, interval=1000/60, blit=True)

plt.show()
