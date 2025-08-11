
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Point-light marker indices
# 0: head, 1: rshoulder, 2: lshoulder, 3: chest, 4: relb, 5: lelb,
# 6: rhip, 7: lhip, 8: rwr, 9: lwr, 10: pelvis,
# 11: rknee, 12: lknee, 13: rankle, 14: lankle
# (standard: 2-head, 2-shoulder, chest, 2-elbow, 2-hip, pelvis, 2-wrist, 2-knee, 2-ankle = 15)

def sad_walk_cycle(t, step_len=40, hip_height=110, sad_drop=10, weight_drag=12):
    # Phase: t in [0, 1]. One cycle of walking.
    # Simulate a sad woman with heavy weight:
    # - Shoulders/cervical/arms slightly slumped (shoulders lower, head forward-down) 
    # - Steps are slow, swing less, upper body drags a bit behind lower
    # - Foot swing doesn't rise high
    # - Arms swing less
    # - General vertical drop (sad drag)
    # - Slight forward lean of upper body (chest, head)
    #
    # Skeleton model (2D side view, walking left-to-right along x)
    # Horizontal movement = walking; vertical = step/hip oscillation
    #
    # t: 0...1 (phase)
    
    # Body joint positions (x, y)
    # Body parameters
    head_radius = 13
    shoulderwidth = 24
    hipwidth = 18
    upper = 33
    lower = 32
    arm = 24
    forearm = 23
    # stride variables
    hip_stride = step_len
    foot_stride = 1.5 * step_len
    arm_swing = 0.46 * step_len
    arm_drop = 10 # arms are heavy
    # Shoulders slouch
    shoulder_drop = 9 + sad_drop
    head_drop = 10 + sad_drop
    head_forward = 3
    torsodepth = 9

    # Pelvis oscillation (walking)
    hip_y = hip_height - sad_drop - 4*np.abs(np.sin(np.pi*t))
    # vertical bob: lower at midstance for a sad, weighted walk
    vertical_bob = -weight_drag * np.sin(2*np.pi*t)**2

    # Hips
    pelvis_x = hip_stride * t

    # Pelvis angle: small
    pelvis_angle = 4 * np.sin(2 * np.pi * t + np.pi)
    # Shoulders: move less, lower
    shoulders_y = hip_y + upper - shoulder_drop

    # Head: further dropped/forward
    head_y = shoulders_y + head_radius - head_drop
    head_x = pelvis_x + head_forward
    # Shoulders, chest, hips keypoints
    right_sh_x = pelvis_x + shoulderwidth/2
    left_sh_x = pelvis_x - shoulderwidth/2
    chest_x = pelvis_x
    chest_y = shoulders_y - (upper * 0.44)
    right_hip_x = pelvis_x + hipwidth/2 * np.cos(np.radians(pelvis_angle))
    left_hip_x = pelvis_x - hipwidth/2 * np.cos(np.radians(pelvis_angle))
    hip_y_point = hip_y

    # Arms swing: smaller and slower, less high
    l_arm_phase = np.pi/10 + np.sin(2*np.pi*t) # Out of phase w/ legs
    r_arm_phase = np.pi/10 - np.sin(2*np.pi*t)

    la_x = left_sh_x - arm * np.sin(0.7*np.pi * np.sin(2*np.pi*t))
    la_y = shoulders_y - arm + arm_drop * np.abs(np.sin(2*np.pi*t))
    ra_x = right_sh_x + arm * np.sin(0.7*np.pi * np.sin(2*np.pi*t))
    ra_y = shoulders_y - arm + arm_drop * np.abs(np.cos(2*np.pi*t))

    # Elbows: bent
    # (Elbow: 2/3 upper-arm away from shoulder in direction of wrist, but raised less)
    r_elb_x = right_sh_x + 0.6 * arm * np.sin(r_arm_phase)
    r_elb_y = shoulders_y - 0.75 * arm + (arm_drop/2) * np.abs(np.cos(2*np.pi*t))
    l_elb_x = left_sh_x - 0.6 * arm * np.sin(l_arm_phase)
    l_elb_y = shoulders_y - 0.75 * arm + (arm_drop/2) * np.abs(np.sin(2*np.pi*t))

    # Wrists
    r_wrist_x = right_sh_x + arm * np.sin(r_arm_phase) * 0.92
    r_wrist_y = shoulders_y - arm * 0.93 + arm_drop * np.abs(np.cos(2*np.pi*t))
    l_wrist_x = left_sh_x - arm * np.sin(l_arm_phase) * 0.92
    l_wrist_y = shoulders_y - arm * 0.93 + arm_drop * np.abs(np.sin(2*np.pi*t))

    # Pelvis "center"
    pelvis_pt_x = pelvis_x
    pelvis_pt_y = hip_y

    # Knees, Ankles positions (legs)
    stride_angle = np.pi/9 # legs never fully extended
    # Gait phase: left lead (t=0), right lead (t=0.5)
    l_stride = -foot_stride/2 * np.sin(2*np.pi*t)
    r_stride =  foot_stride/2 * np.sin(2*np.pi*t)

    # Both knees below hip in y (walking step arc)
    knee_l_x = left_hip_x + l_stride * 0.37
    knee_r_x = right_hip_x + r_stride * 0.37
    knee_l_y = hip_y - lower + 12 * np.abs(np.sin(2 * np.pi * t))
    knee_r_y = hip_y - lower + 12 * np.abs(np.sin(2 * np.pi * (t+0.5)))

    # Ankles
    angle_factor = 0.92 # feet don't lift high because "heavy"
    lame_foot_lift = 6 * np.maximum(0, np.sin(2*np.pi*t))
    lame_foot_rise = 6 * np.maximum(0, np.sin(2*np.pi*(t+0.5)))

    l_ankle_x = left_hip_x + l_stride
    l_ankle_y = hip_y - lower - lower + lame_foot_lift

    r_ankle_x = right_hip_x + r_stride
    r_ankle_y = hip_y - lower - lower + lame_foot_rise

    # Compose joint positions [x, y]
    joints = [
        [head_x, head_y + vertical_bob],                    # 0 head
        [right_sh_x, shoulders_y + vertical_bob],           # 1 right shoulder
        [left_sh_x, shoulders_y + vertical_bob],            # 2 left shoulder
        [chest_x, chest_y + vertical_bob],                  # 3 chest (neck base)
        [r_elb_x, r_elb_y + vertical_bob],                  # 4 right elbow
        [l_elb_x, l_elb_y + vertical_bob],                  # 5 left elbow
        [right_hip_x, hip_y_point + vertical_bob],          # 6 right hip
        [left_hip_x, hip_y_point + vertical_bob],           # 7 left hip
        [r_wrist_x, r_wrist_y + vertical_bob],              # 8 right wrist
        [l_wrist_x, l_wrist_y + vertical_bob],              # 9 left wrist
        [pelvis_pt_x, pelvis_pt_y + vertical_bob],          # 10 pelvis (center)
        [knee_r_x, knee_r_y + vertical_bob],                # 11 right knee
        [knee_l_x, knee_l_y + vertical_bob],                # 12 left knee
        [r_ankle_x, r_ankle_y + vertical_bob],              # 13 right ankle
        [l_ankle_x, l_ankle_y + vertical_bob],              # 14 left ankle
    ]
    return np.array(joints)

# ============= Animation setup ==============

# Visual settings
BG_COLOR = 'black'
FG_COLOR = 'white'
DOT_SIZE = 85

# Animation parameters
frames = 80
duration = 2.0  # seconds
fps = int(frames/duration)
times = np.linspace(0, 1, frames)

# x offset for horizontal movement
XR = (0, 160)
YR = (0, 235)

# Animation function
def gen_walk_frames():
    for t in times:
        pts = sad_walk_cycle(t)
        yield pts

fig, ax = plt.subplots(figsize=(3.6, 5.0))
ax.set_facecolor(BG_COLOR)
fig.patch.set_facecolor(BG_COLOR)
plt.xlim(XR)
plt.ylim(YR)
plt.gca().set_aspect('equal')
plt.axis('off')

# Initial points
points = sad_walk_cycle(0)
sc = ax.scatter(points[:,0], points[:,1], s=DOT_SIZE, edgecolors='none', color=FG_COLOR)

def update(frame):
    pts = sad_walk_cycle(frame)
    sc.set_offsets(pts)
    return sc,

ani = animation.FuncAnimation(
    fig,
    update, 
    frames=[sad_walk_cycle(t) for t in times],
    interval=1000/fps,
    blit=True,
    repeat=True
)

plt.show()
