
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
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Initialize point lights
points = [Circle((0, 0), radius=0.05, color='white') for _ in range(num_points)]
for point in points:
    ax.add_patch(point)

# Define keyframes for the jumping motion
def get_keyframe(t):
    # Normalized time [0, 1]
    t_norm = t / total_frames
    
    # Jumping motion parameters
    jump_height = 1.5
    squat_depth = 0.3
    jump_phase = np.sin(t_norm * np.pi)  # Sinusoidal for smooth jump
    
    # Vertical position (jumping)
    y_offset = jump_height * jump_phase**2 - squat_depth * (1 - jump_phase)
    
    # Horizontal positions (approximate body parts)
    # Head, shoulders, elbows, hands, hips, knees, feet
    x_positions = np.array([
        0.0,  # head
        -0.2, 0.2,  # shoulders
        -0.3, 0.3,  # elbows
        -0.4, 0.4,  # hands
        -0.15, 0.15,  # hips
        -0.2, 0.2,  # knees
        -0.25, 0.25,  # feet
        -0.1, 0.1,  # additional points for heaviness (e.g., belly)
    ])
    
    y_positions = np.array([
        0.7 + y_offset,  # head
        0.5 + y_offset, 0.5 + y_offset,  # shoulders
        0.4 + y_offset, 0.4 + y_offset,  # elbows
        0.3 + y_offset, 0.3 + y_offset,  # hands
        0.2 + y_offset, 0.2 + y_offset,  # hips
        0.0 + y_offset, 0.0 + y_offset,  # knees
        -0.2 + y_offset, -0.2 + y_offset,  # feet
        0.3 + y_offset, 0.3 + y_offset,  # additional points
    ])
    
    # Slight horizontal movement for realism
    x_offset = 0.1 * np.sin(t_norm * 2 * np.pi)
    x_positions += x_offset
    
    # Slight rotation effect (lean forward/backward)
    if t_norm < 0.5:
        lean = 0.2 * t_norm * 2
    else:
        lean = 0.2 * (1 - (t_norm - 0.5) * 2)
    
    y_positions[:7] += lean  # upper body leans
    
    return x_positions, y_positions

# Animation update function
def update(frame):
    x, y = get_keyframe(frame)
    for i, point in enumerate(points):
        point.center = (x[i], y[i])
    return points

# Create animation
ani = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit=True)

plt.title('Point-Light Animation: Heavy Woman Jumping', color='white')
plt.tight_layout()
plt.show()
