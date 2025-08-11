
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configuration Constants ---

# General animation properties
SPEED = 0.035  # Controls the speed of the walking cycle
DOT_SIZE = 50  # Size of the point-light dots

# Biomechanical properties of the walker
FIG_SCALE = 0.9  # Overall size of the figure

# Body segment lengths
HEAD_RADIUS = 0.15 * FIG_SCALE
TORSO_LENGTH = 0.5 * FIG_SCALE
SHOULDER_WIDTH = 0.45 * FIG_SCALE
HIP_WIDTH = 0.35 * FIG_SCALE
THIGH_LENGTH = 0.5 * FIG_SCALE
CALF_LENGTH = 0.5 * FIG_SCALE
UPPER_ARM_LENGTH = 0.4 * FIG_SCALE
FOREARM_LENGTH = 0.35 * FIG_SCALE

# Kinematic parameters for "heavy weight" walking style
# These values are tuned to create the impression of carrying a heavy load.
CENTER_Y_OFFSET = -0.3 * FIG_SCALE  # Lowered center of gravity
TORSO_TILT = np.deg2rad(12)         # Forward lean to counteract weight
SWAY_AMP = 0.09 * FIG_SCALE         # Increased side-to-side sway for balance
BOUNCE_AMP = 0.015 * FIG_SCALE      # Reduced vertical bounce due to weight
STEP_AMP = np.deg2rad(28)           # Amplitude of leg swing (step length)
KNEE_BEND_AMP = np.deg2rad(75)      # Maximum knee bend during leg swing
ARM_SWING_AMP = np.deg2rad(8)       # Severely restricted arm swing
ELBOW_BEND = np.deg2rad(50)         # Arms held in a fixed, bent position

# --- Animation Setup ---

# Create the figure and axes for the animation
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_aspect('equal')
ax.set_facecolor('black')

# Set plot limits to keep the walker centered and visible
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.5, 1.0)

# Remove axes ticks and labels for a clean look
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
fig.tight_layout(pad=0)


# Initialize a scatter plot for the 15 points.
# The points will be updated in each frame.
scatter = ax.scatter([], [], c='white', s=DOT_SIZE)

def rotate_point(point, angle):
    """Utility function to rotate a 2D point around the origin."""
    x, y = point
    new_x = x * np.cos(angle) - y * np.sin(angle)
    new_y = x * np.sin(angle) + y * np.cos(angle)
    return np.array([new_x, new_y])

def update_animation(frame_number):
    """
    Calculates the position of all 15 joints for a given frame.
    This function implements the kinematic model of walking.
    """
    # The phase 't' drives the cyclical motion of the walk
    t = frame_number * SPEED

    # --- Core Body Motion ---
    # The pelvis acts as the root of the kinematic chain.
    # Its motion includes side-to-side sway and vertical bounce.
    pelvis_x = SWAY_AMP * np.sin(t)
    pelvis_y = CENTER_Y_OFFSET + BOUNCE_AMP * np.cos(2 * t)
    pelvis_pos = np.array([pelvis_x, pelvis_y])

    # --- Leg Kinematics ---
    # Leg angles are calculated relative to a vertical line.
    # The two legs are 180 degrees out of phase.
    # Right Leg (phase t)
    hip_angle_r = -STEP_AMP * np.cos(t)
    # The knee bends primarily when the leg is swinging forward.
    knee_angle_r = hip_angle_r + KNEE_BEND_AMP * np.maximum(0, np.sin(t + 0.1))
    
    # Left Leg (phase t + pi)
    hip_angle_l = -STEP_AMP * np.cos(t + np.pi)
    knee_angle_l = hip_angle_l + KNEE_BEND_AMP * np.maximum(0, np.sin(t + np.pi + 0.1))

    # --- Arm Kinematics ---
    # Arm swing is minimal and opposes the corresponding leg's motion.
    # Right Arm
    shoulder_angle_r = -ARM_SWING_AMP * np.cos(t + np.pi)
    elbow_angle_r = shoulder_angle_r + ELBOW_BEND

    # Left Arm
    shoulder_angle_l = -ARM_SWING_AMP * np.cos(t)
    elbow_angle_l = shoulder_angle_l + ELBOW_BEND

    # --- Calculate Joint Positions in World Space ---

    # 1. Define Torso joints relative to a local origin (0,0)
    hip_pos_l_local = np.array([-HIP_WIDTH / 2, 0])
    hip_pos_r_local = np.array([HIP_WIDTH / 2, 0])
    sternum_local = np.array([0, TORSO_LENGTH])
    shoulder_pos_l_local = np.array([-SHOULDER_WIDTH / 2, TORSO_LENGTH])
    shoulder_pos_r_local = np.array([SHOULDER_WIDTH / 2, TORSO_LENGTH])
    head_local = np.array([0, TORSO_LENGTH + HEAD_RADIUS * 1.5])

    # 2. Apply the forward torso tilt to all upper body joints
    sternum_tilted = rotate_point(sternum_local, TORSO_TILT)
    head_tilted = rotate_point(head_local, TORSO_TILT)
    shoulder_pos_l_tilted = rotate_point(shoulder_pos_l_local, TORSO_TILT)
    shoulder_pos_r_tilted = rotate_point(shoulder_pos_r_local, TORSO_TILT)
    
    # 3. Convert local coordinates to world coordinates by adding the pelvis position
    sternum_pos = sternum_tilted + pelvis_pos
    head_pos = head_tilted + pelvis_pos
    shoulder_pos_l = shoulder_pos_l_tilted + pelvis_pos
    shoulder_pos_r = shoulder_pos_r_tilted + pelvis_pos
    hip_pos_l = hip_pos_l_local + pelvis_pos
    hip_pos_r = hip_pos_r_local + pelvis_pos

    # 4. Calculate distal joint positions (knees, ankles, elbows, wrists)
    # Legs: A limb is a vector of a certain length rotated by its angle.
    knee_pos_l = hip_pos_l + rotate_point(np.array([0, -THIGH_LENGTH]), hip_angle_l)
    ankle_pos_l = knee_pos_l + rotate_point(np.array([0, -CALF_LENGTH]), knee_angle_l)
    knee_pos_r = hip_pos_r + rotate_point(np.array([0, -THIGH_LENGTH]), hip_angle_r)
    ankle_pos_r = knee_pos_r + rotate_point(np.array([0, -CALF_LENGTH]), knee_angle_r)

    # Arms: Their angles must also be tilted along with the torso.
    final_shoulder_angle_l = shoulder_angle_l + TORSO_TILT
    final_elbow_angle_l = elbow_angle_l + TORSO_TILT
    elbow_pos_l = shoulder_pos_l + rotate_point(np.array([0, -UPPER_ARM_LENGTH]), final_shoulder_angle_l)
    wrist_pos_l = elbow_pos_l + rotate_point(np.array([0, -FOREARM_LENGTH]), final_elbow_angle_l)
    
    final_shoulder_angle_r = shoulder_angle_r + TORSO_TILT
    final_elbow_angle_r = elbow_angle_r + TORSO_TILT
    elbow_pos_r = shoulder_pos_r + rotate_point(np.array([0, -UPPER_ARM_LENGTH]), final_shoulder_angle_r)
    wrist_pos_r = elbow_pos_r + rotate_point(np.array([0, -FOREARM_LENGTH]), final_elbow_angle_r)

    # 5. Assemble the 15 points in the required order for plotting
    points = np.array([
        head_pos,          # 1
        shoulder_pos_l,    # 2
        shoulder_pos_r,    # 3
        elbow_pos_l,       # 4
        elbow_pos_r,       # 5
        sternum_pos,       # 6
        wrist_pos_l,       # 7
        wrist_pos_r,       # 8
        pelvis_pos,        # 9
        hip_pos_l,         # 10
        hip_pos_r,         # 11
        knee_pos_l,        # 12
        knee_pos_r,        # 13
        ankle_pos_l,       # 14
        ankle_pos_r,       # 15
    ])

    # Update the scatter plot data with the new point positions
    scatter.set_offsets(points)
    return scatter,

def init_animation():
    """Initializes the animation, required for blitting."""
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

# Calculate the number of frames for one full walking cycle to ensure a smooth loop
num_frames = int(2 * np.pi / SPEED)

# Create and run the animation
ani = animation.FuncAnimation(fig, update_animation, frames=num_frames,
                              init_func=init_animation, blit=True, interval=30)

plt.show()
