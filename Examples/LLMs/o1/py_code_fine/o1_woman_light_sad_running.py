import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# This program displays a 2D point-light stimulus of a "sad woman" running.
# It uses 15 white point-lights on a solid black background, with smooth,
# biomechanically-inspired motion.

# ---------------------------------------------------
# PARAMETERS
# ---------------------------------------------------
FPS = 30            # Frames per second
CYCLE_FRAMES = 60   # Number of frames for one running cycle
DOT_COUNT = 15      # Total number of point-lights
DOT_SIZE = 100      # Size of the dots when plotting

# Relative segment lengths (arbitrary biomechanical approximations)
HEAD_RADIUS = 0.08
TORSO_LENGTH = 0.35
SHOULDER_OFFSET = 0.15
ARM_UPPER_LENGTH = 0.25
ARM_LOWER_LENGTH = 0.25
HIP_OFFSET = 0.15
LEG_UPPER_LENGTH = 0.35
LEG_LOWER_LENGTH = 0.35

# A small "sad" slump for the torso and head
SAD_TORSO_FORWARD_ANGLE = np.radians(10)  # forward tilt
SAD_HEAD_FORWARD_ANGLE = np.radians(15)   # head looking down a bit

# ---------------------------------------------------
# FUNCTION TO COMPUTE JOINT POSITIONS
# ---------------------------------------------------
def get_points(frame):
    """
    Return an array of shape (DOT_COUNT, 2) representing (x, y)
    coordinates of each point-light for the given frame index.
    The motion is looped every CYCLE_FRAMES.
    """
    # Phase in [0, 2*pi)
    phase = 2.0 * np.pi * (frame % CYCLE_FRAMES) / CYCLE_FRAMES
    
    # Running motion parameters
    # Basic sinusoidal angles for left/right arms and legs, out of phase
    # We'll treat the runner as jogging in place (vertical bounce, no translation).
    torso_bob = 0.05 * np.cos(2.0 * phase)   # mild up-down torso motion
    l_leg_phase = phase
    r_leg_phase = phase + np.pi  # opposite phase
    l_arm_phase = phase + np.pi  # arms out of phase with legs
    r_arm_phase = phase
    
    # Range of motion (approx)
    # Thigh and upper arm angles swing forward/back
    # Shin/forearm angles also move with a smaller amplitude
    l_thigh_angle  = np.radians(30) * np.sin(l_leg_phase)
    l_shin_angle   = np.radians(20) * np.sin(2.0 * l_leg_phase)
    r_thigh_angle  = np.radians(30) * np.sin(r_leg_phase)
    r_shin_angle   = np.radians(20) * np.sin(2.0 * r_leg_phase)
    
    l_upper_arm_angle = np.radians(30) * np.sin(l_arm_phase)
    l_lower_arm_angle = np.radians(20) * np.sin(2.0 * l_arm_phase)
    r_upper_arm_angle = np.radians(30) * np.sin(r_arm_phase)
    r_lower_arm_angle = np.radians(20) * np.sin(2.0 * r_arm_phase)
    
    # BASE (pelvis) position in 2D
    # We'll keep the pelvis near the origin, incorporate vertical bob
    pelvis = np.array([0.0, 0.0 + torso_bob])
    
    # Torso angle: slight forward lean + sinusoidal rocking
    torso_angle = SAD_TORSO_FORWARD_ANGLE + np.radians(5) * np.sin(2.0 * phase)
    
    # Pelvis to torso/chest
    chest = pelvis + rotation_2d(torso_angle).dot([0, TORSO_LENGTH])
    
    # Head: offset from chest, leaning forward
    head_center = chest + rotation_2d(torso_angle + SAD_HEAD_FORWARD_ANGLE).dot([0, HEAD_RADIUS])
    
    # Shoulders: offset from chest, horizontally spaced
    left_shoulder = chest + rotation_2d(torso_angle).dot([-SHOULDER_OFFSET, 0])
    right_shoulder = chest + rotation_2d(torso_angle).dot([ SHOULDER_OFFSET, 0])
    
    # Hips: offset from pelvis, horizontally spaced
    left_hip = pelvis + rotation_2d(0).dot([-HIP_OFFSET, 0])
    right_hip = pelvis + rotation_2d(0).dot([ HIP_OFFSET, 0])
    
    # Left arm
    l_upper_arm_vec = rotation_2d(torso_angle + l_upper_arm_angle).dot([0, -ARM_UPPER_LENGTH])
    l_elbow = left_shoulder + l_upper_arm_vec
    l_lower_arm_vec = rotation_2d(torso_angle + l_upper_arm_angle + l_lower_arm_angle).dot([0, -ARM_LOWER_LENGTH])
    l_wrist = l_elbow + l_lower_arm_vec
    
    # Right arm
    r_upper_arm_vec = rotation_2d(torso_angle + r_upper_arm_angle).dot([0, -ARM_UPPER_LENGTH])
    r_elbow = right_shoulder + r_upper_arm_vec
    r_lower_arm_vec = rotation_2d(torso_angle + r_upper_arm_angle + r_lower_arm_angle).dot([0, -ARM_LOWER_LENGTH])
    r_wrist = r_elbow + r_lower_arm_vec
    
    # Left leg
    l_thigh_vec = rotation_2d(l_thigh_angle).dot([0, -LEG_UPPER_LENGTH])
    l_knee = left_hip + l_thigh_vec
    l_shin_vec = rotation_2d(l_thigh_angle + l_shin_angle).dot([0, -LEG_LOWER_LENGTH])
    l_ankle = l_knee + l_shin_vec
    
    # Right leg
    r_thigh_vec = rotation_2d(r_thigh_angle).dot([0, -LEG_UPPER_LENGTH])
    r_knee = right_hip + r_thigh_vec
    r_shin_vec = rotation_2d(r_thigh_angle + r_shin_angle).dot([0, -LEG_LOWER_LENGTH])
    r_ankle = r_knee + r_shin_vec
    
    # Collect all 15 points in order
    #  1) Head, 2) Left Shoulder, 3) Right Shoulder,
    #  4) Left Elbow, 5) Right Elbow, 6) Left Wrist, 7) Right Wrist,
    #  8) Chest, 9) Left Hip, 10) Right Hip,
    #  11) Left Knee, 12) Right Knee,
    #  13) Left Ankle, 14) Right Ankle, 15) Pelvis
    points = np.array([
        head_center,
        left_shoulder,
        right_shoulder,
        l_elbow,
        r_elbow,
        l_wrist,
        r_wrist,
        chest,
        left_hip,
        right_hip,
        l_knee,
        r_knee,
        l_ankle,
        r_ankle,
        pelvis
    ])
    
    return points

def rotation_2d(theta):
    """Return 2D rotation matrix for angle theta."""
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[ c, -s],
                     [ s,  c]])

# ---------------------------------------------------
# SETUP MATPLOTLIB FIGURE
# ---------------------------------------------------
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')      # black background for the figure
ax.set_facecolor('black')             # black background in the plot area
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
plt.axis('off')

# Initial scatter (white dots)
scat = ax.scatter([], [], c='white', s=DOT_SIZE)

def init():
    scat.set_offsets([])
    return (scat,)

def update(frame):
    pts = get_points(frame)
    scat.set_offsets(pts)
    return (scat,)

anim = FuncAnimation(fig, update, frames=None, init_func=init,
                     interval=1000//FPS, blit=True, repeat=True)

plt.show()