
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (happyman)
# These coordinates represent a standing pose
initial_positions = np.array([
    [0, 0],  # Head
    [-1, -1], [-1, -2], [-1, -3],  # Left arm
    [1, -1], [1, -2], [1, -3],     # Right arm
    [0, -4],                       # Torso
    [-1, -5], [-1, -6],            # Left leg
    [1, -5], [1, -6],              # Right leg
    [0, -7]                        # Feet
])

# Function to update the positions for rolling motion
def update_positions(positions, angle):
    # Define the center of rotation (torso)
    center = positions[4]
    
    # Translate points so that the center is at the origin
    translated = positions - center
    
    # Apply rotation matrix
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    rotated = np.dot(translated, rotation_matrix)
    
    # Translate back
    new_positions = rotated + center
    
    # Add vertical displacement to simulate rolling along the ground
    new_positions[:, 1] += 0.5 * np.sin(np.radians(angle))
    
    return new_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-8, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    angle = frame * 5  # Angle of rotation in degrees
    updated_positions = update_positions(initial_positions, angle)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=72, interval=50, blit=True  # 72 frames for a full 360-degree rotation
)

# Display the animation
plt.show()
