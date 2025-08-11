
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. Set up the figure and axes for the animation ---
fig, ax = plt.subplots(figsize=(5, 8))
fig.set_facecolor('black')
ax.set_facecolor('black')

# Set plot limits and aspect ratio to frame the animation correctly
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-1.0, 1.2)
ax.set_aspect('equal', adjustable='box')

# Hide the axes, ticks, and spines for a clean look
ax.axis('off')

# --- 2. Define constants and biomechanical parameters ---
N_FRAMES = 32
N_POINTS = 15

# Body proportions in arbitrary units, tuned for a natural look
UPPER_LEG_LEN = 0.38
LOWER_LEG_LEN = 0.40
UPPER_ARM_LEN = 0.30
LOWER_ARM_LEN = 0.32
TORSO_HEIGHT = 0.45
HIP_PROJ_WIDTH = 0.12       # Projected horizontal distance between hips
SHOULDER_PROJ_WIDTH = 0.22  # Projected horizontal distance between shoulders
HEAD_RADIUS = 0.09

# Motion parameters for a realistic running gait
HIP_AMP = np.pi / 4.0        # Amplitude of thigh swing (radians)
KNEE_AMP = np.pi * 0.8       # Maximum knee flexion angle for leg recovery
SHOULDER_AMP = np.pi / 3.5   # Amplitude of arm swing
ELBOW_FLEX_ANGLE = np.pi * 0.55 # Fixed elbow flexion angle
BODY_BOB_AMP = 0.05          # Vertical bobbing amplitude of the pelvis
FORWARD_LEAN = 0.2           # Forward lean of the torso

# --- 3. Pre-calculate all point positions for the entire animation cycle ---
points_data = np.zeros((N_FRAMES, N_POINTS, 2))
time_points = np.linspace(0, 2 * np.pi, N_FRAMES, endpoint=False)

for i, t in enumerate(time_points):
    # --- Central Body Points ---
    # Pelvis: Origin of the hierarchy, with vertical bobbing motion
    pelvis_z = BODY_BOB_AMP * np.cos(2 * t)
    p_pelvis = np.array([0, pelvis_z])

    # Thorax: Positioned above the pelvis with a forward lean
    p_thorax = p_pelvis + np.array([FORWARD_LEAN, TORSO_HEIGHT])

    # Head: Positioned on top of the thorax
    p_head = p_thorax + np.array([0, HEAD_RADIUS])
    
    # --- Leg Kinematics (Right and Left) ---
    # Right Leg (rendered as the 'far' leg)
    hip_angle_r = HIP_AMP * np.cos(t)
    knee_angle_r = KNEE_AMP * (np.sin(t - np.pi / 4) + 1) / 2
    p_r_hip = p_pelvis + np.array([-HIP_PROJ_WIDTH / 2, 0])
    p_r_knee = p_r_hip + np.array([UPPER_LEG_LEN * np.sin(hip_angle_r), 
                                   -UPPER_LEG_LEN * np.cos(hip_angle_r)])
    p_r_ankle = p_r_knee + np.array([LOWER_LEG_LEN * np.sin(hip_angle_r - knee_angle_r), 
                                     -LOWER_LEG_LEN * np.cos(hip_angle_r - knee_angle_r)])

    # Left Leg (rendered as the 'near' leg)
    hip_angle_l = HIP_AMP * np.cos(t + np.pi)
    knee_angle_l = KNEE_AMP * (np.sin(t + np.pi - np.pi / 4) + 1) / 2
    p_l_hip = p_pelvis + np.array([HIP_PROJ_WIDTH / 2, 0])
    p_l_knee = p_l_hip + np.array([UPPER_LEG_LEN * np.sin(hip_angle_l), 
                                   -UPPER_LEG_LEN * np.cos(hip_angle_l)])
    p_l_ankle = p_l_knee + np.array([LOWER_LEG_LEN * np.sin(hip_angle_l - knee_angle_l), 
                                     -LOWER_LEG_LEN * np.cos(hip_angle_l - knee_angle_l)])

    # --- Arm Kinematics (Right and Left) ---
    # Left Arm (near, moves contralaterally with the right leg)
    shoulder_angle_l = SHOULDER_AMP * np.cos(t)
    p_l_shoulder = p_thorax + np.array([SHOULDER_PROJ_WIDTH / 2, 0])
    p_l_elbow = p_l_shoulder + np.array([UPPER_ARM_LEN * np.sin(shoulder_angle_l), 
                                         -UPPER_ARM_LEN * np.cos(shoulder_angle_l)])
    p_l_wrist = p_l_elbow + np.array([LOWER_ARM_LEN * np.sin(shoulder_angle_l - ELBOW_FLEX_ANGLE), 
                                      -LOWER_ARM_LEN * np.cos(shoulder_angle_l - ELBOW_FLEX_ANGLE)])
    
    # Right Arm (far, moves contralaterally with the left leg)
    shoulder_angle_r = SHOULDER_AMP * np.cos(t + np.pi)
    p_r_shoulder = p_thorax + np.array([-SHOULDER_PROJ_WIDTH / 2, 0])
    p_r_elbow = p_r_shoulder + np.array([UPPER_ARM_LEN * np.sin(shoulder_angle_r), 
                                         -UPPER_ARM_LEN * np.cos(shoulder_angle_r)])
    p_r_wrist = p_r_elbow + np.array([LOWER_ARM_LEN * np.sin(shoulder_angle_r - ELBOW_FLEX_ANGLE), 
                                      -LOWER_ARM_LEN * np.cos(shoulder_angle_r - ELBOW_FLEX_ANGLE)])
    
    # --- Assemble the 15 points for the current frame ---
    points_data[i] = np.array([
        p_head, p_thorax, p_pelvis,
        p_l_shoulder, p_r_shoulder,
        p_l_elbow, p_r_elbow,
        p_l_wrist, p_r_wrist,
        p_l_hip, p_r_hip,
        p_l_knee, p_r_knee,
        p_l_ankle, p_r_ankle
    ])

# --- 4. Set up the animation components ---
# Create the scatter plot object with the first frame's data
scatter = ax.scatter(points_data[0, :, 0], points_data[0, :, 1], c='white', s=60)

# The function to update the plot for each frame of the animation
def animate(frame_index):
    scatter.set_offsets(points_data[frame_index])
    return scatter,

# --- 5. Create and run the animation ---
# The interval determines the speed (in milliseconds per frame)
# blit=True ensures smooth rendering
ani = animation.FuncAnimation(fig, animate, frames=N_FRAMES, interval=35, blit=True)

plt.show()
