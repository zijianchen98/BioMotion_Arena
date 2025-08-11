
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points for a happy, heavy person
def init_positions():
    positions = np.array([
        [0.5, 0.1],  # Head
        [0.3, 0.2],  # Left shoulder
        [0.7, 0.2],  # Right shoulder
        [0.2, 0.3],  # Left elbow
        [0.8, 0.3],  # Right elbow
        [0.1, 0.4],  # Left hand
        [0.9, 0.4],  # Right hand
        [0.45, 0.3], # Body center
        [0.55, 0.3], # Body center
        [0.4, 0.6],  # Left hip
        [0.6, 0.6],  # Right hip
        [0.3, 0.7],  # Left knee
        [0.7, 0.7],  # Right knee
        [0.2, 0.8],  # Left foot
        [0.8, 0.8],  # Right foot
    ])
    return positions

# Function to update positions for the jumping motion
def update_positions(positions, t):
    amplitude = 0.1
    freq = 2 * np.pi * 0.1
    offset = amplitude * np.sin(freq * t)
    
    updated_positions = positions.copy()
    updated_positions[:, 1] += offset
    
    return updated_positions

# Initialization function
def init():
    points.set_offsets(init_positions())
    return points,

# Animation update function
def animate(t):
    new_positions = update_positions(init_positions(), t)
    points.set_offsets(new_positions)
    return points,

# Set up figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Plot points
points = ax.scatter([], [], s=100, color='white')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 120),
                                  init_func=init, blit=True)

plt.show()
