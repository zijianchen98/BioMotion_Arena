
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define keyframes for the sitting down motion
def get_keyframe(t):
    # t is a parameter between 0 and 1 representing the progress of the motion
    
    # Key joint positions (simplified model)
    # Head, shoulders, elbows, hands, hips, knees, feet
    # Coordinates are relative to the hip position
    
    # Standing pose (t=0)
    if t == 0:
        return np.array([
            [0.0, 1.6],    # head
            [-0.3, 1.3],   # left shoulder
            [0.3, 1.3],    # right shoulder
            [-0.4, 1.0],   # left elbow
            [0.4, 1.0],    # right elbow
            [-0.5, 0.8],   # left hand
            [0.5, 0.8],    # right hand
            [-0.2, 1.0],   # left hip (fixed)
            [0.2, 1.0],    # right hip (fixed)
            [-0.2, 0.4],   # left knee
            [0.2, 0.4],    # right knee
            [-0.2, 0.0],   # left foot
            [0.2, 0.0],    # right foot
            [0.0, 1.45],   # neck (extra point)
            [0.0, 0.7]     # torso (extra point)
        ])
    
    # Sitting pose (t=1)
    elif t == 1:
        return np.array([
            [0.0, 1.2],    # head
            [-0.3, 1.0],   # left shoulder
            [0.3, 1.0],    # right shoulder
            [-0.4, 0.8],   # left elbow
            [0.4, 0.8],    # right elbow
            [-0.5, 0.6],   # left hand
            [0.5, 0.6],    # right hand
            [-0.2, 1.0],   # left hip (fixed)
            [0.2, 1.0],    # right hip (fixed)
            [-0.2, 0.1],   # left knee (bent)
            [0.2, 0.1],    # right knee (bent)
            [-0.2, -0.2],  # left foot (forward)
            [0.2, -0.2],   # right foot (forward)
            [0.0, 1.1],    # neck
            [0.0, 0.9]     # torso
        ])
    
    # Interpolate between standing and sitting
    standing = get_keyframe(0)
    sitting = get_keyframe(1)
    
    # Apply easing function for more natural motion
    # Using a smoothstep function
    ease_t = t * t * (3 - 2 * t)
    
    # Different parts move at slightly different times
    # Head and torso move first
    head_t = min(1, t * 1.5)
    torso_t = min(1, t * 1.3)
    arms_t = min(1, t * 1.1)
    legs_t = t
    
    # Interpolate each point with different timing
    frame = np.zeros_like(standing)
    
    # Head and neck (points 0 and 13)
    frame[0] = standing[0] + (sitting[0] - standing[0]) * head_t
    frame[13] = standing[13] + (sitting[13] - standing[13]) * head_t
    
    # Shoulders (points 1, 2)
    frame[1] = standing[1] + (sitting[1] - standing[1]) * torso_t
    frame[2] = standing[2] + (sitting[2] - standing[2]) * torso_t
    
    # Arms (points 3, 4, 5, 6)
    frame[3] = standing[3] + (sitting[3] - standing[3]) * arms_t
    frame[4] = standing[4] + (sitting[4] - standing[4]) * arms_t
    frame[5] = standing[5] + (sitting[5] - standing[5]) * arms_t
    frame[6] = standing[6] + (sitting[6] - standing[6]) * arms_t
    
    # Hips don't move (points 7, 8)
    frame[7] = standing[7]
    frame[8] = standing[8]
    
    # Legs (points 9, 10, 11, 12)
    frame[9] = standing[9] + (sitting[9] - standing[9]) * legs_t
    frame[10] = standing[10] + (sitting[10] - standing[10]) * legs_t
    frame[11] = standing[11] + (sitting[11] - standing[11]) * legs_t
    frame[12] = standing[12] + (sitting[12] - standing[12]) * legs_t
    
    # Torso (point 14)
    frame[14] = standing[14] + (sitting[14] - standing[14]) * torso_t
    
    return frame

# Animation update function
def update(frame_num):
    # Total animation frames
    total_frames = 60
    
    # Current progress (0 to 1)
    t = frame_num / total_frames
    
    # Get the current keyframe
    current_frame = get_keyframe(t)
    
    # Update point positions
    points.set_data(current_frame[:, 0], current_frame[:, 1])
    
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=60, interval=50, blit=True
)

plt.tight_layout()
plt.show()
