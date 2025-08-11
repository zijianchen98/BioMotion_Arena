
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights
# These are just example positions, you'll need to adjust them to represent the running motion
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.3, 1.5], # Left shoulder
    [0.3, 1.5],  # Right shoulder
    [-0.7, 1.0], # Left elbow
    [0.7, 1.0],  # Right elbow
    [-1.0, 0.5], # Left wrist
    [1.0, 0.5],  # Right wrist
    [-0.3, 0.8], # Left hip
    [0.3, 0.8],  # Right hip
    [-0.5, 0.0], # Left knee
    [0.5, 0.0],  # Right knee
    [-0.7, -0.8], # Left ankle
    [0.7, -0.8],  # Right ankle
    [-0.7, -1.5], # Left foot
    [0.7, -1.5]   # Right foot
])

# Define the movement of the point lights over time
# This is where you'll need to define the animation logic to simulate the running motion
def update_points(frame_num):
    # This is just an example, you'll need to adjust the movement to represent the running motion
    x = np.sin(np.linspace(0, 2*np.pi, num_lights) + frame_num/10) * 0.2
    y = np.cos(np.linspace(0, 2*np.pi, num_lights) + frame_num/10) * 0.1
    
    # Update the positions of the point lights
    positions = initial_positions + np.column_stack((x,y))
    
    # Update the scatter plot
    scatter.set_offsets(positions)
    
    return scatter,

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')

# Set the limits of the axes
ax.set_xlim([-2, 2])
ax.set_ylim([-3, 3])

# Remove the axes labels
ax.set_xticks([])
ax.set_yticks([])

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, interval=50, blit=True, save_count=num_frames)

# Show the animation
plt.show()
