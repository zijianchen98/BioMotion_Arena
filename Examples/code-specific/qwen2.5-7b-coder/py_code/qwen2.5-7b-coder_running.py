
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# Define the initial positions of the 15 point-lights
initial_positions = np.random.rand(15, 2) * 2 - 1

# Define the target positions for each frame
target_positions = np.array([
    [np.sin(t / 4), np.cos(t / 4)] for t in range(num_frames * 10)
])

# Define the function to update the positions of the point-lights
def update(frame):
    # Calculate the interpolation factor
    t = frame / num_frames
    
    # Interpolate between the initial and target positions
    current_positions = (1 - t) * initial_positions + t * target_positions[frame]
    
    # Clear the previous plot
    ax.clear()
    
    # Set the limits and aspect ratio
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Plot the point-lights
    ax.scatter(current_positions[:, 0], current_positions[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=100, repeat=False)

# Show the animation
plt.show()
