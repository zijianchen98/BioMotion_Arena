
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --------- Constants ---------
FPS = 30
DURATION = 2      # seconds per jump
NUM_FRAMES = DURATION * FPS
FIG_W, FIG_H = 5, 8  # Figure size, aspect matches example image (tall)
DOT_SIZE = 70
NUM_DOTS = 15
BG_COLOR = 'black'
DOT_COLOR = 'white'

# --------- Skeleton Structure ---------
# 15 points: head, neck, RSHO, LSHO, RCHE, LCHE, RHIP, LHIP, lower back, RKNE, LKNE, RANK, LANK, RWR, LWR

JOINTS = [
    "head",    # 0
    "neck",    # 1
    "rsho",    # 2
    "lsho",    # 3
    "rche",    # 4  (right chest/upper arm)
    "lche",    # 5  (left chest/upper arm)
    "rhip",    # 6
    "lhip",    # 7
    "back",    # 8 (mid lower back/pelvis)
    "rkne",    # 9
    "lkne",    #10
    "rank",    #11
    "lank",    #12
    "rwr",     #13 (right wrist)
    "lwr"      #14 (left wrist)
]

# --------- Sad Jump Parameters ---------
# Frame 0: stance, knees/shoulders down, head slumped.
# Jump phase: squat, then extend, leap, airborne (center of mass rises), land, knees/shoulders flex, repeat.
# 'Sad' cues: head/neck/shoulders slouch, wrists droop, minimal arm lift.

# Stick-figure lengths (proportional for a lightweight woman, units arbitrary)
L_HEAD = 0.4
L_NECK = 0.18
L_SHOULDER = 0.45  # Shoulder width
L_TORSO = 0.8
L_PELVIS = 0.34    # Hip width
L_UPPER_ARM = 0.32
L_FOREARM = 0.29
L_UPPER_LEG = 0.54
L_LOWER_LEG = 0.50
STANCE_WIDTH = 0.14

# ------------ Key Pose Configuration --------------
def get_joint_pos(base_x, base_y, phase):
    # Phase: parameter from 0-1 for 1 jump cycle
    # Vertical jump center-of-mass movement (projectile path): h = v0*t - 0.5*g*t^2, t in [0,1]
    # We'll use a parabola so y_cm(t) = H * 4 * t * (1-t), peaking at t=0.5, min at t=0 or t=1

    # JUMP HEIGHT (vertical CoM offset)
    H = 1.1  # Jump height

    y_cm = H * 4 * phase * (1 - phase)  # normalized 0..H skip jump
    x_cm = 2.5 * phase                  # slow forward (rightward) motion

    # Squat timing: squat at phase 0, extend by 0.15, peak airborne at 0.5, land by 0.9, squat again by 1
    if phase < 0.12:           # Squatting
        squat_amt = (0.12 - phase) / 0.12
    elif phase > 0.9:          # Landing squat
        squat_amt = (phase - 0.9) / 0.1
    else:
        squat_amt = 0.

    # Sadness cues curve: slouch (head/neck fw and down), shoulders dropped, wrists pointed down
    sad_slouch = 0.45  # max slouch
    sad_shoulder_drop = 0.09

    base_x += x_cm
    base_y += y_cm - squat_amt*0.32

    # Get basic stick figure pose (y grows up, x grows right)
    # 1. Pelvis (hips): average hip center
    pelvis = np.array([base_x, base_y])
    # 2. Hips: left/right
    lhip = pelvis + np.array([-L_PELVIS/2, 0])
    rhip = pelvis + np.array([+L_PELVIS/2, 0])
    # 3. Spine: up from pelvis by torso
    back = pelvis + np.array([0, L_TORSO*0.5])
    chest = back + np.array([0, L_TORSO*0.5])  # chest = shoulder height
    # 4. Shoulders: centered, lowered for 'sad', slightly forward if slouch
    shoulder_y = chest[1] - sad_shoulder_drop
    lsho = np.array([chest[0] - L_SHOULDER/2, shoulder_y])
    rsho = np.array([chest[0] + L_SHOULDER/2, shoulder_y])
    # 5. Neck up from chest/shoulders (slouched forward for 'sad')
    neck = chest + np.array([0, L_NECK * (1-sad_slouch)])
    head = neck + np.array([0, L_HEAD * (0.86-sad_slouch)])  # Less up, more down
    # 6. Chest points (for completeness; midway to shoulders)
    lche = chest + (lsho - chest) * 0.4
    rche = chest + (rsho - chest) * 0.4
    # 7. Arms: slumped, not swung; wrists below shoulders, elbows near upper arm
    r_elbow = rsho + np.array([0.07, -L_UPPER_ARM*0.93-(squat_amt*0.10)])
    l_elbow = lsho + np.array([-0.07, -L_UPPER_ARM*0.93-(squat_amt*0.10)])

    # Wrists: most 'sad'/relaxed, pointed down & bent
    rwr = r_elbow + np.array([-0.04, -L_FOREARM*0.99])
    lwr = l_elbow + np.array([0.04, -L_FOREARM*0.99])

    # 8. Legs:
    # - For jumping: crouch at start, extend at lift-off, airborne legs lifted
    # - Emphasize lightweight by flexing knees more and tucking feet
    # Crouch angle, airborne foot lift parameters
    angle_crouch = np.interp(squat_amt, [0,1], [0.2, 0.7])  # radians
    angle_air = np.interp(phase, [0.23,0.45,0.72], [0,0.55,0])  # airborne phase: knees flex & feet backward

    # Right leg
    rknee = rhip + np.array([STANCE_WIDTH*0.4 + np.sin(angle_crouch+angle_air)*0.11, -L_UPPER_LEG*np.cos(angle_crouch+angle_air)])
    rank = rknee + np.array([STANCE_WIDTH*0.5, -L_LOWER_LEG*np.cos(angle_crouch*1.13+angle_air)])
    # Left leg
    lknee = lhip + np.array([-STANCE_WIDTH*0.4 - np.sin(angle_crouch+angle_air)*0.10, -L_UPPER_LEG*np.cos(angle_crouch+angle_air)])
    lank = lknee + np.array([-STANCE_WIDTH*0.5, -L_LOWER_LEG*np.cos(angle_crouch*1.13+angle_air)])

    # Done
    points = [
        head,          # 0
        neck,          # 1
        rsho,          # 2
        lsho,          # 3
        rche,          # 4
        lche,          # 5
        rhip,          # 6
        lhip,          # 7
        pelvis,        # 8 (back)
        rknee,         # 9
        lknee,         #10
        rank,          #11
        lank,          #12
        rwr,           #13
        lwr            #14
    ]
    return np.stack(points, axis=0)

# ----------- Animation Setup --------------
# Precompute all frames for efficiency
frames = []
for f in range(NUM_FRAMES):
    ph = (f / NUM_FRAMES)
    frames.append(get_joint_pos(base_x=0, base_y=1.4, phase=ph))

frames = np.stack(frames, axis=0)  # [frames, 15, 2]

# ----------- Matplotlib Animation -----------
fig, ax = plt.subplots(figsize=(FIG_W,FIG_H))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

ax.set_facecolor(BG_COLOR)
ax.set_xlim(-0.6, 4.3)
ax.set_ylim(-0.55, 3.2)
ax.axis('off')

dots = []
for i in range(NUM_DOTS):
    dot, = ax.plot([], [], 'o', markersize=DOT_SIZE/10, color=DOT_COLOR, markeredgewidth=0)
    dots.append(dot)

def init():
    for dot in dots:
        dot.set_data([], [])
    return dots

def animate(i):
    pts = frames[i % NUM_FRAMES]
    for j, dot in enumerate(dots):
        dot.set_data(pts[j,0], pts[j,1])
    return dots

ani = FuncAnimation(
    fig, animate, frames=NUM_FRAMES,
    init_func=init, interval=1000//FPS, blit=True, repeat=True
)

plt.show()
