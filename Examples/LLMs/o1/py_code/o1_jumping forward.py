import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------------------------
# This program creates a biologically inspired point-light animation showing
# a man performing a forward jump. There are exactly 15 white point-lights
# on a black background. The motion is designed to appear smooth and plausible.
# ------------------------------------------------------------------------------

# Number of frames for the jump animation
FRAMES = 60

# Base (rest) joint coordinates in 2D (x, y), standing pose
# Indices of points (15 total):
#  0  = Head
#  1  = Left Shoulder
#  2  = Right Shoulder
#  3  = Mid Torso
#  4  = Left Elbow
#  5  = Right Elbow
#  6  = Left Wrist
#  7  = Right Wrist
#  8  = Pelvis (center)
#  9  = Left Hip
# 10  = Right Hip
# 11  = Left Knee
# 12  = Right Knee
# 13  = Left Ankle
# 14  = Right Ankle
rest_pose = np.array([
    [ 0.00,  0.80],  # Head
    [-0.15,  0.50],  # Left Shoulder
    [ 0.15,  0.50],  # Right Shoulder
    [ 0.00,  0.45],  # Mid Torso
    [-0.30,  0.35],  # Left Elbow
    [ 0.30,  0.35],  # Right Elbow
    [-0.40,  0.20],  # Left Wrist
    [ 0.40,  0.20],  # Right Wrist
    [ 0.00,  0.00],  # Pelvis
    [-0.10,  0.00],  # Left Hip
    [ 0.10,  0.00],  # Right Hip
    [-0.10, -0.40],  # Left Knee
    [ 0.10, -0.40],  # Right Knee
    [-0.10, -0.80],  # Left Ankle
    [ 0.10, -0.80],  # Right Ankle
])

def get_positions(t):
    """
    Given a time parameter t in [0,1], return the 2D coordinates (15x2)
    of each point for the jumping motion.
    """
    # Copy the rest pose so we can modify it
    coords = rest_pose.copy()

    # Pelvis trajectory:
    # Horizontal shift from x=0 to x=1 over the jump
    # Vertical jump as a simple parabola peaking at t=0.5
    pelvis_x_offset = t
    pelvis_y_offset = 0.4 - 1.6 * (t - 0.5) ** 2  # peak ~0.4 at t=0.5

    # Apply pelvis motion to entire body
    coords[:, 0] += pelvis_x_offset
    coords[:, 1] += pelvis_y_offset

    # Knees bending at start (t=0) and end (t=1), more extended near mid-jump
    # We'll shift knees and ankles slightly to simulate bending.
    # A simple approach: bend factor ~ 0.2 at t=0 or t=1, minimal near t=0.5
    bend_factor = 0.2 * (1 - np.cos(np.pi * t))  # peaks at t=0,1 => ~0.4 shift
    # Move the knees and ankles up for extension in the middle
    # and down for bending at edges
    coords[11, 1] += bend_factor   # Left Knee
    coords[12, 1] += bend_factor   # Right Knee
    coords[13, 1] += bend_factor   # Left Ankle
    coords[14, 1] += bend_factor   # Right Ankle

    # Arms swing: behind body at t=0, overhead at t=0.5, forward at t=1
    # We'll shift wrists upward and forward near mid-jump
    # left/right elbow indices: 4,5; wrists: 6,7
    arm_swing_up = 0.2 * np.sin(np.pi * t)  # 0 at t=0, 0.2 at t=0.5, 0 at t=1
    arm_swing_forward = 0.3 * np.sin(np.pi * t)
    # Adjust elbows and wrists
    # Left elbow/wrist: negative x, so we move them "forward" (reduce negative x)
    coords[4, 0] += arm_swing_forward
    coords[4, 1] += arm_swing_up
    coords[6, 0] += arm_swing_forward + 0.1  # extra offset for wrist
    coords[6, 1] += arm_swing_up + 0.1

    # Right elbow/wrist: positive x, move them further positive x
    coords[5, 0] += arm_swing_forward
    coords[5, 1] += arm_swing_up
    coords[7, 0] += arm_swing_forward + 0.1
    coords[7, 1] += arm_swing_up + 0.1

    return coords

# Set up the figure and animation
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-0.5, 1.5)   # Enough room for forward jump
ax.set_ylim(-1.0, 1.2)
ax.axis('off')

# Initial scatter plot
scat = ax.scatter(
    rest_pose[:,0], rest_pose[:,1],
    c='white', s=30
)

def init():
    scat.set_offsets(rest_pose)
    return (scat,)

def animate(frame):
    # time parameter t in [0,1]
    t = frame / (FRAMES - 1)
    coords = get_positions(t)
    scat.set_offsets(coords)
    return (scat,)

anim = animation.FuncAnimation(
    fig, animate, init_func=init,
    frames=FRAMES, interval=50, blit=True, repeat=True
)

plt.show()