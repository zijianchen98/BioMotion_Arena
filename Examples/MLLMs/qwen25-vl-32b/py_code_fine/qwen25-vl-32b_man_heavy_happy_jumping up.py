
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These positions represent the limbs and body parts of the "happyman"
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

# Define the animation parameters
num_frames = 60  # Number of frames in the animation
gravity = 0.05   # Gravity acceleration
jump_height = 1.0  # Maximum jump height
frame_rate = 30  # Frames per second

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

# Function to update the animation frame
def update(frame):
    # Calculate the vertical displacement due to gravity
    t = frame / frame_rate  # Time in seconds
    y_displacement = jump_height * np.sin(t * np.pi)  # Sinusoidal jump motion
    
    # Update the y-coordinates of the points
    updated_coords = initial_coords.copy()
    updated_coords[:, 1] += y_displacement
    
    # Update the scatter plot data
    scatter.set_offsets(updated_coords)
    
    return scatter,

# Create the animation
animation = FuncAnimation(
    fig,
    update,
    frames=num_frames,
    interval=1000 / frame_rate,  # Frame interval in milliseconds
    blit=True
)

# Display the animation
plt.show()
