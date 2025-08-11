
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

# Define the 15 point-light positions (representing body joints)
# These are simplified and biomechanically plausible for a jumping man
# Positions are in x, y coordinates

# Initial positions (simplified human body)
body_positions = np.array([
    [0.0, 0.0],        # Hip
    [0.2, 0.2],        # Knee
    [0.4, 0.4],        # Ankle
    [0.2, 0.4],        # Foot
    [-0.2, 0.2],       # Left hip
    [-0.4, 0.4],       # Left knee
    [-0.6, 0.6],       # Left ankle
    [-0.4, 0.6],       # Left foot
    [0.2, 0.6],        # Right hip
    [0.4, 0.8],        # Right knee
    [0.6, 1.0],        # Right ankle
    [0.4, 1.0],        # Right foot
    [0.0, 0.8],        # Torso
    [0.0, 1.2],        # Head
    [0.0, 1.4]         # Light on head
])

# Create circles for each point-light
points = [Circle((x, y), 0.03, color='white') for x, y in body_positions]
for point in points:
    ax.add_patch(point)

# Define a function to update the position of each point-light over time
def update(frame):
    # Simulate a jumping motion with a sine wave for vertical movement
    # Add a slight forward motion for realism
    y_offset = 0.2 * np.sin(0.1 * frame)
    x_offset = 0.05 * np.sin(0.05 * frame)
    
    for i, point in enumerate(points):
        x, y = body_positions[i]
        # Apply realistic motion (sine for vertical, slight forward)
        new_y = y + y_offset
        new_x = x + x_offset
        point.center = (new_x, new_y)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=False)

plt.show()
