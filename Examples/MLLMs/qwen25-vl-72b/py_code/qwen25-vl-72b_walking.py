
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points representing a walking figure
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], [1, -1],  # Shoulders
    [-2, -2], [2, -2],  # Elbows
    [-3, -3], [3, -3],  # Hands
    [0, -2],  # Waist
    [-1, -3], [1, -3],  # Hips
    [-2, -4], [2, -4],  # Knees
    [-3, -5], [3, -5]   # Feet
])

# Define the walking cycle as a series of transformations
def walk_cycle(t):
    angle = t * 2 * np.pi / 30  # 30 frames per cycle
    x_shift = 0.1 * np.sin(angle)
    y_shift = 0.1 * np.cos(angle)
    
    transformations = [
        [x_shift, y_shift],  # Head
        [x_shift - 0.1, y_shift - 0.1], [x_shift + 0.1, y_shift - 0.1],  # Shoulders
        [x_shift - 0.2, y_shift - 0.2], [x_shift + 0.2, y_shift - 0.2],  # Elbows
        [x_shift - 0.3, y_shift - 0.3], [x_shift + 0.3, y_shift - 0.3],  # Hands
        [x_shift, y_shift - 0.2],  # Waist
        [x_shift - 0.1, y_shift - 0.3], [x_shift + 0.1, y_shift - 0.3],  # Hips
        [x_shift - 0.2, y_shift - 0.4], [x_shift + 0.2, y_shift - 0.4],  # Knees
        [x_shift - 0.3, y_shift - 0.5], [x_shift + 0.3, y_shift - 0.5]   # Feet
    ]
    
    return np.array(transformations)

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-6, 1)
ax.set_aspect('equal')
ax.axis('off')

points, = ax.plot([], [], 'wo', markersize=10)

# Update function for the animation
def update(frame):
    new_positions = initial_positions + walk_cycle(frame)
    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(30), interval=50, blit=True)

plt.show()
