
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frame_rate = 30
duration = 5  # seconds
frames = frame_rate * duration

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions for the lights representing a walking woman
positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.1], [0.1, -0.1],  # Shoulders
    [-0.2, -0.2], [0.2, -0.2],  # Hips
    [-0.3, -0.4], [-0.1, -0.6],  # Left leg
    [0.3, -0.4], [0.1, -0.6],   # Right leg
    [-0.15, -0.3], [-0.05, -0.3],  # Left arm
    [0.15, -0.3], [0.05, -0.3]   # Right arm
])

# Scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

def update(frame):
    global positions
    
    # Update positions for a walking motion
    positions[0][1] = np.sin(frame / 10) * 0.1 + 0.1  # Head bouncing
    
    positions[3][0] += np.sin(frame / 10) * 0.02  # Hip sway
    positions[4][0] -= np.sin(frame / 10) * 0.02
    
    if frame % 20 < 10:
        positions[5][1] = np.sin((frame - 5) / 2) * 0.2 - 0.4  # Left leg up
        positions[7][1] = -0.6  # Right leg down
    else:
        positions[5][1] = -0.4  # Left leg down
        positions[7][1] = np.sin((frame - 15) / 2) * 0.2 - 0.6  # Right leg up
        
    positions[8][0] = np.cos(frame / 10) * 0.1 - 0.15  # Left arm swing
    positions[9][0] = np.cos(frame / 10) * 0.1 - 0.05
    positions[10][0] = -np.cos(frame / 10) * 0.1 + 0.15  # Right arm swing
    positions[11][0] = -np.cos(frame / 10) * 0.1 + 0.05
    
    scat.set_offsets(positions)

ani = FuncAnimation(fig, update, frames=frames, interval=1000/frame_rate, blit=False)
plt.show()
