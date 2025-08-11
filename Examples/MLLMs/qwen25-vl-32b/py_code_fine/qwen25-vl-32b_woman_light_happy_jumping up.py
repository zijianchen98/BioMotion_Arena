
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are relative to the center of the figure
initial_positions = {
    'head': [0, 1.5],
    'torso_top': [0, 1],
    'torso_bottom': [0, 0],
    'left_shoulder': [-0.5, 1],
    'right_shoulder': [0.5, 1],
    'left_elbow': [-1, 0.5],
    'right_elbow': [1, 0.5],
    'left_wrist': [-1.5, 0],
    'right_wrist': [1.5, 0],
    'left_hip': [-0.5, -0.5],
    'right_hip': [0.5, -0.5],
    'left_knee': [-1, -1],
    'right_knee': [1, -1],
    'left_ankle': [-1.5, -1.5],
    'right_ankle': [1.5, -1.5]
}

# Convert the dictionary to a list of coordinates
initial_coords = np.array(list(initial_positions.values()))

# Define the amplitude and frequency for the jump
amplitude = 0.8  # Vertical displacement for the jump
frequency = 0.5  # Frequency of the jump (cycles per second)
duration = 5     # Duration of the animation in seconds
fps = 30         # Frames per second

# Calculate the number of frames
num_frames = int(duration * fps)

# Create a time array for the animation
t = np.linspace(0, duration, num_frames)

# Define the vertical displacement function for the jump
def jump_displacement(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Precompute the vertical displacements for all frames
vertical_displacements = jump_displacement(t, amplitude, frequency)

# Function to update the positions of the points for each frame
def update_points(frame, scat, initial_coords, vertical_displacements):
    # Apply the vertical displacement to all points
    displaced_coords = initial_coords.copy()
    displaced_coords[:, 1] += vertical_displacements[frame]
    
    # Update the scatter plot data
    scat.set_offsets(displaced_coords)
    return scat,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')  # Hide the axes

# Plot the initial positions of the points
scat = ax.scatter(initial_coords[:, 0], initial_coords[:, 1], s=50, c='white')

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update_points,
    frames=num_frames,
    fargs=(scat, initial_coords, vertical_displacements),
    interval=1000 / fps,  # Frame interval in milliseconds
    blit=True
)

# Display the animation
plt.show()
