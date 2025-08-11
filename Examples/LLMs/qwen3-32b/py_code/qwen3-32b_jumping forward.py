
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the joints of a human body (15 joints)
joint_names = [
    'left_ankle', 'left_knee', 'left_hip', 'right_ankle', 'right_knee', 'right_hip',
    'left_wrist', 'left_elbow', 'left_shoulder', 'right_wrist', 'right_elbow', 'right_shoulder',
    'head', 'spine', 'pelvis'
]

# Define the initial positions of the joints (in 2D)
def generate_jump_forward_animation(frames=60, fps=30):
    # Time parameters
    t = np.linspace(0, 2, frames)
    
    # Motion parameters
    jump_height = 1.0
    jump_distance = 2.0
    leg_length = 1.0
    arm_length = 0.8
    spine_length = 1.0

    # Base positions (pelvis as origin)
    base_positions = np.array([
        [0, 0], [0, leg_length], [0, 2*leg_length], [0, 0], [0, leg_length], [0, 2*leg_length],
        [0, 0], [0, arm_length], [0, 2*arm_length], [0, 0], [0, arm_length], [0, 2*arm_length],
        [0, 3*leg_length], [0, 1.5*leg_length], [0, 0]
    ])

    # Animation
    positions = []
    for i in range(frames):
        # Forward jump movement
        x_offset = jump_distance * (1 - np.cos(np.pi * t[i])) / 2
        y_offset = jump_height * np.sin(np.pi * t[i])
        
        # Apply forward jump to all joints
        joint_pos = base_positions.copy()
        joint_pos[:, 0] += x_offset
        joint_pos[:, 1] += y_offset

        # Add some leg and arm motion for realism
        leg_angle = 0.5 * np.sin(2 * np.pi * t[i])
        arm_angle = 0.5 * np.sin(2 * np.pi * t[i] + np.pi)

        # Left leg
        joint_pos[0] = joint_pos[1] + [leg_length * np.sin(leg_angle), -leg_length * np.cos(leg_angle)]
        joint_pos[1] = joint_pos[2] + [0, -leg_length]
        # Right leg
        joint_pos[3] = joint_pos[4] + [leg_length * np.sin(-leg_angle), -leg_length * np.cos(-leg_angle)]
        joint_pos[4] = joint_pos[5] + [0, -leg_length]
        # Left arm
        joint_pos[6] = joint_pos[7] + [arm_length * np.sin(arm_angle), -arm_length * np.cos(arm_angle)]
        joint_pos[7] = joint_pos[8] + [0, -arm_length]
        # Right arm
        joint_pos[9] = joint_pos[10] + [arm_length * np.sin(-arm_angle), -arm_length * np.cos(-arm_angle)]
        joint_pos[10] = joint_pos[11] + [0, -arm_length]
        # Head and spine
        joint_pos[12] = joint_pos[13] + [0, spine_length]
        joint_pos[13] = joint_pos[14] + [0, spine_length]

        positions.append(joint_pos)

    return np.array(positions)

# Generate the animation data
positions = generate_jump_forward_animation()

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.set_aspect('equal')
ax.axis('off')

# Create point lights (white dots)
points, = ax.plot([], [], 'wo', markersize=10)

# Initialization function
def init():
    points.set_data([], [])
    return points,

# Animation function
def update(frame):
    x = positions[frame, :, 0]
    y = positions[frame, :, 1]
    points.set_data(x, y)
    return points,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(positions), init_func=init, blit=True, interval=1000 / 30)

# Display the animation
plt.show()
