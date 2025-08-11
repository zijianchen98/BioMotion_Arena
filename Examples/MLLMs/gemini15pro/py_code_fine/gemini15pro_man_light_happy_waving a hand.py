
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point lights
# These are approximate coordinates based on the provided image
initial_positions = np.array([
    [0, 5], [-1, 4], [1, 4],  # Head
    [-2, 3], [0, 3], [2, 3],  # Shoulders & Neck
    [-3, 2], [-1, 2], [1, 2], [3, 2], # Elbows & Chest 
    [-2, 1], [2, 1], # Hips
    [-2, 0], [2, 0], # Knees
    [0, 6] # waving hand
])


# Number of frames in the animation
num_frames = 60


# Function to update the positions of the point lights for each frame
def update(frame):
    x = initial_positions[:, 0]
    y = initial_positions[:, 1]
    # Simple wave motion for the right hand (point 14)
    y[14] = initial_positions[14, 1] + 0.2 * np.sin(2 * np.pi * frame / num_frames)  # Add some wave motion for hand
    scatter.set_offsets(np.c_[x, y])  # Update the positions of the points
    return scatter,



# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])


# Create the scatter plot for the point lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=20, c='white')



# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, interval = 30)

# Save the animation as a GIF (optional) 
#ani.save('happyman_wave.gif', writer='imagemagick', fps=30)  # Requires imagemagick

# Display the animation
plt.show()
