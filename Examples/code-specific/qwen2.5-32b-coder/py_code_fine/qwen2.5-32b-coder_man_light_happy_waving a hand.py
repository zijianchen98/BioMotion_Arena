
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 30
background_color = 'black'
point_color = 'white'
fig_size = (8, 8)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=fig_size, facecolor=background_color)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the lights (approximate starting positions for happyman waving)
positions = np.array([
    [0.0, 0.7],  # Head
    [-0.1, 0.6], # Left eye
    [0.1, 0.6],  # Right eye
    [0.0, 0.5],  # Nose
    [0.0, 0.4],  # Mouth
    [-0.1, 0.3], # Left shoulder
    [0.1, 0.3],  # Right shoulder
    [-0.2, 0.2], # Left elbow
    [0.2, 0.2],  # Right elbow
    [-0.3, 0.1], # Left wrist
    [0.3, 0.1],  # Right wrist
    [-0.1, 0.2], # Left hip
    [0.1, 0.2],  # Right hip
    [-0.1, 0.1], # Left knee
    [0.1, 0.1]   # Right knee
])

# Scatter plot for point lights
scat = ax.scatter(positions[:, 0], positions[:, 1], color=point_color)

def update(frame):
    # Define the waving motion for the right arm
    t = frame / frames * 2 * np.pi
    amplitude = 0.1
    frequency = 2
    phase = np.pi / 2
    
    # Update positions of the right shoulder, elbow, and wrist
    positions[6] = [0.1 + amplitude * np.sin(frequency * t + phase), 0.3]
    positions[8] = [0.2 + amplitude * np.sin(frequency * t + phase), 0.2]
    positions[10] = [0.3 + amplitude * np.sin(frequency * t + phase), 0.1]
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
