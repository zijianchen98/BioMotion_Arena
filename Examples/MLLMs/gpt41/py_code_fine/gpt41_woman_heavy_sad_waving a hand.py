
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 15 point marker order: 
# [Head, Neck, RShoulder, LShoulder, RElbow, LElbow, RWrist, LWrist, Chest, Abdomen, RHip, LHip, RKnee, LKnee, RFoot, LFoot]
# We'll adjust to 15: Head, Neck, RShoulder, LShoulder, RElbow, LElbow, RWrist, LWrist, Chest, Hip, RKnee, LKnee, RFoot, LFoot, (Heavy object)

# Basic skeleton proportions (relative units)
# y = down, x = right
SKELETON = {
    "Head":        (0,    1.7),
    "Neck":        (0,    1.55),
    "Chest":       (0,    1.4),
    "RShoulder":   (0.22, 1.48),
    "LShoulder":   (-0.22,1.48),
    "RElbow":      (0.42, 1.15),
    "LElbow":      (-0.42,1.15),
    "RWrist":      (0.65,  0.85),
    "LWrist":      (-0.38, 0.53),
    "Hip":         (0,    1.05),
    "RHip":        (0.13, 1.05),
    "LHip":        (-0.13,1.05),
    "RKnee":       (0.17, 0.56),
    "LKnee":       (-0.17,0.56),
    "RFoot":       (0.18, 0.09),
    "LFoot":       (-0.18,0.09),
    "Object":      (0.72, 0.95), # heavy object in right hand
}

# marker order for plotting
MARKERS = ["Head", "Neck", "RShoulder", "LShoulder", "RElbow", "LElbow", "RWrist", "LWrist",
           "Chest", "Hip", "RKnee", "LKnee", "RFoot", "LFoot", "Object"]

# Sad pose bias: head & shoulders slightly drooped
def sad_pose_offsets():
    """Returns per-joint y-offsets for 'sad' effect."""
    return {
        "Head":      -0.07,
        "Neck":      -0.03,
        "Chest":     -0.01,
        "RShoulder": -0.03,
        "LShoulder": -0.03,
        "RElbow":    0.00,
        "LElbow":    0.00,
        "RWrist":    0.00,
        "LWrist":    0.00,
        "Hip":       -0.01,
        "RHip":      -0.01,
        "LHip":      -0.01,
        "RKnee":     0.00,
        "LKnee":     0.00,
        "RFoot":     0.00,
        "LFoot":     0.00,
        "Object":    0.00,
    }

def get_frame_positions(t):
    """
    Generate the 2D positions of all points at time t (seconds).
    Hand-wave in sad, heavy motion (slow, arm not high, weighted object in right hand).
    """
    # Parameters of movement
    freq = 0.7      # waving frequency, slower for "heavy"
    wave_angle_amp = np.deg2rad(27) # smaller amplitude for heavy weight
    shoulder_angle = np.deg2rad(12) # arm raised modestly sideways, not over head
    
    # sadness: overall down/bowed
    offsets = sad_pose_offsets()
    base = {}
    for k, (x,y) in SKELETON.items():
        by = y + offsets.get(k,0)
        # Bias x for heavier body: a bit wider
        if "Shoulder" in k or "Elbow" in k or "Hip" in k:
            bx = x*1.15
        elif "Wrist" in k:
            bx = x*1.25
        elif "Foot" in k or "Knee" in k:
            bx = x*1.18
        else:
            bx = x
        base[k] = np.array([bx, by])
    
    # Animate right arm ("waving" with heavy object in hand)
    # The waving is a slow pendulum-like up/down, with the forearm and wrist swinging more than upper arm
    shoulder = base["RShoulder"]
    upperarm_L = np.linalg.norm(base["RElbow"]-base["RShoulder"])
    forearm_L = np.linalg.norm(base["RWrist"]-base["RElbow"])
    
    # Compute arm angles
    # The shoulder does a small up-down circular arc (sagittal + a bit frontal)
    sh_theta = shoulder_angle + 0.10*np.sin(2*np.pi*freq*t) # shoulder, mild up/down swing
    # The elbow bends a bit more with each wave down (simulate strain)
    wave_phase = np.sin(2*np.pi*freq*t)
    elbow_theta = np.deg2rad(34) + (0.38*wave_angle_amp)*(1-wave_phase) # flex more as hand comes down
    # Forearm swings, but max is below horizontal due to heavy object
    wave_phi = -wave_angle_amp*wave_phase # main waving angle

    # Shoulder position
    shoulder_pos = base["RShoulder"]
    # Elbow position
    elbow_pos = shoulder_pos + upperarm_L * np.array([
        np.cos(sh_theta), -np.sin(sh_theta)
    ])
    # Wrist position: forearm swings relative to elbow
    total_angle = sh_theta + elbow_theta + wave_phi # heavy, not full extension
    wrist_pos = elbow_pos + forearm_L * np.array([
        np.cos(total_angle), -np.sin(total_angle)
    ])
    # Heavy object follows the wrist ("hangs" heavy)
    object_pos = wrist_pos + 0.095 * np.array([np.cos(total_angle-np.pi/2), -np.sin(total_angle-np.pi/2)])

    # Left arm: down, loose (sad, not waving)
    lshoulder = base["LShoulder"]
    lelb_x = lshoulder[0] - 0.17
    lelb_y = lshoulder[1] - 0.33
    lwri_x = lelb_x - 0.09
    lwri_y = lelb_y - 0.23

    # Joints array for all markers
    joints = {
        **base,
        "RElbow": elbow_pos,
        "RWrist": wrist_pos,
        "Object": object_pos,
        "LElbow": np.array([lelb_x, lelb_y]),
        "LWrist": np.array([lwri_x, lwri_y]),
    }

    # Sway: gentle vertical bob of whole body
    bob = -0.01*np.sin(2*np.pi*freq*t+np.pi/2)
    for k in joints:
        joints[k] = np.array([joints[k][0], joints[k][1]+bob])
    
    # Heads: slight turn and droop for "sad"
    th = np.deg2rad(-14)
    head_n = joints["Neck"]
    r = np.linalg.norm(joints["Head"]-head_n)
    joints["Head"] = head_n + np.array([
        0.0 + r*np.sin(th),
        r*np.cos(th),
    ])
    return np.vstack([joints[k] for k in MARKERS])

# --- Animation code starts here ---
fig, ax = plt.subplots(figsize=(4,7))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')

# get bounds for the view
all_pts = np.array([SKELETON[k] for k in SKELETON])
mx = np.max(np.abs(all_pts[:,0]))+0.3
my = np.max(all_pts[:,1])+0.18
ay_min = np.min(all_pts[:,1])-0.2

ax.set_xlim(-mx, mx)
ax.set_ylim(ay_min, my)

points, = ax.plot([], [], 'wo', markersize=9) # main point-lights

def init():
    points.set_data([], [])
    return (points,)

def update(frame):
    t = frame/30 # 30 fps
    xy = get_frame_positions(t)
    points.set_data(xy[:,0], xy[:,1])
    return (points,)

anim = FuncAnimation(
    fig, update, init_func=init, frames=180, interval=1000/30, blit=True
)

plt.show()
