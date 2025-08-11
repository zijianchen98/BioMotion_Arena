
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
fps = 30
duration = 2  # seconds
total_frames = fps * duration

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

# Define keyframes for the jumping motion
def get_keyframes():
    # Keyframes: (time, positions for all points)
    # Positions are (x, y) for each of the 15 points
    keyframes = [
        (0.0, [
            (0.0, 0.0),  # head
            (0.0, -0.2),  # neck
            (-0.2, -0.4),  # left shoulder
            (0.2, -0.4),  # right shoulder
            (-0.2, -0.8),  # left elbow
            (0.2, -0.8),  # right elbow
            (-0.2, -1.2),  # left hand
            (0.2, -1.2),  # right hand
            (0.0, -0.5),  # torso
            (-0.2, -1.0),  # left hip
            (0.2, -1.0),  # right hip
            (-0.2, -1.5),  # left knee
            (0.2, -1.5),  # right knee
            (-0.2, -2.0),  # left foot
            (0.2, -2.0)   # right foot
        ]),
        (0.3, [
            (0.0, 0.2),  # head
            (0.0, 0.0),  # neck
            (-0.2, -0.2),  # left shoulder
            (0.2, -0.2),  # right shoulder
            (-0.3, -0.4),  # left elbow
            (0.3, -0.4),  # right elbow
            (-0.4, -0.5),  # left hand
            (0.4, -0.5),  # right hand
            (0.0, -0.3),  # torso
            (-0.2, -0.8),  # left hip
            (0.2, -0.8),  # right hip
            (-0.2, -1.2),  # left knee
            (0.2, -1.2),  # right knee
            (-0.2, -1.7),  # left foot
            (0.2, -1.7)   # right foot
        ]),
        (0.6, [
            (0.0, 0.8),  # head
            (0.0, 0.6),  # neck
            (-0.2, 0.4),  # left shoulder
            (0.2, 0.4),  # right shoulder
            (-0.3, 0.2),  # left elbow
            (0.3, 0.2),  # right elbow
            (-0.4, 0.1),  # left hand
            (0.4, 0.1),  # right hand
            (0.0, 0.3),  # torso
            (-0.2, -0.2),  # left hip
            (0.2, -0.2),  # right hip
            (-0.2, -0.6),  # left knee
            (0.2, -0.6),  # right knee
            (-0.2, -1.1),  # left foot
            (0.2, -1.1)   # right foot
        ]),
        (0.8, [
            (0.0, 1.2),  # head
            (0.0, 1.0),  # neck
            (-0.2, 0.8),  # left shoulder
            (0.2, 0.8),  # right shoulder
            (-0.3, 0.6),  # left elbow
            (0.3, 0.6),  # right elbow
            (-0.4, 0.5),  # left hand
            (0.4, 0.5),  # right hand
            (0.0, 0.7),  # torso
            (-0.2, 0.2),  # left hip
            (0.2, 0.2),  # right hip
            (-0.2, -0.2),  # left knee
            (0.2, -0.2),  # right knee
            (-0.2, -0.7),  # left foot
            (0.2, -0.7)   # right foot
        ]),
        (1.0, [
            (0.0, 1.5),  # head
            (0.0, 1.3),  # neck
            (-0.2, 1.1),  # left shoulder
            (0.2, 1.1),  # right shoulder
            (-0.3, 0.9),  # left elbow
            (0.3, 0.9),  # right elbow
            (-0.4, 0.8),  # left hand
            (0.4, 0.8),  # right hand
            (0.0, 1.0),  # torso
            (-0.2, 0.5),  # left hip
            (0.2, 0.5),  # right hip
            (-0.2, 0.0),  # left knee
            (0.2, 0.0),  # right knee
            (-0.2, -0.5),  # left foot
            (0.2, -0.5)   # right foot
        ]),
        (1.2, [
            (0.0, 1.2),  # head
            (0.0, 1.0),  # neck
            (-0.2, 0.8),  # left shoulder
            (0.2, 0.8),  # right shoulder
            (-0.3, 0.6),  # left elbow
            (0.3, 0.6),  # right elbow
            (-0.4, 0.5),  # left hand
            (0.4, 0.5),  # right hand
            (0.0, 0.7),  # torso
            (-0.2, 0.2),  # left hip
            (0.2, 0.2),  # right hip
            (-0.2, -0.2),  # left knee
            (0.2, -0.2),  # right knee
            (-0.2, -0.7),  # left foot
            (0.2, -0.7)   # right foot
        ]),
        (1.5, [
            (0.0, 0.8),  # head
            (0.0, 0.6),  # neck
            (-0.2, 0.4),  # left shoulder
            (0.2, 0.4),  # right shoulder
            (-0.3, 0.2),  # left elbow
            (0.3, 0.2),  # right elbow
            (-0.4, 0.1),  # left hand
            (0.4, 0.1),  # right hand
            (0.0, 0.3),  # torso
            (-0.2, -0.2),  # left hip
            (0.2, -0.2),  # right hip
            (-0.2, -0.6),  # left knee
            (0.2, -0.6),  # right knee
            (-0.2, -1.1),  # left foot
            (0.2, -1.1)   # right foot
        ]),
        (1.8, [
            (0.0, 0.2),  # head
            (0.0, 0.0),  # neck
            (-0.2, -0.2),  # left shoulder
            (0.2, -0.2),  # right shoulder
            (-0.3, -0.4),  # left elbow
            (0.3, -0.4),  # right elbow
            (-0.4, -0.5),  # left hand
            (0.4, -0.5),  # right hand
            (0.0, -0.3),  # torso
            (-0.2, -0.8),  # left hip
            (0.2, -0.8),  # right hip
            (-0.2, -1.2),  # left knee
            (0.2, -1.2),  # right knee
            (-0.2, -1.7),  # left foot
            (0.2, -1.7)   # right foot
        ]),
        (2.0, [
            (0.0, 0.0),  # head
            (0.0, -0.2),  # neck
            (-0.2, -0.4),  # left shoulder
            (0.2, -0.4),  # right shoulder
            (-0.2, -0.8),  # left elbow
            (0.2, -0.8),  # right elbow
            (-0.2, -1.2),  # left hand
            (0.2, -1.2),  # right hand
            (0.0, -0.5),  # torso
            (-0.2, -1.0),  # left hip
            (0.2, -1.0),  # right hip
            (-0.2, -1.5),  # left knee
            (0.2, -1.5),  # right knee
            (-0.2, -2.0),  # left foot
            (0.2, -2.0)   # right foot
        ])
    ]
    return keyframes

# Interpolate between keyframes
def interpolate_positions(frame, keyframes):
    time = frame / fps
    # Find the two surrounding keyframes
    prev_time, prev_pos = keyframes[0]
    next_time, next_pos = keyframes[-1]
    for i in range(len(keyframes) - 1):
        if keyframes[i][0] <= time <= keyframes[i+1][0]:
            prev_time, prev_pos = keyframes[i]
            next_time, next_pos = keyframes[i+1]
            break
    
    # Linear interpolation
    alpha = (time - prev_time) / (next_time - prev_time)
    positions = []
    for p1, p2 in zip(prev_pos, next_pos):
        x = p1[0] + alpha * (p2[0] - p1[0])
        y = p1[1] + alpha * (p2[1] - p1[1])
        positions.append((x, y))
    return positions

# Update function for animation
def update(frame):
    keyframes = get_keyframes()
    positions = interpolate_positions(frame, keyframes)
    for i in range(num_points):
        points[i].center = positions[i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
