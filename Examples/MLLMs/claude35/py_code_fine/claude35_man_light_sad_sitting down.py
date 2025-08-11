
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and the axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 2.5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Define the initial positions of 15 points (limbs and head)
points = np.array([
    [0, 1.5],     # Head
    [-0.5, 1],    # Left shoulder
    [0.5, 1],     # Right shoulder
    [-0.5, 0.5],  # Left elbow
    [0.5, 0.5],   # Right elbow
    [-0.75, 0],   # Left hand
    [0.75, 0],    # Right hand
    [-0.5, 0],    # Left hip
    [0.5, 0],     # Right hip
    [-0.5, -0.5], # Left knee
    [0.5, -0.5],  # Right knee
    [-0.25, -1],  # Left foot
    [0.25, -1],   # Right foot
    [0, 0],       # Torso (center)
    [-0.25, 0.5], # Mid torso (left)
    [0.25, 0.5]   # Mid torso (right)
])

# Create scatter plot for points
scat = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Define the sitting down animation function
def animate(frame):
    # Calculate new positions to simulate sitting down
    new_points = points.copy()
    
    # Modify y positions to simulate sitting down
    if frame < 30:
        new_points[:, 1] -= 0.05  # Gradually lower
    elif frame < 60:
        new_points[:, 1] -= 0.05  # Continue lowering
    else:
        new_points[:, 1] += 0.0    # Hold position

    # Update scatter plot data
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=80, interval=50, blit=True)

# Display the animation
plt.show()
