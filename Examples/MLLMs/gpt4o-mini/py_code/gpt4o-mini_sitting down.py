
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Define the initial positions of 15 points representing the man
points = np.array([
    [0, 0.8],  # Head
    [-0.2, 0.6], [0.2, 0.6],  # Shoulders
    [-0.3, 0.4], [0.3, 0.4],  # Elbows
    [-0.1, 0.3], [0.1, 0.3],  # Hands
    [0, 0.1],  # Torso
    [-0.2, -0.2], [0.2, -0.2],  # Hips
    [-0.3, -0.5], [0.3, -0.5],  # Knees
    [-0.1, -0.8], [0.1, -0.8],  # Feet
])

# Create a scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Define the animation function
def update(frame):
    # Update positions to simulate sitting down
    sit_positions = np.copy(points)
    
    # Modify positions to simulate smooth sitting motion
    if frame < 50:
        sit_positions[1:, 1] -= 0.01 * frame  # moving points down a bit
    else:
        sit_positions[1:, 1] -= 0.01 * (100 - frame)  # move back up for exit animation
    
    scat.set_offsets(sit_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 100, 100), interval=50, blit=True)

# Show the animation
plt.show()
