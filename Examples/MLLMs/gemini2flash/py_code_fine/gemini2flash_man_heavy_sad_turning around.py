
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (adjust for "sadman with heavy weight turning around")
# These are just starting points; the animation will modify them
initial_positions = np.array([
    [0, 3],  # Head
    [-0.5, 2.5], # Shoulder left
    [0.5, 2.5], # Shoulder Right
    [-1, 2],  # Elbow Left
    [1, 2],  # Elbow Right
    [-1.5, 1.5],  # Hand Left
    [1.5, 1.5], # Hand Right
    [-0.25, 1],  # Hip Left
    [0.25, 1],  # Hip Right
    [-0.75, 0.5], # Knee left
    [0.75, 0.5], # Knee right
    [-0.5, 0],  # Ankle Left
    [0.5, 0],  # Ankle Right
    [-0.5, -0.5], # Foot Left
    [0.5, -0.5]   # Foot Right
])


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Black background
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 4)
ax.set_aspect('equal')
plt.axis('off')  # Hide the axes


# Create the scatter plot for the points
scat = ax.scatter([], [], s=20, c='white') # White points, smaller size


# Animation function (adjust to create turning motion with sad/heavy characteristics)
def animate(i):
    # Simulate turning motion with some added "sad" characteristics (e.g., slightly hunched, slow movement)
    angle = np.radians(i * 2)  # Slower rotation
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    # Apply rotation and some slight "sad" movement
    new_positions = np.dot(initial_positions, rotation_matrix)

    # Add slight vertical bobbing (sad, heavy movement)
    bob_amount = np.sin(i * 0.1) * 0.05  # Smaller bob
    new_positions[:, 1] += bob_amount  # Apply to y-coordinate

    # Update the scatter plot data
    scat.set_offsets(new_positions)
    return scat,


# Initialization function (required for blitting)
def init():
    scat.set_offsets(np.empty((0, 2)))
    return scat,


# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, blit=True, save_count=200) # Increased save_count

# Show the animation
plt.show()

