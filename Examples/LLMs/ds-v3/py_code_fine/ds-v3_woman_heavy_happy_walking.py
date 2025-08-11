
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60  # Number of frames in the animation
fps = 30  # Frames per second

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define walking motion parameters
def get_point_positions(t):
    # Time-dependent parameters for walking motion
    stride_length = 1.5
    step_height = 0.3
    arm_swing = 0.5
    body_bob = 0.1
    
    # Main body points (e.g., head, torso, hips)
    head_x = 0
    head_y = 1.5 + body_bob * np.sin(t * 2 * np.pi)
    
    torso_x = 0
    torso_y = 1.0 + body_bob * np.sin(t * 2 * np.pi)
    
    hip_x = 0
    hip_y = 0.5 + body_bob * np.sin(t * 2 * np.pi)
    
    # Legs (heavy weight implies wider stance)
    left_leg_phase = t * 2 * np.pi
    right_leg_phase = left_leg_phase + np.pi
    
    left_foot_x = -0.2 + stride_length * np.sin(left_leg_phase)
    left_foot_y = -0.5 + step_height * np.abs(np.sin(left_leg_phase))
    
    right_foot_x = 0.2 + stride_length * np.sin(right_leg_phase)
    right_foot_y = -0.5 + step_height * np.abs(np.sin(right_leg_phase))
    
    left_knee_x = -0.2 + 0.5 * stride_length * np.sin(left_leg_phase)
    left_knee_y = 0.0 + 0.3 * step_height * np.abs(np.sin(left_leg_phase))
    
    right_knee_x = 0.2 + 0.5 * stride_length * np.sin(right_leg_phase)
    right_knee_y = 0.0 + 0.3 * step_height * np.abs(np.sin(right_leg_phase))
    
    # Arms (happy implies more pronounced arm swing)
    left_arm_phase = t * 2 * np.pi + np.pi/2
    right_arm_phase = left_arm_phase + np.pi
    
    left_hand_x = -0.5 + arm_swing * np.sin(left_arm_phase)
    left_hand_y = 1.0 + 0.2 * np.sin(left_arm_phase)
    
    right_hand_x = 0.5 + arm_swing * np.sin(right_arm_phase)
    right_hand_y = 1.0 + 0.2 * np.sin(right_arm_phase)
    
    left_elbow_x = -0.3 + 0.3 * arm_swing * np.sin(left_arm_phase)
    left_elbow_y = 1.0 + 0.1 * np.sin(left_arm_phase)
    
    right_elbow_x = 0.3 + 0.3 * arm_swing * np.sin(right_arm_phase)
    right_elbow_y = 1.0 + 0.1 * np.sin(right_arm_phase)
    
    # Additional points for more natural motion (e.g., shoulders, waist)
    left_shoulder_x = -0.2
    left_shoulder_y = 1.2 + 0.05 * np.sin(t * 2 * np.pi)
    
    right_shoulder_x = 0.2
    right_shoulder_y = 1.2 + 0.05 * np.sin(t * 2 * np.pi)
    
    left_waist_x = -0.15
    left_waist_y = 0.7 + 0.05 * np.sin(t * 2 * np.pi)
    
    right_waist_x = 0.15
    right_waist_y = 0.7 + 0.05 * np.sin(t * 2 * np.pi)
    
    # Return all point positions
    return [
        (head_x, head_y),  # Head
        (torso_x, torso_y),  # Torso
        (hip_x, hip_y),  # Hip
        (left_shoulder_x, left_shoulder_y),  # Left shoulder
        (right_shoulder_x, right_shoulder_y),  # Right shoulder
        (left_elbow_x, left_elbow_y),  # Left elbow
        (right_elbow_x, right_elbow_y_),  # Right elbow
        (left_hand_x, left_hand_y),  # Left hand
        (right_hand_x, right_hand_y),  # Right hand
        (left_waist_x, left_waist_y),  # Left waist
        (right_waist_x, right_waist_y),  # Right waist
        (left_knee_x, left_knee_y),  # Left knee
        (right_knee_x, right_knee_y),  # Right knee
        (left_foot_x, left_foot_y),  # Left foot
        (right_foot_x, right_foot_y)  # Right foot
    ]

# Update function for animation
def update(frame):
    t = frame / num_frames
    positions = get_point_positions(t)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
