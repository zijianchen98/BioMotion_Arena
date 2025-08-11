
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames in the animation
num_frames = 60

# Define the initial positions of the point-lights
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.75],
    'right_elbow': [1, 0.75],
    'left_hand': [-1.5, 0.5],
    'right_hand': [1.5, 0.5],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_foot': [-1.5, -1.5],
    'right_foot': [1.5, -1.5]
}

# Define the amplitude and frequency of the jump
amplitude = 1.0
frequency = 0.5  # Hz

# Define the time array
t = np.linspace(0, 1/frequency, num_frames)

# Define the vertical displacement function for the jump
def jump_displacement(t):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initialize the scatter plot for the point-lights
scatter = ax.scatter([], [], color='white', s=50)

# Function to update the positions of the point-lights
def update(frame):
    # Calculate the vertical displacement for the current frame
    displacement = jump_displacement(t[frame])
    
    # Update the positions of the point-lights
    positions = {
        'head': [0, 1 + displacement],
        'torso': [0, 0 + displacement],
        'left_shoulder': [-0.5, 0.5 + displacement],
        'right_shoulder': [0.5, 0.5 + displacement],
        'left_elbow': [-1, 0.75 + displacement],
        'right_elbow': [1, 0.75 + displacement],
        'left_hand': [-1.5, 0.5 + displacement],
        'right_hand': [1.5, 0.5 + displacement],
        'left_hip': [-0.5, -0.5 + displacement],
        'right_hip': [0.5, -0.5 + displacement],
        'left_knee': [-1, -1 + displacement],
        'right_knee': [1, -1 + displacement],
        'left_foot': [-1.5, -1.5 + displacement],
        'right_foot': [1.5, -1.5 + displacement]
    }
    
    # Update the scatter plot with the new positions
    x = [pos[0] for pos in positions.values()]
    y = [pos[1] for pos in positions.values()]
    scatter.set_offsets(np.c_[x, y])

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)

# Display the animation
plt.show()
