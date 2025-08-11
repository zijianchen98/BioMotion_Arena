
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Joint names for reference
JOINT_NAMES = [
    'head',            # 0
    'neck',            # 1
    'right_shoulder',  # 2
    'left_shoulder',   # 3
    'right_elbow',     # 4
    'left_elbow',      # 5
    'right_wrist',     # 6
    'left_wrist',      # 7
    'pelvis',          # 8
    'right_hip',       # 9
    'left_hip',        # 10
    'right_knee',      # 11
    'left_knee',       # 12
    'right_ankle',     # 13
    'left_ankle',      # 14
]

# Number of joints/points
N_POINTS = 15

# "Stickman" template in standing neutral pose (X, Y) - 2D frontal view, units arbitrary
# All proportions are roughly human
# Centered at (0, 0) pelvis
template = np.array([
    [0, 7.0],      # head: top
    [0, 6.2],      # neck
    [0.8, 6.1],    # right_shoulder
    [-0.8, 6.1],   # left_shoulder
    [1.5, 5.0],    # right_elbow
    [-1.5, 5.0],   # left_elbow
    [1.9, 3.7],    # right_wrist
    [-1.9, 4.5],   # left_wrist (left arm starts out a bit lower, for naturalistic rest)
    [0, 4.0],      # pelvis
    [0.55, 3.7],   # right_hip
    [-0.55, 3.7],  # left_hip
    [0.55, 2.1],   # right_knee
    [-0.55, 2.1],  # left_knee
    [0.55, 0.5],   # right_ankle
    [-0.55, 0.5],  # left_ankle
])

# Parameters for animation duration and frame rate
FPS = 30
DURATION = 2.0  # seconds, one wave cycle
N_FRAMES = int(FPS * DURATION)

# Amplitudes (in "template" units), joint-wise for right arm waving
WAVE_ANGLE_DEG = 45       # Maximum raise of right arm (shoulder)
WAVE_ELBOW_BEND_DEG = 40  # Max deviation in elbow angle during waving
WAVE_FREQ = 1.6           # Number of full waving cycles per second (approx 3 waves in 2s)

def make_pose(t):
    """
    Compute the 2D positions of all 15 joints at time t (in seconds)
    Returns: np.array (15,2)
    """
    pose = template.copy()
    
    # Pelvis, spine and hip positions are fixed (standing in place)
    # Left leg fixed, right leg fixed
    
    # Arms animate:
    # LEFT ARM: Now remains mostly still (relaxed beside the body)
    # RIGHT ARM: Shoulder and elbow move to produce a waving gesture
    # We'll define the waving as a periodic angular change at the right shoulder,
    # and periodic elbow bending
    
    # Base positions
    shoulder_base = template[2]  # right_shoulder
    elbow_base = template[4]     # right_elbow
    wrist_base = template[6]     # right_wrist
    neck_base = template[1]      # neck

    # Parameters for segment lengths (for forward kinematics)
    upper_arm = np.linalg.norm(elbow_base - shoulder_base)
    forearm = np.linalg.norm(wrist_base - elbow_base)
    
    # Animation: right arm waving
    # Right upper arm swings upward from ~rest (~20 deg out) to up (~65 deg out)
    theta_shoulder = np.deg2rad(20) + np.deg2rad(WAVE_ANGLE_DEG) * np.sin(2 * np.pi * WAVE_FREQ * t)
    # Elbow bends in sync, with more flex at the lowest waving point
    theta_elbow = np.deg2rad(160) - np.deg2rad(WAVE_ELBOW_BEND_DEG) * np.abs(np.sin(2 * np.pi * WAVE_FREQ * t))

    # Shoulder position (fixed)
    px, py = shoulder_base
    # Upper arm: angle from vertical (shoulder to neck), positive is outward (to the right)
    # (Human right is positive-x)
    # In template, upper arm points almost down (right), but animation will sweep it up
    # We'll define 0deg as vertical down, so add +90 degrees for side-out horizontal
    angle_shoulder = -np.pi / 2 + theta_shoulder

    # Elbow 2D
    elbow_x = px + upper_arm * np.cos(angle_shoulder)
    elbow_y = py + upper_arm * np.sin(angle_shoulder)
    pose[4] = [elbow_x, elbow_y]     # right_elbow

    # Elbow bend: 0 is straight arm, positive is "closing" the elbow
    # Find vector for lower arm direction (angle: same as upper arm plus elbow flexion, since they are in the same plane)
    angle_elbow = angle_shoulder + np.pi - theta_elbow
    wrist_x = elbow_x + forearm * np.cos(angle_elbow)
    wrist_y = elbow_y + forearm * np.sin(angle_elbow)
    pose[6] = [wrist_x, wrist_y]     # right_wrist

    # Add some small vertical wave to the wrist (imitates wrist flicking as in waving, for realism)
    wrist_wave_mag = 0.25
    wrist_y += wrist_wave_mag * np.sin(4 * np.pi * WAVE_FREQ * t)
    pose[6] = [wrist_x, wrist_y]

    # Optionally, a little head bob to make it more natural
    head_bob = 0.06 * np.sin(2 * np.pi * 1.2 * t)
    pose[0][1] = template[0][1] + head_bob

    # Optionally, a tiny little shoulder movement for realism (shoulder shrugs slightly during waving)
    shoulder_bob = 0.04 * np.sin(2 * np.pi * WAVE_FREQ * t)
    pose[2][1] = template[2][1] + shoulder_bob
    pose[3][1] = template[3][1] + shoulder_bob * 0.5  # left shoulder: half the amount

    return pose

# --- Visualization ---

fig, ax = plt.subplots(figsize=(3.2, 6.0), dpi=100)
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-0.2, 7.8)

scatter = ax.scatter([], [], s=60, color='white', edgecolors='none')

def init():
    scatter.set_offsets(np.zeros([N_POINTS,2]))
    return [scatter]

def animate(i):
    t = i / FPS
    pose = make_pose(t)
    scatter.set_offsets(pose)
    return [scatter]

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, init_func=init, blit=True, interval=1000/FPS, repeat=True)

plt.show()
