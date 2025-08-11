
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Frames per second for the animation
fps = 30

# Total frames for the animation
total_frames = 150

# Frame time interval
frame_interval = 1000 / fps  # milliseconds

# Define the points for the stimulus
points = np.array([
    [0, 0],  # Head
    [1, 1],  # Upper body
    [2, 3],  # Lower body
    [3, 5],  # Upper left leg
    [4, 8],  # Lower left leg
    [3, 5],  # Upper right leg
    [4, 6],  # Lower right leg
    [-1, -1],  # Left arm
    [-2, -2],  # Hand left
    [1, -1],  # Right arm
    [2, -2],  # Hand right
    [0, -3],  # Right Foot
    [1, -6],  # Right Shoe
    [-1, -6],  # Left Shoe
    [-2, -3],  # Left Foot
])

# Point colors (white)
colors = ['white'] * len(points)

# Function to update the positions based on frame number
def update(frame):
    # Sine curve for the upward motion of the jumping
    amplitude = 3
    speed = 0.5
    bounce = amplitude * np.sin(speed * frame)
    
    # Offset points
    x_offset = 0.2 * frame - max(frame, total_frames - frame)
    y_offset = bounce
    
    # Move each point to new coordinates
    for point in points:
        point[0] += x_offset
        point[1] += y_offset
    
    scatter.set_offsets(points)
    return scatter,

# Initialize the plot
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
scatter = ax.scatter(points[:, 0], points[:, 1], c=colors)

# Create the animation
animation = FuncAnimation(fig, update, frames=total_frames, interval=frame_interval, blit=True, repeat=False)

# Show the plot
plt.axis('off')
plt.show()
