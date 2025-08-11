
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights for the sadman
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

# Define the range of motion for the bowing action
def get_bowing_positions(t, amplitude=0.5, frequency=0.1):
    """
    Generate positions for the bowing motion.
    t: Time step (float)
    amplitude: Amplitude of the bowing motion
    frequency: Frequency of the bowing motion
    """
    # Apply a sinusoidal motion to the torso and head
    vertical_offset = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the positions
    updated_positions = initial_coords.copy()
    updated_positions[0] += np.array([0, vertical_offset])  # Head
    updated_positions[1] += np.array([0, vertical_offset])  # Torso
    
    # Bowing motion affects the upper body more than the lower body
    updated_positions[2:8] += np.array([0, vertical_offset * 0.8])  # Upper limbs
    updated_positions[8:] += np.array([0, vertical_offset * 0.5])   # Lower limbs
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def update(frame):
    # Get the updated positions based on the current frame
    positions = get_bowing_positions(frame / 30)  # Assuming 30 frames per second
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=range(100), interval=33, blit=True)

# Display the animation
plt.show()
