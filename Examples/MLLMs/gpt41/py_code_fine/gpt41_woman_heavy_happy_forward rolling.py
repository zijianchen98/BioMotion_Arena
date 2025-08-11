
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ---- 15 Point-Light Marker Definitions ---- #
# 0: Head
# 1: Neck
# 2: Right Shoulder
# 3: Left Shoulder
# 4: Right Elbow
# 5: Left Elbow
# 6: Right Wrist
# 7: Left Wrist
# 8: Pelvis
# 9: Right Hip
# 10: Left Hip
# 11: Right Knee
# 12: Left Knee
# 13: Right Ankle
# 14: Left Ankle

# The skeleton limb structure: (from, to)
LIMB_PAIRS = [
    (0,1),     # head to neck
    (1,2), (1,3),                           # neck to shoulders
    (2,4), (3,5),                           # shoulder to elbow
    (4,6), (5,7),                           # elbow to wrist
    (1,8),                                  # neck to pelvis
    (8,9), (8,10),                          # pelvis to hips
    (9,11), (10,12),                        # hips to knees
    (11,13), (12,14)                        # knees to ankles
    # Only for reference, not rendered
]

# Define the stick figure's "T pose" 3D positions (meters)
# Forward facing, y-up, x-left, z-forward (screen)
BASE_POS = np.array([
    [ 0.00, 1.70, 0.00],   #  0 Head
    [ 0.00, 1.60, 0.00],   #  1 Neck
    [ 0.14, 1.54, 0.00],   #  2 RShoulder
    [-0.14, 1.54, 0.00],   #  3 LShoulder
    [ 0.27, 1.32, 0.00],   #  4 RElbow
    [-0.27, 1.32, 0.00],   #  5 LElbow
    [ 0.34, 1.08, 0.00],   #  6 RWrist
    [-0.34, 1.08, 0.00],   #  7 LWrist
    [ 0.00, 1.10, 0.00],   #  8 Pelvis
    [ 0.08, 1.07, 0.00],   #  9 RHip
    [-0.08, 1.07, 0.00],   # 10 LHip
    [ 0.08, 0.60, 0.00],   # 11 RKnee
    [-0.08, 0.60, 0.00],   # 12 LKnee
    [ 0.08, 0.08, 0.00],   # 13 RAnkle
    [-0.08, 0.08, 0.00],   # 14 LAnkle
])

# Parameters for motion
FRAMES = 100
FPS = 50
DURATION = 2.0      # seconds for a full roll
ROLL_RADIUS = 0.5   # approximate body length
TRAVEL_SPEED = 0.40 # m/sec, forward

def body_scale(x):
    # Simulate a heavier woman: larger body (waist/hips bigger, arms/legs shorter, head larger)
    s = np.copy(x)
    # Enlarge head
    s[0,1] += 0.05
    # Widen shoulders/hips, increase pelvis/hips size
    s[2:4,0] *= 1.05
    s[9:11,0] *= 1.15
    s[8,0] *= 1.10
    # Arms shorter and thicker
    s[4:7,0] *= 0.95
    s[5:8,0] *= 0.95
    s[4,0] += 0.04; s[6,0] += 0.02
    s[5,0] -= 0.04; s[7,0] -= 0.02
    # Legs shorter, stance wider
    s[11:13,0] *= 1.12; s[13:15,0] *= 1.15
    return s

BASE_POS = body_scale(BASE_POS)

def happy_woman_gait(t):
    # t in [0,1], output 15x3 (single frame) 3D positions
    # t=0: start rolling, t=0.5: upside down, t=1: finished roll
    # We'll use a simplified roll around the lateral axis (x), simulating a realistic forward somersault.
    # Add a little happy bounce and arm gesture
    pos = np.copy(BASE_POS)
    # Center of mass for rotation (about pelvis)
    pelvis = pos[8,:]
    # Angle of rotation through the roll (0 to 2*pi)
    theta = 2 * np.pi * t

    # For forward travel
    dz = ROLL_RADIUS * theta      # forward shift

    # Roll the whole body forward around the shoulder line
    angle = theta
    # Axis: lateral axis (x), through the shoulder/pelvis center
    axis = np.array([1,0,0])

    # Move a bit up/down (bounciness, happiness)
    happy_bounce = 0.06*np.sin(2*np.pi*t)
    # Arms up at start and swing, simulating a joyful gesture before tuck
    arm_swing = 0.7 - 0.55*(np.sin(np.pi*t)**2)
    if t < 0.15:
        # Start pose: arms high for happy, heavy stance
        pos[6,1] += 0.14*arm_swing; pos[7,1] += 0.14*arm_swing
        pos[4:8,0] *= 1.12
    elif t < 0.30:
        # Begin to tuck arms/legs
        padj = (t-0.15)/(0.15)
        pos[6,1] -= 0.12*padj; pos[7,1] -= 0.12*padj
        pos[4,0] -= 0.08*padj; pos[5,0] += 0.08*padj
        pos[13:,0] += 0.09*padj; pos[14,0] -= 0.09*padj
    else:
        # Tuck in
        for idx in [6,7,13,14]: # hands and ankles
            pos[idx] = 0.65*pos[idx] + 0.35*pos[8]

    def rot(v, angle, axis, origin):
        # Apply 3d rotation to vector v around axis through origin
        v2 = v - origin
        axis = axis/np.linalg.norm(axis)
        cost = np.cos(angle)
        sint = np.sin(angle)
        cross = np.cross(axis, v2)
        dot = np.dot(axis, v2)
        rotated = cost*v2 + sint*cross + (1-cost)*dot*axis
        return origin + rotated

    # Apply forward roll to the body (about the shoulder axis crossing the pelvis)
    should_axis = np.array([1,0,0])
    pivot = 0.40*pos[1] + 0.60*pos[8]  # point near neck-pelvis
    for i in range(len(pos)):
        pos[i] = rot(pos[i], angle, should_axis, pivot)
        pos[i,2] += dz
        pos[i,1] += happy_bounce

    # Hip/shoulder sway (adds weight gesture)
    sway = 0.10 * np.sin(theta-0.2)
    pos[2,0] += sway * 0.5; pos[3,0] -= sway*0.5    # shoulders
    pos[9,0] += sway * 1.4; pos[10,0] -= sway*1.4   # hips/pelvis widen
    pos[8,0] += sway * 1.1

    # Heavy weight: slight inertia (legs drag a bit)
    lag = 0.10 * np.sin(theta + 0.35)
    pos[13,0] += lag; pos[14,0] -= lag

    return pos

# ------ PROJECT TO 2D (camera) ------
def project(X):
    # Orthographic projection, y up, z forward
    # Flip x axis so realistic for figure (like sample image)
    Y = np.empty((X.shape[0],2))
    Y[:,0] = -X[:,0]
    Y[:,1] = X[:,1]
    return Y

# --------- ANIMATION CODE --------------

fig = plt.figure(figsize=(3.5,5.0), facecolor='black')
ax = plt.axes([0,0,1,1], frameon=False)
ax.set_xlim([-0.55,0.55])
ax.set_ylim([0.0,2.0])
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

pts, = ax.plot([], [], 'o', color='white', ms=7)

def init():
    pts.set_data([], [])
    return (pts,)

def animate(frame):
    t = (frame % FRAMES) / FRAMES
    pos_3d = happy_woman_gait(t)
    pos_2d = project(pos_3d)
    pts.set_data(pos_2d[:,0], pos_2d[:,1])
    return (pts,)

ani = animation.FuncAnimation(
    fig, animate, frames=FRAMES, interval=1000*DURATION/FRAMES,
    init_func=init, blit=True, repeat=True
)
plt.show()
