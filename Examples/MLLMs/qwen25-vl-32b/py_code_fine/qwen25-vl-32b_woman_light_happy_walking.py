
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = {
    'head': [0, 1],
    'torso': [0, 0],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0.5],
    'right_elbow': [1, 0.5],
    'left_hand': [-1.5, 0.5],
    'right_hand': [1.5, 0.5],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_ankle': [-1.5, -1.5],
    'right_ankle': [1.5, -1.5],
    'left_toe': [-1.5, -2],
    'right_toe': [1.5, -2]
}

# Convert the dictionary to a list of (x, y) tuples
positions = np.array(list(initial_positions.values()))

# Define the amplitude and frequency for the walking motion
amplitude = 0.5
frequency = 0.1  # Adjust this for speed

# Function to update the positions based on time
def update_positions(t):
    updated_positions = positions.copy()
    
    # Torso swaying side-to-side
    updated_positions[1][0] = amplitude * np.sin(frequency * t)
    
    # Arms swinging opposite to legs
    updated_positions[4][0] = amplitude * np.cos(frequency * t)  # Left elbow
    updated_positions[7][0] = amplitude * np.cos(frequency * t)  # Right elbow
    
    # Legs stepping forward
    updated_positions[9][0] = amplitude * np.sin(frequency * t + np.pi / 2)  # Right hip
    updated_positions[10][0] = amplitude * np.sin(frequency * t + np.pi / 2)  # Right knee
    updated_positions[11][0] = amplitude * np.sin(frequency * t + np.pi / 2)  # Right ankle
    updated_positions[12][0] = amplitude * np.sin(frequency * t + np.pi / 2)  # Right toe
    
    updated_positions[8][0] = amplitude * np.sin(frequency * t - np.pi / 2)  # Left hip
    updated_positions[13][0] = amplitude * np.sin(frequency * t - np.pi / 2)  # Left knee
    updated_positions[14][0] = amplitude * np.sin(frequency * t - np.pi / 2)  # Left ankle
    updated_positions[15][0] = amplitude * np.sin(frequency * t - np.pi / 2)  # Left toe
    
    return updated_positions

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 10  # Time in seconds
    updated_positions = update_positions(t)
    scat.set_offsets(updated_positions)
    return scat,

# Create the animation
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
