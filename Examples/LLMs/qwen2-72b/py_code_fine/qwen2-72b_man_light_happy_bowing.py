
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the positions of the 15 points representing the happy man
point_positions = np.array([
    [0.2, 0.8],  # head
    [0.15, 0.7], [0.25, 0.7],  # eyes
    [0.1, 0.6], [0.3, 0.6],  # shoulders
    [0.05, 0.5], [0.15, 0.5], [0.25, 0.5], [0.35, 0.5],  # arms
    [0.15, 0.4], [0.25, 0.4],  # waist
    [0.1, 0.3], [0.2, 0.3], [0.3, 0.3],  # legs
])

# Define the initial position and velocity of each point
positions = np.tile(point_positions, (num_frames, 1))
velocities = np.zeros_like(positions)

# Define the animation function
def update(frame):
    global positions, velocities
    
    # Update the positions based on the velocities
    positions[frame] += velocities[frame]
    
    # Ensure the points stay within the figure bounds
    positions[frame] = np.clip(positions[frame], 0, 1)
    
    # Update the velocities for a smooth and natural movement
    velocities[frame] = 0.01 * (np.random.randn(*velocities.shape[1:]) - 0.5)
    
    # Clear the previous frame
    ax.clear()
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_facecolor('black')
    
    # Plot the points
    ax.scatter(positions[frame][:, 0], positions[frame][:, 1], color='white')

# Create the figure and axis
fig, ax = plt.subplots(figsize=(5, 5))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Show the animation
plt.show()
