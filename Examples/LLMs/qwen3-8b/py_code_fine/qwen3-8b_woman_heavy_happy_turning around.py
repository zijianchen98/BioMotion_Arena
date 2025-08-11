
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.axis('off')

# Define the 15 point-light positions for a happy woman turning around
# These are simplified coordinates representing joints and body parts
# Positions are relative to the center of the body

# Initial positions (approximate joint positions)
initial_positions = np.array([
    [0.0, 0.5],   # Head
    [0.0, 0.2],   # Neck
    [-0.3, 0.1],  # Left shoulder
    [-0.2, -0.2], # Left elbow
    [-0.1, -0.5], # Left wrist
    [0.3, 0.1],   # Right shoulder
    [0.2, -0.2],  # Right elbow
    [0.1, -0.5],  # Right wrist
    [-0.5, -0.5], # Left hip
    [0.5, -0.5],  # Right hip
    [-0.5, -1.0], # Left knee
    [0.5, -1.0],  # Right knee
    [-0.5, -1.5], # Left ankle
    [0.5, -1.5],  # Right ankle
    [0.0, -0.75]  # Torso center
])

# Define a function to animate the turning motion
def animate(frame):
    # Rotate the positions around the center of the body
    center = initial_positions[14]  # torso center
    rotated = np.zeros_like(initial_positions)
    for i in range(15):
        x, y = initial_positions[i] - center
        angle = np.radians(frame * 10)  # rotate by 10 degrees per frame
        rotated_x = x * np.cos(angle) - y * np.sin(angle)
        rotated_y = x * np.sin(angle) + y * np.cos(angle)
        rotated[i] = [rotated_x + center[0], rotated_y + center[1]]
    
    # Clear previous points
    for point in points:
        point.remove()
    
    # Plot new points
    points.clear()
    for x, y in rotated:
        point = Circle((x, y), 0.03, color='white')
        ax.add_patch(point)
        points.append(point)

# Create a list to hold the point light objects
points = []

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=72, interval=50, blit=False)

# Show the animation
plt.show()
