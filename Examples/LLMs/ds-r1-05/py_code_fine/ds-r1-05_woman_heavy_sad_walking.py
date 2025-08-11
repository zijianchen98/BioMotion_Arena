
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Set dimensions and timing parameters
shoulder_width = 0.25
hip_width = 0.20
head_height = 1.0
torso_height = 0.8
upper_arm_len = 0.20
forearm_len = 0.18
thigh_len = 0.5
shin_len = 0.4
foot_len = 0.12

# Create figure and axes with black background
fig = plt.figure(figsize=(6, 6))
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-1.3, 1.3))
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')  # Hide axes and borders

# Initialize scatter plot for 15 white points
points = ax.scatter([], [], s=100, c='white', edgecolors='none')

def update(frame):
    cycle_time = 2.0  # Total gait cycle time (seconds)
    t = frame % (cycle_time * 30) / 30  # Time in seconds
    phase = 2 * math.pi * t / cycle_time
    
    # Body motion parameters (realistic human gait characteristics)
    lateral_sway = 0.08 * math.sin(phase) 
    vertical_bounce = -0.02 * math.sin(2 * phase)  
    shoulder_dip = -0.03 * math.sin(phase)  

    # Head motion (subtle movement)
    head_x = lateral_sway
    head_y = head_height + vertical_bounce
    
    # Shoulders (incorporates lateral sway and shoulder dip)
    shoulder_y = torso_height + vertical_bounce + shoulder_dip
    left_shoulder = [head_x - shoulder_width / 2, shoulder_y]
    right_shoulder = [head_x + shoulder_width / 2, shoulder_y]
    
    # Arms (realistic pendulum motion with delayed elbow movement)
    arm_swing_r = math.radians(10) * math.sin(phase + math.pi)
    arm_swing_l = math.radians(10) * math.sin(phase)
    
    # Right arm segments
    right_elbow_x = right_shoulder[0] + upper_arm_len * math.sin(arm_swing_r)
    right_elbow_y = right_shoulder[1] - upper_arm_len * math.cos(arm_swing_r)
    # Add slight delay in wrist movement relative to elbow
    wrist_phase_offset = phase + 0.3
    wrist_swing_r = math.radians(10) * math.sin(wrist_phase_offset + math.pi)
    right_wrist_x = right_elbow_x + forearm_len * math.sin(wrist_swing_r)
    right_wrist_y = right_elbow_y - forearm_len * math.cos(wrist_swing_r)
    
    # Left arm segments
    left_elbow_x = left_shoulder[0] + upper_arm_len * math.sin(arm_swing_l)
    left_elbow_y = left_shoulder[1] - upper_arm_len * math.cos(arm_swing_l)
    wrist_swing_l = math.radians(10) * math.sin(wrist_phase_offset)
    left_wrist_x = left_elbow_x + forearm_len * math.sin(wrist_swing_l)
    left_wrist_y = left_elbow_y - forearm_len * math.cos(wrist_swing_l)
    
    # Hips (lateral sway and vertical bounce)
    mid_hip_y = vertical_bounce
    left_hip = [-hip_width/2 + lateral_sway, mid_hip_y]
    right_hip = [hip_width/2 + lateral_sway, mid_hip_y]
    
    # Legs (realistic swing and stance phases with biomechanical constraints)
    # Thigh angles with phase offset
    thigh_angle_r = math.radians(18) * math.cos(phase)
    thigh_angle_l = math.radians(18) * math.cos(phase + math.pi)
    
    # Knee bend parameters
    knee_bend_r = math.radians(45) * (1 + math.sin(phase + math.pi/2)) / 2.5
    knee_bend_l = math.radians(45) * (1 + math.sin(phase + math.pi/2 + math.pi)) / 2.5
    
    # Right leg segments
    right_knee_x = right_hip[0] + thigh_len * math.sin(thigh_angle_r)
    right_knee_y = right_hip[1] - thigh_len * math.cos(thigh_angle_r)
    right_ankle_x = right_knee_x + shin_len * math.sin(thigh_angle_r - knee_bend_r)
    right_ankle_y = right_knee_y - shin_len * math.cos(thigh_angle_r - knee_bend_r)
    # Toes anchored during stance phase
    toe_lift_r = 0.03 * (1 + math.sin(phase + math.pi/2)) / 2  # Only lift during swing
    right_toe_x = right_ankle_x + foot_len
    right_toe_y = right_ankle_y - toe_lift_r  # Subtle lift during swing phase
    
    # Left leg segments
    left_knee_x = left_hip[0] + thigh_len * math.sin(thigh_angle_l)
    left_knee_y = left_hip[1] - thigh_len * math.cos(thigh_angle_l)
    left_ankle_x = left_knee_x + shin_len * math.sin(thigh_angle_l - knee_bend_l)
    left_ankle_y = left_knee_y - shin_len * math.cos(thigh_angle_l - knee_bend_l)
    toe_lift_l = 0.03 * (1 + math.sin(phase + math.pi/2 + math.pi)) / 2
    left_toe_x = left_ankle_x + foot_len
    left_toe_y = left_ankle_y - toe_lift_l
    
    # Compile all 15 points into an array
    point_positions = np.array([
        [head_x, head_y],           # Head
        left_shoulder,               # Left shoulder
        right_shoulder,              # Right shoulder
        [left_elbow_x, left_elbow_y], # Left elbow
        [right_elbow_x, right_elbow_y], # Right elbow
        [left_wrist_x, left_wrist_y], # Left wrist
        [right_wrist_x, right_wrist_y], # Right wrist
        left_hip,                    # Left hip
        right_hip,                   # Right hip
        [left_knee_x, left_knee_y],  # Left knee
        [right_knee_x, right_knee_y], # Right knee
        [left_ankle_x, left_ankle_y], # Left ankle
        [right_ankle_x, right_ankle_y], # Right ankle
        [left_toe_x, left_toe_y],    # Left toe
        [right_toe_x, right_toe_y]   # Right toe
    ])
    
    points.set_offsets(point_positions)
    return points,

def init():
    points.set_offsets([])
    return points,

# Create animation with smooth framerate
fps = 30
ani = animation.FuncAnimation(
    fig, update, init_func=init, 
    frames=100, interval=1000/fps, 
    blit=True
)

plt.tight_layout()
plt.show()
