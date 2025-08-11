
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define parameters for the animation
T = 2.0          # Period of one walking cycle in seconds
fps = 30         # Frames per second
duration = 10.0  # Total duration of the animation in seconds
num_frames = int(duration * fps)  # Total number of frames
w = 0.05         # Horizontal offset for left/right points
H = 1.0          # Average height of hips
A = 0.02         # Amplitude of vertical body motion (small for light weight)
L_torso = 0.4    # Length of torso
L_head = 0.2     # Length from shoulder to head
L_upper_arm = 0.3  # Length of upper arm
L_forearm = 0.3   # Length of forearm
L_hand = 0.1      # Length from wrist to hand
L_upper_leg = 0.4  # Length of upper leg
L_lower_leg = 0.4  # Length of lower leg

# Angle amplitudes (radians)
θ_upper_leg_max = np.pi / 6   # Max angle for upper leg swing
θ_knee_max = np.pi / 3        # Max angle for knee flexion
θ_upper_arm_max = np.pi / 12  # Smaller arm swing for sad demeanor

# Function to compute the positions of the 15 points at time t
def get_positions(t):
    # Vertical position of hips with oscillation
    y_hips = H + A * np.cos(4 * np.pi * t / T)
    y_shoulder = y_hips + L_torso

    # Define point positions
    right_hip = (w, y_hips)
    left_hip = (-w, y_hips)
    right_shoulder = (w, y_shoulder)
    left_shoulder = (-w, y_shoulder)
    head = (0, y_shoulder + L_head)

    # Right leg angles and positions
    θ_R_upper_leg = θ_upper_leg_max * np.sin(2 * np.pi * t / T)
    θ_R_lower_leg = θ_knee_max * (np.sin(2 * np.pi * t / T) + 1) / 2
    right_knee = (
        right_hip[0] + L_upper_leg * np.sin(θ_R_upper_leg),
        right_hip[1] - L_upper_leg * np.cos(θ_R_upper_leg)
    )
    right_ankle = (
        right_knee[0] + L_lower_leg * np.sin(θ_R_upper_leg + θ_R_lower_leg),
        right_knee[1] - L_lower_leg * np.cos(θ_R_upper_leg + θ_R_lower_leg)
    )

    # Left leg angles and positions
    θ_L_upper_leg = -θ_upper_leg_max * np.sin(2 * np.pi * t / T)
    θ_L_lower_leg = θ_knee_max * (-np.sin(2 * np.pi * t / T) + 1) / 2
    left_knee = (
        left_hip[0] + L_upper_leg * np.sin(θ_L_upper_leg),
        left_hip[1] - L_upper_leg * np.cos(θ_L_upper_leg)
    )
    left_ankle = (
        left_knee[0] + L_lower_leg * np.sin(θ_L_upper_leg + θ_L_lower_leg),
        left_knee[1] - L_lower_leg * np.cos(θ_L_upper_leg + θ_L_lower_leg)
    )

    # Right arm angles and positions
    θ_R_upper_arm = -θ_upper_arm_max * np.sin(2 * np.pi * t / T)
    θ_R_forearm = 0  # Straight arm for simplicity
    right_elbow = (
        right_shoulder[0] + L_upper_arm * np.sin(θ_R_upper_arm),
        right_shoulder[1] - L_upper_arm * np.cos(θ_R_upper_arm)
    )
    right_wrist = (
        right_elbow[0] + L_forearm * np.sin(θ_R_upper_arm + θ_R_forearm),
        right_elbow[1] - L_forearm * np.cos(θ_R_upper_arm + θ_R_forearm)
    )
    right_hand = (
        right_wrist[0] + L_hand * np.sin(θ_R_upper_arm + θ_R_forearm),
        right_wrist[1] - L_hand * np.cos(θ_R_upper_arm + θ_R_forearm)
    )

    # Left arm angles and positions
    θ_L_upper_arm = θ_upper_arm_max * np.sin(2 * np.pi * t / T)
    θ_L_forearm = 0  # Straight arm for simplicity
    left_elbow = (
        left_shoulder[0] + L_upper_arm * np.sin(θ_L_upper_arm),
        left_shoulder[1] - L_upper_arm * np.cos(θ_L_upper_arm)
    )
    left_wrist = (
        left_elbow[0] + L_forearm * np.sin(θ_L_upper_arm + θ_L_forearm),
        left_elbow[1] - L_forearm * np.cos(θ_L_upper_arm + θ_L_forearm)
    )
    left_hand = (
        left_wrist[0] + L_hand * np.sin(θ_L_upper_arm + θ_L_forearm),
        left_wrist[1] - L_hand * np.cos(θ_L_upper_arm + θ_L_forearm)
    )

    # List of all 15 points in order
    points = [
        head,         # 0
        left_shoulder, # 1
        right_shoulder, # 2
        left_elbow,   # 3
        right_elbow,  # 4
        left_wrist,   # 5
        right_wrist,  # 6
        left_hand,    # 7
        right_hand,   # 8
        left_hip,     # 9
        right_hip,    # 10
        left_knee,    # 11
        right_knee,   # 12
        left_ankde,   # 13
        right_ankle   # 14
    ]
    return points

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Solid black background
ax.set_xlim(-0.5, 0.5)     # X-axis limits
ax.set_ylim(0, 1.5)        # Y-axis limits (y increases upwards)
ax.set_aspect('equal')     # Maintain aspect ratio
ax.axis('off')             # Hide axes

# Initial scatter plot with 15 white points
initial_points = get_positions(0)
x = [p[0] for p in initial_points]
y = [p[1] for p in initial_points]
scatter = ax.scatter(x, y, color='white', s=10)  # White points, size 10

# Animation update function
def update(frame):
    t = frame / fps
    points = get_positions(t)
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    scatter.set_offsets(np.c_[x, y])  # Update point positions
    return scatter,

# Create and display the animation
ani = FuncAnimation(
    fig,
    update,
    frames=num_frames,
    interval=1000/fps,  # Time between frames in milliseconds
    blit=True           # Optimize animation
)
plt.show()
