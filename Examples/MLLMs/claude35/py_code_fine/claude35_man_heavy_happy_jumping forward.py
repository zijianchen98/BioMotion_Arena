
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 1)
ax.axis('off')  # Turn off the axis

# Number of point lights
num_points = 15

# Initialize positions of point lights
# Create a basic skeleton with static positions for the happy man's key points
skeleton_positions = np.array([
    [0, 1],    # head
    [-0.5, 0.5],  # left shoulder
    [0.5, 0.5],   # right shoulder
    [-0.5, 0],     # left elbow
    [0.5, 0],      # right elbow
    [-0.6, -0.5],  # left hand
    [0.6, -0.5],   # right hand
    [-0.5, -1],    # left hip
    [0.5, -1],     # right hip
    [-0.8, -1.5],  # left knee
    [0.8, -1.5],   # right knee
    [-0.5, -2],    # left foot
    [0.5, -2],     # right foot
    [0, 0],        # center of the mass
])

# Create scatter points for the point lights
points = ax.scatter([], [], color='white')

# Update function for the animation
def update(frame):
    # Clear the previous frame
    points.set_offsets([])
    
    # Update positions to simulate jumping forward
    translation = 0.05 * frame  # Forward movement
    vertical_stretch = np.sin(np.pi * frame / 20) / 3  # Jump height adjustment

    # Calculate new positions
    updated_positions = skeleton_positions + np.array([[translation, vertical_stretch]] * num_points)
    
    # Update the scatter plot
    points.set_offsets(updated_positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
