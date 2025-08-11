
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These points represent:
# 0-Head, 1-Neck, 2-Chest, 3-Spine, 4-Pelvis,
# 5-R Shoulder, 6-L Shoulder, 7-R Elbow, 8-L Elbow,
# 9-R Hand, 10-L Hand, 11-R Hip, 12-L Hip,
# 13-R Knee, 14-L Knee
initial_positions = np.array([
    [0, 1],   # Head
    [0, 0.8], # Neck
    [0, 0.6], # Chest
    [0, 0.4], # Spine
    [0, 0.2], # Pelvis
    [-0.3, 0.6], # R Shoulder
    [0.3, 0.6],  # L Shoulder
    [-0.5, 0.4], # R Elbow
    [0.5, 0.4],  # L Elbow
    [-0.7, 0.2], # R Hand
    [0.7, 0.2],  # L Hand
    [-0.3, 0.2], # R Hip
    [0.3, 0.2],  # L Hip
    [-0.3, 0],   # R Knee
    [0.3, 0]     # L Knee
])

# Define the amplitude and frequency for the jump
amplitude = 0.5  # Vertical displacement
frequency = 0.5  # Frequency of the jump (cycles per second)
duration = 5     # Duration of the animation in seconds
fps = 30         # Frames per second
num_frames = duration * fps

# Generate time array
t = np.linspace(0, duration, num_frames)

# Define the vertical displacement function for the jump
def jump_displacement(t):
    return amplitude * np.sin(2 * np.pi * frequency * t)

# Update function for the animation
def update(frame, positions, scat):
    # Apply vertical displacement to all points
    vertical_offset = jump_displacement(t[frame])
    updated_positions = positions.copy()
    updated_positions[:, 1] += vertical_offset
    
    # Add forward motion (horizontal displacement)
    horizontal_offset = 0.1 * np.sin(2 * np.pi * frequency * t[frame])  # Forward motion
    updated_positions[:, 0] += horizontal_offset
    
    # Update the scatter plot data
    scat.set_offsets(updated_positions)
    return scat,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initialize the scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, fargs=(initial_positions, scat),
    interval=1000 / fps, blit=True
)

# Display the animation
plt.show()
