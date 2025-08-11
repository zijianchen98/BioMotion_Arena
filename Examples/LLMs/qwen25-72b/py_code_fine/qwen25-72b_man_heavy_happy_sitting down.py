
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
ax.axis('off')

# Define the points representing the body parts
points = [
    [0, 0],  # Torso center
    [-2, 2], [2, 2],  # Shoulders
    [-3, 4], [3, 4],  # Elbows
    [-4, 6], [4, 6],  # Hands
    [-2, -2], [2, -2],  # Hips
    [-3, -4], [3, -4],  # Knees
    [-4, -6], [4, -6],  # Feet
    [0, -8]  # Weight
]

# Convert points to a NumPy array
points = np.array(points)

# Create scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Function to update the position of the points
def update(frame):
    # Apply a sitting down motion
    if frame < 30:
        # Initial standing position
        pass
    elif frame < 60:
        # Transition to sitting position
        t = (frame - 30) / 30
        points[0, 1] = -t * 8  # Torso moves down
        points[1:7, 1] -= t * 2  # Upper body leans forward
        points[7:13, 1] -= t * 4  # Lower body bends
        points[13, 1] = -8  # Weight stays at the same height
    else:
        # Final sitting position
        points[0, 1] = -8  # Torso fully down
        points[1:7, 1] -= 2  # Upper body fully leaned forward
        points[7:13, 1] -= 4  # Lower body fully bent

    scat.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=90, interval=50)

# Display the animation
plt.show()
