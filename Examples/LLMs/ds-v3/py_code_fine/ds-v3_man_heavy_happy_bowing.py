
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Parameters
num_points = 15
frames = 100
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
plt.axis('off')

# Initialize points (positions for a standing figure)
def initial_positions():
    # Head, shoulders, elbows, hands, hips, knees, feet
    points = np.array([
        [0.0, 1.8],    # head
        [-0.3, 1.5],   # left shoulder
        [0.3, 1.5],    # right shoulder
        [-0.5, 1.2],   # left elbow
        [0.5, 1.2],    # right elbow
        [-0.6, 0.9],   # left hand
        [0.6, 0.9],    # right hand
        [-0.3, 1.0],   # left hip
        [0.3, 1.0],    # right hip
        [-0.3, 0.4],   # left knee
        [0.3, 0.4],    # right knee
        [-0.3, 0.0],   # left foot
        [0.3, 0.0],    # right foot
        [0.0, 1.2],    # torso midpoint
        [0.0, 0.7]     # waist
    ])
    return points

points = initial_positions()
patches = [Circle((x, y), 0.05, color='white') for x, y in points]
for patch in patches:
    ax.add_patch(patch)

# Bowing motion: head and torso move forward, arms may swing slightly
def update(frame):
    t = frame / frames
    bow_angle = np.sin(t * np.pi) * 0.5  # Bowing motion (forward lean)
    
    # Original positions
    original = initial_positions()
    
    # Apply bowing motion
    new_points = original.copy()
    
    # Head moves forward and down
    new_points[0, 0] = original[0, 0] + 0.2 * np.sin(bow_angle)
    new_points[0, 1] = original[0, 1] - 0.5 * (1 - np.cos(bow_angle))
    
    # Torso bends forward
    new_points[13, 0] = original[13, 0] + 0.1 * np.sin(bow_angle)
    new_points[13, 1] = original[13, 1] - 0.3 * (1 - np.cos(bow_angle))
    new_points[14, 0] = original[14, 0] + 0.05 * np.sin(bow_angle)
    new_points[14, 1] = original[14, 1] - 0.1 * (1 - np.cos(bow_angle))
    
    # Arms may swing slightly back
    arm_swing = 0.1 * np.sin(bow_angle)
    new_points[2:7, 0] = original[2:7, 0] + arm_swing * np.array([0.5, 0.5, 0.7, 0.7, 0.8, 0.8])
    
    # Update patches
    for i, patch in enumerate(patches):
        patch.center = (new_points[i, 0], new_points[i, 1])
    
    return patches

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.show()
