
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points representing the key joints of a sitting woman
points = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Neck
    [0.3, 0.7],  # Left Shoulder
    [0.6, 0.7],  # Right Shoulder
    [0.2, 0.6],  # Left Elbow
    [0.7, 0.6],  # Right Elbow
    [0.1, 0.5],  # Left Wrist
    [0.8, 0.5],  # Right Wrist
    [0.4, 0.5],  # Left Hip
    [0.6, 0.5],  # Right Hip
    [0.3, 0.4],  # Left Knee
    [0.7, 0.4],  # Right Knee
    [0.2, 0.3],  # Left Ankle
    [0.8, 0.3],  # Right Ankle
    [0.5, 0.2]   # Pelvis
])

# Normalize points to fit within the plot area
points[:, 0] *= 10
points[:, 1] *= 10

# Function to update the frame
def update(frame):
    # Simulate the sitting down motion by adjusting the y-coordinates
    y_offset = np.sin(frame * np.pi / 30) * 0.5
    points[:, 1] += y_offset
    
    # Ensure the points stay within the plot area
    points[:, 1] = np.clip(points[:, 1], 0, 10)
    
    # Update the scatter plot
    scat.set_offsets(points)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
plt.axis('off')

# Create the scatter plot for the points
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60), interval=50, blit=True)

# Display the animation
plt.show()
