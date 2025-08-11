
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions for the points (happyman with heavy weight jumping forward)
def initial_positions():
    positions = np.array([
        [0, 0.9],  # Head
        [-0.1, 0.7], [0.1, 0.7],  # Eyes
        [0, 0.6],  # Nose
        [0, 0.4],  # Neck
        [0, 0.2],  # Spine
        [0, 0],  # Hip
        [-0.3, -0.2], [0.3, -0.2],  # Knees
        [-0.3, -0.6], [0.3, -0.6],  # Ankles
        [-0.2, 0.2], [0.2, 0.2],  # Shoulders
        [-0.4, 0.4], [0.4, 0.4],  # Elbows
        [-0.4, 0.6], [0.4, 0.6]   # Hands
    ])
    return positions

# Update function for the animation
def update(frame):
    t = frame / TOTAL_FRAMES
    phase = 2 * np.pi * t
    
    # Jumping forward motion
    positions = initial_positions()
    
    # Head bobbing
    positions[0, 1] += 0.05 * np.sin(phase)
    
    # Spine bending forward
    spine_bend = 0.1 * np.sin(phase)
    positions[4:, 1] -= spine_bend
    
    # Hip movement
    hip_movement = 0.1 * np.sin(phase)
    positions[5, 0] += hip_movement
    
    # Knee movement
    knee_movement = 0.2 * np.sin(phase + np.pi / 2)
    positions[7:9, 0] += knee_movement
    
    # Ankle movement
    ankle_movement = 0.2 * np.sin(phase + np.pi)
    positions[9:, 0] += ankle_movement
    
    # Shoulder movement
    shoulder_movement = 0.1 * np.sin(phase + np.pi / 4)
    positions[10:12, 0] += shoulder_movement
    
    # Elbow movement
    elbow_movement = 0.2 * np.sin(phase + 3 * np.pi / 4)
    positions[12:14, 0] += elbow_movement
    
    # Hand movement
    hand_movement = 0.2 * np.sin(phase + np.pi / 2)
    positions[14:, 0] += hand_movement
    
    scatter.set_offsets(positions)
    return scatter,

# Create scatter plot
positions = initial_positions()
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

# Create animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=True, interval=1000/FPS)

plt.show()
