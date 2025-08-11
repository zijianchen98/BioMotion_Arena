
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')  # Remove the axis

# Create points to represent joints and ends
num_points = 15
points = np.zeros((num_points, 2))
points[0] = [0, 0]  # Center (hips)
points[1] = [0, 1.5]  # Head
points[2] = [-0.5, 1.3]  # Left shoulder
points[3] = [0.5, 1.3]  # Right shoulder
points[4] = [-0.5, 1.0]  # Left elbow
points[5] = [0.5, 1.0]  # Right elbow
points[6] = [-1, 0.5]  # Left wrist
points[7] = [1, 0.5]  # Right wrist
points[8] = [-0.5, 0]  # Left hip
points[9] = [0.5, 0]  # Right hip
points[10] = [-1.5, -2]  # Left knee
points[11] = [1.5, -2]  # Right knee
points[12] = [-2, -4]  # Left foot
points[13] = [2, -4]  # Right foot
# Add a weight point
points[14] = [0, 2.5]  # Weight above hip

# Initialize the scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update the animation
def update(frame):
    # Update position for a walking motion
    shift = np.sin(frame / 10) * 0.1
    points[0, 0] += shift  # Hips move side to side
    points[:-1, 1] += np.sin(frame / 10) * 0.1  # Up and down motion for legs
    points[14, 1] += np.sin(frame / 10) * 0.1  # Weight follows the motion
    scat.set_offsets(points)
    return scat,

# Create animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), blit=True, interval=50)

plt.show()
