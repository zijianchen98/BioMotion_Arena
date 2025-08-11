
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Create an array for the points representing the limbs
points = np.zeros((num_points, 2))

# Initial positions for a standing person (limb positions)
points[0] = [0, 0]        # Head
points[1] = [0, -0.4]     # Body
points[2] = [-0.1, -0.8]  # Left leg
points[3] = [0.1, -0.8]   # Right leg
points[4] = [-0.4, -0.4]  # Left arm
points[5] = [0.4, -0.4]   # Right arm
# Additional points for stiffness or hand movement
# (You can modify these for realism)
for i in range(6, num_points):
    points[i] = [0.0, -0.4 + (i - 6) * 0.1]

# Plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Simulate the jump by adjusting y-coordinates
    jump_height = 0.5 * np.sin(frame / 10 * np.pi)
    
    # Adjusting the positions of the points
    points[0, 1] = jump_height + 1.0  # Head
    points[1, 1] = jump_height + 0.6  # Body
    points[2, 1] = jump_height + 0.2  # Left leg 
    points[3, 1] = jump_height + 0.2  # Right leg
    points[4, 1] = jump_height + 0.6  # Left arm
    points[5, 1] = jump_height + 0.6  # Right arm
    
    # Update the scatter plot
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True)

# Show the animation
plt.show()
