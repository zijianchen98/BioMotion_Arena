
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the point lights
positions = np.zeros((num_lights, 2))

# Create scatter plot for point lights
scatter = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=100)

def update(frame):
    t = frame / frames * 2 * np.pi
    
    # Positions based on a simple model of a jump
    # Head
    positions[0] = [0, 0.8 + 0.2 * np.sin(t)]
    
    # Shoulders
    positions[1] = [-0.1, 0.6 + 0.1 * np.sin(t - 0.2)]
    positions[2] = [0.1, 0.6 + 0.1 * np.sin(t - 0.2)]
    
    # Elbows
    positions[3] = [-0.2, 0.4 + 0.1 * np.sin(t - 0.4)]
    positions[4] = [0.2, 0.4 + 0.1 * np.sin(t - 0.4)]
    
    # Hands
    positions[5] = [-0.3, 0.2 + 0.1 * np.sin(t - 0.6)]
    positions[6] = [0.3, 0.2 + 0.1 * np.sin(t - 0.6)]
    
    # Hips
    positions[7] = [-0.1, 0.4 + 0.1 * np.sin(t - 0.2)]
    positions[8] = [0.1, 0.4 + 0.1 * np.sin(t - 0.2)]
    
    # Knees
    positions[9] = [-0.2, 0.2 + 0.1 * np.sin(t - 0.4)]
    positions[10] = [0.2, 0.2 + 0.1 * np.sin(t - 0.4)]
    
    # Feet
    positions[11] = [-0.3, 0 + 0.1 * np.sin(t - 0.6)]
    positions[12] = [0.3, 0 + 0.1 * np.sin(t - 0.6)]
    
    # Toes
    positions[13] = [-0.35, -0.1 + 0.1 * np.sin(t - 0.8)]
    positions[14] = [0.35, -0.1 + 0.1 * np.sin(t - 0.8)]
    
    scatter.set_offsets(positions)
    return scatter,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
