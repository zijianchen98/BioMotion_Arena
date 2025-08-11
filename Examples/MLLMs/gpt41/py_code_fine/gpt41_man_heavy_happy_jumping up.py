
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Defines the structure and linkage of the points
JOINT_NAMES = [
    'head',            #0
    'neck',            #1
    'r_shoulder',      #2
    'l_shoulder',      #3
    'chest',           #4
    'r_elbow',         #5
    'l_elbow',         #6
    'r_wrist',         #7
    'l_wrist',         #8
    'pelvis',          #9
    'r_hip',           #10
    'l_hip',           #11
    'r_knee',          #12
    'l_knee',          #13
    'r_ankle'          #14
    # l_ankle is not in 15 points, so omit
]

# Connections (for artist reference, not displayed)
CONNECTIONS = [
    (0, 1),   # head->neck
    (1, 2), (1, 3),  # neck->shoulders
    (1, 4),   # neck->chest
    (2, 5), (3, 6),  # shoulders->elbows
    (5, 7), (6, 8),  # elbows->wrists
    (4, 9),   # chest->pelvis
    (9, 10), (9, 11), # pelvis->hips
    (10, 12), (11, 13), # hips->knees
    (12, 14),      # r_knee->r_ankle
    # No left ankle for 15 points
]

# Relative segment lengths (arbitrary units, to get plausible motion)
LENGTHS = {
    ('neck','head'): 0.18,
    ('neck','r_shoulder'): 0.16,
    ('neck','l_shoulder'): 0.16,
    ('neck','chest'): 0.18,
    ('r_shoulder','r_elbow'): 0.22,
    ('l_shoulder','l_elbow'): 0.22,
    ('r_elbow','r_wrist'): 0.22,
    ('l_elbow','l_wrist'): 0.22,
    ('chest','pelvis'): 0.20,
    ('pelvis','r_hip'): 0.10,
    ('pelvis','l_hip'): 0.10,
    ('r_hip','r_knee'): 0.28,
    ('l_hip','l_knee'): 0.28,
    ('r_knee','r_ankle'): 0.26,
}

# Helper: Build a skeleton frame
def happyman_skeleton(jump_phase, heavy_factor=1.0):
    # jump_phase in [0, 1), describes where in the jump motion (0: on ground, 0.5: top in air, 1: ground)
    # heavy_factor tweaks how compressed the body is (heavier: more tucked on ground, fast squat action)
    c = np.cos
    s = np.sin
    pi = np.pi

    jump_height = 0.33 * c(pi * jump_phase) ** 2  # smooth, highest at jump_phase = 0.5 (top)
    compress = 1 - 0.18 * s(pi * jump_phase) ** 2 * heavy_factor # body squashed downward most before jump
    swing = 0.65 * s(pi * jump_phase)  # arms swing up during take-off, down at landing

    # Center of mass (pelvis)
    pelvis = np.array([0.0, compress + jump_height])
    
    # chest above pelvis
    chest = pelvis + np.array([0, LENGTHS[('chest','pelvis')]])

    # neck above chest
    neck = chest + np.array([0, LENGTHS[('neck','chest')]])
    head = neck + np.array([0, LENGTHS[('neck','head')]])

    # shoulders (left/right)
    shoulder_y = neck[1] - 0.04
    r_shoulder = neck + np.array([LENGTHS[('neck','r_shoulder')], -0.04])
    l_shoulder = neck + np.array([-LENGTHS[('neck','l_shoulder')], -0.04])

    # arms: swing direction depends on jumping phase, heavy arms swing a little less
    swing_r_ang = np.pi/2 - 0.9 + swing * (0.7 + 0.2*heavy_factor)
    swing_l_ang = np.pi/2 + 0.9 - swing * (0.7 + 0.2*heavy_factor)
    r_elbow = r_shoulder + LENGTHS[('r_shoulder','r_elbow')]*np.array([c(swing_r_ang), s(swing_r_ang)])
    l_elbow = l_shoulder + LENGTHS[('l_shoulder','l_elbow')]*np.array([c(swing_l_ang), s(swing_l_ang)])

    r_wrist = r_elbow + LENGTHS[('r_elbow','r_wrist')]*np.array([c(swing_r_ang-0.23), s(swing_r_ang-0.23)])
    l_wrist = l_elbow + LENGTHS[('l_elbow','l_wrist')]*np.array([c(swing_l_ang+0.23), s(swing_l_ang+0.23)])

    # hips (pelvis is between them)
    r_hip = pelvis + np.array([0.09, -LENGTHS[('pelvis','r_hip')]])
    l_hip = pelvis + np.array([-0.09, -LENGTHS[('pelvis','l_hip')]])

    # legs: bending for squatting, then extending for take-off/air
    squat = 0.9 - 0.7 * s(pi * jump_phase) ** 2 * heavy_factor
    ext = (pi/2) * (jump_phase - 0.5) * 1.3
    # right leg
    r_thigh_ang = pi * 5/4 + 0.19 * squat + 0.25*ext
    r_knee = r_hip + LENGTHS[('r_hip','r_knee')]*np.array([c(r_thigh_ang), s(r_thigh_ang)])
    r_calf_ang = pi + 0.64 * squat + 0.28*ext
    r_ankle = r_knee + LENGTHS[('r_knee','r_ankle')]*np.array([c(r_calf_ang), s(r_calf_ang)])

    # left leg
    l_thigh_ang = pi * 3/4 - 0.19 * squat - 0.25*ext
    l_knee = l_hip + LENGTHS[('l_hip','l_knee')]*np.array([c(l_thigh_ang), s(l_thigh_ang)])
    l_calf_ang = pi - 0.64 * squat - 0.28*ext
    l_ankle = l_knee + LENGTHS[('r_knee','r_ankle')]*np.array([c(l_calf_ang), s(l_calf_ang)])
    
    points = [
        head,           #0
        neck,           #1
        r_shoulder,     #2
        l_shoulder,     #3
        chest,          #4
        r_elbow,        #5
        l_elbow,        #6
        r_wrist,        #7
        l_wrist,        #8
        pelvis,         #9
        r_hip,          #10
        l_hip,          #11
        r_knee,         #12
        l_knee,         #13
        r_ankle,        #14
        #l_ankle is omitted for 15 lights
    ]
    return np.array(points)

# Animation parameters
FPS = 50
CYCLE_SEC = 1.6
FRAMES = int(CYCLE_SEC * FPS)

def get_all_frames():
    # Returns an array of frames: shape [frames, points, 2]
    all_frames = []
    for f in range(FRAMES):
        phase = (f / FRAMES) % 1.0                  # phase in [0,1)
        pts = happyman_skeleton(phase, heavy_factor=1.13)
        all_frames.append(pts)
    arr = np.stack(all_frames, axis=0)
    # Center horizontally (so the jumping is more up-n-down)
    arr[:,:,0] -= np.mean(arr[:,:,0])
    # Shift so bottoms are always at y=0.1 in display
    min_y = arr[:,:,1].min()
    arr[:,:,1] += 0.1 - min_y
    return arr

frames = get_all_frames()

# --- Matplotlib Animation ---

fig = plt.figure(figsize=(3.2, 5.4))
ax = fig.add_subplot(111)
plt.axis('off')
ax.set_facecolor("black")
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(0, 2.4)
# Frame color: white points
sc = ax.scatter([], [], s=82, c='white', edgecolors='none')

def init():
    sc.set_offsets(np.zeros((15,2)))
    return (sc,)

def animate(i):
    pts = frames[i%FRAMES]
    sc.set_offsets(pts)
    return (sc,)

ani = animation.FuncAnimation(
    fig, animate, frames=FRAMES, interval=1000//FPS, blit=True, init_func=init)

plt.show()
