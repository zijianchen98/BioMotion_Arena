
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set number of point-lights
num_lights = 15

# Initialize positions of the point-lights
positions = np.zeros((num_lights, 2))

# Define body part locations for the animation
def initialize_positions():
    # Example positions for a simple human-like structure
    positions[0] = [0, 5]   # Head
    positions[1] = [-1, 4]  # Left Shoulder
    positions[2] = [1, 4]   # Right Shoulder
    positions[3] = [-1, 3]  # Left Elbow
    positions[4] = [1, 3]   # Right Elbow
    positions[5] = [-1, 1]  # Left Hand
    positions[6] = [1, 1]   # Right Hand
    positions[7] = [0, 2]   # Torso
    positions[8] = [-1, 0]  # Left Hip
    positions[9] = [1, 0]   # Right Hip
    positions[10] = [-1, -3]  # Left Knee
    positions[11] = [1, -3]  # Right Knee
    positions[12] = [-1, -5]  # Left Foot
    positions[13] = [1, -5]   # Right Foot
    positions[14] = [0, -2]    # Mid Body

def update_positions(frame):
    # Update the positions to simulate turning around
    theta = frame * np.pi / 60  # 0 to 360 degrees over 60 frames
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                                 [np.sin(theta), np.cos(theta)]])
    
    global positions
    positions_rotated = np.dot(positions, rotation_matrix)
    
    # Clear the axis for new frame
    ax.clear()
    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)
    ax.set_facecolor('black')
    
    # Plot each point-light
    ax.scatter(positions_rotated[:, 0], positions_rotated[:, 1], color='white', s=100)

# Create plot
fig, ax = plt.subplots()
initialize_positions()

# Animation
ani = animation.FuncAnimation(fig, update_positions, frames=60, interval=100)

plt.show()
