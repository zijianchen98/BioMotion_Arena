
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 15 point-light marker names and order
MARKER_NAMES = [
    'head',
    'shoulder_l', 'shoulder_r',
    'elbow_l', 'elbow_r',
    'wrist_l', 'wrist_r',
    'hip_l', 'hip_r',
    'knee_l', 'knee_r',
    'ankle_l', 'ankle_r',
    'foot_l', 'foot_r'
]

# Lying down, figure is horizontal:
# x is along the body ("height"), y is vertical in screen (left/right).
# We'll center the figure in the middle of the frame.
#
# We simulate a resting and slightly breathing motion, maybe a small arm/leg twitch.
#
# The base pose is 'lying on his/her back' and head to the right.

def generate_pose(t, n_frames):
    """Returns (15,2) array of marker positions at time t (0..1)"""
    # Center of scene
    x0 = 0.0
    y0 = 0.0

    # main axes (horizontal body): x increases from feet to head
    body_length = 2.0  # total length (arbitrary units)

    # Define joint positions (body) for horizontal lying pose
    # Start at feet, along x direction

    # Basic body landmarks along x axis (feet to head)
    x_feet = -body_length/2
    x_ankle = x_feet + 0.1
    x_knee = x_feet + 0.4
    x_hip = x_feet + 0.8
    x_shoulder = x_feet + 1.5
    x_elbow = x_feet + 1.7
    x_wrist = x_feet + 1.95
    x_head = x_feet + 2.1

    # y coordinates for symmetry (lying on back)
    # All central joints along y=0, left is -y and right is +y

    hip_space = 0.18
    shoulder_space = 0.52
    elbow_space = 0.62
    wrist_space = 0.65
    knee_space = 0.17
    ankle_space = 0.17
    foot_space = 0.22

    # Baseline positions
    points = np.zeros((15,2))
    # head
    points[0] = [x_head, y0]
    # shoulders
    points[1] = [x_shoulder, -shoulder_space/2]
    points[2] = [x_shoulder, +shoulder_space/2]
    # elbows
    points[3] = [x_elbow, -elbow_space/2]
    points[4] = [x_elbow, +elbow_space/2]
    # wrists
    points[5] = [x_wrist, -wrist_space/2]
    points[6] = [x_wrist, +wrist_space/2]
    # hips
    points[7] = [x_hip, -hip_space/2]
    points[8] = [x_hip, +hip_space/2]
    # knees
    points[9] = [x_knee, -knee_space/2]
    points[10]= [x_knee, +knee_space/2]
    # ankles
    points[11]= [x_ankle, -ankle_space/2]
    points[12]= [x_ankle, +ankle_space/2]
    # feet
    points[13]= [x_feet, -foot_space/2]
    points[14]= [x_feet, +foot_space/2]

    # Animate: add slight movement
    # Breathing motion: chest and belly go up/down with a sine
    resp_amp = 0.11  # amplitude of breathing
    resp = resp_amp * np.sin(2*np.pi*t)
    # Shoulders and hips move slightly up, head tilts a tad.
    points[1,1] -= resp*1.1   # Left shoulder upward
    points[2,1] += resp*1.1   # Right shoulder upward
    points[7,1] -= resp*0.6   # Left hip
    points[8,1] += resp*0.6   # Right hip
    # Head moves a little further up
    points[0,1] += resp*0.35

    # Arms: subtle postural shift
    arm_twist = 0.05 * np.sin(2*np.pi*t + np.pi/2)
    points[5,1] -= arm_twist
    points[6,1] += arm_twist
    points[3,1] -= arm_twist*0.5
    points[4,1] += arm_twist*0.5

    # Legs: very small movement (twitch)
    leg_twitch = 0.025*np.sin(4*np.pi*t)
    points[11,1] -= leg_twitch
    points[12,1] += leg_twitch
    points[13,1] -= leg_twitch*0.7
    points[14,1] += leg_twitch*0.7

    # The whole body can have a very slow gentle "shift" (e.g. from heartbeat); optional:
    osc = 0.02*np.sin(2*np.pi*t*3)
    points[:,1] += osc

    # All points: some common shift to place in visible frame
    points = points + np.array([0, 0])

    return points

# Plotting and animation setup
fig, ax = plt.subplots(figsize=(6,4))
plt.style.use('dark_background')
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Set fixed limits (centered)
buff = 0.3
ax.set_xlim(-1.3-buff, 1.3+buff)
ax.set_ylim(-0.95-buff, 0.95+buff)

n_frames = 72
# For smooth animation, save the scatter plot object
scat = ax.scatter([], [], s=90, c='w', edgecolors='none')  # large white points

def init():
    scat.set_offsets(np.zeros((15,2)))
    return (scat,)

def animate(i):
    t = i / n_frames
    pts = generate_pose(t, n_frames)
    scat.set_offsets(pts)
    return (scat,)

ani = animation.FuncAnimation(fig, animate, frames=n_frames, interval=35, init_func=init,
                              blit=True, repeat=True)

plt.show()
