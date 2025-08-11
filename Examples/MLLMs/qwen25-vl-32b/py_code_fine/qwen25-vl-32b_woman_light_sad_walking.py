
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These positions represent the body parts of the woman
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
    'right_ankle': [1.5, -3.5],
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the walking cycle parameters
cycle_length = 100  # Number of frames per cycle
amplitude = 0.5     # Amplitude of the walking motion
frequency = 0.1     # Frequency of the walking motion

# Function to update the positions based on the walking cycle
def update_positions(frame):
    # Calculate the phase of the walking cycle
    phase = frame / cycle_length * 2 * np.pi
    
    # Update the positions of the legs to simulate walking
    left_leg_y = amplitude * np.sin(phase)
    right_leg_y = amplitude * np.sin(phase + np.pi)
    
    # Update the torso to sway slightly
    torso_y = 0.1 * np.sin(phase)
    
    # Update the head to move slightly in sync with the torso
    head_y = torso_y + 0.1 * np.sin(phase)
    
    # Update the arm positions to swing naturally
    left_arm_x = 0.1 * np.cos(phase)
    right_arm_x = -0.1 * np.cos(phase)
    
    # Create the updated coordinates array
    updated_coords = initial_coords.copy()
    
    # Apply the walking motion to the legs
    updated_coords[9][1] += left_leg_y  # Left hip
    updated_coords[10][1] += left_leg_y  # Left knee
    updated_coords[11][1] += left_leg_y  # Left ankle
    
    updated_coords[12][1] += right_leg_y  # Right hip
    updated_coords[13][1] += right_leg_y  # Right knee
    updated_coords[14][1] += right_leg_y  # Right ankle
    
    # Apply the torso sway
    updated_coords[1][1] += torso_y  # Torso
    
    # Apply the head movement
    updated_coords[0][1] += head_y  # Head
    
    # Apply the arm swinging
    updated_coords[4][0] += left_arm_x  # Left elbow
    updated_coords[6][0] += left_arm_x  # Left wrist
    
    updated_coords[5][0] += right_arm_x  # Right elbow
    updated_coords[7][0] += right_arm_x  # Right wrist
    
    return updated_coords

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initial scatter plot
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    updated_coords = update_positions(frame)
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, animate, frames=cycle_length, interval=50, blit=True)

# Display the animation
plt.show()
