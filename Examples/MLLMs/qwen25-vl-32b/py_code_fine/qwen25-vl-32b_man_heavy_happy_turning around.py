
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights for the "happyman"
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, -0.5],
    'right_shoulder': [0.5, -0.5],
    'left_elbow': [-1, -1],
    'right_elbow': [1, -1],
    'left_wrist': [-1.5, -1.5],
    'right_wrist': [1.5, -1.5],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the range of angles for the turning motion
angles = np.linspace(0, 2 * np.pi, 100)  # 100 frames for a full rotation

# Function to rotate a point around the origin
def rotate_point(point, angle):
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    return np.dot(rotation_matrix, point)

# Function to update the positions of the points for each frame
def update(frame):
    global scatter
    angle = angles[frame]
    
    # Rotate the torso and head around the center
    torso_head = initial_coords[[1, 0]]  # Torso and head indices
    rotated_torso_head = np.array([rotate_point(p, angle) for p in torso_head])
    initial_coords[[1, 0]] = rotated_torso_head
    
    # Update the limbs' positions based on the new torso position
    torso_position = initial_coords[1]  # Torso position after rotation
    
    # Left arm
    left_shoulder = initial_coords[2] + torso_position
    left_elbow = initial_coords[6] + torso_position
    left_wrist = initial_coords[7] + torso_position
    
    # Right arm
    right_shoulder = initial_coords[3] + torso_position
    right_elbow = initial_coords[8] + torso_position
    right_wrist = initial_coords[9] + torso_position
    
    # Left leg
    left_hip = initial_coords[4] + torso_position
    left_knee = initial_coords[10] + torso_position
    left_ankle = initial_coords[11] + torso_position
    
    # Right leg
    right_hip = initial_coords[5] + torso_position
    right_knee = initial_coords[12] + torso_position
    right_ankle = initial_coords[13] + torso_position
    
    # Update the scatter plot data
    scatter.set_offsets(initial_coords)
    return scatter,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initialize the scatter plot
scatter = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], c='white', s=50)

# Create the animation
animation = FuncAnimation(fig, update, frames=len(angles), interval=50, blit=True)

# Display the animation
plt.show()
