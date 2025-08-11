
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
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for the running motion (simplified)
def get_keyframes():
    # Keyframes for each point (x, y positions over time)
    # This is a simplified approximation of a running motion
    keyframes = np.zeros((num_frames, num_points, 2))
    
    # Torso (point 0)
    keyframes[:, 0, 0] = 0  # x position (centered)
    keyframes[:, 0, 1] = 1.5 + 0.1 * np.sin(np.linspace(0, 4*np.pi, num_frames))  # y position (bobbing)
    
    # Head (point 1)
    keyframes[:, 1, 0] = 0  # x position
    keyframes[:, 1, 1] = keyframes[:, 0, 1] + 0.3  # above torso
    
    # Shoulders (points 2 and 3)
    shoulder_width = 0.4
    keyframes[:, 2, 0] = -shoulder_width  # left shoulder
    keyframes[:, 2, 1] = keyframes[:, 0, 1] + 0.1
    keyframes[:, 3, 0] = shoulder_width  # right shoulder
    keyframes[:, 3, 1] = keyframes[:, 0, 1] + 0.1
    
    # Arms (points 4-7: elbows and hands)
    arm_swing = 0.5 * np.sin(np.linspace(0, 4*np.pi, num_frames))
    # Left arm
    keyframes[:, 4, 0] = -shoulder_width - 0.2 * np.sin(arm_swing)  # left elbow
    keyframes[:, 4, 1] = keyframes[:, 0, 1] - 0.2 * np.cos(arm_swing)
    keyframes[:, 5, 0] = -shoulder_width - 0.4 * np.sin(arm_swing + 0.3)  # left hand
    keyframes[:, 5, 1] = keyframes[:, 0, 1] - 0.4 * np.cos(arm_swing + 0.3)
    # Right arm (opposite phase)
    keyframes[:, 6, 0] = shoulder_width + 0.2 * np.sin(arm_swing)  # right elbow
    keyframes[:, 6, 1] = keyframes[:, 0, 1] - 0.2 * np.cos(arm_swing)
    keyframes[:, 7, 0] = shoulder_width + 0.4 * np.sin(arm_swing + 0.3)  # right hand
    keyframes[:, 7, 1] = keyframes[:, 0, 1] - 0.4 * np.cos(arm_swing + 0.3)
    
    # Hips (points 8 and 9)
    hip_width = 0.3
    keyframes[:, 8, 0] = -hip_width  # left hip
    keyframes[:, 8, 1] = keyframes[:, 0, 1] - 0.3
    keyframes[:, 9, 0] = hip_width  # right hip
    keyframes[:, 9, 1] = keyframes[:, 0, 1] - 0.3
    
    # Legs (points 10-13: knees and feet)
    leg_swing = 0.7 * np.sin(np.linspace(0, 4*np.pi, num_frames))
    # Left leg
    keyframes[:, 10, 0] = -hip_width - 0.1 * np.sin(leg_swing)  # left knee
    keyframes[:, 10, 1] = keyframes[:, 0, 1] - 0.6 - 0.2 * np.cos(leg_swing)
    keyframes[:, 11, 0] = -hip_width - 0.2 * np.sin(leg_swing + 0.3)  # left foot
    keyframes[:, 11, 1] = keyframes[:, 0, 1] - 1.0 - 0.3 * np.cos(leg_swing + 0.3)
    # Right leg (opposite phase)
    keyframes[:, 12, 0] = hip_width + 0.1 * np.sin(leg_swing)  # right knee
    keyframes[:, 12, 1] = keyframes[:, 0, 1] - 0.6 - 0.2 * np.cos(leg_swing)
    keyframes[:, 13, 0] = hip_width + 0.2 * np.sin(leg_swing + 0.3)  # right foot
    keyframes[:, 13, 1] = keyframes[:, 0, 1] - 1.0 - 0.3 * np.cos(leg_swing + 0.3)
    
    # Additional point for realism (e.g., mid-torso or another joint)
    keyframes[:, 14, 0] = 0  # mid-torso
    keyframes[:, 14, 1] = keyframes[:, 0, 1] - 0.15
    
    return keyframes

keyframes = get_keyframes()

# Update function for animation
def update(frame):
    for i, point in enumerate(points):
        point.center = keyframes[frame, i, 0], keyframes[frame, i, 1]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
