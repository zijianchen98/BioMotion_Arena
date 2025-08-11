
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Parameters for animation
num_frames = 100  # Total number of frames in animation
fps = 30  # Frames per second

# Define the anatomical points and their motion patterns
# These points correspond to a simplified representation of a human figure sitting down
initial_points = np.array([
    [0, 3],  # Head
    [-1, 2.5], [1, 2.5],  # Shoulders
    [-1.5, 1.5], [1.5, 1.5],  # Elbows
    [-2, 0.5], [2, 0.5],  # Hands
    [0, 2],  # Torso center
    [-0.8, 1], [0.8, 1],  # Hip region
    [-1, 0], [1, 0],  # Knees
    [-1.2, -1], [1.2, -1],  # Ankles
    [-0.5, -2], [0.5, -2],  # Feet
])

# Generate biomechanically plausible motion for sitting down
def generate_sitting_motion(frame):
    progress = frame / num_frames
    points = initial_points.copy()

    # Simulate head movement downwards
    points[0, 1] -= progress
    
    # Arms move inward as sitting down progresses
    points[3, 0] += 0.5 * progress  # Left elbow
    points[4, 0] -= 0.5 * progress  # Right elbow
    points[5, 0] += 0.8 * progress  # Left hand
    points[6, 0] -= 0.8 * progress  # Right hand
    
    points[3, 1] -= 0.5 * progress  # Left elbow
    points[4, 1] -= 0.5 * progress  # Right elbow
    
    # Torso moves slightly down
    points[7, 1] -= 0.8 * progress  # Torso
    
    # Legs bend as sitting down progresses
    points[10, 1] -= 0.6 * progress  # Left knee
    points[11, 1] -= 0.6 * progress  # Right knee
    points[12, 1] -= 0.3 * progress  # Left ankle
    points[13, 1] -= 0.3 * progress  # Right ankle
    
    # Feet move back slightly
    points[14, 0] += 0.3 * progress  # Left foot
    points[15, 0] -= 0.3 * progress  # Right foot
    
    return points

# Create figure and axis for animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 4)
ax.set_facecolor('black')
ax.axis('off')

scatter = ax.scatter(initial_points[:, 0], initial_points[:, 1], c='white', s=50)

# Update function for animation
def update(frame):
    points = generate_sitting_motion(frame)
    scatter.set_offsets(points)

# Create animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=1000/fps)

# Display animation
plt.show()
