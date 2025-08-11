
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These points represent the joints of a human figure
initial_positions = {
    'head': [0, 1],
    'torso_top': [0, 0],
    'torso_bottom': [0, -1],
    'left_shoulder': [-0.5, 0],
    'right_shoulder': [0.5, 0],
    'left_elbow': [-1, -0.5],
    'right_elbow': [1, -0.5],
    'left_wrist': [-1.5, -1],
    'right_wrist': [1.5, -1],
    'left_hip': [-0.5, -2],
    'right_hip': [0.5, -2],
    'left_knee': [-1, -3],
    'right_knee': [1, -3],
    'left_ankle': [-1.5, -4],
    'right_ankle': [1.5, -4]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the amplitude and frequency for the jumping motion
amplitude = 0.5  # Vertical displacement
frequency = 0.5  # Frequency of the jump (Hz)
time_step = 0.1  # Time step for each frame
num_frames = 100  # Total number of frames in the animation

# Function to update the positions based on time
def update_positions(t):
    # Apply vertical oscillation to the torso and head
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Update the positions of the torso and head
    updated_coords = initial_coords.copy()
    updated_coords[0] += [0, vertical_displacement]  # Head
    updated_coords[1] += [0, vertical_displacement]  # Torso top
    updated_coords[2] += [0, vertical_displacement]  # Torso bottom
    
    # Adjust the limbs to reflect the jumping motion
    updated_coords[3:] += [0, vertical_displacement / 2]  # Shoulders, elbows, wrists, hips, knees, ankles
    
    return updated_coords

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-5, 2)
ax.axis('off')  # Hide the axes

# Scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame * time_step  # Current time
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()
