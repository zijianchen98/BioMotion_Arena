
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# These positions are placeholders and will be updated dynamically
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -3], # Left elbow
    [2, -3],  # Right elbow
    [-3, -5], # Left wrist
    [3, -5],  # Right wrist
    [-1, -6], # Left hip
    [1, -6],  # Right hip
    [-2, -8], # Left knee
    [2, -8],  # Right knee
    [-3, -10], # Left ankle
    [3, -10], # Right ankle
    [-4, -12], # Left foot
    [4, -12]  # Right foot
])

# Function to update the positions based on the frame
def update_positions(frame):
    # Simulate rolling motion by rotating and translating the points
    angle = np.radians(360 * frame / num_frames)  # Full rotation over the animation
    
    # Define the center of rotation (e.g., the head)
    center = initial_positions[0]
    
    # Create a rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation around the center
    rotated_points = []
    for point in initial_positions:
        # Translate point to origin, apply rotation, then translate back
        translated_point = point - center
        rotated_point = np.dot(rotation_matrix, translated_point)
        final_point = rotated_point + center
        rotated_points.append(final_point)
    
    return np.array(rotated_points)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def update(frame):
    positions = update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
