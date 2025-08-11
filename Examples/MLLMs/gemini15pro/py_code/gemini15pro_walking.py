
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the coordinates of the 15 point-lights
# These coordinates are placeholders and need to be adjusted based on the actual motion
# The structure should resemble a human figure with appropriate joint placements
initial_coordinates = np.array([
    [0, 100],  # Head top
    [-5, 90],  # Left shoulder
    [5, 90],   # Right shoulder
    [-10, 70], # Left elbow
    [10, 70],  # Right elbow
    [-15, 50], # Left wrist
    [15, 50],  # Right wrist
    [0, 70], # Center of the body
    [-5, 40], # Left hip
    [5, 40],  # Right hip 
    [-10, 20], # Left knee
    [10, 20], # Right knee
    [-15, 0], # Left ankle
    [15, 0], # Right ankle
    [0, -10] # Center of the feet
])

# Number of frames in the animation
num_frames = 50

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-20, 20) # Adjust limits as needed
ax.set_ylim(-20, 110)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter([], [], s=20, c='white') # Initialize scatter plot

def animate(i):
    # Simulate walking motion by updating coordinates
    coordinates = initial_coordinates.copy() # Make a copy to avoid modifying the original array
    # Example motion: Simple periodic movement
    coordinates[:, 0] += np.sin(2 * np.pi * i / num_frames) * 5  # Side-to-side sway
    coordinates[:, 1] -= 5 # Simulate forward walking by shifting down 
    # Add more sophisticated motion logic here based on walking biomechanics

    scat.set_offsets(coordinates) # Update point light locations in the scatter plot
    return scat,


ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Save the animation as a GIF (optional)
#ani.save('walking_animation.gif', writer='imagemagick', fps=20)


plt.show()




