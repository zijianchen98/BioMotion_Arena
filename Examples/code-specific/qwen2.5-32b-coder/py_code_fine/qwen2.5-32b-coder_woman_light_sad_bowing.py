
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 200
fps = 30
background_color = 'black'
light_color = 'white'
fig_size = (6, 6)

# Initialize positions
np.random.seed(42)
initial_positions = np.array([
    [0.0, 0.8],   # Head
    [-0.1, 0.7],  # Left Eye
    [0.1, 0.7],   # Right Eye
    [0.0, 0.6],   # Nose
    [0.0, 0.5],   # Mouth
    [-0.2, 0.4],  # Left Shoulder
    [-0.2, 0.2],  # Left Elbow
    [-0.2, 0.0],  # Left Wrist
    [0.2, 0.4],   # Right Shoulder
    [0.2, 0.2],   # Right Elbow
    [0.2, 0.0],   # Right Wrist
    [0.0, 0.4],   # Spine
    [0.0, 0.2],   # Hip
    [-0.1, 0.0],  # Left Knee
    [0.1, 0.0]    # Right Knee
])

# Function to update positions for bowing motion
def update_positions(t):
    t /= frames
    new_positions = initial_positions.copy()
    
    # Bowing motion
    new_positions[12:, 1] -= 0.2 * np.sin(2 * np.pi * t)
    new_positions[10, 1] -= 0.1 * np.sin(2 * np.pi * t)
    new_positions[8, 1] -= 0.1 * np.sin(2 * np.pi * t)
    new_positions[11, 1] -= 0.1 * np.sin(2 * np.pi * t)
    new_positions[9, 1] -= 0.1 * np.sin(2 * np.pi * t)
    
    # Arm movement
    new_positions[5:8, 1] -= 0.1 * np.sin(2 * np.pi * t)
    new_positions[8:11, 1] -= 0.1 * np.sin(2 * np.pi * t)
    
    return new_positions

# Initialize plot
fig, ax = plt.subplots(figsize=fig_size, facecolor=background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
scat = ax.scatter([], [], s=100, color=light_color)

# Animation function
def animate(i):
    positions = update_positions(i)
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

plt.show()
