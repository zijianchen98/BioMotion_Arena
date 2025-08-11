
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of 15 point-lights for a happy woman jumping
# These positions are approximate and based on a simplified human stick figure
# Adjusted for a heavier build and jumping motion
initial_positions = np.array([
    [0, 10],  # Head
    [-1, 8], [-1, 6],  # Left arm
    [1, 8], [1, 6],   # Right arm
    [0, 5],          # Chest
    [-1, 3], [-1, 1],  # Left leg
    [1, 3], [1, 1],   # Right leg
    [-0.5, 4], [0.5, 4],  # Shoulders
    [0, 2],          # Hips
    [-0.5, 0], [0.5, 0]  # Feet adjustment for weight
])

# Number of frames for the animation
frames = 50

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 12)
ax.axis('off')

# Scatter plot for point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=100)

# Function to update positions for each frame
def update(frame):
    # Simulate jumping motion with a heavier build
    t = frame / frames
    amplitude = 2.0  # Reduced amplitude for heavier weight
    frequency = 2 * np.pi / frames
    vertical_offset = amplitude * np.sin(frequency * frame) + 5  # Jumping up and down
    
    # Adjusted positions for biomechanical plausibility
    positions = initial_positions.copy()
    positions[:, 1] += vertical_offset  # Vertical jump motion
    
    # Arm and leg swing for natural motion
    if t < 0.5:
        # Upward phase: arms swing back, legs bend
        positions[1:5, 0] *= 0.8  # Arms back
        positions[6:10, 1] *= 0.9  # Legs bend
    else:
        # Downward phase: arms swing forward, legs extend
        positions[1:5, 0] *= 1.2  # Arms forward
        positions[6:10, 1] *= 1.1  # Legs extend
    
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
