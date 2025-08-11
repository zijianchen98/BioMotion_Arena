
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human-like structure:
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 1],   # Head
    [-0.5, 0], # Left shoulder
    [0.5, 0],  # Right shoulder
    [-1, -1],  # Left elbow
    [1, -1],   # Right elbow
    [-0.5, -2], # Left wrist
    [0.5, -2],  # Right wrist
    [0, -3],   # Pelvis
    [-0.7, -4], # Left hip
    [-1.2, -6], # Left knee
    [-1.5, -7], # Left ankle
    [0.7, -4],  # Right hip
    [1.2, -6],  # Right knee
    [1.5, -7]   # Right ankle
])

# Define the walking cycle parameters
num_frames = 100  # Number of frames in the animation
step_size = 0.1   # Step size for walking
amplitude = 0.5   # Amplitude of vertical oscillation
frequency = 0.1   # Frequency of vertical oscillation

# Function to update the positions for each frame
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Simulate walking by shifting the legs forward
    left_leg_shift = step_size * np.sin(2 * np.pi * frequency * frame)
    right_leg_shift = step_size * np.sin(2 * np.pi * frequency * (frame + 0.5))
    
    # Update left leg positions
    positions[9, 0] += left_leg_shift  # Left knee
    positions[10, 0] += left_leg_shift  # Left ankle
    
    # Update right leg positions
    positions[12, 0] += right_leg_shift  # Right knee
    positions[13, 0] += right_leg_shift  # Right ankle
    
    # Add vertical oscillation for a bouncing effect
    vertical_oscillation = amplitude * np.sin(2 * np.pi * frequency * frame)
    positions[:, 1] += vertical_oscillation
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-8, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()
