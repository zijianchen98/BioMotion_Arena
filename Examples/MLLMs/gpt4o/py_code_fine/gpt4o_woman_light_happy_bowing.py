
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 2)
ax.set_facecolor('black')
ax.axis('off')

# Define the initial positions of the 15 point-lights in the Biomechanical Human Body
# Format: [x, y]
points = np.array([
    [0, 1.8],  # Head
    [-0.3, 1.5], [0.3, 1.5],  # Shoulders
    [-0.5, 1.2], [0.5, 1.2],  # Elbows
    [-0.4, 0.9], [0.4, 0.9],  # Hands
    [0, 1.2],  # Chest
    [0, 0.8],  # Waist
    [-0.3, 0.5], [0.3, 0.5],  # Hips
    [-0.5, 0.3], [0.5, 0.3],  # Knees
    [-0.4, 0.1], [0.4, 0.1],  # Feet
])

# Create a scatter plot for the point-lights
scatter = ax.scatter(points[:, 0], points[:, 1], s=100, color='white')

# Animation function to simulate the bowing motion
def animate(frame):
    global points
    # Simulate bowing motion by moving the upper body parts forward and downward
    bow_amount = 0.2 * np.sin(frame / 10)
    points[[0, 1, 2, 3, 4, 6], 1] -= bow_amount  # Move upper body down
    points[[0, 1, 2, 3, 4, 6], 0] += bow_amount / 2  # Move upper body forward
    
    points[[8, 9], 1] += bow_amount / 3  # Adjust waist and hips slightly
    scatter.set_offsets(points)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

plt.show()
