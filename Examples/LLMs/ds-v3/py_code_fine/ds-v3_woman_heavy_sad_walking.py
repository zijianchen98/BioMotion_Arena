
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define key points for a walking motion (simplified)
# Points could represent head, shoulders, elbows, hands, hips, knees, feet, etc.
def get_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Time parameter
    
    # Main body movement (vertical and horizontal sway)
    body_x = 0.2 * np.sin(t * 2)  # Side-to-side sway
    body_y = 0.1 * np.sin(t) + 1.0  # Up-down movement
    
    # Head
    head_x = body_x
    head_y = body_y + 0.3
    
    # Shoulders
    shoulder_width = 0.4
    left_shoulder_x = body_x - shoulder_width/2
    left_shoulder_y = body_y + 0.2
    right_shoulder_x = body_x + shoulder_width/2
    right_shoulder_y = body_y + 0.2
    
    # Arms (elbows and hands)
    arm_swing = 0.3 * np.sin(t * 2)
    left_elbow_x = left_shoulder_x - 0.1
    left_elbow_y = left_shoulder_y - 0.2 + 0.1 * np.sin(t * 2 + np.pi/2)
    left_hand_x = left_elbow_x - 0.1
    left_hand_y = left_elbow_y - 0.2 + 0.1 * np.sin(t * 2 + np.pi/2)
    
    right_elbow_x = right_shoulder_x + 0.1
    right_elbow_y = right_shoulder_y - 0.2 + 0.1 * np.sin(t * 2 + np.pi/2)
    right_hand_x = right_elbow_x + 0.1
    right_hand_y = right_elbow_y - 0.2 + 0.1 * np.sin(t * 2 + np.pi/2)
    
    # Hips
    hip_width = 0.3
    left_hip_x = body_x - hip_width/2
    left_hip_y = body_y - 0.2
    right_hip_x = body_x + hip_width/2
    right_hip_y = body_y - 0.2
    
    # Legs (knees and feet)
    leg_swing = 0.4 * np.sin(t * 2)
    left_knee_x = left_hip_x - 0.1 * np.sin(t * 2)
    left_knee_y = left_hip_y - 0.3 + 0.1 * np.cos(t * 2)
    left_foot_x = left_knee_x - 0.1 * np.sin(t * 2)
    left_foot_y = left_knee_y - 0.3 + 0.1 * np.cos(t * 2)
    
    right_knee_x = right_hip_x + 0.1 * np.sin(t * 2)
    right_knee_y = right_hip_y - 0.3 - 0.1 * np.cos(t * 2)
    right_foot_x = right_knee_x + 0.1 * np.sin(t * 2)
    right_foot_y = right_knee_y - 0.3 - 0.1 * np.cos(t * 2)
    
    # Additional points for more natural motion (e.g., torso, mid-spine)
    mid_spine_x = body_x
    mid_spine_y = body_y
    
    # Return all points' positions
    return [
        (head_x, head_y),  # 0: head
        (left_shoulder_x, left_shoulder_y),  # 1: left shoulder
        (right_shoulder_x, right_shoulder_y),  # 2: right shoulder
        (left_elbow_x, left_elbow_y),  # 3: left elbow
        (right_elbow_x, right_elbow_y),  # 4: right elbow
        (left_hand_x, left_hand_y),  # 5: left hand
        (right_hand_x, right_hand_y),  # 6: right hand
        (left_hip_x, left_hip_y),  # 7: left hip
        (right_hip_x, right_hip_y),  # 8: right hip
        (left_knee_x, left_knee_y),  # 9: left knee
        (right_knee_x, right_knee_y),  # 10: right knee
        (left_foot_x, left_foot_y),  # 11: left foot
        (right_foot_x, right_foot_y),  # 12: right foot
        (mid_spine_x, mid_spine_y),  # 13: mid spine
        (body_x, body_y - 0.1)  # 14: lower spine
    ]

# Update function for animation
def update(frame):
    positions = get_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.title('Biological Motion: Sad Woman Walking', color='white')
plt.tight_layout()
plt.show()
