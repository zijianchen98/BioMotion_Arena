
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
# Points are arranged to represent a human figure
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-1, -2], # Left elbow
    [1, -2],  # Right elbow
    [-1, -3], # Left hand
    [1, -3],  # Right hand
    [0, -4],  # Torso
    [-1, -5], # Left hip
    [1, -5],  # Right hip
    [-1, -6], # Left knee
    [1, -6],  # Right knee
    [-1, -7], # Left foot
    [1, -7],  # Right foot
    [0, -8]   # Center of mass (for rolling)
])

# Define the number of frames for the animation
num_frames = 100

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 5)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Function to update the positions of the points for each frame
def update(frame):
    # Define the rolling motion parameters
    angle = np.radians(360 / num_frames * frame)  # Rolling angle
    center_of_mass = initial_positions[-1]  # Last point is the center of mass
    
    # Apply rotation around the center of mass
    rotated_positions = []
    for pos in initial_positions[:-1]:  # Exclude the center of mass
        relative_pos = pos - center_of_mass
        rotated_x = relative_pos[0] * np.cos(angle) - relative_pos[1] * np.sin(angle)
        rotated_y = relative_pos[0] * np.sin(angle) + relative_pos[1] * np.cos(angle)
        new_pos = np.array([rotated_x, rotated_y]) + center_of_mass
        rotated_positions.append(new_pos)
    
    # Add the center of mass back
    rotated_positions.append(center_of_mass)
    
    # Update the scatter plot
    scatter.set_offsets(rotated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
