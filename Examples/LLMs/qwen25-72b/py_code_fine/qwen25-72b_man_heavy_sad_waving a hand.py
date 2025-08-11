
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the point-lights for the sadman waving a hand
# These positions are simplified and may need to be adjusted for more realism
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-1.5, -2], # Left elbow
    [1.5, -2],  # Right elbow
    [-2, -3],   # Left hand
    [1.5, -3],  # Right hand (initial position)
    [0, -2],    # Spine
    [0, -3],    # Hip
    [-1, -4],   # Left knee
    [1, -4],    # Right knee
    [-1.5, -5], # Left foot
    [1.5, -5],  # Right foot
    [0, -4],    # Center of mass
    [1.5, -3]   # Right hand (final position after wave)
])

# Function to update the positions of the point-lights
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Wave the right hand
    if frame < 50:
        positions[6] = [1.5 + 0.5 * np.sin(2 * np.pi * frame / 50), -3]
    else:
        positions[6] = [1.5 + 0.5 * np.sin(2 * np.pi * (frame - 50) / 50), -3]
    
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-6, 1)
ax.set_aspect('equal')
ax.axis('off')

# Create the point-lights
points = ax.scatter([], [], s=50, color='white')

# Update function for the animation
def animate(frame):
    positions = update_positions(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
