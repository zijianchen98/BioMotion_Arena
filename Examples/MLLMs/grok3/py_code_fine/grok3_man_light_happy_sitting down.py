
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define initial positions for 15 point-lights (simplified human sitting motion)
# Joints: head, shoulders, elbows, wrists, hips, knees, ankles, torso points
initial_positions = np.array([
    [0, 10],  # head
    [-2, 8], [2, 8],  # shoulders
    [-4, 6], [4, 6],  # elbows
    [-6, 4], [6, 4],  # wrists
    [0, 0], [-2, 0], [2, 0],  # hips, left hip, right hip
    [-2, -4], [2, -4],  # knees
    [-2, -8], [2, -8],  # ankles
    [0, 4], [0, 2]  # torso points
])

# Number of frames for the animation
n_frames = 60

# Create figure and axis with black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update positions for each frame
def update(frame):
    # Simple sinusoidal motion to simulate sitting down (head and limbs adjust)
    t = frame / n_frames
    positions = initial_positions.copy()
    
    # Head moves slightly down
    positions[0, 1] = 10 - 4 * t
    
    # Shoulders and arms adjust
    positions[1:5, 1] = 8 - 3 * t
    positions[5:7, 1] = 4 - 2 * t
    
    # Hips and legs bend
    positions[6:10, 1] = -t * 4
    positions[10:14, 1] = -4 - t * 4
    positions[14:, 1] = 2 - 2 * t
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=n_frames, interval=50, blit=True)

plt.show()
