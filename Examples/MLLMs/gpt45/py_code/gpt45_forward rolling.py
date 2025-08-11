
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(5, 7))
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_facecolor('black')
ax.axis('off')

# Define the initial coordinates of 15 points representing key joints
points = np.array([
    [0.0, 2.0],   # Head
    [-0.5, 1.5],  # Left shoulder
    [0.5, 1.5],   # Right shoulder
    [-0.8, 1.0],  # Left elbow
    [0.8, 1.0],   # Right elbow
    [-1.0, 0.5],  # Left wrist
    [1.0, 0.5],   # Right wrist
    [0.0, 1.0],   # Middle Torso
    [-0.5, 0.5],  # Left hip
    [0.5, 0.5],   # Right hip
    [-0.5, -0.5], # Left knee
    [0.5, -0.5],  # Right knee
    [-0.5, -1.5], # Left ankle
    [0.5, -1.5],  # Right ankle
    [0, -2.0]     # Bottom point (floor-center reference)
])

# Plot the initial points
dots, = ax.plot(points[:,0], points[:,1], 'wo', markersize=8)

# Animation function for rotation (turning around)
def animate(i):
    angle = 2 * np.pi * (i / 100)
    rotated_points = points.copy()
    # Rotating around the vertical middle axis (y-axis)
    rotated_points[:,0] = points[:,0] * np.cos(angle)
    # Oscillating points slightly in the horizontal axis for increased realism
    rotated_points[:,1] += 0.05 * np.sin(angle * 2)
    dots.set_data(rotated_points[:,0], rotated_points[:,1])
    return dots,

# Create and run the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=30, blit=True, repeat=True)

plt.show()
