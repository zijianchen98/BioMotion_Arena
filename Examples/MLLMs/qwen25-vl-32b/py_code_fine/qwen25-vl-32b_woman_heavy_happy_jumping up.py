
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These positions represent the body parts of the woman
initial_positions = {
    'head': [0, 1.5],
    'left_shoulder': [-0.5, 1.0],
    'right_shoulder': [0.5, 1.0],
    'left_elbow': [-1.0, 0.5],
    'right_elbow': [1.0, 0.5],
    'left_wrist': [-1.5, 0.0],
    'right_wrist': [1.5, 0.0],
    'left_hip': [-0.5, 0.0],
    'right_hip': [0.5, 0.0],
    'left_knee': [-0.5, -0.5],
    'right_knee': [0.5, -0.5],
    'left_ankle': [-0.5, -1.0],
    'right_ankle': [0.5, -1.0]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Function to update the positions based on time
def update_positions(coords, t):
    # Amplitude and frequency for the jump
    amplitude = 0.5
    frequency = 0.5  # Adjust this for speed
    
    # Vertical displacement for the jump
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the y-coordinates of all points
    coords[:, 1] += vertical_displacement
    
    # Simulate leg extension/compression
    leg_amplitude = 0.3
    leg_frequency = 2 * frequency
    leg_displacement = leg_amplitude * np.sin(2 * np.pi * leg_frequency * t)
    
    # Update knee and ankle positions
    coords[8, 1] -= leg_displacement  # Left knee
    coords[9, 1] -= leg_displacement  # Right knee
    coords[10, 1] -= 2 * leg_displacement  # Left ankle
    coords[11, 1] -= 2 * leg_displacement  # Right ankle
    
    # Simulate arm swing
    arm_amplitude = 0.2
    arm_frequency = 2 * frequency
    arm_displacement = arm_amplitude * np.sin(2 * np.pi * arm_frequency * t + np.pi / 2)
    
    # Update wrist positions
    coords[5, 0] += arm_displacement  # Left wrist
    coords[6, 0] -= arm_displacement  # Right wrist
    
    return coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_facecolor('black')  # Set background to black

# Scatter plot for the point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Initialize the data
t = 0
coords = initial_coords.copy()

# Animation function
def animate(frame):
    global t
    t += 0.05  # Time step
    new_coords = update_positions(coords.copy(), t)
    scatter.set_offsets(new_coords)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
