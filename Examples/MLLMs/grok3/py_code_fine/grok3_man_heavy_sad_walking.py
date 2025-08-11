
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human stick figure)
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 10],  # Head
    [-1, 8], [1, 8],  # Shoulders
    [-2, 6], [2, 6],  # Elbows
    [-2.5, 4], [2.5, 4],  # Wrists
    [0, 5],  # Chest
    [-0.5, 3], [0.5, 3],  # Hips
    [-0.5, 1], [0.5, 1],  # Knees
    [-0.5, -1], [0.5, -1],  # Ankles
    [0, 7]  # Neck
]) * 10  # Scale up for visibility

# Parameters for walking motion
frames = 100
step_size = 0.1
swing_amplitude = 2
leg_phase = np.pi / 2

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-30, 30)
ax.set_ylim(-20, 50)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

def update(frame):
    # Calculate new positions for walking motion
    t = frame / frames * 2 * np.pi
    new_positions = initial_positions.copy()
    
    # Horizontal movement (walking forward)
    new_positions[:, 0] += frame * step_size
    
    # Arm and leg swing (simplified sinusoidal motion)
    # Arms
    new_positions[3:5, 1] += np.sin(t) * swing_amplitude  # Elbows
    new_positions[5:7, 1] += np.sin(t + np.pi) * swing_amplitude  # Wrists
    # Legs
    new_positions[9:11, 1] += np.sin(t + leg_phase) * swing_amplitude  # Knees
    new_positions[11:13, 1] += np.sin(t + leg_phase + np.pi) * swing_amplitude  # Ankles
    
    # Update scatter plot
    scatter.set_offsets(new_positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
