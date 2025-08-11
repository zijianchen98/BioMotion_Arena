
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are relative to the center of the figure
initial_positions = {
    'head': [0, 0],
    'torso_top': [0, -1],
    'torso_bottom': [0, -2],
    'left_shoulder': [-0.5, -1],
    'right_shoulder': [0.5, -1],
    'left_elbow': [-1, -1.5],
    'right_elbow': [1, -1.5],
    'left_wrist': [-1.5, -2],
    'right_wrist': [1.5, -2],
    'left_hip': [-0.5, -2.5],
    'right_hip': [0.5, -2.5],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_ankle': [-1.5, -4],
    'right_ankle': [1.5, -4]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the range of motion for turning around
angle_range = np.linspace(0, 2 * np.pi, 100)  # Full rotation

# Function to rotate a set of points around the origin
def rotate_points(points, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(points, rotation_matrix)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')  # Hide axes
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 1)

# Initialize the scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation update function
def update(frame):
    # Rotate the points around the torso's center
    rotated_coords = rotate_points(initial_coords, angle_range[frame])
    
    # Update the scatter plot data
    scatter.set_offsets(rotated_coords)
    
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(angle_range), interval=50, blit=True
)

# Display the animation
plt.show()
