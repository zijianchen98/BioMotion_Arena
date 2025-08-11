
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.axis('off')

# Define the initial positions of the points
points = [
    [0, 5],  # Head
    [-2, 4], [2, 4],  # Shoulders
    [-3, 3], [3, 3],  # Elbows
    [-4, 2], [4, 2],  # Hands
    [0, 3],  # Spine
    [-1, 1], [1, 1],  # Hips
    [-2, 0], [2, 0],  # Knees
    [-3, -1], [3, -1],  # Ankles
    [-4, -2], [4, -2]  # Feet
]

# Convert points to numpy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Define the sitting down motion
def update(frame):
    # Apply a smooth sitting down motion
    if frame < 30:
        # Initial phase: bending at the hips and knees
        points[8:, 1] -= 0.1 * np.sin(frame / 10)
        points[7, 1] -= 0.1 * np.sin(frame / 10)
        points[9, 1] -= 0.1 * np.sin(frame / 10)
        points[10:12, 1] -= 0.2 * np.sin(frame / 10)
        points[12:14, 1] -= 0.3 * np.sin(frame / 10)
        points[14:16, 1] -= 0.4 * np.sin(frame / 10)
    elif frame < 60:
        # Middle phase: lowering the body
        points[7:, 1] -= 0.1 * np.sin((frame - 30) / 10)
        points[10:12, 1] -= 0.2 * np.sin((frame - 30) / 10)
        points[12:14, 1] -= 0.3 * np.sin((frame - 30) / 10)
        points[14:16, 1] -= 0.4 * np.sin((frame - 30) / 10)
    else:
        # Final phase: stabilizing in the sitting position
        points[7:, 1] += 0.05 * np.sin((frame - 60) / 10)
        points[10:12, 1] += 0.1 * np.sin((frame - 60) / 10)
        points[12:14, 1] += 0.15 * np.sin((frame - 60) / 10)
        points[14:16, 1] += 0.2 * np.sin((frame - 60) / 10)
    
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=90, interval=50, blit=True)

# Display the animation
plt.show()
