
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import patches

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.5, 2.5)
ax.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define key points for the jumping motion (simplified)
# Each point represents a joint or key body part (head, shoulders, elbows, hands, hips, knees, feet)
# The motion will interpolate between these key frames

# Key frames for the jumping motion (positions at different phases)
# Each key frame is a list of (x, y) coordinates for the 15 points
key_frames = [
    # Start: standing
    [
        (0.0, 1.7),    # head
        (0.0, 1.5),    # neck
        (-0.2, 1.4), (0.2, 1.4),  # shoulders
        (-0.3, 1.2), (0.3, 1.2),  # elbows
        (-0.4, 1.0), (0.4, 1.0),  # hands
        (0.0, 1.0),    # torso mid
        (-0.2, 0.7), (0.2, 0.7),  # hips
        (-0.2, 0.4), (0.2, 0.4),  # knees
        (-0.2, 0.0), (0.2, 0.0)   # feet
    ],
    # Crouch before jump
    [
        (0.0, 1.6),
        (0.0, 1.4),
        (-0.2, 1.3), (0.2, 1.3),
        (-0.3, 1.1), (0.3, 1.1),
        (-0.4, 0.9), (0.4, 0.9),
        (0.0, 0.8),
        (-0.2, 0.6), (0.2, 0.6),
        (-0.2, 0.3), (0.2, 0.3),
        (-0.2, 0.0), (0.2, 0.0)
    ],
    # Mid-jump (apex)
    [
        (0.0, 2.2),
        (0.0, 2.0),
        (-0.2, 1.9), (0.2, 1.9),
        (-0.3, 1.7), (0.3, 1.7),
        (-0.4, 1.5), (0.4, 1.5),
        (0.0, 1.4),
        (-0.2, 1.2), (0.2, 1.2),
        (-0.2, 1.0), (0.2, 1.0),
        (-0.2, 0.8), (0.2, 0.8)
    ],
    # Landing (back to crouch)
    [
        (0.0, 1.6),
        (0.0, 1.4),
        (-0.2, 1.3), (0.2, 1.3),
        (-0.3, 1.1), (0.3, 1.1),
        (-0.4, 0.9), (0.4, 0.9),
        (0.0, 0.8),
        (-0.2, 0.6), (0.2, 0.6),
        (-0.2, 0.3), (0.2, 0.3),
        (-0.2, 0.0), (0.2, 0.0)
    ],
    # Back to standing
    [
        (0.0, 1.7),
        (0.0, 1.5),
        (-0.2, 1.4), (0.2, 1.4),
        (-0.3, 1.2), (0.3, 1.2),
        (-0.4, 1.0), (0.4, 1.0),
        (0.0, 1.0),
        (-0.2, 0.7), (0.2, 0.7),
        (-0.2, 0.4), (0.2, 0.4),
        (-0.2, 0.0), (0.2, 0.0)
    ]
]

# Interpolate between key frames for smooth animation
def interpolate_frames(frame_idx, total_frames):
    num_key_frames = len(key_frames)
    frames_per_key = total_frames // (num_key_frames - 1)
    key_idx = frame_idx // frames_per_key
    t = (frame_idx % frames_per_key) / frames_per_key
    
    if key_idx >= num_key_frames - 1:
        return key_frames[-1]
    
    prev_frame = key_frames[key_idx]
    next_frame = key_frames[key_idx + 1]
    
    interpolated = []
    for (x1, y1), (x2, y2) in zip(prev_frame, next_frame):
        x = x1 + t * (x2 - x1)
        y = y1 + t * (y2 - y1)
        interpolated.append((x, y))
    
    return interpolated

# Total frames for the animation
total_frames = 100

# Animation update function
def update(frame):
    current_frame = interpolate_frames(frame, total_frames)
    x_data = [p[0] for p in current_frame]
    y_data = [p[1] for p in current_frame]
    points.set_data(x_data, y_data)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=50, blit=True)

plt.title('Point-Light Jumping Animation', color='white')
plt.show()
