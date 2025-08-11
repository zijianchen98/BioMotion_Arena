
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure and axes for the animation
fig, ax = plt.subplots(figsize=(5, 9))
ax.set_facecolor('black')

# Set the viewing window properties
ax.set_xlim(-30, 30)
ax.set_ylim(-45, 45)
ax.set_aspect('equal', adjustable='box')
plt.axis('off')

# Define skeleton proportions for a "light weight woman"
# These constants define the length of each body part.
HEAD_NECK_DIST = 6
NECK_PELVIS_DIST = 19
SHOULDER_WIDTH = 11
HIP_WIDTH = 9
UPPER_ARM_LEN = 11
FOREARM_LEN = 10
UPPER_LEG_LEN = 14
LOWER_LEG_LEN = 13

# Define indices for the 15 points for clarity in the update function
# This maps each body part to an index in our coordinate array.
P_HEAD, P_NECK = 0, 1
P_L_SHOULDER, P_L_ELBOW, P_L_WRIST = 2, 3, 4
P_R_SHOULDER, P_R_ELBOW, P_R_WRIST = 5, 6, 7
P_PELVIS = 8
P_L_HIP, P_L_KNEE, P_L_ANKLE = 9, 10, 11
P_R_HIP, P_R_KNEE, P_R_ANKLE = 12, 13, 14

# Initialize a scatter plot for the 15 points.
# The points will be white and will be updated each frame.
initial_coords = np.zeros((15, 2))
scatter = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], c='white', s=60)

# Total number of frames for one cycle of the animation
num_frames = 150

def update_animation(frame):
    """
    This function is called for each frame of the animation.
    It calculates the new positions of the 15 points.
    """
    # Create a normalized time variable 't' that cycles from 0 to 2*pi
    t = 2 * np.pi * frame / num_frames

    # --- Core Body Motion & Posture ---
    # A subtle sway is added to the whole body for realism.
    body_sway_x = 0.5 * np.sin(t)
    body_sway_y = 0.5 * np.cos(2 * t)  # Simulates a gentle breathing motion

    # The pelvis is the root of the skeleton's hierarchy.
    pelvis_pos = np.array([0 + body_sway_x, -15 + body_sway_y])

    # A "sad" posture is created by slumping the torso forward and down.
    slump_forward = -1.5
    slump_down = -1.0
    neck_pos = pelvis_pos + np.array([slump_forward, NECK_PELVIS_DIST + slump_down])
    
    # The head is lowered to enhance the sad emotion.
    head_pos = neck_pos + np.array([0.5, HEAD_NECK_DIST])

    # --- Limb Positions ---
    # Shoulders are drooped down from the neck line.
    r_shoulder_pos = neck_pos + np.array([SHOULDER_WIDTH / 2, -1.5])
    l_shoulder_pos = neck_pos + np.array([-SHOULDER_WIDTH / 2, -1.5])

    # Hips are positioned relative to the pelvis center.
    r_hip_pos = pelvis_pos + np.array([HIP_WIDTH / 2, 0])
    l_hip_pos = pelvis_pos + np.array([-HIP_WIDTH / 2, 0])

    # Legs have a slight, natural bend at the knees.
    r_knee_pos = r_hip_pos + np.array([1, -UPPER_LEG_LEN])
    l_knee_pos = l_hip_pos + np.array([-1, -UPPER_LEG_LEN])
    r_ankle_pos = r_knee_pos + np.array([-0.5, -LOWER_LEG_LEN])
    l_ankle_pos = l_knee_pos + np.array([0.5, -LOWER_LEG_LEN])

    # The left arm hangs limply, with a slight bend.
    l_elbow_pos = l_shoulder_pos + np.array([-1, -UPPER_ARM_LEN + 1])
    l_wrist_pos = l_elbow_pos + np.array([1, -FOREARM_LEN + 1])

    # --- The Waving Motion (Right Arm) ---
    # The upper arm is raised to a waving position.
    upper_arm_angle = np.deg2rad(120) + 0.1 * np.sin(t)
    r_elbow_pos = r_shoulder_pos + np.array([
        UPPER_ARM_LEN * np.cos(upper_arm_angle),
        UPPER_ARM_LEN * np.sin(upper_arm_angle)
    ])

    # The forearm performs a slow, low-energy wave by pivoting at the elbow.
    wave_base_angle = -np.pi / 2  # The forearm is bent 90 degrees from the upper arm.
    wave_amplitude = 0.7  # The range of the wave in radians.
    wave_frequency = 2  # The number of waves per animation cycle.
    wave_motion = wave_amplitude * np.sin(wave_frequency * t)
    
    forearm_angle = upper_arm_angle + wave_base_angle + wave_motion
    
    r_wrist_pos = r_elbow_pos + np.array([
        FOREARM_LEN * np.cos(forearm_angle),
        FOREARM_LEN * np.sin(forearm_angle)
    ])
    
    # --- Assemble and Update All Point Coordinates ---
    # An array is created to hold the (x, y) coordinates of all 15 points.
    coords = np.zeros((15, 2))
    coords[P_HEAD] = head_pos
    coords[P_NECK] = neck_pos
    coords[P_L_SHOULDER] = l_shoulder_pos
    coords[P_L_ELBOW] = l_elbow_pos
    coords[P_L_WRIST] = l_wrist_pos
    coords[P_R_SHOULDER] = r_shoulder_pos
    coords[P_R_ELBOW] = r_elbow_pos
    coords[P_R_WRIST] = r_wrist_pos
    coords[P_PELVIS] = pelvis_pos
    coords[P_L_HIP] = l_hip_pos
    coords[P_L_KNEE] = l_knee_pos
    coords[P_L_ANKLE] = l_ankle_pos
    coords[P_R_HIP] = r_hip_pos
    coords[P_R_KNEE] = r_knee_pos
    coords[P_R_ANKLE] = r_ankle_pos

    # Update the positions of the points in the scatter plot.
    scatter.set_offsets(coords)
    return scatter,

# Create the animation object. `FuncAnimation` repeatedly calls the update function.
# `interval` is the delay between frames in milliseconds.
ani = animation.FuncAnimation(
    fig, update_animation, frames=num_frames, interval=50, blit=True
)

# Display the animation.
plt.show()
