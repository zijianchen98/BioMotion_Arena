
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 point-lights
# These points represent the joints of a human figure in a lying-down position
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.8],  # Left shoulder
    [0.6, 0.8],  # Right shoulder
    [0.3, 0.7],  # Left elbow
    [0.7, 0.7],  # Right elbow
    [0.2, 0.6],  # Left wrist
    [0.8, 0.6],  # Right wrist
    [0.5, 0.5],  # Waist
    [0.3, 0.4],  # Left hip
    [0.7, 0.4],  # Right hip
    [0.2, 0.3],  # Left knee
    [0.8, 0.3],  # Right knee
    [0.1, 0.2],  # Left ankle
    [0.9, 0.2],  # Right ankle
    [0.5, 0.1]   # Feet (center)
])

# Define the range of motion for each joint
motion_amplitude = {
    'head': 0.02,
    'shoulders': 0.03,
    'elbows': 0.04,
    'wrists': 0.05,
    'waist': 0.03,
    'hips': 0.04,
    'knees': 0.05,
    'ankles': 0.06,
    'feet': 0.03
}

# Define the frequency of oscillation for each joint
frequency = {
    'head': 0.5,
    'shoulders': 0.6,
    'elbows': 0.7,
    'wrists': 0.8,
    'waist': 0.5,
    'hips': 0.6,
    'knees': 0.7,
    'ankles': 0.8,
    'feet': 0.5
}

# Function to update the positions of the point-lights
def update(frame):
    global initial_positions
    
    # Apply oscillatory motion to each joint
    positions = initial_positions.copy()
    
    # Head
    positions[0, 1] += motion_amplitude['head'] * np.sin(2 * np.pi * frequency['head'] * frame / 60)
    
    # Shoulders
    positions[1, 1] += motion_amplitude['shoulders'] * np.sin(2 * np.pi * frequency['shoulders'] * frame / 60)
    positions[2, 1] += motion_amplitude['shoulders'] * np.sin(2 * np.pi * frequency['shoulders'] * frame / 60)
    
    # Elbows
    positions[3, 1] += motion_amplitude['elbows'] * np.sin(2 * np.pi * frequency['elbows'] * frame / 60)
    positions[4, 1] += motion_amplitude['elbows'] * np.sin(2 * np.pi * frequency['elbows'] * frame / 60)
    
    # Wrists
    positions[5, 1] += motion_amplitude['wrists'] * np.sin(2 * np.pi * frequency['wrists'] * frame / 60)
    positions[6, 1] += motion_amplitude['wrists'] * np.sin(2 * np.pi * frequency['wrists'] * frame / 60)
    
    # Waist
    positions[7, 1] += motion_amplitude['waist'] * np.sin(2 * np.pi * frequency['waist'] * frame / 60)
    
    # Hips
    positions[8, 1] += motion_amplitude['hips'] * np.sin(2 * np.pi * frequency['hips'] * frame / 60)
    positions[9, 1] += motion_amplitude['hips'] * np.sin(2 * np.pi * frequency['hips'] * frame / 60)
    
    # Knees
    positions[10, 1] += motion_amplitude['knees'] * np.sin(2 * np.pi * frequency['knees'] * frame / 60)
    positions[11, 1] += motion_amplitude['knees'] * np.sin(2 * np.pi * frequency['knees'] * frame / 60)
    
    # Ankles
    positions[12, 1] += motion_amplitude['ankles'] * np.sin(2 * np.pi * frequency['ankles'] * frame / 60)
    positions[13, 1] += motion_amplitude['ankles'] * np.sin(2 * np.pi * frequency['ankles'] * frame / 60)
    
    # Feet
    positions[14, 1] += motion_amplitude['feet'] * np.sin(2 * np.pi * frequency['feet'] * frame / 60)
    
    # Update the scatter plot
    scatter.set_offsets(positions)

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Initialize the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Create the animation
animation = FuncAnimation(fig, update, frames=300, interval=30, blit=False)

# Display the animation
plt.show()
