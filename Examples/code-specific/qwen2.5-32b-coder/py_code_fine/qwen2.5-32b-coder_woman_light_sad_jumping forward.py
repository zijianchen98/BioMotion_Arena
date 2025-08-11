
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
fps = 30
duration = 5  # seconds
frames = fps * duration

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')
ax.set_facecolor('black')

# Initial positions of the lights
positions = np.zeros((num_lights, 2))

# Define the trajectory for each light
def trajectory(t):
    # Time normalized between 0 and 1
    t_norm = t / frames
    
    # Jumping forward trajectory
    x = t_norm - 0.5
    y = -0.2 + 0.3 * np.sin(4 * np.pi * t_norm) * np.exp(-2 * t_norm)
    
    # Adjustments for a "sad" pose
    adjustments = np.array([
        [0.0, 0.0],  # Head
        [-0.05, 0.1], # Left eye
        [0.05, 0.1],  # Right eye
        [0.0, 0.05],  # Nose
        [0.0, -0.1],  # Mouth
        [-0.1, 0.0],  # Left shoulder
        [-0.2, -0.2], # Left elbow
        [-0.2, -0.4], # Left hand
        [0.1, 0.0],   # Right shoulder
        [0.2, -0.2],  # Right elbow
        [0.2, -0.4],  # Right hand
        [0.0, -0.2],  # Hip
        [-0.1, -0.5], # Left knee
        [-0.1, -0.7], # Left foot
        [0.1, -0.5],  # Right knee
        [0.1, -0.7]   # Right foot
    ])
    
    # Apply trajectory to each light
    adjusted_positions = np.array([x, y]) + adjustments.T
    
    return adjusted_positions

# Create scatter plot for the lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

def update(frame):
    pos = trajectory(frame)
    scat.set_offsets(pos.T)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
