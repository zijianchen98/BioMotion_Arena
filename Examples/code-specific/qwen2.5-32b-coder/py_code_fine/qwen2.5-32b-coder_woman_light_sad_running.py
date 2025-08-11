
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initialize positions and velocities
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define joint indices for a simple stick figure
joints = [
    (0, 1), (1, 2), (2, 3),  # Head and neck
    (1, 4), (4, 5), (5, 6),  # Right arm
    (1, 7), (7, 8), (8, 9),  # Left arm
    (2, 10), (10, 11), (11, 12),  # Right leg
    (2, 13), (13, 14), (14, 15)   # Left leg
]

# Initial setup
def init():
    scat.set_offsets(positions)
    return scat,

# Update function for animation
def update(frame):
    global positions, velocities
    
    # Simple running motion simulation
    phase = frame / frames * 2 * np.pi
    amplitude = 0.1
    
    # Head and neck
    positions[0] = [0.5 + amplitude * np.sin(phase), 0.8]
    positions[1] = [0.5 + amplitude * np.sin(phase), 0.7]
    positions[2] = [0.5 + amplitude * np.sin(phase), 0.6]
    
    # Right arm
    positions[4] = [0.5 + amplitude * np.sin(phase - 0.5), 0.7]
    positions[5] = [0.5 + amplitude * np.sin(phase - 0.5), 0.6]
    positions[6] = [0.5 + amplitude * np.sin(phase - 0.5), 0.5]
    
    # Left arm
    positions[7] = [0.5 + amplitude * np.sin(phase + 0.5), 0.7]
    positions[8] = [0.5 + amplitude * np.sin(phase + 0.5), 0.6]
    positions[9] = [0.5 + amplitude * np.sin(phase + 0.5), 0.5]
    
    # Right leg
    positions[10] = [0.5 + amplitude * np.sin(phase + 0.5), 0.5]
    positions[11] = [0.5 + amplitude * np.sin(phase + 0.5), 0.4]
    positions[12] = [0.5 + amplitude * np.sin(phase + 0.5), 0.3]
    
    # Left leg
    positions[13] = [0.5 + amplitude * np.sin(phase - 0.5), 0.5]
    positions[14] = [0.5 + amplitude * np.sin(phase - 0.5), 0.4]
    positions[15] = [0.5 + amplitude * np.sin(phase - 0.5), 0.3]
    
    scat.set_offsets(positions)
    return scat,

# Setup plot
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
scat = ax.scatter([], [], s=100, c='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True, interval=1000/fps)

plt.show()
