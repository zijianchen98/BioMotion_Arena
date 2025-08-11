
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the initial positions of the points (standing position)
initial_positions = np.array([
    [0, 10],   # Head
    [-1, 9],  # Left Shoulder
    [1, 9],   # Right Shoulder
    [-2, 7],  # Left Elbow
    [2, 7],   # Right Elbow
    [-3, 5],  # Left Wrist
    [3, 5],   # Right Wrist
    [0, 7],   # Torso
    [-1, 3],  # Left Hip
    [1, 3],   # Right Hip
    [-2, 1],  # Left Knee
    [2, 1],   # Right Knee
    [-1, -1], # Left Ankle
    [1, -1],  # Right Ankle
    [0, 1]    # Center point
])


# Define the animation function for a forward roll
def forward_roll(frame):
    angle = np.radians(frame * 5)  # Adjust speed by changing the multiplier
    center_x = 0
    center_y = 5 # Center of rotation (adjust as needed)

    # Rotation and translation for rolling
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])

    new_positions = []
    for point in initial_positions:
        rotated_x = (point[0] - center_x) * rotation_matrix[0, 0] + (point[1] - center_y) * rotation_matrix[0, 1] + center_x
        rotated_y = (point[0] - center_x) * rotation_matrix[1, 0] + (point[1] - center_y) * rotation_matrix[1, 1] + center_y
        new_positions.append([rotated_x, rotated_y + frame * 0.01]) # Add a slight downward drift

    return np.array(new_positions)


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor("black")  # Set background to black
ax.set_xlim(-5, 5)  # Adjust limits for better view
ax.set_ylim(-5, 12)
ax.set_aspect('equal')  # Make sure the aspect ratio is equal
ax.axis('off')  # Hide the axes

# Create the scatter plot for the points
scatter = ax.scatter([], [], s=50, color='white')  # White points

# Initialize the animation
def init():
    scatter.set_offsets(np.empty((0, 2)))
    return scatter,

# Animation function
def animate(frame):
    positions = forward_roll(frame)
    scatter.set_offsets(positions)
    return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
