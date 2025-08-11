
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

# Configure plot style
style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 6), facecolor='black')
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 2)
ax.axis('off')

# Set plot titles
fig.suptitle('Biological Motion Animation', fontsize=16, color='white')
ax.set_title('Point-Light Walker: Happy Man Walking', color='lightgray')

# Configure point markers
points = ax.scatter([], [], s=100, c='white', edgecolors='none', alpha=0.9)

# Define body proportions (relative units)
HEAD = 0
NECK = 1
RSHOULDER = 2
LSHOULDER = 3
RELBOW = 4
LELBOW = 5
RHAND = 6
LHAND = 7
TORSO = 8
RHIP = 9
LHIP = 10
RKNEE = 11
LKNEE = 12
RANKLE = 13
LANKLE = 14

# Joint positions in T-pose
rest_position = np.array([
    [0, 1.80],    # Head
    [0, 1.65],    # Neck
    [0.35, 1.50],  # RShoulder
    [-0.35, 1.50], # LShoulder
    [0.60, 1.40],  # RElbow
    [-0.60, 1.40], # LElbow
    [0.80, 1.20],  # RHand
    [-0.80, 1.20], # LHand
    [0, 1.25],     # Torso
    [0.20, 0.90],  # RHip
    [-0.20, 0.90], # LHip
    [0.20, 0.50],  # RKnee
    [-0.20, 0.50], # LKnee
    [0.20, 0.10],  # RAnkle
    [-0.20, 0.10]  # LAnkle
])

# Realistic walking motion parameters
WALKING_SPEED = 0.5
STRIDE_LENGTH = 0.8
VERTICAL_BOB = 0.08
ARM_SWING_AMP = 0.3
LEG_SWING_AMP = 0.4
KNEE_BEND_AMP = 0.4
HIP_SWAY_AMP = 0.1

def get_animation_frame(t):
    # Calculate phase variables
    cycle_pos = t % 1.0
    leg_phase = 2 * np.pi * cycle_pos
    arm_phase = leg_phase + np.pi  # Arms counter-phase to legs
    
    # Body core movement
    torso_offset = np.array([HIP_SWAY_AMP * np.sin(leg_phase), VERTICAL_BOB * np.sin(2*leg_phase)])
    torso_center = rest_position[TORSO] + torso_offset
    
    # Arm movements
    arm_swing = ARM_SWING_AMP * np.sin(arm_phase)
    
    # Leg movements
    leg_swing = LEG_SWING_AMP * np.sin(leg_phase)
    knee_bend = KNEE_BEND_AMP * abs(np.sin(leg_phase))
    foot_angle = 0.3 * np.sin(2*leg_phase)
    
    # Generate joint positions
    pos = rest_position.copy()
    
    # Head/neck motion
    pos[HEAD] += 0.5 * torso_offset
    pos[NECK] += 0.7 * torso_offset
    
    # Arm motions
    pos[RELBOW] = np.array([0.60, 1.40]) + np.array([arm_swing, 0])
    pos[LELBOW] = np.array([-0.60, 1.40]) + np.array([-arm_swing, 0])
    pos[RHAND] = rest_position[RHAND] + np.array([arm_swing, 0])
    pos[LHAND] = rest_position[LHAND] + np.array([-arm_swing, 0])
    
    # Leg motions
    pos[RKNEE] = torso_center + np.array([0.2, -0.4]) + np.array([-leg_swing, -knee_bend])
    pos[LKNEE] = torso_center + np.array([-0.2, -0.4]) + np.array([leg_swing, -knee_bend])
    pos[RANKLE] = pos[RKNEE] + [leg_swing, -0.4 + foot_angle]
    pos[LANKLE] = pos[LKNEE] + [-leg_swing, -0.4 + foot_angle]
    
    # Adjust for torso movement
    pos[TORSO] = torso_center
    pos[RSHOULDER] += torso_offset
    pos[LSHOULDER] += torso_offset
    pos[RHIP] = torso_center + [0.2, -0.35]
    pos[LHIP] = torso_center + [-0.2, -0.35]
    
    # Apply overall walking motion
    walk_offset = np.array([t * WALKING_SPEED, 0])
    return pos + walk_offset

# Animation loop
def update(frame):
    t = frame * 0.05
    data = get_animation_frame(t)
    points.set_offsets(data)
    return points,

# Create and show animation
num_frames = 100
ani = FuncAnimation(fig, update, frames=num_frames, 
                    interval=50, blit=True)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
