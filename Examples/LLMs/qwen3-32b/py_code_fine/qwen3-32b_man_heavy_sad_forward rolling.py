
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

# Define the 15 joints of a human body for biological motion
joint_names = [
    'Hip',
    'Left Knee',
    'Right Knee',
    'Left Ankle',
    'Right Ankle',
    'Spine',
    'Left Shoulder',
    'Right Shoulder',
    'Left Elbow',
    'Right Elbow',
    'Left Wrist',
    'Right Wrist',
    'Neck',
    'Left Head',
    'Right Head'
]

# Number of frames in the animation
num_frames = 120

# Function to simulate the forward rolling of a sad man with heavy weight
def generate_sad_heavy_rolling_motion(num_frames):
    # Time axis for motion
    t = np.linspace(0, 2 * np.pi, num_frames)

    # Base joint positions (Hip, Spine, Neck) - forward rolling
    hip_x = np.sin(t)
    hip_y = np.cos(t) * 0.2 + 0.5
    spine_x = hip_x + 0.1 * np.sin(t)
    spine_y = hip_y + 0.1 * np.cos(t)
    neck_x = spine_x + 0.1 * np.sin(t)
    neck_y = spine_y + 0.1 * np.cos(t)

    # Left leg joints - forward rolling with heavy weight
    left_knee_x = hip_x - 0.3 * np.sin(t)
    left_knee_y = hip_y - 0.3 * np.cos(t)
    left_ankle_x = left_knee_x - 0.3 * np.sin(t)
    left_ankle_y = left_knee_y - 0.3 * np.cos(t)

    # Right leg joints - forward rolling with heavy weight
    right_knee_x = hip_x + 0.3 * np.sin(t)
    right_knee_y = hip_y - 0.3 * np.cos(t)
    right_ankle_x = right_knee_x + 0.3 * np.sin(t)
    right_ankle_y = right_knee_y - 0.3 * np.cos(t)

    # Left arm joints - forward rolling with heavy weight
    left_shoulder_x = spine_x - 0.2 * np.sin(t)
    left_shoulder_y = spine_y + 0.1 * np.cos(t)
    left_elbow_x = left_shoulder_x - 0.3 * np.sin(t)
    left_elbow_y = left_shoulder_y - 0.2 * np.cos(t)
    left_wrist_x = left_elbow_x - 0.3 * np.sin(t)
    left_wrist_y = left_elbow_y - 0.2 * np.cos(t)

    # Right arm joints - forward rolling with heavy weight
    right_shoulder_x = spine_x + 0.2 * np.sin(t)
    right_shoulder_y = spine_y + 0.1 * np.cos(t)
    right_elbow_x = right_shoulder_x + 0.3 * np.sin(t)
    right_elbow_y = right_shoulder_y - 0.2 * np.cos(t)
    right_wrist_x = right_elbow_x + 0.3 * np.sin(t)
    right_wrist_y = right_elbow_y - 0.2 * np.cos(t)

    # Head
    left_head_x = neck_x - 0.1 * np.sin(t)
    left_head_y = neck_y + 0.1 * np.cos(t)
    right_head_x = neck_x + 0.1 * np.sin(t)
    right_head_y = neck_y + 0.1 * np.cos(t)

    # Combine all joint positions
    positions = np.array([
        (hip_x, hip_y),
        (left_knee_x, left_knee_y),
        (right_knee_x, right_knee_y),
        (left_ankle_x, left_ankle_y),
        (right_ankle_x, right_ankle_y),
        (spine_x, spine_y),
        (left_shoulder_x, left_shoulder_y),
        (right_shoulder_x, right_shoulder_y),
        (left_elbow_x, left_elbow_y),
        (right_elbow_x, right_elbow_y),
        (left_wrist_x, left_wrist_y),
        (right_wrist_x, right_wrist_y),
        (neck_x, neck_y),
        (left_head_x, left_head_y),
        (right_head_x, right_head_y)
    ])

    # Normalize to fit in [0, 1] range
    positions = (positions - positions.min(axis=1, keepdims=True)) / (positions.max(axis=1, keepdims=True) - positions.min(axis=1, keepdims=True))

    return positions

# Generate the motion
joint_positions = generate_sad_heavy_rolling_motion(num_frames)

# Define connections between joints for drawing lines
connections = [
    (0, 5),  # Hip to Spine
    (5, 12), # Spine to Neck
    (12, 13), # Neck to Left Head
    (12, 14), # Neck to Right Head
    (5, 6),  # Spine to Left Shoulder
    (5, 7),  # Spine to Right Shoulder
    (6, 8),  # Left Shoulder to Left Elbow
    (8, 10), # Left Elbow to Left Wrist
    (7, 9),  # Right Shoulder to Right Elbow
    (9, 11), # Right Elbow to Right Wrist
    (0, 1),  # Hip to Left Knee
    (1, 3),  # Left Knee to Left Ankle
    (0, 2),  # Hip to Right Knee
    (2, 4)   # Right Knee to Right Ankle
]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Create point lights (white circles)
points = [plt.Circle((0, 0), radius=0.01, color='white') for _ in range(15)]
for point in points:
    ax.add_patch(point)

# Create connection lines
lines = [ConnectionPatch((0, 0), (0, 0), "data", "data", color='white', linewidth=1) for _ in connections]
for line in lines:
    ax.add_artist(line)

# Function to update the animation
def update(frame):
    for i, point in enumerate(points):
        x, y = joint_positions[i, :, frame]
        point.center = (x, y)
    for i, ((start, end), line) in enumerate(zip(connections, lines)):
        x1, y1 = joint_positions[start, :, frame]
        x2, y2 = joint_positions[end, :, frame]
        line.set_positions((x1, y1), (x2, y2))
    return points + lines

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
