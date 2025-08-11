
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 1],
    'torso_top': [0, 0],
    'torso_bottom': [0, -0.5],
    'left_shoulder': [-0.3, 0],
    'right_shoulder': [0.3, 0],
    'left_elbow': [-0.6, -0.3],
    'right_elbow': [0.6, -0.3],
    'left_wrist': [-0.9, -0.6],
    'right_wrist': [0.9, -0.6],
    'left_hip': [-0.4, -1],
    'right_hip': [0.4, -1],
    'left_knee': [-0.7, -1.5],
    'right_knee': [0.7, -1.5],
    'left_ankle': [-0.9, -2],
    'right_ankle': [0.9, -2]
}

# Convert the dictionary to a list of positions
initial_positions_list = [
    initial_positions['head'],
    initial_positions['torso_top'],
    initial_positions['torso_bottom'],
    initial_positions['left_shoulder'],
    initial_positions['right_shoulder'],
    initial_positions['left_elbow'],
    initial_positions['right_elbow'],
    initial_positions['left_wrist'],
    initial_positions['right_wrist'],
    initial_positions['left_hip'],
    initial_positions['right_hip'],
    initial_positions['left_knee'],
    initial_positions['right_knee'],
    initial_positions['left_ankle'],
    initial_positions['right_ankle']
]

# Function to update the positions based on the animation frame
def update_positions(frame, positions):
    # Simulate sitting down motion
    if frame <= 50:
        # Move torso and head downward
        positions[0][1] -= 0.01  # Head
        positions[1][1] -= 0.01  # Torso top
        positions[2][1] -= 0.01  # Torso bottom
        
        # Move hips downward
        positions[9][1] -= 0.01  # Left hip
        positions[10][1] -= 0.01  # Right hip
        
        # Move knees slightly forward and downward
        positions[11][1] -= 0.01  # Left knee
        positions[12][1] -= 0.01  # Right knee
        positions[11][0] += 0.01  # Left knee
        positions[12][0] -= 0.01  # Right knee
        
        # Move ankles slightly forward and downward
        positions[13][1] -= 0.01  # Left ankle
        positions[14][1] -= 0.01  # Right ankle
        positions[13][0] += 0.01  # Left ankle
        positions[14][0] -= 0.01  # Right ankle
    
    elif frame > 50:
        # Stop further movement after reaching the sitting position
        pass
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2.5, 1.5)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    global initial_positions_list
    updated_positions = update_positions(frame, initial_positions_list.copy())
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Display the animation
plt.show()
