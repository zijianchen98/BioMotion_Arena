
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
import math

# Parameters
num_points = 15
fps = 30
duration = 3  # seconds
total_frames = fps * duration

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for the sitting down motion
def get_keyframes():
    # Keyframes: (time, positions for 15 points)
    # Positions are (x, y) for each point
    keyframes = [
        (0.0, [
            (0.0, 1.2),    # head
            (0.0, 1.0),    # neck
            (-0.2, 0.9),   # left shoulder
            (0.2, 0.9),    # right shoulder
            (-0.2, 0.7),   # left elbow
            (0.2, 0.7),    # right elbow
            (-0.2, 0.4),   # left hand
            (0.2, 0.4),    # right hand
            (0.0, 0.8),    # torso top
            (0.0, 0.4),    # torso bottom
            (-0.2, 0.2),   # left hip
            (0.2, 0.2),    # right hip
            (-0.3, -0.2),  # left knee
            (0.3, -0.2),   # right knee
            (-0.3, -0.6),  # left foot
        ]),
        (0.0, [
            (0.0, 1.2),    # head
            (0.0, 1.0),    # neck
            (-0.2, 0.9),   # left shoulder
            (0.2, 0.9),    # right shoulder
            (-0.2, 0.7),   # left elbow
            (0.2, 0.7),    # right elbow
            (-0.2, 0.4),   # left hand
            (0.2, 0.4),    # right hand
            (0.0, 0.8),    # torso top
            (0.0, 0.4),    # torso bottom
            (-0.2, 0.2),   # left hip
            (0.2, 0.2),    # right hip
            (-0.3, -0.2),  # left knee
            (0.3, -0.2),   # right knee
            (-0.3, -0.6),  # left foot
        ]),
        (0.5, [
            (0.0, 1.1),    # head
            (0.0, 0.9),    # neck
            (-0.2, 0.8),   # left shoulder
            (0.2, 0.8),    # right shoulder
            (-0.25, 0.6),  # left elbow
            (0.25, 0.6),   # right elbow
            (-0.3, 0.3),   # left hand
            (0.3, 0.3),    # right hand
            (0.0, 0.7),    # torso top
            (0.0, 0.3),    # torso bottom
            (-0.2, 0.1),   # left hip
            (0.2, 0.1),    # right hip
            (-0.3, -0.3),  # left knee
            (0.3, -0.3),   # right knee
            (-0.3, -0.7),  # left foot
        ]),
        (1.0, [
            (0.0, 1.0),    # head
            (0.0, 0.8),    # neck
            (-0.2, 0.7),   # left shoulder
            (0.2, 0.7),    # right shoulder
            (-0.3, 0.5),   # left elbow
            (0.3, 0.5),    # right elbow
            (-0.4, 0.2),   # left hand
            (0.4, 0.2),    # right hand
            (0.0, 0.6),    # torso top
            (0.0, 0.2),    # torso bottom
            (-0.2, 0.0),   # left hip
            (0.2, 0.0),    # right hip
            (-0.3, -0.4),  # left knee
            (0.3, -0.4),   # right knee
            (-0.3, -0.8),  # left foot
        ]),
        (1.5, [
            (0.0, 0.9),    # head
            (0.0, 0.7),    # neck
            (-0.2, 0.6),   # left shoulder
            (0.2, 0.6),    # right shoulder
            (-0.35, 0.4),  # left elbow
            (0.35, 0.4),   # right elbow
            (-0.45, 0.1),  # left hand
            (0.45, 0.1),   # right hand
            (0.0, 0.5),    # torso top
            (0.0, 0.1),    # torso bottom
            (-0.2, -0.1),  # left hip
            (0.2, -0.1),   # right hip
            (-0.3, -0.5),  # left knee
            (0.3, -0.5),   # right knee
            (-0.3, -0.9),  # left foot
        ]),
        (2.0, [
            (0.0, 0.8),    # head
            (0.0, 0.6),    # neck
            (-0.2, 0.5),   # left shoulder
            (0.2, 0.5),    # right shoulder
            (-0.4, 0.3),   # left elbow
            (0.4, 0.3),    # right elbow
            (-0.5, 0.0),   # left hand
            (0.5, 0.0),    # right hand
            (0.0, 0.4),    # torso top
            (0.0, 0.0),    # torso bottom
            (-0.2, -0.2),  # left hip
            (0.2, -0.2),   # right hip
            (-0.3, -0.6),  # left knee
            (0.3, -0.6),   # right knee
            (-0.3, -1.0),  # left foot
        ]),
        (2.5, [
            (0.0, 0.7),    # head
            (0.0, 0.5),    # neck
            (-0.2, 0.4),   # left shoulder
            (0.2, 0.4),    # right shoulder
            (-0.45, 0.2),  # left elbow
            (0.45, 0.2),   # right elbow
            (-0.55, -0.1), # left hand
            (0.55, -0.1),  # right hand
            (0.0, 0.3),    # torso top
            (0.0, -0.1),   # torso bottom
            (-0.2, -0.3),  # left hip
            (0.2, -0.3),   # right hip
            (-0.3, -0.7),  # left knee
            (0.3, -0.7),   # right knee
            (-0.3, -1.1),  # left foot
        ]),
        (3.0, [
            (0.0, 0.6),    # head
            (0.0, 0.4),    # neck
            (-0.2, 0.3),   # left shoulder
            (0.2, 0.3),    # right shoulder
            (-0.5, 0.1),   # left elbow
            (0.5, 0.1),    # right elbow
            (-0.6, -0.2),  # left hand
            (0.6, -0.2),   # right hand
            (0.0, 0.2),    # torso top
            (0.0, -0.2),   # torso bottom
            (-0.2, -0.4),  # left hip
            (0.2, -0.4),   # right hip
            (-0.3, -0.8),  # left knee
            (0.3, -0.8),   # right knee
            (-0.3, -1.2),  # left foot
        ])
    ]
    return keyframes

# Interpolate between keyframes
def interpolate_keyframes(keyframes, frame, total_frames):
    t = frame / total_frames * keyframes[-1][0]  # Normalized time
    
    # Find the two closest keyframes
    prev_kf = None
    next_kf = None
    for i in range(len(keyframes)):
        if keyframes[i][0] <= t:
            prev_kf = keyframes[i]
        else:
            next_kf = keyframes[i]
            break
    
    if prev_kf is None:
        return keyframes[0][1]
    if next_kf is None:
        return keyframes[-1][1]
    
    # Linear interpolation
    t_prev, positions_prev = prev_kf
    t_next, positions_next = next_kf
    alpha = (t - t_prev) / (t_next - t_prev)
    
    interpolated_positions = []
    for (x_prev, y_prev), (x_next, y_next) in zip(positions_prev, positions_next):
        x = x_prev + alpha * (x_next - x_prev)
        y = y_prev + alpha * (y_next - y_prev)
        interpolated_positions.append((x, y))
    
    return interpolated_positions

# Animation update function
def update(frame):
    keyframes = get_keyframes()
    positions = interpolate_keyframes(keyframes, frame, total_frames)
    for i, point in enumerate(points):
        point.center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
