
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (joints)
initial_positions = {
    'head': [0, 1.5],
    'left_shoulder': [-0.5, 1],
    'right_shoulder': [0.5, 1],
    'left_elbow': [-1, 0.5],
    'right_elbow': [1, 0.5],
    'left_wrist': [-1.5, 0],
    'right_wrist': [1.5, 0],
    'left_hip': [-0.5, 0],
    'right_hip': [0.5, 0],
    'left_knee': [-1, -0.5],
    'right_knee': [1, -0.5],
    'left_ankle': [-1.5, -1],
    'right_ankle': [1.5, -1],
    'left_toe': [-1.5, -1.5],
    'right_toe': [1.5, -1.5]
}

# Convert to a list of coordinates
positions = np.array(list(initial_positions.values()))

# Function to update the positions for walking animation
def update_positions(frame):
    global positions
    
    # Walking parameters
    amplitude = 0.5  # Amplitude of leg movement
    frequency = 0.05  # Frequency of leg movement
    phase_diff = np.pi  # Phase difference between left and right legs
    
    # Update leg positions (sine wave for walking)
    left_leg_y = amplitude * np.sin(frame * frequency)
    right_leg_y = amplitude * np.sin(frame * frequency + phase_diff)
    
    # Update foot positions
    positions[10][1] = -1 + left_leg_y  # Left knee
    positions[11][1] = -1 + right_leg_y  # Right knee
    positions[12][1] = -1.5 + left_leg_y  # Left ankle
    positions[13][1] = -1.5 + right_leg_y  # Right ankle
    positions[14][1] = -1.5 + left_leg_y  # Left toe
    positions[15][1] = -1.5 + right_leg_y  # Right toe
    
    # Slight swaying of the upper body
    body_sway = 0.1 * np.sin(frame * frequency / 2)
    positions[0][0] += body_sway  # Head
    positions[1][0] += body_sway  # Left shoulder
    positions[2][0] += body_sway  # Right shoulder
    
    return positions

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    global positions
    updated_positions = update_positions(frame)
    scat.set_offsets(updated_positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
