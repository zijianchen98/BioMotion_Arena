
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# JOINTS:   0:Head 1:Neck 2:RShoulder 3:LShoulder 4:RElbow 5:LElbow
#           6:RWrist 7:LWrist 8:Torso 9:RHip 10:LHip 11:RKnee
#           12:LKnee 13:RAnkle 14:LAnkle

# Skeleton connections for reference, not drawn (just for biomechanics)
# Pairs: (from, to)
SKELETON = [
    (0, 1), (1,2), (1,3), (2,4), (4,6), (3,5), (5,7), (1,8), (8,9), (8,10),
    (9,11), (11,13), (10,12), (12,14)
]

# "Standing" base posture (biomechanical plausible, facing right, units arbitrary)
POSE_STAND = np.array([
    [ 0,    8 ],    # 0: Head
    [ 0,    7 ],    # 1: Neck
    [ 1,    7 ],    # 2: RShoulder
    [-1,    7 ],    # 3: LShoulder
    [ 1.5,  5.75],  # 4: RElbow
    [-1.5,  5.75],  # 5: LElbow
    [ 2,    4.5 ],  # 6: RWrist
    [-2,    4.5 ],  # 7: LWrist
    [ 0,    5.5 ],  # 8: Torso
    [ 0.7,  4   ],  # 9: RHip
    [-0.7,  4   ],  #10: LHip
    [ 1.1,  2.2 ],  #11: RKnee
    [-1.1,  2.2 ],  #12: LKnee
    [ 1.0,  0 ],    #13: RAnkle
    [-1.0,  0 ],    #14: LAnkle
])

# "Sitting" base posture (body lowered, hips and knees bent, feet forward)
POSE_SIT = np.array([
    [ 0,   8 ],    # 0: Head (little vertical shift)
    [ 0,   7 ],    # 1: Neck
    [ 1,   7 ],    # 2: RShoulder (shoulders drop with body)
    [-1,   7 ],    # 3: LShoulder
    [ 1.1, 6 ],    # 4: RElbow (elbows slightly lower)
    [-1.1, 6 ],    # 5: LElbow
    [ 1.7, 4.5],   # 6: RWrist (hands almost on knees)
    [-1.7, 4.5],   # 7: LWrist
    [ 0,   5.5],   # 8: Torso (lowered)
    [ 0.9, 4.2],   # 9: RHip (hips forward, lower)
    [-0.9, 4.2],   #10: LHip
    [ 2.1, 2.2],   #11: RKnee (knees far forward)
    [-2.1, 2.2],   #12: LKnee
    [ 2,   0.3],   #13: RAnkle (ankles forward, close to knees)
    [-2,   0.3],   #14: LAnkle
])

# KEY CONFIGS: "down" phase weight shift, so ankles and hips move forward, knees bend, torso lowers and leans

def interpolate_pose(pose1, pose2, t):
    """Smooth interpolation between two poses."""
    return (1-t)*pose1 + t*pose2

def ease_in_out(t):
    # Smooth transition for natural motion
    return 0.5 - 0.5 * np.cos(np.pi * t)

def generate_sitdown_motion(n_frames=100):
    """Generate joint positions for sit-down motion."""
    sequence = []
    for i in range(n_frames):
        t = i / (n_frames - 1)
        if t < 0.7:
            # Downward phase
            t_down = t / 0.7
            phase = ease_in_out(t_down)
            pose = interpolate_pose(POSE_STAND, POSE_SIT, phase)
        else:
            # Pause at bottom
            pose = POSE_SIT.copy()
        # Add subtle arm movement: slightly bring wrists onto knees as sitting down
        arm_t = min(t/0.7, 1) # arm move with sit
        pose[6] += (pose[11] - pose[6]) * 0.3 * arm_t # right wrist approaches right knee
        pose[7] += (pose[12] - pose[7]) * 0.3 * arm_t # left wrist approaches left knee
        sequence.append(pose.copy())
    return np.array(sequence)

# Animation parameters
fig, ax = plt.subplots(figsize=(4,8))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 9)
ax.axis('off')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
scatter = ax.scatter([], [], c='white', s=60)

n_frames = 80
motion = generate_sitdown_motion(n_frames)

def init():
    scatter.set_offsets(np.zeros((15,2)))
    return scatter,

def animate(i):
    coords = motion[i]
    scatter.set_offsets(coords)
    return scatter,

ani = animation.FuncAnimation(
    fig, animate, frames=n_frames, interval=28, blit=True, init_func=init, repeat=True
)

plt.show()
