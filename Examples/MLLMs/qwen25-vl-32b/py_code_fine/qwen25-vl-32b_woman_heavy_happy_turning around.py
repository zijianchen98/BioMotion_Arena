
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are relative to the center of the figure
initial_positions = {
    'head': [0, 1.5],
    'torso_top': [0, 1],
    'torso_bottom': [0, 0],
    'left_shoulder': [-0.5, 1],
    'right_shoulder': [0.5, 1],
    'left_elbow': [-1, 0.5],
    'right_elbow': [1, 0.5],
    'left_wrist': [-1.5, 0],
    'right_wrist': [1.5, 0],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_ankle': [-1.5, -1.5],
    'right_ankle': [1.5, -1.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Function to update the positions based on the angle of rotation
def update_positions(coords, angle):
    # Apply rotation matrix to each point
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(coords, rotation_matrix)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_facecolor('black')  # Set background to black

# Scatter plot for the point lights
scatter = ax.scatter([], [], c='white', s=50)

# Animation function
def animate(frame):
    angle = np.radians(45 * np.sin(frame / 50))  # Smooth oscillating turn
    new_coords = update_positions(initial_coords, angle)
    scatter.set_offsets(new_coords)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=200, interval=50, blit=True
)

# Display the animation
plt.show()
