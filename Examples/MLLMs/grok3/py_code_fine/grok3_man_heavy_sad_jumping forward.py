
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point lights (simplified human figure)
def init_positions():
    # Head, torso, hips, shoulders, elbows, wrists, knees, ankles
    positions = np.array([
        [0, 10],  # Head
        [0, 8],   # Torso top
        [0, 4],   # Torso bottom
        [1, 8],   # Right shoulder
        [-1, 8],  # Left shoulder
        [2, 6],   # Right elbow
        [-2, 6],  # Left elbow
        [2.5, 4], # Right wrist
        [-2.5, 4],# Left wrist
        [0.5, 4], # Right hip
        [-0.5, 4],# Left hip
        [1, 2],   # Right knee
        [-1, 2],  # Left knee
        [1.5, 0], # Right ankle
        [-1.5, 0] # Left ankle
    ])
    return positions

# Update positions for jumping forward motion
def update(frame, positions):
    t = frame * 0.1  # Time parameter for smooth motion
    # Jumping forward with a slight sad slump (lower torso, slower arms)
    vertical_offset = 2 * np.sin(t) - 0.5  # Jump height with slump
    forward_offset = t  # Forward movement
    torso_angle = 0.1 * np.sin(t)  # Slight slump in torso
    
    new_positions = positions.copy()
    # Apply forward jump
    new_positions += [forward_offset, vertical_offset]
    # Adjust torso and limbs for realistic motion
    new_positions[1] += [0, -0.5 * np.sin(t)]  # Torso top slump
    new_positions[2] += [0, -0.5 * np.sin(t)]  # Torso bottom slump
    new_positions[3:5] += [0.2 * np.sin(t), 0]  # Shoulders slight swing
    new_positions[5:7] += [0.3 * np.cos(t), -0.2 * np.sin(t)]  # Elbows
    new_positions[7:9] += [0.4 * np.cos(t), -0.3 * np.sin(t)]  # Wrists
    new_positions[9:11] += [0, -0.1 * np.sin(t)]  # Hips
    new_positions[11:13] += [0.2 * np.cos(t), -0.4 * np.sin(t)]  # Knees
    new_positions[13:] += [0.3 * np.cos(t), -0.5 * np.sin(t)]  # Ankles
    
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 12)
ax.axis('off')

# Initial positions
positions = init_positions()
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

# Create animation
ani = FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

plt.show()
