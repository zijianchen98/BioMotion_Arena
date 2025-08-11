
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set Parameters
num_points = 15
duration = 5  # seconds
fps = 30  # frames per second
total_frames = duration * fps

# Setup Figure
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')

# Create Point-Light Positions (dummy data for demonstration)
# Adjust these coordinates to match a realistic running man
points = np.array([
    [0, 0],   # Center of the body
    [-1, 2],  # Head
    [1, 2],   # Head
    [-1, 1],  # Left shoulder
    [1, 1],   # Right shoulder
    [-1, 0],  # Left hand
    [1, 0],   # Right hand
    [-1.5, -1], # Left leg upper
    [1.5, -1], # Right leg upper
    [-1, -3], # Left leg lower
    [1, -3],  # Right leg lower
    [-2, -1], # Left foot
    [2, -1],  # Right foot
    [0, 3],   # Left side
    [0, -4],  # Right side
    [1, -4]   # Back-side
])

# Function to update the positions of points
def update(frame):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_facecolor('black')
    
    # Calculate new positions based on frame
    # Simple vertical running motion
    new_positions = points.copy()
    new_positions[:, 1] += np.sin(np.radians(frame * 10)) * 0.5  # simulate running motion
    
    # Draw points
    for point in new_positions:
        ax.plot(point[0], point[1], 'o', color='white', markersize=10)

# Create Animation
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=1000/fps)

# Display the Animation
plt.show()
