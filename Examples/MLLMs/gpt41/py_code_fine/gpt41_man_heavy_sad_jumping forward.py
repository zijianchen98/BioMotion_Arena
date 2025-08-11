
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------ PARAMETERS ------------------
# Coordinates (x,y) layout in head-toe order
# 15 points: [Head, Neck, RShoulder, LShoulder, RElbow, LElbow, RWrist, LWrist,
# Chest, Pelvis, RHip, LHip, RKnee, LKnee, RAnkle, LAnkle] (combined for simplicity)
# We'll use:
# 0: Head
# 1: Neck
# 2: R Shoulder
# 3: L Shoulder
# 4: R Elbow
# 5: L Elbow
# 6: R Wrist
# 7: L Wrist
# 8: Chest
# 9: Pelvis
#10: R Hip
#11: L Hip
#12: R Knee
#13: L Knee
#14: R Ankle
#15: L Ankle
# But we need exactly 15, so let's merge chest and pelvis
# 0: Head, 1: Neck, 2: R Shoulder, 3: L Shoulder, 4: R Elbow, 5: L Elbow,
# 6: R Wrist, 7: L Wrist, 8: Spine (chest/pelvis), 9: R Hip, 10: L Hip,
# 11: R Knee, 12: L Knee, 13: R Ankle, 14: L Ankle

# ------------------ MOTION GENERATION ------------------

# Define skeleton proportions (relative)
SKELETON = {
    "head_neck": 20,
    "neck_shoulder": 15,
    "shoulder_elbow": 20,
    "elbow_wrist": 20,
    "neck_spine": 20,
    "spine_hip": 20,
    "spine_offset": 0,    # for curving the spine
    "hip_knee": 30,
    "knee_ankle": 30,
    "hip_offset_x": 10,   # horizontal offset of each hip from spine
    "shoulder_offset_x": 15
}

# Initialise the base pose, facing right, standing vertical
def base_skeleton(x0=0, y0=0, lean=0.0):
    """Returns a [15,2] array of point coordinates"""
    sk = SKELETON
    # Core positions (y increases up)
    neck = np.array([x0, y0])
    head = neck + np.array([0, sk['head_neck']])
    spine = neck + np.array([0, -sk['neck_spine']])
    pelvis = spine + np.array([0, -sk['spine_hip']])
    # Shoulders
    r_shoulder = neck + np.array([sk["shoulder_offset_x"], 0])
    l_shoulder = neck + np.array([-sk["shoulder_offset_x"], 0])
    # Elbows
    r_elbow = r_shoulder + np.array([sk["shoulder_elbow"]*np.cos(np.pi/8+lean), 
                                     -sk["shoulder_elbow"]*np.sin(np.pi/8+lean)])
    l_elbow = l_shoulder + np.array([-sk["shoulder_elbow"]*np.cos(np.pi/8-lean), 
                                     -sk["shoulder_elbow"]*np.sin(np.pi/8-lean)])
    # Wrists
    r_wrist = r_elbow + np.array([sk["elbow_wrist"]*np.cos(np.pi/5+lean), 
                                  -sk["elbow_wrist"]*np.sin(np.pi/5+lean)])
    l_wrist = l_elbow + np.array([-sk["elbow_wrist"]*np.cos(np.pi/5-lean), 
                                  -sk["elbow_wrist"]*np.sin(np.pi/5-lean)])
    # Hips
    r_hip = pelvis + np.array([sk["hip_offset_x"], 0])
    l_hip = pelvis + np.array([-sk["hip_offset_x"], 0])
    # Knees (straight under hips to start)
    r_knee = r_hip + np.array([0, -sk["hip_knee"]])
    l_knee = l_hip + np.array([0, -sk["hip_knee"]])
    # Ankles (straight under knees)
    r_ankle = r_knee + np.array([0, -sk["knee_ankle"]])
    l_ankle = l_knee + np.array([0, -sk["knee_ankle"]])

    # Assemble into [15,2]
    points = np.array([
        head,             # 0
        neck,             # 1
        r_shoulder,       # 2
        l_shoulder,       # 3
        r_elbow,          # 4
        l_elbow,          # 5
        r_wrist,          # 6
        l_wrist,          # 7
        spine,            # 8
        r_hip,            # 9
        l_hip,            # 10
        r_knee,           # 11
        l_knee,           # 12
        r_ankle,          # 13
        l_ankle           # 14
    ])
    return points

def sad_head_neck(base_points, f):
    """Sad: lower head tilt for sadness"""
    p = base_points.copy()
    # Head droop / tilt down
    dx = 0
    dy = -5 - 5*np.sin(np.pi*f)
    p[0] += [dx, dy]
    return p

def arms_heavy_down(base_points, f):
    """Lower, heavy arms, for carrying weight. Some sway."""
    p = base_points.copy()
    # Dampen amplitude for sadness and weight
    sway = 8*np.sin(2*np.pi*f)    # gentle sway left/right
    # Both wrists move lower and a bit forward
    p[6] += [7 + sway/2, -10]   # right wrist
    p[7] += [-7 + sway/2, -10]  # left wrist
    p[4] += [3, -6]             # right elbow
    p[5] += [-3, -6]            # left elbow
    return p

def legs_jump_forward(base_points, f):
    """Simulate realistic leg motion for jump forward, with sadness/strain."""
    p = base_points.copy()
    # f in [0,1]; 
    # Forwards jump: legs bend before takeoff, straighten midair, bend at landing
    # Divide jump: crouch (0.0-0.2), takeoff (0.2-0.4), flight (0.4-0.7), land (0.7-1.0)
    # Heavy weight: less lift, more knee bend, smaller stride
    takeoff_y = 15
    forward_x = 35
    jump_phase = f
    # Stages: crouch-down, takeoff-up, airborne, landing
    if jump_phase < 0.20:  # crouch
        c = jump_phase / 0.20
        # knees/ankles move forward, body sags
        knee_offset = 10*c
        ankle_offset = 7*c
        pelvis_drop = 7*c
        # Hips & spine lower a bit, knees/ankles move forward
        p[9:11] += [2*c, -pelvis_drop]
        p[11] += [knee_offset, 0]
        p[12] += [knee_offset, 0]
        p[13] += [ankle_offset, 0]
        p[14] += [ankle_offset, 0]
        p[8] += [0, -pelvis_drop]
    elif jump_phase < 0.40: # takeoff
        c = (jump_phase-0.20)/0.20
        # legs start to straighten, body launches
        knee_offset = 10*(1-c)
        ankle_offset = 7*(1-c)
        pelvis_drop = 7*(1-c)
        p[9:11] += [2*(1-c), -pelvis_drop]
        p[11] += [knee_offset, 0]
        p[12] += [knee_offset, 0]
        p[13] += [ankle_offset, 0]
        p[14] += [ankle_offset, 0]
        # upward and forward motion begins
        dy = takeoff_y * c
        dx = forward_x*0.2 * c
        p += [dx, dy]
    elif jump_phase < 0.70: # airborne
        c = (jump_phase-0.40)/0.30
        # legs straightened, body lifted
        dx = forward_x*(0.2 + 0.7*c)
        t = np.pi*(1 + c)/2   # peak then descend (for sadness, not too high/athletic)
        # Parabola: up and down
        dy = takeoff_y*np.sin(t)
        p += [dx, dy]
    else: # landing
        c = (jump_phase-0.70)/0.30
        # Land: body comes down, knees bend on impact, stride continues forward
        dx = forward_x*(0.9 + 0.1*c)
        dy = takeoff_y*(1-c)
        pelvis_drop = 4*c
        knee_offset = 4*c
        ankle_offset = 3*c
        p[9:11] += [1.5*c, -pelvis_drop]
        p[11] += [knee_offset, 0]
        p[12] += [knee_offset, 0]
        p[13] += [ankle_offset, 0]
        p[14] += [ankle_offset, 0]
        p[8] += [0, -pelvis_drop]
        p += [dx, dy]
    return p

def anim_sad_jump_forward(f, base_x=0, base_y=80):
    """Returns shape [15,2] for normalized phase f in [0,1)"""
    # Subtle body lean for sad/weight
    base_pts = base_skeleton(base_x, base_y, lean=-0.08 + -0.04*np.cos(2*np.pi*f))
    # Head droop, arms heavy, legs jump
    pts = sad_head_neck(base_pts, f)
    pts = arms_heavy_down(pts, f)
    pts = legs_jump_forward(pts, f)
    return pts

# ------------ ANIMATION SETUP ----------

n_frames = 60
duration = 2.0  # seconds
pointsize = 64  # Large dots for example
W, H = 200, 220 # Figure size (pixels)

fig, ax = plt.subplots(figsize=(W/100,H/100), facecolor=(0,0,0))
plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-40,120)
ax.set_ylim(-30,190)

scat = ax.scatter([], [], s=pointsize, c='white', edgecolors='none')

def init():
    scat.set_offsets([])
    return (scat,)

def animate(i):
    phase = (i % n_frames) / n_frames
    pts = anim_sad_jump_forward(phase)
    scat.set_offsets(pts)
    return (scat,)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=n_frames,
    interval=duration*1000/n_frames,
    blit=True,
    repeat=True,
    init_func=init
)

plt.show()
