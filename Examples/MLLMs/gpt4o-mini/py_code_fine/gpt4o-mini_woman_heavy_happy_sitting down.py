
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set parameters
num_points = 15
frames = 100
point_size = 100
width, height = 640, 480

# Set up point-light positions for a happy woman sitting down
# Representing point-lights in a rough skeletal form
points_initial = np.array([
    [0, 5],    # Head
    [-1, 4],   # Left shoulder
    [1, 4],    # Right shoulder
    [-1.5, 3], # Left elbow
    [1.5, 3],  # Right elbow
    [-1, 2],   # Left hand
    [1, 2],    # Right hand
    [0, 3],    # Chest
    [-1, 1],   # Left hip
    [1, 1],    # Right hip
    [0, 0],    # Pelvis
    [-0.5, -2],# Left knee
    [0.5, -2], # Right knee
    [-0.5, -3],# Left foot
    [0.5, -3], # Right foot
    [0, -2]    # Center bottom (weight)
])

# Simulation function for the animation
def animate(i):
    # Clear the plot
    plt.clf()
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.axis('off')

    # Update the position of each point
    # Simple modeling of the sitting motion
    points = points_initial.copy()
    # Mimic sitting down action
    vertical_movement = -0.02 * i
    for j in range(len(points)):
        points[j, 1] += vertical_movement

    # Introduce a slight horizontal swing to simulate upper body movement
    horizontal_swing = np.sin(i / 10) * 0.1
    points[2, 0] += horizontal_swing  # Right shoulder
    points[1, 0] -= horizontal_swing  # Left shoulder
    points[4, 0] += horizontal_swing  # Right elbow
    points[3, 0] -= horizontal_swing  # Left elbow

    # Draw points
    plt.scatter(points[:, 0], points[:, 1], s=point_size, color='white')

# Set up the figure and animation
fig = plt.figure(figsize=(8, 6), facecolor='black')
anim = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/30)

# Show the animation
plt.show()
