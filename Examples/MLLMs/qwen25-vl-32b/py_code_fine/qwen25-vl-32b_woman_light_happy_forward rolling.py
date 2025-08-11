
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (joints)
# These positions are placeholders and will be updated dynamically
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -3], # Left elbow
    [2, -3],  # Right elbow
    [-2, -5], # Left wrist
    [2, -5],  # Right wrist
    [0, -6],  # Chest
    [-1, -8], # Left hip
    [1, -8],  # Right hip
    [-2, -10], # Left knee
    [2, -10], # Right knee
    [-2, -12], # Left ankle
    [2, -12], # Right ankle
    [0, -14]  # Feet
])

# Function to update the positions based on the rolling motion
def update_positions(frame):
    # Simulate rolling motion by rotating and translating the points
    angle = np.radians(360 * frame / num_frames)  # Full rotation over the animation
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Apply rotation to each point
    rotated_points = np.dot(initial_positions, rotation_matrix)
    
    # Translate the points to simulate rolling along the x-axis
    translation = np.array([frame * 0.1, 0])  # Adjust speed as needed
    translated_points = rotated_points + translation
    
    return translated_points

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_facecolor('black')  # Set background to black

# Initialize the scatter plot for the points
scatter = ax.scatter([], [], c='white', s=50)

# Animation function
def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()
