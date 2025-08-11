
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
FRAME_RATE = 30  # Frames per second
CYCLE_PERIOD = 1.0  # One walk cycle in seconds (s)
NUM_FRAMES = int(FRAME_RATE * CYCLE_PERIOD)

# Link lengths (in arbitrary units)
HEAD_NECK = 5
NECK_TORSO = 10
SHOULDER_ELBOW = 15
ELBOW_WRIST = 15
TORSO_HIP = 10
HIP_KNEE = 20
KNEE_ANKLE = 20

# Initial y-positions when standing (adjusted to match lengths)
BASE_POSITIONS = {
    'head': 65,
    'neck': 60,
    'torso_center': 50,
    'left_shoulder': 55,
    'right_shoulder': 55,
    'left_elbow': 40,
    'right_elbow': 40,
    'left_wrist': 25,
    'right_wrist': 25,
    'left_hip': 40,
    'right_hip': 40,
    'left_knee': 20,
    'right_knee': 20,
    'left_ankle': 0,
    'right_ankle': 0
}

# Joint angle amplitudes (in radians)
HIP_AMP = np.pi / 6  # 30 degrees
KNEE_AMP = np.pi / 4  # 45 degrees
SHOULDER_AMP = np.pi / 6  # 30 degrees
ELBOW_AMP = np.pi / 12  # 15 degrees

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-30, 30)
ax.set_ylim(-10, 80)
ax.set_facecolor('black')
plt.axis('off')

# Initialize scatter plot for 15 points
points = ax.scatter([], [], c='white', s=50)

# Define the 15 points in order
POINT_NAMES = [
    'head', 'neck', 'torso_center',
    'left_shoulder', 'right_shoulder',
    'left_elbow', 'right_elbow',
    'left_wrist', 'right_wrist',
    'left_hip', 'right_hip',
    'left_knee', 'right_knee',
    'left_ankle', 'right_ankle'
]

def compute_positions(t):
    """Compute positions of all points at time t."""
    positions = {}
    t_norm = 2 * np.pi * t / CYCLE_PERIOD  # Normalized time for one cycle
    
    # Small vertical bob for "happy" bounce (twice per cycle)
    y_offset = 1 * np.sin(4 * np.pi * t / CYCLE_PERIOD)
    
    # Torso center (fixed x, slight y bounce)
    torso_x = 0
    torso_y = BASE_POSITIONS['torso_center'] + y_offset
    positions['torso_center'] = (torso_x, torso_y)
    
    # Head and neck (aligned with torso, slight bounce)
    positions['neck'] = (torso_x, torso_y + NECK_TORSO)
    positions['head'] = (torso_x, torso_y + NECK_TORSO + HEAD_NECK)
    
    # Hip angles (out of phase for walking)
    right_hip_angle = HIP_AMP * np.sin(t_norm)
    left_hip_angle = HIP_AMP * np.sin(t_norm + np.pi)  # Opposite phase
    
    # Knee angles (flex during swing phase)
    right_knee_angle = KNEE_AMP * (1 + np.sin(t_norm - np.pi/2)) / 2
    left_knee_angle = KNEE_AMP * (1 + np.sin(t_norm + np.pi - np.pi/2)) / 2
    
    # Right leg
    right_hip_x = torso_x + TORSO_HIP * np.sin(right_hip_angle)
    right_hip_y = torso_y - TORSO_HIP * np.cos(right_hip_angle)
    positions['right_hip'] = (right_hip_x, right_hip_y)
    
    right_knee_x = right_hip_x + HIP_KNEE * np.sin(right_hip_angle - right_knee_angle)
    right_knee_y = right_hip_y - HIP_KNEE * np.cos(right_hip_angle - right_knee_angle)
    positions['right_knee'] = (right_knee_x, right_knee_y)
    
    right_ankle_x = right_knee_x + KNEE_ANKLE * np.sin(right_hip_angle - right_knee_angle)
    right_ankle_y = right_knee_y - KNEE_ANKLE * np.cos(right_hip_angle - right_knee_angle)
    positions['right_ankle'] = (right_ankle_x, right_ankle_y)
    
    # Left leg
    left_hip_x = torso_x + TORSO_HIP * np.sin(left_hip_angle)
    left_hip_y = torso_y - TORSO_HIP * np.cos(left_hip_angle)
    positions['left_hip'] = (left_hip_x, left_hip_y)
    
    left_knee_x = left_hip_x + HIP_KNEE * np.sin(left_hip_angle - left_knee_angle)
    left_knee_y = left_hip_y - HIP_KNEE * np.cos(left_hip_angle - left_knee_angle)
    positions['left_knee'] = (left_knee_x, left_knee_y)
    
    left_ankle_x = left_knee_x + KNEE_ANKLE * np.sin(left_hip_angle - left_knee_angle)
    left_ankle_y = left_knee_y - KNEE_ANKLE * np.cos(left_hip_angle - left_knee_angle)
    positions['left_ankle'] = (left_ankle_x, left_ankle_y)
    
    # Shoulder angles (opposite to hips for natural arm swing)
    right_shoulder_angle = -SHOULDER_AMP * np.sin(t_norm)
    left_shoulder_angle = -SHOULDER_AMP * np.sin(t_norm + np.pi)
    
    # Elbow angles (slight bend during swing)
    right_elbow_angle = ELBOW_AMP * (1 + np.sin(t_norm)) / 2
    left_elbow_angle = ELBOW_AMP * (1 + np.sin(t_norm + np.pi)) / 2
    
    # Right arm
    right_shoulder_x = torso_x + TORSO_HIP * np.sin(right_shoulder_angle)
    right_shoulder_y = torso_y + TORSO_HIP * np.cos(right_shoulder_angle)
    positions['right_shoulder'] = (right_shoulder_x, right_shoulder_y)
    
    right_elbow_x = right_shoulder_x + SHOULDER_ELBOW * np.sin(right_shoulder_angle - right_elbow_angle)
    right_elbow_y = right_shoulder_y - SHOULDER_ELBOW * np.cos(right_shoulder_angle - right_elbow_angle)
    positions['right_elbow'] = (right_elbow_x, right_elbow_y)
    
    right_wrist_x = right_elbow_x + ELBOW_WRIST * np.sin(right_shoulder_angle - right_elbow_angle)
    right_wrist_y = right_elbow_y - ELBOW_WRIST * np.cos(right_shoulder_angle - right_elbow_angle)
    positions['right_wrist'] = (right_wrist_x, right_wrist_y)
    
    # Left arm
    left_shoulder_x = torso_x + TORSO_HIP * np.sin(left_shoulder_angle)
    left_shoulder_y = torso_y + TORSO_HIP * np.cos(left_shoulder_angle)
    positions['left_shoulder'] = (left_shoulder_x, left_shoulder_y)
    
    left_elbow_x = left_shoulder_x + SHOULDER_ELBOW * np.sin(left_shoulder_angle - left_elbow_angle)
    left_elbow_y = left_shoulder_y - SHOULDER_ELBOW * np.cos(left_shoulder_angle - left_elbow_angle)
    positions['left_elbow'] = (left_elbow_x, left_elbow_y)
    
    left_wrist_x = left_elbow_x + ELBOW_WRIST * np.sin(left_shoulder_angle - left_elbow_angle)
    left_wrist_y = left_elbow_y - ELBOW_WRIST * np.cos(left_shoulder_angle - left_elbow_angle)
    positions['left_wrist'] = (left_wrist_x, left_wrist_y)
    
    # Return positions as list in order
    return [positions[name] for name in POINT_NAMES]

def update(frame):
    """Update function for animation."""
    t = frame / FRAME_RATE
    pos = compute_positions(t)
    x = [p[0] for p in pos]
    y = [p[1] for p in pos]
    points.set_offsets(np.column_stack((x, y)))
    return points,

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=NUM_FRAMES, interval=1000/FRAME_RATE, blit=True, repeat=True
)

plt.show()
