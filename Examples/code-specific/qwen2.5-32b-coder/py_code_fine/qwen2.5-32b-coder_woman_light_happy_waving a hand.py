
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
background_color = 'black'
point_color = 'white'

# Initial positions of the point lights (simplified model)
initial_positions = np.array([
    [0.5, 0.7],  # Head
    [0.4, 0.6],  # Left shoulder
    [0.6, 0.6],  # Right shoulder
    [0.3, 0.5],  # Left elbow
    [0.7, 0.5],  # Right elbow
    [0.2, 0.4],  # Left wrist
    [0.8, 0.4],  # Right wrist
    [0.5, 0.5],  # Spine
    [0.5, 0.4],  # Hip
    [0.4, 0.3],  # Left knee
    [0.6, 0.3],  # Right knee
    [0.4, 0.2],  # Left ankle
    [0.6, 0.2],  # Right ankle
    [0.5, 0.3],  # Pelvis
    [0.8, 0.5]   # Right hand waving start position
])

# Function to generate the wave motion
def wave_hand(t):
    x_offset = 0.05 * np.sin(2 * np.pi * t / frames)
    y_offset = 0.05 * np.cos(2 * np.pi * t / frames)
    return x_offset, y_offset

# Update function for the animation
def update(frame, scat):
    positions = initial_positions.copy()
    x_offset, y_offset = wave_hand(frame)
    positions[14] += np.array([x_offset, y_offset])  # Update right hand position
    scat.set_offsets(positions)
    return scat,

# Setup figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_facecolor(background_color)

# Scatter plot for point lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color=point_color, s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, fargs=(scat,), blit=True, repeat=True)

# Show animation
plt.show()
