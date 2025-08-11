
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

# Define the trajectory for the jump
def jump_trajectory(t):
    # t ranges from 0 to 1 (normalized time)
    amplitude = 1.0  # Jump height
    frequency = 2 * np.pi  # Frequency of the jump
    phase = np.pi / 2  # Phase shift to start at the peak
    return amplitude * np.sin(frequency * t + phase)

# Define the animation function
def update(frame):
    ax.clear()
    
    # Calculate the current time in the jump cycle
    t = frame / num_frames
    
    # Update the positions based on the jump trajectory
    positions = {}
    for key, pos in initial_positions.items():
        if key in ['left_foot', 'right_foot']:
            # Feet move forward during the jump
            x_offset = 0.5 * t
            y_offset = jump_trajectory(t)
            positions[key] = [pos[0] + x_offset, pos[1] + y_offset]
        elif key in ['left_knee', 'right_knee']:
            # Knees follow the feet
            x_offset = 0.3 * t
            y_offset = jump_trajectory(t)
            positions[key] = [pos[0] + x_offset, pos[1] + y_offset]
        elif key in ['left_hip', 'right_hip']:
            # Hips follow the knees
            x_offset = 0.2 * t
            y_offset = jump_trajectory(t)
            positions[key] = [pos[0] + x_offset, pos[1] + y_offset]
        else:
            # Other parts remain relatively stationary
            positions[key] = pos
    
    # Plot the updated positions
    x_coords = [pos[0] for pos in positions.values()]
    y_coords = [pos[1] for pos in positions.values()]
    ax.scatter(x_coords, y_coords, color='white', s=50)
    
    # Connect the points with lines to form the body
    connections = [
        ('head', 'torso'),
        ('torso', 'left_shoulder'),
        ('left_shoulder', 'left_elbow'),
        ('left_elbow', 'left_hand'),
        ('torso', 'right_shoulder'),
        ('right_shoulder', 'right_elbow'),
        ('right_elbow', 'right_hand'),
        ('torso', 'left_hip'),
        ('left_hip', 'left_knee'),
        ('left_knee', 'left_foot'),
        ('torso', 'right_hip'),
        ('right_hip', 'right_knee'),
        ('right_knee', 'right_foot')
    ]
    for connection in connections:
        start = positions[connection[0]]
        end = positions[connection[1]]
        ax.plot([start[0], end[0]], [start[1], end[1]], color='white')

    # Set the plot limits and remove axis labels
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=True)

# Display the animation
plt.show()
