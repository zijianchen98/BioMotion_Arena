
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights and their initial positions
num_points = 15
points = np.zeros((num_points, 2))

# Head
points[0, :] = [0, 10]

# Torso
points[1, :] = [0, 5]
points[2, :] = [0, 0]

# Left arm
points[3, :] = [-2, 7]
points[4, :] = [-4, 4]

# Right arm
points[5, :] = [2, 7]
points[6, :] = [4, 4]

# Left leg
points[7, :] = [-1, -2]
points[8, :] = [-2, -5]

# Right leg
points[9, :] = [1, -2]
points[10, :] = [2, -5]

# Left foot
points[11, :] = [-2, -7]
points[12, :] = [-1, -8]

# Right foot
points[13, :] = [2, -7]
points[14, :] = [1, -8]

# Define the animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 15)
    ax.set_facecolor('black')
    ax.set_aspect('equal')

    # Update point positions based on the jumping motion
    points_updated = points.copy()
    
    # Head
    points_updated[0, 1] = 10 + 2 * np.sin(2 * np.pi * i / 100)
    
    # Torso
    points_updated[1, 1] = 5 + 2 * np.sin(2 * np.pi * i / 100)
    points_updated[2, 1] = 0 + 2 * np.sin(2 * np.pi * i / 100)
    
    # Left arm
    points_updated[3, 0] = -2 + 1 * np.cos(2 * np.pi * i / 100)
    points_updated[3, 1] = 7 + 2 * np.sin(2 * np.pi * i / 100)
    points_updated[4, 0] = -4 + 1 * np.cos(2 * np.pi * i / 100)
    points_updated[4, 1] = 4 + 2 * np.sin(2 * np.pi * i / 100)
    
    # Right arm
    points_updated[5, 0] = 2 + 1 * np.cos(2 * np.pi * i / 100)
    points_updated[5, 1] = 7 + 2 * np.sin(2 * np.pi * i / 100)
    points_updated[6, 0] = 4 + 1 * np.cos(2 * np.pi * i / 100)
    points_updated[6, 1] = 4 + 2 * np.sin(2 * np.pi * i / 100)
    
    # Left leg
    points_updated[7, 0] = -1 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[7, 1] = -2 + 2 * np.sin(2 * np.pi * i / 50)
    points_updated[8, 0] = -2 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[8, 1] = -5 + 2 * np.sin(2 * np.pi * i / 50)
    
    # Right leg
    points_updated[9, 0] = 1 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[9, 1] = -2 + 2 * np.sin(2 * np.pi * i / 50)
    points_updated[10, 0] = 2 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[10, 1] = -5 + 2 * np.sin(2 * np.pi * i / 50)
    
    # Left foot
    points_updated[11, 0] = -2 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[11, 1] = -7 + 2 * np.sin(2 * np.pi * i / 50)
    points_updated[12, 0] = -1 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[12, 1] = -8 + 2 * np.sin(2 * np.pi * i / 50)
    
    # Right foot
    points_updated[13, 0] = 2 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[13, 1] = -7 + 2 * np.sin(2 * np.pi * i / 50)
    points_updated[14, 0] = 1 + 1 * np.cos(2 * np.pi * i / 50)
    points_updated[14, 1] = -8 + 2 * np.sin(2 * np.pi * i / 50)
    
    # Plot the updated points
    ax.scatter(points_updated[:, 0], points_updated[:, 1], c='white', s=10)

# Create the figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=20)

plt.show()
