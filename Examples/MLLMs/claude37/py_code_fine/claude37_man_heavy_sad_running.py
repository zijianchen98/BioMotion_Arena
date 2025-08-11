
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# **Define Constants**
NUM_POINTS = 15
FPS = 30               # Frames per second
DURATION = 5           # Duration in seconds

# Define initial positions of the point-lights representing the sad man's body
def init_positions():
    # Set dynamic positions for a 'running' motion
    body_positions = np.zeros((NUM_POINTS, 2))
    
    # Placement of points
    body_positions[0] = [0, 2]   # Head
    body_positions[1] = [-0.5, 1.5] # Left shoulder
    body_positions[2] = [0.5, 1.5]  # Right shoulder
    body_positions[3] = [-0.5, 1]    # Left elbow
    body_positions[4] = [0.5, 1]     # Right elbow
    body_positions[5] = [0, 0]      # Body center
    body_positions[6] = [-0.5, -1]   # Left hip
    body_positions[7] = [0.5, -1]    # Right hip
    body_positions[8] = [-1, -2]      # Left knee
    body_positions[9] = [1, -2]       # Right knee
    body_positions[10] = [-1, -3]     # Left foot
    body_positions[11] = [1, -3]      # Right foot
    body_positions[12] = [0, -3.5]    # Weight
    body_positions[13] = [0, 0]       # Center point for weight
    body_positions[14] = [0, 1]       # Additional point for more realism

    return body_positions

# Animation update function
def update(frame):
    # Clear the current points
    plt.clf()

    # Update positions with a simple running motion
    t = frame / (DURATION * FPS) * 2 * np.pi  # Normalized time
    positions = init_positions()
    
    # Apply motion with a sine wave for natural running effect
    positions[:, 0] += np.sin(t * 2) * 0.2  # Horizontal motion
    positions[:, 1] += np.cos(t * 2) * 0.2 - 0.1  # Vertical motion (would simulate running)

    # Plotting the points (white points on the black background)
    plt.scatter(positions[:, 0], positions[:, 1], color='white', s=100)
    plt.xlim(-3, 3)
    plt.ylim(-4, 1)
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axes

# **Setup Animation**
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=int(DURATION * FPS), interval=1000/FPS)
plt.show()
