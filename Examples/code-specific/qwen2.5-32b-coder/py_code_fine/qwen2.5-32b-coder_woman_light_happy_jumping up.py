
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of lights
positions = np.array([
    [0, 0],  # Head
    [-0.1, 0.1], [-0.1, -0.1],  # Eyes
    [0.1, 0.1], [0.1, -0.1],  # Shoulders
    [0.3, 0.2], [0.3, -0.2],  # Elbows
    [0.6, 0.1], [0.6, -0.1],  # Hands
    [0, -0.2],  # Neck
    [0, -0.4],  # Waist
    [-0.2, -0.5], [-0.2, -0.7],  # Left Hip, Knee
    [-0.4, -0.8],  # Left Foot
    [0.2, -0.5], [0.2, -0.7],  # Right Hip, Knee
    [0.4, -0.8]   # Right Foot
])

# Scatter plot for lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

def update(frame):
    t = 2 * np.pi * frame / frames
    
    # Update head position
    positions[0, 1] = 0.1 * np.sin(t)
    
    # Update shoulders
    positions[3, 1] = 0.2 + 0.05 * np.sin(t)
    positions[4, 1] = -0.2 - 0.05 * np.sin(t)
    
    # Update elbows
    positions[5, 1] = 0.2 + 0.1 * np.sin(t + 0.5)
    positions[6, 1] = -0.2 - 0.1 * np.sin(t + 0.5)
    
    # Update hands
    positions[7, 1] = 0.1 + 0.2 * np.sin(t + 1)
    positions[8, 1] = -0.1 - 0.2 * np.sin(t + 1)
    
    # Update waist
    positions[9, 1] = -0.2 - 0.05 * np.sin(t)
    
    # Update left leg
    positions[10, 1] = -0.5 - 0.1 * np.sin(t + 0.5)
    positions[11, 1] = -0.7 - 0.2 * np.sin(t + 1)
    positions[12, 1] = -0.8 - 0.3 * np.sin(t + 1.5)
    
    # Update right leg
    positions[13, 1] = -0.5 + 0.1 * np.sin(t + 0.5)
    positions[14, 1] = -0.7 + 0.2 * np.sin(t + 1)
    positions[15, 1] = -0.8 + 0.3 * np.sin(t + 1.5)
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
