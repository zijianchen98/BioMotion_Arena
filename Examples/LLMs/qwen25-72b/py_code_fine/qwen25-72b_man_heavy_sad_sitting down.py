
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axes
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Number of point-lights
num_points = 15

# Initial positions of the points (x, y)
positions = np.array([
    [0, 5],  # Head
    [-1, 4], [1, 4],  # Shoulders
    [-2, 3], [2, 3],  # Elbows
    [-3, 2], [3, 2],  # Hands
    [0, 3],  # Spine
    [0, 2],  # Waist
    [-1, 1], [1, 1],  # Hips
    [-2, 0], [2, 0],  # Knees
    [-3, -1], [3, -1],  # Ankles
    [-4, -2], [4, -2]  # Feet
])

# Create scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    global positions
    # Simulate sitting down motion
    if frame < 30:
        # Lower the body gradually
        positions[:, 1] -= 0.1
        # Bend knees and elbows
        positions[4:6, 1] -= 0.05
        positions[6:8, 1] -= 0.05
        positions[9:11, 1] -= 0.05
        positions[11:13, 1] -= 0.05
        positions[13:15, 1] -= 0.05
    elif frame < 60:
        # Continue lowering the body
        positions[:, 1] -= 0.1
        # Further bend knees and elbows
        positions[4:6, 1] -= 0.05
        positions[6:8, 1] -= 0.05
        positions[9:11, 1] -= 0.05
        positions[11:13, 1] -= 0.05
        positions[13:15, 1] -= 0.05
    else:
        # Final adjustment to make the sitting position more stable
        positions[4:6, 1] -= 0.05
        positions[6:8, 1] -= 0.05
        positions[9:11, 1] -= 0.05
        positions[11:13, 1] -= 0.05
        positions[13:15, 1] -= 0.05
    
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=90, interval=50, blit=True)

# Show the animation
plt.show()
