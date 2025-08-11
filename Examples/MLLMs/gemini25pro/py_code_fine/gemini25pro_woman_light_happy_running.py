
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure and axes for the animation
fig, ax = plt.subplots()
fig.set_facecolor('black')
ax.set_facecolor('black')

# Set the axis limits and aspect ratio.
# The axis limits will be updated dynamically to follow the runner.
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal')

# Remove axis ticks, labels, and spines for a clean look
ax.axis('off')

# Initialize the 15 points for the point-light display.
# A scatter plot object is created and will be updated in each frame.
initial_positions = np.zeros((15, 2))
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=45, c='white')

# --- Model and Animation Parameters ---

# Body segment lengths (proportions)
TORSO_LENGTH = 0.65
NECK_LENGTH = 0.15
HEAD_RADIUS = 0.15
SHOULDER_OFFSET = 0.05  # Small horizontal offset for side view
HIP_OFFSET = 0.04

UPPER_ARM_LENGTH = 0.4
LOWER_ARM_LENGTH = 0.38
THIGH_LENGTH = 0.55
LOWER_LEG_LENGTH = 0.5

# Motion parameters for a "happy, lightweight woman running"
# Higher frequency, speed, and bounciness convey an energetic, happy mood.
RUN_FREQ = 1.9  # Hz, cycles per second.
HORIZONTAL_SPEED = 2.8  # units per second
VERTICAL_BOB_AMP = 0.07  # Amplitude of the up-and-down motion

# Joint angle amplitudes (in radians)
FORWARD_LEAN = np.deg2rad(12)
THIGH_AMP = np.deg2rad(42)
KNEE_FLEX_AMP = np.deg2rad(75)
KNEE_KICK_AMP = np.deg2rad(30)
ARM_SWING_AMP = np.deg2rad(50)
ELBOW_FLEX_BASE = np.deg2rad(35)
ELBOW_FLEX_AMP = np.deg2rad(45)

# Map point names to array indices for clarity
point_map = {
    'head': 0, 'sternum': 1, 'pelvis': 2,
    'l_shoulder': 3, 'r_shoulder': 4,
    'l_elbow': 5, 'r_elbow': 6,
    'l_wrist': 7, 'r_wrist': 8,
    'l_hip': 9, 'r_hip': 10,
    'l_knee': 11, 'r_knee': 12,
    'l_ankle': 13, 'r_ankle': 14
}
points = np.zeros((15, 2))

def update(frame):
    """
    Calculates the position of each of the 15 points for a given frame.
    The model uses a hierarchical kinematic structure, starting from the pelvis.
    """
    # Calculate time 't' and the angular progress 'omega_t' through the run cycle
    t = frame / 60.0  # Assuming 60 FPS for smooth time progression
    omega_t = 2 * np.pi * RUN_FREQ * t

    # --- 1. Torso and Core Body Motion ---

    # The pelvis is the root of the hierarchy.
    # It moves forward at a constant speed and bobs vertically.
    pelvis_x = HORIZONTAL_SPEED * t
    pelvis_y = VERTICAL_BOB_AMP * np.cos(omega_t * 2)  # Double freq for two steps per cycle
    points[point_map['pelvis']] = [pelvis_x, pelvis_y]

    # Sternum position is based on the pelvis, torso length, and forward lean.
    sternum_x = pelvis_x + TORSO_LENGTH * np.sin(FORWARD_LEAN)
    sternum_y = pelvis_y + TORSO_LENGTH * np.cos(FORWARD_LEAN)
    points[point_map['sternum']] = [sternum_x, sternum_y]

    # Head position is relative to the sternum.
    head_x = sternum_x + (NECK_LENGTH + HEAD_RADIUS) * np.sin(FORWARD_LEAN)
    head_y = sternum_y + (NECK_LENGTH + HEAD_RADIUS) * np.cos(FORWARD_LEAN)
    points[point_map['head']] = [head_x, head_y]

    # --- 2. Leg Motion (Right and Left) ---
    # The two legs are 180 degrees (pi radians) out of phase.
    for side in ['r', 'l']:
        phase_shift = 0 if side == 'r' else np.pi
        side_sign = 1 if side == 'r' else -1

        # Hip joint position.
        hip_x = pelvis_x + side_sign * HIP_OFFSET * np.cos(FORWARD_LEAN)
        hip_y = pelvis_y - side_sign * HIP_OFFSET * np.sin(FORWARD_LEAN)
        points[point_map[f'{side}_hip']] = [hip_x, hip_y]

        # Thigh angle oscillates back and forth.
        thigh_angle = THIGH_AMP * np.cos(omega_t + phase_shift)

        # Knee angle has a more complex motion for a natural heel kick.
        knee_flex_angle = KNEE_FLEX_AMP * (np.sin(omega_t + phase_shift - np.pi/2) + 1)/2 \
                        + KNEE_KICK_AMP * (np.sin(2 * (omega_t + phase_shift)) + 1)/2

        # Calculate joint positions using forward kinematics.
        # The thigh's angle is relative to the leaned torso.
        world_thigh_angle = thigh_angle + FORWARD_LEAN

        knee_x = hip_x + THIGH_LENGTH * np.sin(world_thigh_angle)
        knee_y = hip_y - THIGH_LENGTH * np.cos(world_thigh_angle)
        points[point_map[f'{side}_knee']] = [knee_x, knee_y]

        # The lower leg's angle is relative to the thigh.
        world_lower_leg_angle = world_thigh_angle - knee_flex_angle

        ankle_x = knee_x + LOWER_LEG_LENGTH * np.sin(world_lower_leg_angle)
        ankle_y = knee_y - LOWER_LEG_LENGTH * np.cos(world_lower_leg_angle)
        points[point_map[f'{side}_ankle']] = [ankle_x, ankle_y]

    # --- 3. Arm Motion (Right and Left) ---
    # Arms swing in opposition to the corresponding legs.
    for side in ['r', 'l']:
        phase_shift = np.pi if side == 'r' else 0 # Opposite phase to leg
        side_sign = 1 if side == 'r' else -1

        # Shoulder joint position.
        shoulder_x = sternum_x + side_sign * SHOULDER_OFFSET * np.cos(FORWARD_LEAN)
        shoulder_y = sternum_y - side_sign * SHOULDER_OFFSET * np.sin(FORWARD_LEAN)
        points[point_map[f'{side}_shoulder']] = [shoulder_x, shoulder_y]

        # Upper arm swings back and forth.
        arm_swing_angle = ARM_SWING_AMP * np.cos(omega_t + phase_shift)

        # Elbow has a base bend plus some oscillation.
        elbow_flex_angle = ELBOW_FLEX_BASE + ELBOW_FLEX_AMP * (np.sin(omega_t + phase_shift + np.pi/2) + 1)/2

        # Calculate joint positions using forward kinematics.
        world_arm_angle = arm_swing_angle + FORWARD_LEAN

        elbow_x = shoulder_x + UPPER_ARM_LENGTH * np.sin(world_arm_angle)
        elbow_y = shoulder_y - UPPER_ARM_LENGTH * np.cos(world_arm_angle)
        points[point_map[f'{side}_elbow']] = [elbow_x, elbow_y]

        world_lower_arm_angle = world_arm_angle - elbow_flex_angle

        wrist_x = elbow_x + LOWER_ARM_LENGTH * np.sin(world_lower_arm_angle)
        wrist_y = elbow_y - LOWER_ARM_LENGTH * np.cos(world_lower_arm_angle)
        points[point_map[f'{side}_wrist']] = [wrist_x, wrist_y]

    # --- 4. Update the Plot ---
    
    # Update the positions of all 15 points in the scatter plot.
    scatter.set_offsets(points)

    # Update the axis limits to keep the runner horizontally centered in the view.
    ax.set_xlim(pelvis_x - 2.5, pelvis_x + 2.5)

    return scatter,

# Create the animation object using FuncAnimation.
# blit=True is used for performance, redrawing only the parts that have changed.
# interval=16 corresponds to ~62.5 FPS for smooth motion.
ani = animation.FuncAnimation(
    fig, update, frames=600, interval=16, blit=True
)

# Display the animation window.
plt.show()
