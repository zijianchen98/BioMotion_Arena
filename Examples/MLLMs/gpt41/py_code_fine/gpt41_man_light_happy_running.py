
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint indices
# 0: Head
# 1: R Shoulder
# 2: L Shoulder
# 3: Chest
# 4: R Elbow
# 5: L Elbow
# 6: Pelvis
# 7: R Hip
# 8: L Hip
# 9: R Wrist
# 10: L Wrist
# 11: R Knee
# 12: L Knee
# 13: R Ankle
# 14: L Ankle

# Limb lengths (relative)
l_head_neck = 0.2
l_neck_shoulder = 0.2
l_shoulder_chest = 0.12
l_chest_pelvis = 0.22
l_shoulder_elbow = 0.22
l_elbow_wrist = 0.22
l_pelvis_hip = 0.11
l_hip_knee = 0.33
l_knee_ankle = 0.33

# Speed and gait-cycle params for running
period = 50  # frames per cycle
fps = 30

def get_joint_positions(frame_idx):
    # Parameters for running gait
    t = (frame_idx % period) / period * 2 * np.pi  # 0 to 2pi over cycle
    
    # Trunk
    pelvis_x = 0
    pelvis_y = 0
    trunk_sway = 0.08 * np.sin(2*t)  # trunk sways while running
    trunk_bob = 0.10 * np.sin(t)     # up/down
    chest_y = pelvis_y + l_chest_pelvis + trunk_bob
    chest_x = pelvis_x + trunk_sway

    head_y = chest_y + l_head_neck
    head_x = chest_x

    # Shoulders
    sh_sway = 0.11 * np.sin(2*t)
    r_sh_x = chest_x + sh_sway
    l_sh_x = chest_x - sh_sway
    r_sh_y = chest_y
    l_sh_y = chest_y

    # Hips
    hip_sway = 0.09 * np.sin(2*t)
    r_hip_x = pelvis_x + hip_sway
    l_hip_x = pelvis_x - hip_sway
    r_hip_y = pelvis_y
    l_hip_y = pelvis_y

    # Arms: Opposing phase to legs
    # Upper arms swing out-of-phase w/ legs
    arm_swing = 0.6 * np.sin(t)
    # Forearm swing
    elb_wave_r = 0.5 * np.sin(t + 0.8)
    elb_wave_l = 0.5 * np.sin(t - 0.8)
    # Wrists
    wrist_wave_r = 0.35 * np.sin(t + 1.2)
    wrist_wave_l = 0.35 * np.sin(t - 1.2)

    # Right arm
    r_elb_x = r_sh_x + l_shoulder_elbow * np.sin(arm_swing)
    r_elb_y = r_sh_y - l_shoulder_elbow * np.cos(arm_swing)
    r_wrist_x = r_elb_x + l_elbow_wrist * np.sin(arm_swing + elb_wave_r)
    r_wrist_y = r_elb_y - l_elbow_wrist * np.cos(arm_swing + elb_wave_r)
    # Left arm
    l_elb_x = l_sh_x + l_shoulder_elbow * np.sin(-arm_swing)
    l_elb_y = l_sh_y - l_shoulder_elbow * np.cos(-arm_swing)
    l_wrist_x = l_elb_x + l_elbow_wrist * np.sin(-arm_swing + elb_wave_l)
    l_wrist_y = l_elb_y - l_elbow_wrist * np.cos(-arm_swing + elb_wave_l)

    # Legs (running: hip, knee, ankle)
    # Right Leg: forward at t=0
    hip_cycle_r = +0.7 * np.sin(t)
    hip_cycle_l = -0.7 * np.sin(t)

    r_knee_x = r_hip_x + l_hip_knee * np.sin(hip_cycle_r)
    r_knee_y = r_hip_y - l_hip_knee * np.cos(hip_cycle_r)
    r_ankle_x = r_knee_x + l_knee_ankle * np.sin(hip_cycle_r - 0.5*np.sin(t)*np.cos(t))
    r_ankle_y = r_knee_y - l_knee_ankle * np.cos(hip_cycle_r - 0.5*np.sin(t)*np.cos(t))

    # Add a bounce to foot y at low points (mimic running stance phase)
    stance_r = (np.sin(t) > 0)
    if stance_r:
        r_ankle_y += 0.09*(np.abs(np.sin(t))**1.1)

    l_knee_x = l_hip_x + l_hip_knee * np.sin(hip_cycle_l)
    l_knee_y = l_hip_y - l_hip_knee * np.cos(hip_cycle_l)
    l_ankle_x = l_knee_x + l_knee_ankle * np.sin(hip_cycle_l - 0.5*np.sin(t+np.pi)*np.cos(t+np.pi))
    l_ankle_y = l_knee_y - l_knee_ankle * np.cos(hip_cycle_l - 0.5*np.sin(t+np.pi)*np.cos(t+np.pi))

    stance_l = (np.sin(t+np.pi) > 0)
    if stance_l:
        l_ankle_y += 0.09*(np.abs(np.sin(t+np.pi))**1.1)

    # Build point-lights list in order matching the schema above
    points = np.array([
        [head_x, head_y],           # 0 Head
        [r_sh_x, r_sh_y],           # 1 R Shoulder
        [l_sh_x, l_sh_y],           # 2 L Shoulder
        [chest_x, chest_y],         # 3 Chest
        [r_elb_x, r_elb_y],         # 4 R Elbow
        [l_elb_x, l_elb_y],         # 5 L Elbow
        [pelvis_x, pelvis_y],       # 6 Pelvis (center)
        [r_hip_x, r_hip_y],         # 7 R Hip
        [l_hip_x, l_hip_y],         # 8 L Hip
        [r_wrist_x, r_wrist_y],     # 9 R Wrist
        [l_wrist_x, l_wrist_y],     # 10 L Wrist
        [r_knee_x, r_knee_y],       # 11 R Knee
        [l_knee_x, l_knee_y],       # 12 L Knee
        [r_ankle_x, r_ankle_y],     # 13 R Ankle
        [l_ankle_x, l_ankle_y],     # 14 L Ankle
    ])
    # Add leftward movement to mimic running to the right
    move = 0.0125 * frame_idx
    points[:, 0] += move

    return points

# Set up visualization
fig, ax = plt.subplots(figsize=(3,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

def init():
    ax.set_xlim(-1, 2)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    return []

dots, = ax.plot([], [], 'o', color='white', markersize=9)
def animate(i):
    points = get_joint_positions(i)
    dots.set_data(points[:,0], points[:,1])
    return [dots]

init()
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=240, interval=1000//fps, blit=True)

plt.show()
