
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Initialize point-light positions for a "sadman"
# Body parts as coordinates in a 2D array (x, y)
body_parts = np.array([
    [0, 4],   # Head
    [-1, 3],  # Left Shoulder
    [1, 3],   # Right Shoulder
    [-1, 2],  # Left Elbow
    [1, 2],   # Right Elbow
    [-1, 1],  # Left Hand
    [1, 1],   # Right Hand
    [0, 2],   # Torso
    [-1, 0],  # Left Hip
    [1, 0],   # Right Hip
    [-1, -1], # Left Knee
    [1, -1],  # Right Knee
    [-1, -2], # Left Foot
    [1, -2],  # Right Foot
    [0, -1]   # Extra point for realism (center of mass)
])

# Function to update the positions for a jump
def update_positions(frame):
    plt.cla()  # Clear the current axes
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    # Calculate new positions for "jump" motion
    jump_height = np.sin(frame / 10.0) * 2  # Sine wave for vertical movement
    jump_forward = frame / 10.0             # Linear forward motion
    
    # Update coordinates with jump effect
    updated_parts = body_parts + np.array([jump_forward, jump_height])
    
    # Draw updated points
    plt.scatter(updated_parts[:, 0], updated_parts[:, 1], color='white')
    
    plt.gca().set_facecolor('black')

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update_positions, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()
