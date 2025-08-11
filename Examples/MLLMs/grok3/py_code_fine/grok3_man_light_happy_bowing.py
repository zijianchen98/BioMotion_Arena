
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human bowing pose)
# Points represent: head, shoulders, elbows, wrists, hips, knees, ankles
# Adjusted for bowing motion over time
def initialize_positions():
    t = 0
    base_positions = np.array([
        [0, 10],    # head
        [-2, 8],    # left shoulder
        [2, 8],     # right shoulder
        [-3, 6],    # left elbow
        [3, 6],     # right elbow
        [-4, 4],    # left wrist
        [4, 4],     # right wrist
        [0, 2],     # hip
        [-1, 0],    # left knee
        [1, 0],     # right knee
        [-1.5, -2], # left ankle
        [1.5, -2],  # right ankle
        [0, 1],     # chest
        [-0.5, 3],  # left upper arm
        [0.5, 3]    # right upper arm
    ])
    return base_positions, t

# Update function for animation
def update(frame, scat, positions, t):
    t += 0.1  # Time step
    # Simple parametric bowing motion: head and upper body tilt forward, legs bend
    angle = np.sin(t) * 0.5  # Bowing angle oscillation
    hip_y = 2 - np.abs(np.sin(t) * 1)  # Hip moves down slightly
    knee_bend = np.sin(t) * 0.5
    
    new_positions = positions.copy()
    # Head and upper body tilt
    new_positions[0] = [0, 10 - angle * 2]  # Head moves down
    new_positions[1:3] = [[-2 + angle, 8 - angle], [2 - angle, 8 - angle]]  # Shoulders tilt
    new_positions[3:5] = [[-3 + angle * 1.5, 6 - angle * 1.5], [3 - angle * 1.5, 6 - angle * 1.5]]  # Elbows
    new_positions[5:7] = [[-4 + angle * 2, 4 - angle * 2], [4 - angle * 2, 4 - angle * 2]]  # Wrists
    new_positions[12] = [0, 1 - angle]  # Chest
    
    # Hip and legs
    new_positions[7] = [0, hip_y]  # Hip
    new_positions[8:10] = [[-1, knee_bend], [1, knee_bend]]  # Knees bend
    new_positions[10:12] = [[-1.5, -2 + knee_bend], [1.5, -2 + knee_bend]]  # Ankles
    
    # Update scatter points
    scat.set_offsets(new_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-3, 12)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
positions, t = initialize_positions()
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Create animation
ani = FuncAnimation(fig, update, fargs=(scat, positions, t), frames=100, interval=50, blit=True)

plt.show()
