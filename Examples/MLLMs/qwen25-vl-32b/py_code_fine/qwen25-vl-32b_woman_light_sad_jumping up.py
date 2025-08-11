
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure
initial_positions = {
    'head': [0, 1],
    'torso_top': [0, 0],
    'torso_bottom': [0, -1],
    'left_shoulder': [-0.5, 0.5],
    'right_shoulder': [0.5, 0.5],
    'left_elbow': [-1, 0],
    'right_elbow': [1, 0],
    'left_wrist': [-1.5, -0.5],
    'right_wrist': [1.5, -0.5],
    'left_hip': [-0.5, -1.5],
    'right_hip': [0.5, -1.5],
    'left_knee': [-1, -2.5],
    'right_knee': [1, -2.5],
    'left_ankle': [-1.5, -3.5],
    'right_ankle': [1.5, -3.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the amplitude and frequency for the jumping motion
amplitude = 0.5  # Vertical displacement for the jump
frequency = 0.5  # Frequency of the jump (cycles per second)

# Define the time range for the animation
num_frames = 100  # Number of frames in the animation
dt = 0.1  # Time step between frames
t = np.linspace(0, num_frames * dt, num_frames)  # Time array

# Function to update the positions of the points over time
def update_positions(frame):
    # Apply vertical sinusoidal motion to all points
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t[frame])
    updated_coords = initial_coords.copy()
    updated_coords[:, 1] += vertical_displacement  # Apply vertical displacement
    
    # Adjust the torso and head to show a "sad" posture
    updated_coords[initial_coords == initial_positions['torso_top']] -= 0.1  # Slightly lower the torso
    updated_coords[initial_coords == initial_positions['head']] -= 0.1  # Slightly lower the head
    
    # Adjust the arms to show a "sad" posture
    updated_coords[initial_coords == initial_positions['left_wrist']] -= 0.2  # Lower the left wrist
    updated_coords[initial_coords == initial_positions['right_wrist']] -= 0.2  # Lower the right wrist
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-4, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    updated_coords = update_positions(frame)
    scatter.set_offsets(updated_coords)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
