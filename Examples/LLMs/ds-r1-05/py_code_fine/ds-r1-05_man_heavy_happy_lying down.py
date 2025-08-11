
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import collections as mc

# Configure matplotlib for a dark background
plt.style.use('dark_background')

# Define the body points in a standard configuration (standing pose)
def get_initial_pose():
    points = np.array([
        [ 0.00,  1.70],  # Head top
        [ 0.00,  1.62],  # Head base
        [-0.22,  1.55],  # Left shoulder
        [ 0.22,  1.55],  # Right shoulder
        [-0.45,  1.30],  # Left elbow
        [ 0.45,  1.30],  # Right elbow
        [-0.55,  0.95],  # Left hand
        [ 0.55,  0.95],  # Right hand
        [-0.18,  1.00],  # Left hip
        [ 0.18,  1.00],  # Right hip
        [-0.20,  0.60],  # Left knee
        [ 0.20,  0.60],  # Right knee
        [-0.20,  0.15],  # Left ankle
        [ 0.20,  0.15],  # Right ankle
        [ 0.00,  1.20]   # Torso center
    ])
    return points

# Define the target pose (lying down)
def get_final_pose(initial_pose):
    # Rotate and translate points to lying position
    angle = np.pi/2  # 90 degrees rotation
    rotation = np.array([[np.cos(angle), -np.sin(angle)],
                         [np.sin(angle), np.cos(angle)]])
    
    # Translate to center at hips, rotate, then move to ground
    hip_center = np.mean(initial_pose[[8,9], :], axis=0)
    final_pose = initial_pose - hip_center
    final_pose = np.dot(final_pose, rotation.T)
    final_pose += [0.0, -0.15]  # Move to ground with slight elevation
    
    return final_pose

# Animation update function
def update(frame, initial, final, scatter, total_frames=75):
    # Cubic easing function for natural movement
    progress = frame / total_frames
    t = 3*progress**2 - 2*progress**3 if progress < 1 else 1.0
    
    # Interpolate between poses with realistic timing
    current_pose = initial + t*(final - initial)
    
    # Update scatter plot data
    scatter.set_offsets(current_pose)
    return scatter,

# Create figure with black background
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.7, 1.8)
ax.set_aspect('equal')
ax.axis('off')  # Hide axes

# Get the poses
initial_pose = get_initial_pose()
final_pose = get_final_pose(initial_pose)

# Create initial scatter plot for points
scatter = ax.scatter(initial_pose[:, 0], initial_pose[:, 1], 
                     s=70, c='white', edgecolors='none')

# Create animation with smooth timing
fps = 30
total_frames = 75  # ~2.5 seconds
animation = FuncAnimation(fig, update, frames=total_frames,
                          fargs=(initial_pose, final_pose, scatter, total_frames-1),
                          interval=1000//fps, blit=True)

plt.tight_layout()
plt.show()
