
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights for a lying-down posture
initial_positions = {
    'head': [0, 0],        # Head
    'neck': [0, -0.5],     # Neck
    'torso': [0, -1],      # Torso
    'pelvis': [0, -2],     # Pelvis
    'left_shoulder': [-0.5, 0],  # Left shoulder
    'right_shoulder': [0.5, 0],   # Right shoulder
    'left_elbow': [-1, -0.5],     # Left elbow
    'right_elbow': [1, -0.5],     # Right elbow
    'left_wrist': [-1.5, -1],     # Left wrist
    'right_wrist': [1.5, -1],     # Right wrist
    'left_hip': [-0.5, -2],       # Left hip
    'right_hip': [0.5, -2],       # Right hip
    'left_knee': [-0.5, -3],      # Left knee
    'right_knee': [0.5, -3],      # Right knee
    'left_ankle': [-0.5, -4],     # Left ankle
    'right_ankle': [0.5, -4]      # Right ankle
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Function to update the positions for the "lying down" posture with subtle sadness movements
def update_positions(frame):
    # Base positions
    positions = initial_coords.copy()
    
    # Add subtle movements to convey sadness
    if frame % 20 == 0:  # Every 20 frames, change the head tilt
        positions[0][1] += 0.1  # Tilt the head slightly downward
    
    # Slight arm and leg movements to show relaxation/sadness
    positions[6][0] -= 0.01 * np.sin(frame / 10)  # Left elbow moves slightly
    positions[7][0] += 0.01 * np.sin(frame / 10)  # Right elbow moves slightly
    positions[12][1] += 0.01 * np.cos(frame / 10)  # Left knee moves slightly
    positions[13][1] += 0.01 * np.cos(frame / 10)  # Right knee moves slightly
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Initial scatter plot
scatter = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    new_positions = update_positions(frame)
    scatter.set_offsets(new_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
