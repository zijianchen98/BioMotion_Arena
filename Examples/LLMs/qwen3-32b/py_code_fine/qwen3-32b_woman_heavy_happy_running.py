
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Define the joints for a human figure (15 points)
joint_names = [
    'Hip', 'Right Hip', 'Right Knee', 'Right Ankle',
    'Left Hip', 'Left Knee', 'Left Ankle',
    'Spine', 'Shoulder', 'Right Shoulder', 'Right Elbow', 'Right Wrist',
    'Left Shoulder', 'Left Elbow', 'Left Wrist'
]

# Resting joint positions (relative to Hip)
resting_positions = np.array([
    [0.0, 0.0],   # Hip
    [0.5, -1.0],  # Right Hip
    [0.5, -2.5],  # Right Knee
    [0.5, -4.0],  # Right Ankle
    [-0.5, -1.0], # Left Hip
    [-0.5, -2.5], # Left Knee
    [-0.5, -4.0], # Left Ankle
    [0.0, 1.0],   # Spine
    [0.0, 2.5],   # Shoulder
    [1.0, 2.0],   # Right Shoulder
    [1.5, 1.0],   # Right Elbow
    [1.5, 0.0],   # Right Wrist
    [-1.0, 2.0],  # Left Shoulder
    [-1.5, 1.0],  # Left Elbow
    [-1.5, 0.0],  # Left Wrist
])

# Parameters for animation
frame_rate = 30
duration = 5  # seconds
num_frames = frame_rate * duration

# Generate motion over time
def generate_motion(t, amplitude=0.5, frequency=1.5, phase_shift=0):
    return amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)

positions = []
for frame in range(num_frames):
    t = frame / frame_rate

    # Basic running motion
    hip_offset = generate_motion(t, amplitude=0.2, frequency=2.0)
    right_leg_offset = generate_motion(t + 0.1, amplitude=0.5, frequency=2.0)
    left_leg_offset = generate_motion(t - 0.1, amplitude=0.5, frequency=2.0)
    spine_offset = generate_motion(t, amplitude=0.1, frequency=1.0)
    arm_offset = generate_motion(t, amplitude=0.3, frequency=1.5)

    current_positions = resting_positions.copy()

    # Adjust positions based on motion
    current_positions[0] = [0.0, 0.0 + hip_offset]  # Hip

    current_positions[1] = [0.5 + right_leg_offset, -1.0 + hip_offset]  # Right Hip
    current_positions[2] = [0.5 + right_leg_offset, -2.5 + hip_offset]  # Right Knee
    current_positions[3] = [0.5 + right_leg_offset, -4.0 + hip_offset]  # Right Ankle

    current_positions[4] = [-0.5 + left_leg_offset, -1.0 + hip_offset]  # Left Hip
    current_positions[5] = [-0.5 + left_leg_offset, -2.5 + hip_offset]  # Left Knee
    current_positions[6] = [-0.5 + left_leg_offset, -4.0 + hip_offset]  # Left Ankle

    current_positions[7] = [0.0, 1.0 + spine_offset]  # Spine
    current_positions[8] = [0.0, 2.5 + spine_offset]  # Shoulder

    current_positions[9] = [1.0 + arm_offset, 2.0 + spine_offset]  # Right Shoulder
    current_positions[10] = [1.5 + arm_offset, 1.0 + spine_offset]  # Right Elbow
    current_positions[11] = [1.5 + arm_offset, 0.0 + spine_offset]  # Right Wrist

    current_positions[12] = [-1.0 - arm_offset, 2.0 + spine_offset]  # Left Shoulder
    current_positions[13] = [-1.5 - arm_offset, 1.0 + spine_offset]  # Left Elbow
    current_positions[14] = [-1.5 - arm_offset, 0.0 + spine_offset]  # Left Wrist

    positions.append(current_positions)

positions = np.array(positions)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot for point lights
scat = ax.scatter([], [], c='white', s=100)

# Animation update function
def update(frame):
    scat.set_offsets(positions[frame])
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000 / frame_rate, blit=True)

# Display the animation
plt.show()
