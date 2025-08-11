
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Number of frames
frames = 100
# Number of points
num_points = 15
# Angle for rotation
angle = np.linspace(0, 2 * np.pi, frames)

# Define initial positions for points to form a happy woman running
points = np.array([
    [0.1, 0.5], [0.15, 0.5], [0.2, 0.5],
    [0.25, 0.6], [0.3, 0.7], [0.35, 0.6],
    [0.4, 0.5], [0.45, 0.5], [0.5, 0.5],
    [0.55, 0.4], [0.6, 0.3], [0.65, 0.4],
    [0.7, 0.5], [0.75, 0.5], [0.8, 0.5]
])

# Function to update the position of points
def update(frame):
    fig.clear()
    x, y = points[:, 0], points[:, 1]
    
    # Simulating running motion by adjusting x and y coordinates
    for i in range(num_points):
        offset = 0.05 * np.sin(2 * np.pi * (frame + i) / 20)
        points[i, 1] = 0.5 + 0.2 * np.sin(angle[frame] + i * np.pi / 8) + offset
    
    # Plot points
    plt.scatter(x, y, color='white', s=100)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')

# Create a figure for plotting
fig = plt.figure(figsize=(5, 5), facecolor='black')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, repeat=True)
plt.show()
