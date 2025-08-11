
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 50

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 3],  # Head
    [-0.5, 2.5], [0.5, 2.5],  # Shoulders
    [-1, 2], [1, 2],  # Elbows
    [-1.5, 1.5], [1.5, 1.5],  # Wrists
    [-0.2, 1.5], [0.2, 1.5],  # Torso
    [-0.5, 0], [0.5, 0],  # Hips
    [-1, -1], [1, -1],  # Knees
    [-1.5, -2], [1.5, -2]   # Ankles
])

# Define the range for random movement
movement_range = 0.1

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 4)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20)

# Define the update function for the animation
def update(frame):
    # Calculate new positions for each point-light with vertical jump
    new_positions = initial_positions + np.random.uniform(-movement_range, movement_range, size=initial_positions.shape)
    
    # Simulate a jump-like motion
    jump_height = 1  # Adjust for jump height
    jump_frequency = 5 # How many frames constitute the jump
    
    # This section creates the jump
    jump_factor = np.sin(2 * np.pi * frame / jump_frequency)  # A sinusoid to create a "jump"
    
    # Now modify the y positions
    new_positions[:, 1] = initial_positions[:, 1] + jump_height*np.abs(jump_factor) + np.random.uniform(-movement_range, movement_range, size=initial_positions[:, 1].shape)

    # Update the scatter plot with the new positions
    scatter.set_offsets(new_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
