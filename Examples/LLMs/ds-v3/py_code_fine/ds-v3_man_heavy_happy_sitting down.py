
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters
num_points = 15
num_frames = 60
fps = 30

# Initialize figure and axis
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

# Define keyframes for sitting down motion
def get_keyframes():
    # Keyframes for each point (simplified for demonstration)
    # Points are ordered as: head, shoulders (2), elbows (2), hands (2), hips (2), knees (2), feet (2), torso (1), center (1)
    keyframes = np.zeros((num_frames, num_points, 2))
    
    # Standing position (initial)
    keyframes[0] = np.array([
        [0.0, 1.2],    # head
        [-0.2, 1.0], [0.2, 1.0],  # shoulders
        [-0.3, 0.8], [0.3, 0.8],  # elbows
        [-0.4, 0.6], [0.4, 0.6],  # hands
        [-0.2, 0.5], [0.2, 0.5],  # hips
        [-0.2, 0.2], [0.2, 0.2],  # knees
        [-0.2, 0.0], [0.2, 0.0],  # feet
        [0.0, 0.7],    # torso
        [0.0, 0.85]     # center (between shoulders and hips)
    ])
    
    # Sitting position (final)
    keyframes[-1] = np.array([
        [0.0, 0.8],    # head
        [-0.2, 0.7], [0.2, 0.7],  # shoulders
        [-0.3, 0.6], [0.3, 0.6],  # elbows
        [-0.4, 0.5], [0.4, 0.5],  # hands
        [-0.3, 0.3], [0.3, 0.3],  # hips (wider when sitting)
        [-0.3, 0.1], [0.3, 0.1],  # knees (bent)
        [-0.3, -0.1], [0.3, -0.1],  # feet (slightly forward)
        [0.0, 0.5],    # torso
        [0.0, 0.6]     # center
    ])
    
    # Interpolate between keyframes
    for i in range(1, num_frames - 1):
        alpha = i / (num_frames - 1)
        keyframes[i] = keyframes[0] * (1 - alpha) + keyframes[-1] * alpha
        
        # Add some vertical movement to simulate the weight and biomechanics
        if i < num_frames // 2:
            # Slight downward acceleration
            keyframes[i, :, 1] -= 0.1 * np.sin(alpha * np.pi)
        else:
            # Deceleration and settling
            keyframes[i, :, 1] -= 0.1 * np.sin(alpha * np.pi) + 0.05 * np.sin(2 * alpha * np.pi)
    
    return keyframes

keyframes = get_keyframes()

# Animation update function
def update(frame):
    for i, point in enumerate(points):
        point.center = keyframes[frame, i]
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps, blit=True)

plt.tight_layout()
plt.show()
