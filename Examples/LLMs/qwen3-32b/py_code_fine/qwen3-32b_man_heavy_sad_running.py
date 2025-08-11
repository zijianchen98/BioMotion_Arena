
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# Define the joint positions relative to the body (in normalized units)
joint_names = [
    'left shoulder',
    'right shoulder',
    'left elbow',
    'right elbow',
    'left hand',
    'right hand',
    'torso center',
    'left hip',
    'right hip',
    'left knee',
    'right knee',
    'left foot',
    'right foot',
    'head center',
    'neck center'
]

# Initial joint positions (relative to torso center)
joint_positions = [
    [-0.1, 0.4],  # left shoulder
    [0.1, 0.4],   # right shoulder
    [-0.1, 0.2],  # left elbow
    [0.1, 0.2],   # right elbow
    [-0.1, 0.0],  # left hand
    [0.1, 0.0],   # right hand
    [0.0, 0.0],   # torso center
    [-0.1, -0.4], # left hip
    [0.1, -0.4],  # right hip
    [-0.1, -0.8], # left knee
    [0.1, -0.8],  # right knee
    [-0.1, -1.2], # left foot
    [0.1, -1.2],  # right foot
    [0.0, 0.6],   # head center
    [0.0, 0.5],   # neck center
]

# Normalize joint positions around torso center
joint_positions = np.array(joint_positions)
torso = joint_positions[6]
joint_positions -= torso

# Animation parameters
num_frames = 120
speed = 0.05  # Walking speed
step_height = 0.2  # Height of foot lift
sad_weight_factor = 0.8  # Factor to make movement slower and heavier

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create scatter points for the joints
scat = ax.scatter([], [], color='white', s=100)

# Function to update the positions for each frame
def update(frame):
    t = frame * speed
    positions = []

    # Torso movement (slightly forward and up-down to simulate running)
    torso_x = 0.0 + 0.1 * math.sin(t)
    torso_y = 0.0 + 0.05 * math.sin(t)

    # Arm movement (simulating running arms)
    arm_offset = 0.1 * math.sin(t + math.pi)
    arm_offset *= sad_weight_factor  # Make it heavier

    # Arm angles
    left_arm_angle = math.pi / 4 * math.sin(t)
    right_arm_angle = -math.pi / 4 * math.sin(t)

    # Left arm
    left_shoulder = np.array([-0.1, 0.4]) + [torso_x, torso_y]
    left_elbow = left_shoulder + 0.2 * np.array([math.cos(left_arm_angle), math.sin(left_arm_angle)])
    left_hand = left_elbow + 0.2 * np.array([math.cos(left_arm_angle), math.sin(left_arm_angle)])

    # Right arm
    right_shoulder = np.array([0.1, 0.4]) + [torso_x, torso_y]
    right_elbow = right_shoulder + 0.2 * np.array([math.cos(right_arm_angle), math.sin(right_arm_angle)])
    right_hand = right_elbow + 0.2 * np.array([math.cos(right_arm_angle), math.sin(right_arm_angle)])

    # Leg movement (simulating running with heavy step)
    left_leg_angle = math.pi / 2 * math.sin(t)
    right_leg_angle = math.pi / 2 * math.sin(t + math.pi)

    # Left leg
    left_hip = np.array([-0.1, -0.4]) + [torso_x, torso_y]
    left_knee = left_hip + 0.4 * np.array([math.cos(left_leg_angle), math.sin(left_leg_angle)])
    left_foot = left_knee + 0.4 * np.array([math.cos(left_leg_angle), math.sin(left_leg_angle)])
    left_foot[1] += step_height * math.sin(left_leg_angle)  # Add foot lift

    # Right leg
    right_hip = np.array([0.1, -0.4]) + [torso_x, torso_y]
    right_knee = right_hip + 0.4 * np.array([math.cos(right_leg_angle), math.sin(right_leg_angle)])
    right_foot = right_knee + 0.4 * np.array([math.cos(right_leg_angle), math.sin(right_leg_angle)])
    right_foot[1] += step_height * math.sin(right_leg_angle)  # Add foot lift

    # Head movement
    head_center = np.array([0.0, 0.6]) + [torso_x, torso_y]
    head_center[1] += 0.02 * math.sin(t)  # Small up-down head movement for realism

    # Neck center
    neck_center = np.array([0.0, 0.5]) + [torso_x, torso_y]
    neck_center[1] += 0.01 * math.sin(t)  # Small up-down head movement for realism

    # Collect all joint positions
    positions.append(left_shoulder)
    positions.append(right_shoulder)
    positions.append(left_elbow)
    positions.append(right_elbow)
    positions.append(left_hand)
    positions.append(right_hand)
    positions.append(np.array([torso_x, torso_y]))
    positions.append(left_hip)
    positions.append(right_hip)
    positions.append(left_knee)
    positions.append(right_knee)
    positions.append(left_foot)
    positions.append(right_foot)
    positions.append(head_center)
    positions.append(neck_center)

    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
