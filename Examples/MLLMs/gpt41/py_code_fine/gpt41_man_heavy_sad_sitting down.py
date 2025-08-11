
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Body Model: 15 points (labels for clarity) ---
# 0: head
# 1: right shoulder
# 2: left shoulder
# 3: right elbow
# 4: left elbow
# 5: right hand
# 6: left hand
# 7: chest
# 8: hips
# 9: right hip
# 10: left hip
# 11: right knee
# 12: left knee
# 13: right ankle
# 14: left ankle

# The following keypoint skeleton and segment lengths (arbitrary units)
# match the point pattern in the image

# Body segment hierarchy and lengths (in "pixels")
LEN_HEAD = 40
LEN_TORSO = 60
LEN_SHOULDER = 35
LEN_UPPER_ARM = 35
LEN_FOREARM = 30
LEN_HAND = 13
LEN_PELVIS = 35
LEN_UPPER_LEG = 45
LEN_LOWER_LEG = 45
LEN_FOOT = 13

def skeleton_keypoints(params):
    """
    Given angles (shoulder, elbow, hip, knee), return 15 x,y coordinates
    params: dict of all needed joint angles (in radians) and offsets.
    """
    # Unpack params
    # Torso: chest-hip vector angle & offset
    chest_xy = np.array(params["chest_xy"])
    hip_xy = chest_xy + np.array([0, -LEN_TORSO])
    torso_theta = params["torso_theta"]
    
    # Head
    head_xy = chest_xy + np.array([0, LEN_HEAD])
    
    # Shoulders
    right_shoulder = chest_xy + np.array([-LEN_SHOULDER/2, 0])
    left_shoulder = chest_xy + np.array([LEN_SHOULDER/2, 0])
    
    # Hips (pelvis line)
    right_hip = hip_xy + np.array([-LEN_PELVIS/2, 0])
    left_hip = hip_xy + np.array([LEN_PELVIS/2, 0])
    
    # Arms
    # Right arm
    rs = right_shoulder
    re = rs + LEN_UPPER_ARM * np.array([
        np.cos(params["right_shoulder_angle"]), 
        np.sin(params["right_shoulder_angle"])
    ])
    rh = re + LEN_FOREARM * np.array([
        np.cos(params["right_elbow_angle"]),
        np.sin(params["right_elbow_angle"])
    ])
    # Left arm
    ls = left_shoulder
    le = ls + LEN_UPPER_ARM * np.array([
        np.cos(params["left_shoulder_angle"]), 
        np.sin(params["left_shoulder_angle"])
    ])
    lh = le + LEN_FOREARM * np.array([
        np.cos(params["left_elbow_angle"]),
        np.sin(params["left_elbow_angle"])
    ])
    
    # Legs (origin from hips)
    # Right leg
    rhp = right_hip
    rk = rhp + LEN_UPPER_LEG * np.array([
        np.cos(params["right_hip_angle"]), 
        np.sin(params["right_hip_angle"])
    ])
    ra = rk + LEN_LOWER_LEG * np.array([
        np.cos(params["right_knee_angle"]),
        np.sin(params["right_knee_angle"])
    ])
    # Left leg
    lhp = left_hip
    lk = lhp + LEN_UPPER_LEG * np.array([
        np.cos(params["left_hip_angle"]), 
        np.sin(params["left_hip_angle"])
    ])
    la = lk + LEN_LOWER_LEG * np.array([
        np.cos(params["left_knee_angle"]),
        np.sin(params["left_knee_angle"])
    ])
    
    points = [
        head_xy,       # 0: head
        right_shoulder,# 1
        left_shoulder, # 2
        re,            # 3: right elbow
        le,            # 4: left elbow
        rh,            # 5: right hand
        lh,            # 6: left hand
        chest_xy,      # 7: chest
        hip_xy,        # 8: hips center
        right_hip,     # 9: right hip
        left_hip,      # 10: left hip
        rk,            # 11: right knee
        lk,            # 12: left knee
        ra,            # 13: right ankle (foot)
        la,            # 14: left ankle (foot)
    ]
    
    return np.array(points)

# --- Sitting Down Motion Trajectory Generation ---
def sitting_down_motion(frames=60):
    """
    Return a list of 'frames' body keypoints (Nx15x2) embodying
    a heavy, sad, sitting-down biological motion.
    """
    # Setup motion key parameters
    # - The body bends at hips and knees, upper body leans forward when sitting down
    # - Arms hang more, then rest toward lap
    # - All angles in rad; y axis is up
    # - We'll interpolate a sequence between stand and seated posture
    
    motion = []
    for t in np.linspace(0, 1, frames):
        # t in [0,1], 0=stand, 1=sit
        # Torso position: starts high, ends low and forward
        chest_x = 0
        chest_y = 300 - 60 * t  # drop chest
        
        # Torso lean: add more lean as sits down (downward/forward)
        torso_theta = np.deg2rad(-8) * (0.5 + t)
        
        # Hips p/v: stays below chest
        # Arms: from hanging to resting on lap
        arm_down = np.deg2rad(100)  # almost vertical down
        arm_lap = np.deg2rad(60)    # up towards lap
        # interpolate arm swing outward excessively if sad/tired ("heavy")
        right_shoulder_angle = np.pi * 3/2 + (arm_down - arm_lap)*t + np.deg2rad(-13)*t
        left_shoulder_angle = np.pi * 3/2 - (arm_down - arm_lap)*t + np.deg2rad(13)*t
        
        # Wrists: hanging, then go toward lap
        right_elbow_angle = right_shoulder_angle + (np.deg2rad(25) + t*np.deg2rad(-18))
        left_elbow_angle = left_shoulder_angle - (np.deg2rad(25) + t*np.deg2rad(-18))
        
        # Legs:
        # Start: straight standing. End: knees bent, hips flexed.
        hip_start = np.deg2rad(270)
        hip_end = np.deg2rad(270+65)      # sit flexion
        right_hip_angle = hip_start + (hip_end - hip_start)*t
        left_hip_angle = hip_start + (hip_end - hip_start)*t
        
        knee_start = np.deg2rad(270)
        knee_end = knee_start + np.deg2rad(65)   # knee flexion for sitting
        right_knee_angle = knee_start + (knee_end - knee_start)*t
        left_knee_angle = knee_start + (knee_end - knee_start)*t
        
        frame = skeleton_keypoints({
            "chest_xy": (chest_x, chest_y),
            "torso_theta": torso_theta,
            "right_shoulder_angle": right_shoulder_angle,
            "left_shoulder_angle": left_shoulder_angle,
            "right_elbow_angle": right_elbow_angle,
            "left_elbow_angle": left_elbow_angle,
            "right_hip_angle": right_hip_angle,
            "left_hip_angle": left_hip_angle,
            "right_knee_angle": right_knee_angle,
            "left_knee_angle": left_knee_angle,
        })
        # For a "sad, heavy" PLW: slow initial movement, some body slump, head lower
        frame[0,1] -= 8*t**1.5 * 18     # slightly dips the head more as sits
        frame[7,0] -= 12*t**2           # chest slumps forward
        frame[5,1] += 8*t**2            # hands drop a bit more
        frame[6,1] += 8*t**2
        frame[5,0] += 6*t**2            # hands forward from lap
        frame[6,0] += -6*t**2
        motion.append(frame)
    # Loop the motion into return-to-stand (reversed, slower, for realism)
    fwd = motion
    bwd = motion[::-1][:-1]
    all_frames = fwd + bwd
    return all_frames

# --- Visualization (matplotlib animation) ---
frames = sitting_down_motion(frames=30)
dot_size = 36
fig, ax = plt.subplots(figsize=(4,6))
plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

# Black background, remove axes
ax.set_facecolor('black')
ax.set_xlim(-110, 110)
ax.set_ylim(50, 410)
ax.axis('off')
scat = ax.scatter([], [], s=dot_size, c="white", edgecolors='none')

# Optionally, render as circular dots, anti-aliased
for spine in ax.spines.values():
    spine.set_visible(False)

def update(n):
    frame = frames[n]
    scat.set_offsets(frame)
    return scat,

ani = animation.FuncAnimation(
    fig, update, frames=len(frames), interval=36, blit=True, repeat=True)

plt.show()
