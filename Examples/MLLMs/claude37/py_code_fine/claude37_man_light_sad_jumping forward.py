
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the point-lights (simplified human figure)
# Initial positions for the lights
initial_positions = np.array([
    [0, 4],    # Head
    [-1, 3],   # Left shoulder
    [1, 3],    # Right shoulder
    [-1, 2],   # Left elbow
    [1, 2],    # Right elbow
    [0, 1],    # Torso
    [-1, 0],   # Left hip
    [1, 0],    # Right hip
    [-1, -2],  # Left knee
    [1, -2],   # Right knee
    [0, -3],   # Feet (middle foot)
    [-0.5, -3],# Left foot
    [0.5, -3], # Right foot
    [-1, 1],   # Left wrist
    [1, 1],    # Right wrist
    [0, 2]     # Hands (for dynamic motion)
])

# Function to update the position of point-lights for animation
def update(frame):
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_facecolor('black')
    
    # Calculate the new positions for the jump
    t = frame / 10  # time variable to control jump dynamics
    jump_height = 2 * np.sin(t * np.pi)  # sinewave for smooth jump
    forward_movement = t * 0.5  # linear forward movement

    # Update the positions
    positions = initial_positions.copy()
    positions[:, 0] += forward_movement  # Move forward
    positions[:, 1] += jump_height  # Jump up

    # Draw the points
    ax.plot(positions[:, 0], positions[:, 1], 'o', color='white')

# Set up the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 20), interval=100)

# Display the animation
plt.show()
