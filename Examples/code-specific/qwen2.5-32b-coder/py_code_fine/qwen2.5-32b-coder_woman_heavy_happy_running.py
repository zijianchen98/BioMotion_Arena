
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
num_lights = 15
frames = 200
fps = 30

# Initial positions of the lights (simplified model)
initial_positions = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8],  # Left Shoulder
    [0.6, 0.8],  # Right Shoulder
    [0.3, 0.6],  # Left Elbow
    [0.7, 0.6],  # Right Elbow
    [0.4, 0.4],  # Left Hand
    [0.6, 0.4],  # Right Hand
    [0.5, 0.6],  # Hip
    [0.4, 0.4],  # Left Knee
    [0.6, 0.4],  # Right Knee
    [0.3, 0.2],  # Left Ankle
    [0.7, 0.2],  # Right Ankle
    [0.4, 0.0],  # Left Foot
    [0.6, 0.0],  # Right Foot
    [0.5, 0.2]   # Pelvis
])

# Function to update positions based on running motion
def update_positions(frame):
    t = frame / frames * 2 * np.pi
    positions = initial_positions.copy()
    
    # Running motion adjustments
    positions[:, 1] += 0.1 * np.sin(t + np.linspace(0, 2*np.pi, num_lights))
    positions[4:6, 0] += 0.1 * np.sin(t + np.pi/2)  # Hands move forward and backward
    positions[8:10, 1] += 0.1 * np.sin(t + np.pi)   # Knees move up and down
    positions[12:14, 1] += 0.1 * np.sin(t)         # Feet move up and down
    
    return positions

# Setup plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)
ax.axis('off')
scat = ax.scatter([], [], s=100, color='white')

# Animation function
def animate(frame):
    positions = update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

plt.show()
