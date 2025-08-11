
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
NUM_POINTS = 15
FPS = 30
DURATION = 5  # seconds
TOTAL_FRAMES = FPS * DURATION

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the points (simplified model for sitting down)
initial_positions = np.array([
    [0, 0.7],  # Head
    [-0.1, 0.6], [0.1, 0.6],  # Eyes
    [0, 0.5],  # Nose
    [0, 0.4],  # Mouth
    [-0.2, 0.3], [0.2, 0.3],  # Shoulders
    [-0.2, 0.2], [0.2, 0.2],  # Elbows
    [-0.2, 0.1], [0.2, 0.1],  # Hands
    [0, 0.1],  # Chest
    [-0.1, 0], [0.1, 0],  # Hips
    [-0.1, -0.2], [0.1, -0.2],  # Knees
    [0, -0.4]  # Feet
])

# Create scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, color='white')

def update(frame):
    t = frame / TOTAL_FRAMES  # Normalized time from 0 to 1
    
    # Simplified motion for sitting down with a heavy load
    positions = initial_positions.copy()
    
    # Head bobs slightly
    positions[0, 1] += 0.01 * np.sin(2 * np.pi * t)
    
    # Shoulders move slightly back and forth
    positions[4:6, 0] += 0.02 * np.sin(2 * np.pi * t)
    
    # Elbows move slightly up and down
    positions[6:8, 1] += 0.02 * np.cos(2 * np.pi * t)
    
    # Hands move slightly side to side
    positions[8:10, 0] += 0.02 * np.sin(2 * np.pi * t)
    
    # Chest moves slightly up and down
    positions[10, 1] += 0.01 * np.sin(2 * np.pi * t)
    
    # Hips move slightly side to side
    positions[11:13, 0] += 0.02 * np.sin(2 * np.pi * t)
    
    # Knees move slightly up and down
    positions[13:15, 1] += 0.02 * np.cos(2 * np.pi * t)
    
    # Update scatter plot
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, interval=1000/FPS, blit=True)

# Show plot
plt.show()
