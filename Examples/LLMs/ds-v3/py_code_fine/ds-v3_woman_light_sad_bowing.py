
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
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define the motion of a bowing sad woman
def get_positions(frame):
    t = frame / num_frames * 2 * np.pi  # Normalized time
    
    # Head
    head_x = 0
    head_y = 0.8 - 0.5 * np.sin(t * 2)  # Bowing motion
    
    # Shoulders
    shoulder_y = head_y - 0.2
    left_shoulder_x = -0.2
    right_shoulder_x = 0.2
    
    # Elbows
    elbow_y = shoulder_y - 0.2
    left_elbow_x = -0.25 + 0.05 * np.sin(t * 4)
    right_elbow_x = 0.25 - 0.05 * np.sin(t * 4)
    
    # Hands
    hand_y = elbow_y - 0.2
    left_hand_x = -0.3 + 0.1 * np.sin(t * 4 + np.pi/4)
    right_hand_x = 0.3 - 0.1 * np.sin(t * 4 + np.pi/4)
    
    # Torso
    torso_top_y = shoulder_y
    torso_bottom_y = torso_top_y - 0.4
    torso_x = 0
    
    # Hips
    hip_y = torso_bottom_y
    left_hip_x = -0.15
    right_hip_x = 0.15
    
    # Knees
    knee_y = hip_y - 0.4 + 0.1 * np.sin(t * 2)  # Slight bending
    left_knee_x = -0.1
    right_knee_x = 0.1
    
    # Feet
    foot_y = knee_y - 0.4
    left_foot_x = -0.1
    right_foot_x = 0.1
    
    # Combine all points
    positions = np.array([head_x, head_y]),  # Head
np.array([left_shoulder_x, shoulder_y]),  # Left shoulder
np.array([right_shoulder_x, shoulder_y]),  # Right shoulder
np.array([left_elbow_x, elbow_y]),  # Left elbow
np.array([right_elbow_x, elbow_y]),  # Right elbow
np.array([left_hand_x, hand_y]),  # Left hand
np.array([right_hand_x, hand_y]),  # Right hand
np.array([torso_x, (torso_top_y + torso_bottom_y)/2]),  # Mid torso
np.array([left_hip_x, hip_y]),  # Left hip
np.array([right_hip_x, hip_y]),  # Right hip
np.array([left_knee_x, knee_y]),  # Left knee
np.array([right_knee_x, knee_y]),  # Right knee
np.array([left_foot_x, foot_y]),  # Left foot
np.array([right_foot_x, foot_y]),  # Right foot
np.array([0, torso_bottom_y - 0.2])  # Additional point for realism (e.g., belly)
    
    return positions

# Update function for animation
def update(frame):
    positions = get_positions(frame)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
