
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent the body parts: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -3], # Left elbow
    [2, -3],  # Right elbow
    [-1, -5], # Left wrist
    [1, -5],  # Right wrist
    [0, -6],  # Hips
    [-1, -8], # Left knee
    [1, -8],  # Right knee
    [-1, -10], # Left ankle
    [1, -10], # Right ankle
    [-2, -7], # Left hip
    [2, -7],  # Right hip
    [0, -9]   # Center of mass
])

# Function to update the positions of the points for each frame
def update_points(frame):
    # Define the rolling motion parameters
    radius = 2  # Radius of the rolling circle
    angle = 2 * np.pi / num_frames  # Angular increment per frame
    
    # Calculate the new center of rotation based on the rolling motion
    center_x = radius * np.sin(frame * angle)
    center_y = -radius * np.cos(frame * angle)
    
    # Update the positions of the points around the center of rotation
    updated_positions = []
    for pos in initial_positions:
        # Translate the point to the origin, rotate, and translate back
        translated_pos = pos - initial_positions[-1]  # Use the center of mass as reference
        rotated_pos = np.array([
            translated_pos[0] * np.cos(frame * angle) - translated_pos[1] * np.sin(frame * angle),
            translated_pos[0] * np.sin(frame * angle) + translated_pos[1] * np.cos(frame * angle)
        ])
        updated_pos = rotated_pos + np.array([center_x, center_y])
        updated_positions.append(updated_pos)
    
    return np.array(updated_positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-12, 2)
ax.axis('off')  # Hide the axes

# Initialize the scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    positions = update_points(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
