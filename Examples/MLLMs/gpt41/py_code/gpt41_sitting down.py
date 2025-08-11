
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- BIOLOGICAL MOTION MODEL ("SITTING DOWN") ---

# 15 point labels (common in biological motion displays)
# 0: Head
# 1,2: Shoulders (L,R)
# 3,4: Elbows (L,R)
# 5,6: Wrists (L,R)
# 7,8: Hips (L,R)
# 9,10: Knees (L,R)
# 11,12: Ankles (L,R)
# 13,14: Feet (L,R)

# 2D stick-figure segment lengths (arbitrary units)
seglen = {
    'neck': 0.18,
    'shoulder': 0.25,
    'upparm': 0.25,
    'lowarm': 0.23,
    'spine': 0.32,
    'pelvis': 0.22,
    'thigh': 0.44,
    'shank': 0.40,
    'foot': 0.18
}

def lerp(a, b, t):
    return a + (b - a) * t

# Key poses function for temporal interpolation
def pose_sitting_down(t):
    """
    Returns a list of (x, y) positions for the 15 markers at normalized time t in [0,1].
    t=0: fully standing; t=1: fully sitting.
    """
    # Fixed horizontal position for simplicity
    x0 = 0
    y_base = 0

    # Stand-to-sit: vertical base drops, hips move back, knees flex forward
    # Poses at start and end
    # Initial joint y positions (roughly vertical, standing)
    y_head0 = y_base + seglen['neck'] + seglen['spine'] + seglen['thigh'] + seglen['shank'] + 0.2
    y_shoulder0 = y_head0 - seglen['neck']
    y_pelvis0 = y_base + seglen['thigh'] + seglen['shank']
    y_hip0 = y_pelvis0
    y_knee0 = y_base + seglen['shank']
    y_ankle0 = y_base
    # Final joint y positions (sitting, thighs horizontal, shanks vertical)
    y_head1 = y_base + seglen['shank'] + seglen['neck'] + seglen['spine'] + 0.1
    y_shoulder1 = y_head1 - seglen['neck']
    y_pelvis1 = y_base + seglen['shank']
    y_hip1 = y_pelvis1
    y_knee1 = y_base + seglen['shank']
    y_ankle1 = y_base

    # Horizontal (x) offsets
    shoulder_offset = seglen['shoulder'] / 2
    hip_offset = seglen['pelvis'] / 2

    # 'Sit back' offset: as t increases, hips move backward, knees forward
    hip_back = -0.24 * t
    knee_fwd =  0.30 * t

    # Trunk 'pitch' forward as person sits
    trunk_angle_stand = 0       # vertical
    trunk_angle_sit = np.deg2rad(20)
    trunk_angle = lerp(trunk_angle_stand, trunk_angle_sit, t)

    # Head marker (top center)
    head = np.array([x0, lerp(y_head0, y_head1, t)])

    # Shoulders
    sh_c = np.array([x0, lerp(y_shoulder0, y_shoulder1, t)])
    shL = sh_c + np.array([-shoulder_offset, 0])
    shR = sh_c + np.array([ shoulder_offset, 0])

    # Hips
    hip_c = np.array([x0 + hip_back, lerp(y_hip0, y_hip1, t)])
    hipL = hip_c + np.array([-hip_offset, 0])
    hipR = hip_c + np.array([ hip_offset, 0])

    # Knees
    y_knee = lerp(y_knee0, y_knee1, t)
    kneeL = np.array([x0 + hip_back + knee_fwd, y_knee])
    kneeR = np.array([x0 + hip_back + knee_fwd, y_knee])

    # Ankles
    # (Assume shanks remain vertical)
    anL = np.array([x0 + hip_back + knee_fwd, y_ankle0])
    anR = np.array([x0 + hip_back + knee_fwd, y_ankle0])

    # Feet
    # During sit-down, feet stay fixed or slide slightly
    foot_shift = 0.05 * t
    fL = np.array([anL[0] + foot_shift, y_ankle0])
    fR = np.array([anR[0] + foot_shift, y_ankle0])

    # Arms move with the trunk; swing forward as a counterbalance during sitting
    upper_arm_angle_0 = np.deg2rad(10)     # almost straight down
    upper_arm_angle_1 = np.deg2rad(-60)    # forward swing
    uaL_angle = lerp(upper_arm_angle_0, upper_arm_angle_1, t) + trunk_angle
    uaR_angle = -lerp(upper_arm_angle_0, upper_arm_angle_1, t) + trunk_angle
    elbowL = shL + seglen['upparm'] * np.array([np.sin(uaL_angle), -np.cos(uaL_angle)])
    elbowR = shR + seglen['upparm'] * np.array([np.sin(uaR_angle), -np.cos(uaR_angle)])

    lower_arm_angleL = np.deg2rad(18) - np.deg2rad(48)*t
    lower_arm_angleR = -np.deg2rad(18) + np.deg2rad(48)*t
    wrL = elbowL + seglen['lowarm'] * np.array([np.sin(uaL_angle+lower_arm_angleL), -np.cos(uaL_angle+lower_arm_angleL)])
    wrR = elbowR + seglen['lowarm'] * np.array([np.sin(uaR_angle+lower_arm_angleR), -np.cos(uaR_angle+lower_arm_angleR)])

    # All 15 points: head, shL, shR, elL, elR, wrL, wrR, hipL, hipR, kneeL, kneeR, anL, anR, footL, footR
    return np.vstack([
        head,      # 0
        shL, shR,  # 1 2
        elbowL, elbowR, # 3 4
        wrL, wrR,  # 5 6
        hipL, hipR, # 7 8
        kneeL, kneeR, # 9 10
        anL, anR,   # 11 12
        fL, fR      # 13 14
    ])

# --- MATPLOTLIB ANIMATION SETUP ---

fig, ax = plt.subplots(figsize=(3.2, 6))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.set_xlim(-0.65, 0.65)
ax.set_ylim(-0.10, 1.65)
ax.axis('off')

# Draw 15 points
points, = ax.plot([], [], 'wo', markersize=8)

# --- ANIMATION LOOP ---

N_FRAMES = 70
FPS = 24

def update(frame):
    # Use a gently tapered velocity profile for smoothness
    t = frame / (N_FRAMES - 1)
    t_traj = 0.5 - 0.5 * np.cos(t * np.pi)  # cosine ease
    pos = pose_sitting_down(t_traj)
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

ani = animation.FuncAnimation(fig, update, frames=N_FRAMES, interval=1000/FPS, blit=True, repeat=True)

plt.show()
