
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configure the number of points and frames
num_points = 15  # Number of point lights
num_frames = 60  # Total number of frames in the animation

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_facecolor('black')
ax.axis('off')  # Turn off the axis

# Prepare point light positions
points = np.array([[0, -2], 
                   [-1, -3], [1, -3],
                   [-2, -1], [2, -1],
                   [-1, 0], [1, 0], 
                   [-1, 1], [1, 1],
                   [-2, 2], [2, 2],
                   [0, 3], [0, 4], 
                   [-1.5, 2.5], [1.5, 2.5],
                   [0, -4]])

# Initialize scatter object
scatter = ax.scatter(points[:, 0], points[:, 1], color='white')

# Function to update point positions for each frame
def update(frame):
    # Simple running motion simulation
    offset = 0.1 * np.sin(frame / 10.0)  # Oscillation effect
    new_positions = points.copy()
    
    # Adjust y-coordinates to simulate running
    new_positions[:, 1] += offset + (frame / 20.0) if frame/20.0 < 5 else 0
    
    # Circular motion for realistic motion
    if frame < num_frames // 2:
        new_positions[:, 0] += np.sin(frame / 10.0) * 0.5  # Float side to side
    
    scatter.set_offsets(new_positions)  # Update positions
    return scatter,

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=50)

# Show the animation
plt.show()
