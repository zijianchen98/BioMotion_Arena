
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the animation
n_points = 15
frames = 100
base_height = 0.5  # The center height of the points
step_size = 0.1    # How much the points move per frame

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 2)
ax.set_facecolor('black')

# Initialize the point-light positions
# The points layout similar to a stick figure
points = np.array([[0, 1.5],  # Head
                   [-0.1, 1.3], [0.1, 1.3],  # Shoulders
                   [-0.15, 1.0], [0.15, 1.0],  # Arms
                   [0, 1.0],  # Center
                   [0, 0.8],  # Torso
                   [-0.1, 0.5], [0.1, 0.5],  # Hips
                   [-0.1, 0.2], [0.1, 0.2],  # Legs
                   [0, 0.0]]).astype(float)  # Feet

# Add a "weight" point as a heavier mass in the left hand
weight = np.array([-0.2, 0.5])

# Initialize scatter object
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    global points
    
    # Update the positions of points to create a walking effect
    # Calculate walking movement by adjusting vertical heights
    points[1][:] += np.cos(frame * 0.1) * step_size  # Right shoulder
    points[2][:] += np.cos(frame * 0.1) * step_size  # Left shoulder
    points[3][:] += np.sin(frame * 0.1) * step_size  # Right arm
    points[4][:] += np.sin(frame * 0.1) * step_size  # Left arm
    points[6][:] += np.cos(frame * 0.1) * step_size  # Torso
    points[7][:] += np.cos(frame * 0.1) * step_size  # Hips
    points[8][:] += np.sin(frame * 0.1) * step_size  # Right leg
    points[9][:] += np.sin(frame * 0.1) * step_size  # Left leg
     
    # Make the points move left and right depending on the frame
    points[:, 0] += np.sin(frame * 0.05) * 0.02

    # Update scatter object data
    scatter.set_offsets(points)
    
    # Update the weight position
    weight[1] = 0.5 + np.sin(frame * 0.1) * 0.05  # Move weight vertically
    ax.scatter(weight[0], weight[1], color='white', s=100)  # Plot weight on top
    
    return scatter,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
