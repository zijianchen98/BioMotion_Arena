
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- Stimulus Parameters ----
N_MARKERS = 15  # Number of white points
FIGSIZE = (5, 8)
POINT_SIZE = 80
FIG_BG = 'black'
POINT_COLOR = 'white'
ANIMATION_SECONDS = 2.2
FPS = 40

# Marker order based on standard biological motion displays:
# 0: Head
# 1-2: Shoulders (L,R)
# 3-4: Elbows (L,R)
# 5-6: Hands (L,R)
# 7-8: Hips (L,R)
# 9-10: Knees (L,R)
# 11-12: Ankles (L,R)
# 13-14: Feet (L,R)

def body_pose(t, total_jump_x=2.0, jump_height=1.0):
    # t in [0, 1]: normalized phase in jump
    # Setup body segment lengths (all values in arbitrary units)
    head_y = 7.8
    neck_len = 0.5
    shoulder_span = 1.2
    upperarm = 1.0
    forearm = 1.0
    torso = 2.2
    hip_span = 0.7
    thigh = 1.4
    shank = 1.4
    foot_len = 0.5

    # 1. "Jump" = squat (preload), explode up, translate forward, land.
    squat = 0.8  # Crouched by up to this much
    body_swing = 0.4  # Forward lean in crouch

    # t: 0      (squat/crouch) -> 0.18 (push) -> 0.82 (apex) -> 1 (land)
    # Vertical profile: like jump parabola
    g = 2 * jump_height  # pseudo-gravity, unit/sec^2

    # "Squat before jump" (first 12% of time): body dips down and leans forward.
    if t < 0.12:
        frac = t / 0.12
        root_y = 2.0 - squat * (1 - frac)  # move down
        root_lean = body_swing * (1 - frac)
    else:
        # Jump trajectory: up and forward arc
        t_jump = (t - 0.12) / (0.88)
        root_y = 2.0 + jump_height * 4 * t_jump * (1 - t_jump)
        root_lean = (1 - 2 * t_jump) * body_swing * 0.6  # minimal lean in air

    # Hips move forward over time (push-off + aerial)
    root_x = -total_jump_x/2 + total_jump_x * t
    # Hip center
    hip_center = np.array([root_x, root_y])

    # Shoulders, head (torso direction: some lean forward when bending, otherwise upright)
    torso_angle = np.pi/2 - root_lean  # pi/2 is vertical up, reduce by lean
    hip_l = hip_center + np.array([-hip_span/2, 0])
    hip_r = hip_center + np.array([ hip_span/2, 0])
    shoulder_center = hip_center + np.array([np.cos(torso_angle), np.sin(torso_angle)]) * torso
    shoulder_l = shoulder_center + np.array([-shoulder_span/2, 0])
    shoulder_r = shoulder_center + np.array([ shoulder_span/2, 0])
    head = shoulder_center + np.array([0, neck_len + 0.3])
    
    # Arms: realistic swinging
    # Arms swing upward during push, backward through air, forward for landing (simplified)
    swing = 0.7*np.sin(np.pi*t)
    arm_angles = [
        torso_angle + np.pi/2 + 0.4*swing, # left up
        torso_angle + np.pi/2 - 0.4*swing  # right up
    ]
    # Elbows & hands
    elbows = []
    hands = []
    for idx, (sc, sign) in enumerate([(shoulder_l,1), (shoulder_r,-1)]):
        # Swing forwards when jumping, backward on landing (by sign)
        # elbow position
        e_ang = arm_angles[idx] - 0.25*sign*np.cos(np.pi*t)
        hand_ang = e_ang - 0.14*sign
        elbow = sc + 0.9*np.array([np.cos(e_ang), np.sin(e_ang)])*upperarm
        hand = elbow + 0.9*np.array([np.cos(hand_ang), np.sin(hand_ang)])*forearm
        elbows.append(elbow)
        hands.append(hand)

    # Legs: squat -> extend (toes up), tuck knees in air, land knees bend
    if t < 0.16:
        # squat, legs folded
        knee_y = -0.4
        knee_x = 0.35
        ankle_y = -1.7
        ankle_x = 0.45
    elif t > 0.75:
        # landing, crouch knees
        knee_y = -0.6
        knee_x = 0.39
        ankle_y = -2.1
        ankle_x = 0.48
    else:
        # airborne: knees a bit flexed
        tt = min((t-0.16)/0.6,1)
        knee_y = -0.23 - 0.07*np.sin(np.pi*tt)
        knee_x = 0.33 + 0.09*np.sin(np.pi*tt)
        ankle_y = -1.8
        ankle_x = 0.44

    # Ankles and knees
    knees = []
    ankles = []
    feet = []
    for hip, sign in [(hip_l, 1), (hip_r, -1)]:
        knee = hip + np.array([sign*knee_x, knee_y])
        ankle = knee + np.array([sign*(ankle_x-knee_x), ankle_y-knee_y])
        foot = ankle + np.array([sign*foot_len, -0.1])
        knees.append(knee)
        ankles.append(ankle)
        feet.append(foot)
        
    # Compose marker sequence
    XY = np.stack([
        head,           # 0 Head
        shoulder_l,     # 1 LShoulder
        shoulder_r,     # 2 RShoulder
        elbows[0],      # 3 LElbow
        elbows[1],      # 4 RElbow
        hands[0],       # 5 LHand
        hands[1],       # 6 RHand
        hip_l,          # 7 LHip
        hip_r,          # 8 RHip
        knees[0],       # 9 LKnee
        knees[1],       # 10 RKnee
        ankles[0],      # 11 LAnkle
        ankles[1],      # 12 RAnkle
        feet[0],        # 13 LFoot
        feet[1],        # 14 RFoot
    ])
    return XY

# ---- Animation Prep ----
nframes = int(ANIMATION_SECONDS * FPS)
X_all = np.zeros((nframes, N_MARKERS, 2))
for f in range(nframes):
    t = f / (nframes-1)
    X_all[f] = body_pose(t)

# Center all X,Y for nice plotting
allxy = X_all.reshape(-1, 2)
xmin, xmax = np.min(allxy[:,0]), np.max(allxy[:,0])
ymin, ymax = np.min(allxy[:,1]), np.max(allxy[:,1])
x_margin = 0.3
y_margin = 0.5

# For smooth loop, double and reverse frames for fade-out ("ping-pong")
X_anim = np.concatenate([X_all, X_all[::-1]], axis=0)

# ---- Plot and Animate ----
fig, ax = plt.subplots(figsize=FIGSIZE, facecolor=FIG_BG)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
scat = ax.scatter([], [], c=POINT_COLOR, s=POINT_SIZE, edgecolor='none')

ax.set_xlim(xmin-x_margin, xmax+x_margin)
ax.set_ylim(ymin-y_margin, ymax+y_margin)
ax.set_facecolor(FIG_BG)
ax.axis('off')

def init():
    scat.set_offsets(np.zeros((N_MARKERS, 2)))
    return scat,

def animate(i):
    XY = X_anim[i]
    scat.set_offsets(XY)
    return scat,

ani = animation.FuncAnimation(
    fig, animate, frames=len(X_anim), init_func=init, interval=1000/FPS, blit=True
)

plt.show()
