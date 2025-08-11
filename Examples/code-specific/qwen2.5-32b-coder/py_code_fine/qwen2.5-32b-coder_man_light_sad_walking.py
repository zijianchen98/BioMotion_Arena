
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initial positions of the lights (simplified model of a walking figure)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.5], [-0.2, -1.0], [-0.3, -1.5],  # Left arm
    [0.1, -0.5], [0.2, -1.0], [0.3, -1.5],   # Right arm
    [0, -0.8],  # Torso
    [-0.1, -1.3], [-0.2, -2.0], [-0.3, -2.7],  # Left leg
    [0.1, -1.3], [0.2, -2.0], [0.3, -2.7]   # Right leg
])

# Function to update the positions based on walking motion
def update_positions(frame):
    phase = frame / frames * 2 * np.pi
    x_shift = 0.2 * np.sin(phase)
    y_shift = 0.1 * np.cos(phase)
    
    # Update positions for walking motion
    positions = initial_positions.copy()
    positions[[1, 2, 3, 10, 11, 12]] += [x_shift, -y_shift]  # Left arm/leg
    positions[[4, 5, 6, 7, 13, 14]] -= [x_shift, -y_shift]  # Right arm/leg
    
    # Smooth transition for torso
    positions[7] += [0, 0.05 * np.sin(phase)]
    
    return positions

# Setup plot
fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-3, 1)
ax.axis('off')

# Initialize scatter plot
scatter = ax.scatter([], [], s=100, c='white')

# Update function for animation
def animate(i):
    positions = update_positions(i)
    scatter.set_offsets(positions)
    return scatter,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/fps, blit=True)

# Show plot
plt.show()
