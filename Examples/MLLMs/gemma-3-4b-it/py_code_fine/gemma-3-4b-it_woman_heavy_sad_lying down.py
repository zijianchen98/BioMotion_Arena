
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the action and subject
action = "lying down"
subject = "sadwoman"

# Define the number of points
num_points = 15

# Define the starting positions of the points
# These coordinates are just a starting point and will be updated during the animation
start_positions = np.array([
    [0.2, 0.5],
    [0.3, 0.7],
    [0.4, 0.9],
    [0.5, 0.7],
    [0.6, 0.5],
    [0.7, 0.3],
    [0.8, 0.5],
    [0.9, 0.7],
    [1.0, 0.9],
    [0.9, 0.7],
    [0.8, 0.5],
    [0.7, 0.3],
    [0.6, 0.5],
    [0.5, 0.7],
    [0.4, 0.9]
])

# Define the movement patterns
# These patterns will be applied to each point to simulate movement
# Adjust these values to change the animation style
movement_patterns = [
    [0.01, 0.02],  # Small forward movement
    [0.01, -0.02], # Slight backward movement
    [0.02, 0.01],  # Slight rightward movement
    [-0.02, 0.01], # Slight leftward movement
    [0.005, 0.005],  # Very small circular movement
    [-0.005, -0.005], # Very small circular movement
    [0.01, 0.01],
    [-0.01, 0.01],
    [0.01, -0.01],
    [-0.01, -0.01],
    [0.005, 0.005],
    [-0.005, -0.005],
    [0.01, 0.01],
    [-0.01, 0.01],
    [0.005, 0.005]
]

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 1.1)
ax.set_aspect('equal')
ax.axis('off')

# Create the points
points, = ax.plot([], [], 'w.', markersize=10)

# Animation function
def animate(frame):
    # Update the positions of the points
    positions = start_positions
    for i in range(num_points):
        positions[i] = [positions[i][0] + movement_patterns[i][0],
                         positions[i][1] + movement_patterns[i][1]]
    
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, blit=True, interval=50)

# Save the animation
ani.save("sadwoman_lying_down.gif", writer='pillow', fps=15)

plt.show()
