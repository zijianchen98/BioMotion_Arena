
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a woman sitting down
# These points are simplified and may need to be adjusted for more realism
points = np.array([
    [0.5, 1.0],  # Head
    [0.4, 0.8],  # Neck
    [0.3, 0.6],  # Left Shoulder
    [0.7, 0.6],  # Right Shoulder
    [0.2, 0.4],  # Left Elbow
    [0.8, 0.4],  # Right Elbow
    [0.1, 0.2],  # Left Hand
    [0.9, 0.2],  # Right Hand
    [0.4, 0.6],  # Left Hip
    [0.6, 0.6],  # Right Hip
    [0.3, 0.4],  # Left Knee
    [0.7, 0.4],  # Right Knee
    [0.2, 0.2],  # Left Foot
    [0.8, 0.2],  # Right Foot
    [0.5, 0.3]   # Torso Center
])

# Define the movement of the points over time
def update_points(frame):
    # Apply a downward movement to simulate sitting down
    if frame < 50:
        scale = frame / 50.0
        points[:, 1] -= scale * 0.01
    else:
        points[:, 1] = np.clip(points[:, 1] - 0.005, 0, 1)
    
    # Adjust the positions to make the movement more natural
    points[0, 1] += 0.005  # Head slightly up
    points[1, 1] += 0.003  # Neck slightly up
    points[2:4, 1] += 0.002  # Shoulders slightly up
    points[4:6, 1] += 0.001  # Elbows slightly up
    points[6:8, 1] -= 0.001  # Hands slightly down
    points[8:10, 1] -= 0.002  # Hips slightly down
    points[10:12, 1] -= 0.003  # Knees slightly down
    points[12:14, 1] -= 0.004  # Feet slightly down
    points[14, 1] -= 0.002  # Torso center slightly down

    return points

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
ax.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

# Update function for the animation
def animate(frame):
    new_points = update_points(frame)
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
