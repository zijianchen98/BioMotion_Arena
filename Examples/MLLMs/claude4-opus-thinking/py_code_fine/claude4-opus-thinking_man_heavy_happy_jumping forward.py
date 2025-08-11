
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_facecolor('black')
ax.set_xticks([]) 
ax.set_yticks([])

# Define the initial positions of the point lights
# (head, shoulders, elbows, wrists, hips, knees, ankles)
points = np.array([
    [0, 5],  # head
    [-1, 4], [1, 4],  # shoulders
    [-1, 3], [1, 3],  # elbows
    [-1, 2], [1, 2],  # wrists
    [-1, 1], [1, 1],  # hips
    [-1, 0], [1, 0],  # knees
    [-1, -1], [1, -1],  # ankles
    [0, 4],  # weight
])

# Animation function
def animate(i):
    ax.clear()
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_facecolor('black')

    # Calculate the jumping motion
    jump_height = np.sin(i / 10.0) * 2  # Simulate the vertical jump
    horizontal_movement = i / 10.0  # Simulate forward movement

    # Update points positions for the animation
    new_points = points.copy()
    
    # Update vertical positions
    new_points[:, 1] += jump_height
    
    # Update horizontal positions for the jumping forward effect
    new_points[:, 0] += horizontal_movement

    # Plot the point lights
    for point in new_points:
        ax.plot(point[0], point[1], 'wo', markersize=10)  # white points

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)

# Show the animation
plt.show()
