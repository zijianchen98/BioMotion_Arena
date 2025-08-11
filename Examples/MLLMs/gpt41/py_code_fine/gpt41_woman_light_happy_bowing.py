
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint indices and names
#             0       1        2       3      4     5     6        7        8        9       10      11     12    13    14
joint_names = ["Head", "LShoulder", "RShoulder", "LElbow", "RElbow", "LWrist", "RWrist", "Hip", "LHip", "RHip", "LKnee", "RKnee", "LAnkle", "RAnkle", "Chest"]

# Human joint structure for 15 markers
# This array assigns markers to anatomical positions:
# 0: Head, 1: LShoulder, 2: RShoulder, 3: LElbow, 4: RElbow, 5: LWrist, 6: RWrist, 7: Hip(center), 8: LHip, 9: RHip, 10: LKnee, 11: RKnee, 12: LAnkle, 13: RAnkle, 14: Chest

# Helper function: Generate the skeleton in a canonical pose
def canonical_pose():
    # We'll use (x, y) in a 1x2 array for each point. Units are arbitrary.
    pose = np.zeros((15, 2))
    # Torso base positions
    torso_x = 0.0
    hip_y = 0.0
    shoulder_y = 2.0
    chest_y = 2.5
    head_y = 3.2
    
    # Hip center
    pose[7]  = [torso_x, hip_y]
    # Chest & shoulders
    pose[14] = [torso_x, chest_y]
    pose[1]  = [torso_x-0.33, shoulder_y] # LShoulder
    pose[2]  = [torso_x+0.33, shoulder_y] # RShoulder
    # Head
    pose[0]  = [torso_x, head_y]
    # Elbows
    pose[3]  = [torso_x-0.55, shoulder_y-0.42] # LElbow
    pose[4]  = [torso_x+0.55, shoulder_y-0.42] # RElbow
    # Wrists
    pose[5]  = [torso_x-0.8, shoulder_y-0.85]  # LWrist
    pose[6]  = [torso_x+0.8, shoulder_y-0.85]  # RWrist
    # LHip/RHip
    pose[8]  = [torso_x-0.20, hip_y]
    pose[9]  = [torso_x+0.20, hip_y]
    # Knees
    pose[10] = [torso_x-0.19, hip_y-1.08] # LKnee
    pose[11] = [torso_x+0.19, hip_y-1.08] # RKnee
    # Ankles
    pose[12] = [torso_x-0.17, hip_y-2.0] # LAnkle
    pose[13] = [torso_x+0.17, hip_y-2.0] # RAnkle
    return pose

# Key points of bowing motion: 
# 0: standing upright, 1: bow start, 2: bow deep, 3: bow recover.
def bow_pose(phase):
    """Return 15x2 array of joint positions for bow at phase [0,1]."""
    # We'll interpolate between upright and full bow
    upright = canonical_pose()
    bow = canonical_pose()
    
    # Bowing: torso and head pitch forward, hips move back, knees bend, arms at side, wrists near thighs.
    # We'll pitch torso + head by about 55deg (full bow), knees bend to ~30deg, hips move slightly back.
    theta = np.deg2rad(phase * 55.0)  # torso-head pitch angle
    
    # Move hips backward and downward for realism
    hip_shift_x = -0.08 * phase
    hip_shift_y = -0.07 * phase
    
    # Torso vector: from hip to chest
    torso = upright[14] - upright[7]
    torso_len = np.linalg.norm(torso)
    # New torso vector, pitched
    torso_rot = np.array([np.sin(theta), np.cos(theta)]) * torso_len
    bow[7] = upright[7] + [hip_shift_x, hip_shift_y]  # New hip
    bow[14] = bow[7] + torso_rot                    # New chest
    
    # Shoulders: rotate with torso
    sh_offset = upright[1] - upright[14]  # Shoulder relative to chest (L)
    sh_rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                              [np.sin(theta),  np.cos(theta)]])
    bow[1] = bow[14] + sh_rot_matrix @ sh_offset          # LShoulder
    sh_offset_r = upright[2] - upright[14]
    bow[2] = bow[14] + sh_rot_matrix @ sh_offset_r        # RShoulder
    
    # Head: rotate same as chest, offset from chest
    head_offset = upright[0] - upright[14]
    bow[0] = bow[14] + sh_rot_matrix @ head_offset
    
    # Arms: Hang arms, elbows and wrists lower and forward with torso
    fe = 0.7*phase   # elbow flexion amount (increases as bow deepens)
    arm_theta = theta + np.deg2rad(min(45*fe, 35))  # arms a bit more forward
    upper_arm_len = np.linalg.norm(upright[3] - upright[1])
    forearm_len = np.linalg.norm(upright[5] - upright[3])
    # Left arm
    bow[3] = bow[1] + np.array([np.sin(arm_theta), -np.cos(arm_theta)]) * upper_arm_len  # LElbow
    bow[5] = bow[3] + np.array([np.sin(arm_theta+0.25), -np.cos(arm_theta+0.25)]) * forearm_len # LWrist
    # Right arm (mirror)
    bow[4] = bow[2] + np.array([np.sin(arm_theta), -np.cos(arm_theta)]) * upper_arm_len  # RElbow
    bow[6] = bow[4] + np.array([np.sin(arm_theta+0.25), -np.cos(arm_theta+0.25)]) * forearm_len # RWrist

    # Hips
    hips_width = np.linalg.norm(upright[8] - upright[9])
    bow[8] = bow[7] + [-hips_width/2, 0]       # LHip
    bow[9] = bow[7] + [hips_width/2, 0]        # RHip
    
    # Knees/ankles: knees bend as bow deepens
    knee_deg = 15 + 25*phase
    knee_theta = np.deg2rad(knee_deg)
    upper_leg_len = np.linalg.norm(upright[10] - upright[8])
    lower_leg_len = np.linalg.norm(upright[12] - upright[10])
    # LKnee and RKnee (forward with bow, down)
    bow[10] = bow[8] + [np.sin(knee_theta)*upper_leg_len, -np.cos(knee_theta)*upper_leg_len]
    bow[11] = bow[9] + [np.sin(knee_theta)*upper_leg_len, -np.cos(knee_theta)*upper_leg_len]
    # LAnkle and RAnkle
    ankle_theta = np.deg2rad(80 - 40*phase)
    bow[12] = bow[10] + [np.sin(ankle_theta)*lower_leg_len, -np.cos(ankle_theta)*lower_leg_len]
    bow[13] = bow[11] + [np.sin(ankle_theta)*lower_leg_len, -np.cos(ankle_theta)*lower_leg_len]
    
    return bow

# Animation function
def animate_func(num, pts, scat):
    # num ranges 0 to nframes-1; make smooth bow motion (down and up)
    cycle = num / nframes
    if cycle < 0.5:  # bowing
        phase = cycle*2
    else:            # recovering
        phase = 2 - cycle*2
    pose = bow_pose(phase)
    scat.set_offsets(pose)
    return [scat]

# Animation parameters
nframes = 80
fps = 30

# Create figure
fig, ax = plt.subplots(figsize=(4, 7), facecolor='black')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.5, 4)

# Initial points
pts = canonical_pose()
scat = ax.scatter(pts[:,0], pts[:,1], c='white', s=54, edgecolors='white', linewidths=0, zorder=10)

# Animate
ani = animation.FuncAnimation(fig, animate_func, fargs=(pts, scat),
                             frames=nframes, interval=1000//fps, blit=True)

plt.show()
