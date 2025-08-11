
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These positions represent a simplified human figure
initial_positions = np.array([
    [0, 0],  # Head
    [-0.5, -0.5],  # Left shoulder
    [0.5, -0.5],  # Right shoulder
    [-1, -1],  # Left elbow
    [1, -1],  # Right elbow
    [-1.25, -1.5],  # Left hand
    [1.25, -1.5],  # Right hand
    [0, -0.75],  # Spine
    [0, -1.5],  # Waist
    [-0.5, -2],  # Left hip
    [0.5, -2],  # Right hip
    [-0.75, -3],  # Left knee
    [0.75, -3],  # Right knee
    [-0.75, -4],  # Left foot
    [0.75, -4],  # Right foot
])

# Define the motion pattern (vertical movement for jumping)
def motion_pattern(t):
    height = 0.5 * np.sin(t)
    return height

# Animation update function
def update(frame):
    t = frame / 10.0  # Adjust speed of animation
    height = motion_pattern(t)
    
    # Update the positions
    new_positions = initial_positions.copy()
    new_positions[:, 1] += height
    
    # Update the plot
    scatter.set_offsets(new_positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-4.5, 0.5)
ax.set_facecolor('black')
plt.axis('off')

# Create the scatter plot of the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200), interval=20, blit=True)

# Display the animation
plt.show()
