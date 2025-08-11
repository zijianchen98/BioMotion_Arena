
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the joint names/labels (15 points)
joint_names = [
    'Head',
    'Neck',
    'RightShoulder', 'LeftShoulder',
    'RightElbow', 'LeftElbow',
    'RightWrist', 'LeftWrist',
    'Spine', 'Pelvis',
    'RightHip', 'LeftHip',
    'RightKnee', 'LeftKnee',
    'RightAnkle', 'LeftAnkle'
]
# Select 15: Head, Neck, RShoulder, LShoulder, RElbow, LElbow, RWrist, LWrist, Spine, Pelvis,
#                                RHip,      LHip,    RKnee,  LKnee,   RAnkle, LAnkle
# We'll use head, neck, 2 shoulders, 2 elbows, 2 wrists, spine, pelvis, 2 hips, 2 knees, 2 ankles

JOINTS = [
    'Head', 'Neck',
    'RightShoulder', 'LeftShoulder',
    'RightElbow', 'LeftElbow',
    'RightWrist', 'LeftWrist',
    'Spine', 'Pelvis',
    'RightHip', 'LeftHip',
    'RightKnee', 'LeftKnee',
    'RightAnkle', 'LeftAnkle'
][:15]

JOINT_INDEX = {k: i for i, k in enumerate(JOINTS)}

# Stick-figure skeleton: parent->child for each bone (no lines drawn, but bone lengths used)
# Segment lengths in arbitrary units
bones = [
    ('Head', 'Neck', 0.15),
    ('Neck', 'Spine', 0.20),
    ('Spine', 'Pelvis', 0.15),
    ('Neck', 'RightShoulder', 0.15),
    ('Neck', 'LeftShoulder', 0.15),
    ('RightShoulder', 'RightElbow', 0.18),
    ('LeftShoulder', 'LeftElbow', 0.18),
    ('RightElbow', 'RightWrist', 0.18),
    ('LeftElbow', 'LeftWrist', 0.18),
    ('Pelvis', 'RightHip', 0.10),
    ('Pelvis', 'LeftHip', 0.10),
    ('RightHip', 'RightKnee', 0.22),
    ('LeftHip', 'LeftKnee', 0.22),
    ('RightKnee', 'RightAnkle', 0.22),
    ('LeftKnee', 'LeftAnkle', 0.22),
]

# Indices for joints used in animation
jidx = JOINT_INDEX

# Initial t-pose coordinates, centered, upright (units: meters, anthropometric proportions)
pose_rest = np.array([
    [0.0, 1.70],  # Head (top)
    [0.0, 1.55],  # Neck
    [0.15, 1.52], # Right Shoulder
    [-0.15, 1.52],# Left Shoulder
    [0.30, 1.32], # Right Elbow
    [-0.30, 1.32],# Left Elbow
    [0.35, 1.10], # Right Wrist
    [-0.35, 1.10],# Left Wrist
    [0.0, 1.32],  # Spine (mid back)
    [0.0, 1.15],  # Pelvis
    [0.10, 1.05], # Right Hip
    [-0.10, 1.05],# Left Hip
    [0.10, 0.65], # Right Knee
    [-0.10, 0.65],# Left Knee
    [0.10, 0.25], # Right Ankle
    [-0.10, 0.25] # Left Ankle
])[:15]

# Parameters for the animation
FPS = 30
DURATION = 2.5 # seconds
N_FRAMES = int(FPS * DURATION)

def get_waving_pose(t):
    """
    Returns the 15x2 array of joint positions at time t (seconds).
    The left hand (by convention, for 'happywoman', we'll wave left hand) does the waving motion.
    All other joints perform minor shifting for liveliness and weight shift.
    """
    # Base pose
    pose = pose_rest.copy()
    
    # Body: Add a subtle horizontal 'bouncing' for 'happy, light' mood
    bounce_mag = 0.02
    bounce = bounce_mag * np.sin(2*np.pi*t*1.0)  # 1 Hz
    # Head, neck, spine, pelvis, hips shift slightly
    for i in [jidx['Head'], jidx['Neck'], jidx['Spine'], jidx['Pelvis']]:
        pose[i, 0] += bounce
    for i in [jidx['LeftHip'], jidx['RightHip']]:
        pose[i, 0] += bounce / 2

    # Left leg: "light weight" effect, slightly bent/flexed and bounces a bit
    leg_bounce = 0.015 * np.sin(2*np.pi*t*1.0 + np.pi/2)
    pose[jidx['LeftKnee'], 1] += leg_bounce
    pose[jidx['LeftAnkle'], 1] += leg_bounce

    # Right leg: support, steady
    pose[jidx['RightKnee'], 1] -= leg_bounce/1.5
    pose[jidx['RightAnkle'], 1] -= leg_bounce/1.5

    # Waving left hand: oscillate elbow and wrist with natural shoulder opening
    wave_speed = 2  # Hz (waving at 2x/sec)
    waving_phase = np.pi * t * wave_speed
    wave_angle = np.pi/4 * np.sin(waving_phase)    # ±45°

    # Move left elbow outward in a circular arc around the left shoulder
    sh = pose[jidx['LeftShoulder']]
    upperarm_len = np.linalg.norm(pose[jidx['LeftElbow']] - sh)
    # Arc: swing vertically and outward
    angle0 = -3*np.pi/4  # natural downward angle for upper arm (+ open
    angle = angle0 + 0.22*np.sin(waving_phase)   # opening/closing effect
    pose[jidx['LeftElbow'], 0] = sh[0] + upperarm_len * np.cos(angle)
    pose[jidx['LeftElbow'], 1] = sh[1] + upperarm_len * np.sin(angle)
    # Move left wrist, waving about the elbow, hand swings up and out
    forearm_len = np.linalg.norm(pose[jidx['LeftWrist']] - pose[jidx['LeftElbow']])
    hand_angle0 = angle + np.pi/1.7  # natural slight bend
    hand_angle = hand_angle0 + wave_angle
    pose[jidx['LeftWrist'], 0] = pose[jidx['LeftElbow'], 0] + forearm_len * np.cos(hand_angle)
    pose[jidx['LeftWrist'], 1] = pose[jidx['LeftElbow'], 1] + forearm_len * np.sin(hand_angle)
    # Add 'happy' bounce: lift wrist higher at wave peak
    pose[jidx['LeftWrist'], 1] += 0.03 * np.abs(np.sin(waving_phase))

    # For added realism: rotate left shoulder point with waveform (shoulder rises/lifts and outward a bit)
    pose[jidx['LeftShoulder'], 1] += 0.015 * np.abs(np.sin(waving_phase))
    pose[jidx['LeftShoulder'], 0] += 0.009 * np.sin(waving_phase)

    # Subtle happy upward torso/neck bop
    bop = 0.009 * np.abs(np.sin(waving_phase))
    pose[jidx['Neck'], 1] += bop
    pose[jidx['Head'], 1] += bop

    # Face "happy": slight head bobble
    pose[jidx['Head'], 1] += 0.008 * np.sin(2*waving_phase)

    # Optional: move right arm for natural counterbalance (small, smooth wave opposite)
    # Right arm gently swings
    right_angle = (3*np.pi/4) + 0.20*np.sin(waving_phase + np.pi)
    rsh = pose[jidx['RightShoulder']]
    pose[jidx['RightElbow'], 0] = rsh[0] + upperarm_len * np.cos(right_angle)
    pose[jidx['RightElbow'], 1] = rsh[1] + upperarm_len * np.sin(right_angle)
    forearm_len_r = np.linalg.norm(pose_rest[jidx['RightWrist']]-pose_rest[jidx['RightElbow']])
    hand_angle_r = right_angle - np.pi/1.7
    pose[jidx['RightWrist'], 0] = pose[jidx['RightElbow'], 0] + forearm_len_r * np.cos(hand_angle_r)
    pose[jidx['RightWrist'], 1] = pose[jidx['RightElbow'], 1] + forearm_len_r * np.sin(hand_angle_r)
    pose[jidx['RightShoulder'], 1] += 0.008 * np.abs(np.sin(waving_phase + np.pi))

    return pose

# Setup matplotlib
fig, ax = plt.subplots(figsize=(4, 7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
plt.axis('off')

# Dot style
dot_size = 50
dot_color = 'white'
# Animation: plot 15 points
scat = ax.scatter(
    pose_rest[:, 0], pose_rest[:, 1],
    s=dot_size, c=dot_color, edgecolor='none'
)
# Optionally: for debugging, plot skeleton lines (uncomment if needed)

def animate(frame):
    t = frame / FPS
    pose = get_waving_pose(t)
    scat.set_offsets(pose)
    return scat,

# Configure limits to match the sample image, with padding
ax.set_xlim(-0.45, 0.45)
ax.set_ylim(0.0, 1.82)

ani = animation.FuncAnimation(
    fig, animate, frames=N_FRAMES, interval=1000/FPS, blit=True
)

plt.show()
