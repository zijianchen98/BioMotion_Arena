
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define the initial positions of the point-lights
points = np.array([
    [0.5, 0.1], [0.4, 0.2], [0.6, 0.2], [0.35, 0.3], [0.65, 0.3],
    [0.3, 0.4], [0.7, 0.4], [0.5, 0.45], [0.45, 0.55], [0.55, 0.55],
    [0.4, 0.6], [0.6, 0.6], [0.45, 0.7], [0.55, 0.7], [0.5, 0.9]
])

# Create the scatter plot
scatter = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

def update(frame):
    # Update the positions of the point-lights to simulate running motion
    offset = 0.01 * frame
    points[1:4, 0] += np.sin(offset)
    points[4:7, 0] -= np.sin(offset)
    points[7:10, 0] += np.sin(offset) * 0.8
    points[10:13, 0] -= np.sin(offset) * 0.8
    
    points[0, 1] += np.cos(offset) * 0.015
    points[3, 1] += np.cos(offset) * 0.01
    points[6, 1] += np.cos(offset) * 0.01
    
    points[8, 1] += np.cos(offset) * 0.015
    points[11, 1] += np.cos(offset) * 0.01
    
    scatter.set_offsets(points)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=300, interval=30, blit=False)

plt.show()
