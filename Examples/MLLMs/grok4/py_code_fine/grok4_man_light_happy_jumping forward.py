
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Setting up the figure
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Number of point-lights
num_points = 15

# Initial positions for the point-lights
initial_positions = np.array([
    [0, 2],  # Head
    [-1, 1.5], [1, 1.5],  # Shoulders
    [-1, 1], [1, 1],       # Elbows
    [-1, 0.5], [1, 0.5],  # Wrists
    [-0.5, 0], [0.5, 0],   # Hands
    [-0.5, -1], [0.5, -1], # Hips
    [-0.5, -2], [0.5, -2], # Knees
    [-0.5, -3], [0.5, -3], # Ankles
])

# Function to update the positions for jumping motion
def update(frame):
    ax.cla()  # Clear the previous frame
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')
    
    # Calculate new positions
    forward_shift = frame * 0.1  # Forward movement
    vertical_jump = np.abs(np.sin(frame * 0.2) * 2)  # Jumping motion

    new_positions = initial_positions.copy()
    
    # Shift points
    new_positions[:, 0] += forward_shift
    new_positions[:, 1] += vertical_jump

    # Plot the point-lights
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=100)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50)

plt.show()
