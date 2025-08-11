
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These positions represent the body parts of the woman
initial_positions = {
    'head': [0, 0],
    'torso': [0, -1],
    'left_shoulder': [-0.5, -1],
    'right_shoulder': [0.5, -1],
    'left_elbow': [-1, -2],
    'right_elbow': [1, -2],
    'left_hand': [-1.5, -3],
    'right_hand': [1.5, -3],
    'left_hip': [-0.5, -2],
    'right_hip': [0.5, -2],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_foot': [-1.5, -4],
    'right_foot': [1.5, -4]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the number of frames in the animation
num_frames = 100

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

# Function to update the animation frame by frame
def update(frame):
    # Define the running motion pattern
    # This is a simplified biomechanical model for running
    t = frame / num_frames * 2 * np.pi  # Normalize time
    
    # Update positions based on the running motion
    updated_coords = initial_coords.copy()
    
    # Head bobs up and down slightly
    updated_coords[0][1] += 0.1 * np.sin(t)
    
    # Torso sways side to side
    updated_coords[1][0] += 0.1 * np.cos(t)
    
    # Arms swing back and forth
    updated_coords[2][0] -= 0.5 * np.sin(t)  # Left shoulder
    updated_coords[3][0] += 0.5 * np.sin(t)  # Right shoulder
    updated_coords[4][0] -= 0.8 * np.sin(t)  # Left elbow
    updated_coords[5][0] += 0.8 * np.sin(t)  # Right elbow
    updated_coords[6][0] -= 1.0 * np.sin(t)  # Left hand
    updated_coords[7][0] += 1.0 * np.sin(t)  # Right hand
    
    # Legs move in a running gait
    updated_coords[8][0] += 0.5 * np.sin(t)  # Left hip
    updated_coords[9][0] -= 0.5 * np.sin(t)  # Right hip
    updated_coords[10][0] += 0.8 * np.sin(t)  # Left knee
    updated_coords[11][0] -= 0.8 * np.sin(t)  # Right knee
    updated_coords[12][0] += 1.0 * np.sin(t)  # Left foot
    updated_coords[13][0] -= 1.0 * np.sin(t)  # Right foot
    
    # Add vertical bouncing for the legs
    updated_coords[10][1] += 0.5 * np.sin(2 * t)  # Left knee
    updated_coords[11][1] += 0.5 * np.sin(2 * t)  # Right knee
    updated_coords[12][1] += 0.8 * np.sin(2 * t)  # Left foot
    updated_coords[13][1] += 0.8 * np.sin(2 * t)  # Right foot
    
    # Update the scatter plot data
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
