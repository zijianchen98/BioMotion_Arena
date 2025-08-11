
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-1, -2], # Left elbow
    [1, -2],  # Right elbow
    [-1, -4], # Left wrist
    [1, -4],  # Right wrist
    [0, -3],  # Spine
    [0, -5],  # Pelvis
    [-1, -6], # Left hip
    [1, -6],  # Right hip
    [-1, -7], # Left knee
    [1, -7],  # Right knee
    [-1, -8], # Left ankle
    [1, -8]   # Right ankle
])

# Define the animation parameters
num_frames = 100  # Number of frames in the animation
frame_rate = 30   # Frames per second
roll_speed = 0.1  # Speed of the roll (adjustable)

# Function to update the positions for each frame
def update_positions(frame):
    # Simulate forward rolling by rotating and translating the points
    theta = roll_speed * frame  # Angle of rotation
    
    # Rotation matrix for rolling around the y-axis
    rotation_matrix = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    
    # Apply rotation to each point
    rotated_points = np.dot(initial_positions, rotation_matrix.T)
    
    # Translate the points forward along the x-axis
    translation = np.array([theta * 0.5, 0, 0])  # Forward movement
    translated_points = rotated_points + translation
    
    # Extract x and y coordinates for plotting
    x = translated_points[:, 0]
    y = translated_points[:, 1]
    
    return x, y

# Create the animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    x, y = update_positions(frame)
    scatter.set_offsets(np.c_[x, y])
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=1000 / frame_rate, blit=True
)

# Display the animation
plt.show()
