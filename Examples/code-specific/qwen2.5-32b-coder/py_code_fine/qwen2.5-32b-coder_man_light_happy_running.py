
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
light_color = 'white'

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Initial positions of the lights
positions = np.array([
    [-0.5, 0.9],  # Head
    [-0.6, 0.7],  # Left eye
    [-0.4, 0.7],  # Right eye
    [-0.5, 0.5],  # Nose
    [-0.5, 0.3],  # Neck
    [-0.6, 0.1],  # Left shoulder
    [-0.8, -0.1], # Left elbow
    [-0.6, -0.3], # Left hand
    [-0.4, 0.1],  # Right shoulder
    [-0.2, -0.1], # Right elbow
    [-0.4, -0.3], # Right hand
    [-0.5, -0.5], # Hip
    [-0.6, -0.7], # Left knee
    [-0.6, -0.9], # Left foot
    [-0.4, -0.7], # Right knee
    [-0.4, -0.9]  # Right foot
])

# Scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color=light_color)

def update(frame):
    t = frame / frames * 2 * np.pi  # Time variable
    
    # Update head position
    positions[0, 0] = -0.5 + 0.1 * np.sin(t)
    
    # Update shoulders
    positions[5, 0] = -0.6 + 0.05 * np.cos(t)
    positions[9, 0] = -0.4 + 0.05 * np.cos(t)
    
    # Update elbows
    positions[6, 0] = -0.8 + 0.1 * np.sin(t)
    positions[10, 0] = -0.2 + 0.1 * np.sin(t)
    
    # Update hands
    positions[7, 0] = -0.6 + 0.1 * np.cos(t)
    positions[11, 0] = -0.4 + 0.1 * np.cos(t)
    
    # Update hips
    positions[12, 0] = -0.6 + 0.05 * np.sin(t)
    positions[14, 0] = -0.4 + 0.05 * np.sin(t)
    
    # Update knees
    positions[13, 0] = -0.6 + 0.1 * np.cos(t)
    positions[15, 0] = -0.4 + 0.1 * np.cos(t)
    
    # Update feet
    positions[13, 1] = -0.9 + 0.1 * np.sin(t)
    positions[15, 1] = -0.9 + 0.1 * np.sin(t)
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
