
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames for the animation
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

# Define keyframe positions for a jumping motion
def get_keyframe_positions(frame, total_frames):
    t = frame / total_frames * 2 * np.pi  # Normalized time
    
    # Key points for a jumping motion (simplified)
    # Head, shoulders, elbows, hands, hips, knees, feet
    # The motion will be a jump forward with arms swinging
    
    # Vertical motion (jump)
    jump_height = 1.5
    vertical = np.sin(t) * jump_height if t <= np.pi else 0  # Only upward phase
    
    # Forward motion (progress)
    forward = t / (2 * np.pi) * 3  # Move forward over time
    
    # Body parts' relative positions
    head_x = forward
    head_y = 1.7 + vertical
    
    shoulder_x = forward
    shoulder_y = 1.5 + vertical
    
    # Arms: swinging during jump
    arm_angle = np.sin(t * 2) * 0.5  # Arms swing back and forth
    left_elbow_x = forward - 0.3 * np.cos(arm_angle)
    left_elbow_y = 1.4 + vertical - 0.3 * np.sin(arm_angle)
    right_elbow_x = forward + 0.3 * np.cos(arm_angle)
    right_elbow_y = 1.4 + vertical - 0.3 * np.sin(arm_angle)
    
    left_hand_x = forward - 0.6 * np.cos(arm_angle)
    left_hand_y = 1.2 + vertical - 0.6 * np.sin(arm_angle)
    right_hand_x = forward + 0.6 * np.cos(arm_angle)
    right_hand_y = 1.2 + vertical - 0.6 * np.sin(arm_angle)
    
    # Hips
    hip_x = forward
    hip_y = 1.0 + vertical
    
    # Legs: bending during jump
    leg_angle = np.sin(t * 2) * 0.4  # Legs bend and extend
    left_knee_x = forward - 0.2 * np.cos(leg_angle)
    left_knee_y = 0.6 + vertical - 0.2 * np.sin(leg_angle)
    right_knee_x = forward + 0.2 * np.cos(leg_angle)
    right_knee_y = 0.6 + vertical - 0.2 * np.sin(leg_angle)
    
    left_foot_x = forward - 0.2 * np.cos(leg_angle)
    left_foot_y = 0.2 + vertical - 0.4 * np.sin(leg_angle)
    right_foot_x = forward + 0.2 * np.cos(leg_angle)
    right_foot_y = 0.2 + vertical - 0.4 * np.sin(leg_angle)
    
    # Additional points for more natural motion (e.g., torso, mid-limbs)
    torso_x = forward
    torso_y = 1.25 + vertical
    
    # Return all points' positions
    return [
        (head_x, head_y),  # 0
        (shoulder_x - 0.2, shoulder_y),  # Left shoulder1
        (shoulder_x + 0.2, shoulder_y),  # Right shoulder2
        (left_elbow_x, left_elbow_y),  # Left elbow3
        (right_elbow_x, right_elbow_y),  # Right elbow4
        (left_hand_x, left_hand_y),  # Left hand5
        (right_hand_x, right_hand_y),  # Right hand6
        (torso_x, torso_y),  # Torso7
        (hip_x - 0.15, hip_y),  # Left hip8
        (hip_x + 0.15, hip_y),  # Right hip9
        (left_knee_x, left_knee_y),  # Left knee10
        (right_knee_x, right_knee_y),  # Right knee11
        (left_foot_x, left_foot_y),  # Left foot12
        (right_foot_x, right_foot_y),  # Right foot13
        (torso_x, hip_y - 0.1)  # Lower torso14
    ]

# Update function for animation
def update(frame):
    positions = get_keyframe_positions(frame, num_frames)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.title('Point-Light Jumping Animation', color='white')
plt.tight_layout()
plt.show()
