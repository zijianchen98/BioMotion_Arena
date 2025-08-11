
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
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Define the keyframes for the bowing motion
def get_keyframes():
    # Keyframes: each entry is a tuple of (x, y) positions for all 15 points
    # The points are ordered as follows (example, adjust as needed):
    # 0: head, 1-4: shoulders and arms, 5-8: torso and hips, 9-14: legs and feet
    
    # Neutral standing position
    neutral = np.array([
        [0.0, 1.4],    # head
        [-0.3, 1.2], [0.3, 1.2],  # shoulders
        [-0.4, 1.1], [0.4, 1.1],  # arms (elbows)
        [-0.2, 0.8], [0.2, 0.8],  # hands
        [0.0, 1.0], [0.0, 0.7],   # torso and hips
        [-0.2, 0.4], [0.2, 0.4],  # knees
        [-0.2, 0.0], [0.2, 0.0],  # feet
        [0.0, 0.5]                # center of hips (optional)
    ])
    
    # Bowing position (head and torso move forward, arms may slightly move)
    bowing = np.array([
        [0.0, 1.0],    # head moves down
        [-0.3, 1.2], [0.3, 1.2],  # shoulders
        [-0.4, 1.0], [0.4, 1.0],  # arms slightly down
        [-0.2, 0.9], [0.2, 0.9],  # hands
        [0.0, 0.8], [0.0, 0.7],   # torso and hips (torso bends)
        [-0.2, 0.4], [0.2, 0.4],  # knees
        [-0.2, 0.0], [0.2, 0.0],  # feet
        [0.0, 0.5]                # center of hips
    ])
    
    # Return keyframes (neutral -> bowing -> neutral)
    return [neutral, bowing, neutral]

keyframes = get_keyframes()

# Interpolate between keyframes for smooth animation
def interpolate_frames(keyframes, num_frames_per_keyframe):
    frames = []
    for i in range(len(keyframes) - 1):
        start = keyframes[i]
        end = keyframes[i + 1]
        for t in np.linspace(0, 1, num_frames_per_keyframe):
            frame = start + t * (end - start)
            frames.append(frame)
    return frames

frames = interpolate_frames(keyframes, 20)

# Animation update function
def update(frame):
    points.set_data(frame[:, 0], frame[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=frames, interval=50, blit=True
)

plt.tight_layout()
plt.show()
