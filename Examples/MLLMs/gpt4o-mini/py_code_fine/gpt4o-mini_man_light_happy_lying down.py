
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Define point light positions for lying down action
# Starting positions of the point lights (15 lights in a lying down position)
positions = np.array([
    [0, 1],    # Head
    [-0.3, 0.8], [0.3, 0.8],  # Shoulders
    [-0.5, 0.5], [0, 0.5], [0.5, 0.5],  # Elbows/Chest
    [-0.6, 0], [-0.3, 0], [0, 0], [0.3, 0], [0.6, 0],  # Hips/Torso
    [-0.5, -0.5], [0, -0.5], [0.5, -0.5],  # Legs
    [-0.3, -1], [0.3, -1]   # Feet
])

# Create scatter plot for the point-lights
points = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Update function for the animation
def update(frame):
    # Define motion parameters for lying down
    motion = 0.02 * np.sin(np.linspace(0, 2 * np.pi, len(positions)) + frame * 0.1)
    # Update positions smoothly
    new_positions = positions + motion[:, np.newaxis] * np.array([0.1, -0.1])
    points.set_offsets(new_positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show animation
plt.axis('off')  # Hide axes
plt.show()
