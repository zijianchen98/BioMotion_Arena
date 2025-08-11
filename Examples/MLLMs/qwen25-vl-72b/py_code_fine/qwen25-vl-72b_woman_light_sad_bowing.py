
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.5], [0, 0.5], [0.5, 0.5],
    [-0.7, 0], [-0.3, 0], [0, 0], [0.3, 0], [0.7, 0],
    [-0.5, -0.5], [0, -0.5], [0.5, -0.5],
    [-0.3, -1], [0, -1], [0.3, -1]
])

# Define the parameters for the animation
num_frames = 100
frame_rate = 30

# Create a function to update the positions of the points for each frame
def update(frame):
    # Calculate the new positions of the points based on the current frame number
    new_positions = initial_positions.copy()
    new_positions[:, 1] -= 0.01 * frame  # Move the points downward over time
    
    # Update the positions of the points in the scatter plot
    scat.set_offsets(new_positions)
    
    return scat,

# Set up the figure and axis for the animation
fig, ax = plt.subplots(figsize=(4, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/frame_rate, blit=True)

# Display the animation
plt.show()
