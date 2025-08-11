
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent:
# 0-Head, 1-Left Shoulder, 2-Right Shoulder, 3-Left Elbow, 4-Right Elbow,
# 5-Left Hand, 6-Right Hand, 7-Spine, 8-Pelvis, 9-Left Knee, 10-Right Knee,
# 11-Left Ankle, 12-Right Ankle, 13-Left Toe, 14-Right Toe
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [1, -1],  # Right Shoulder
    [-2, -3], # Left Elbow
    [2, -3],  # Right Elbow
    [-3, -5], # Left Hand
    [3, -5],  # Right Hand
    [0, -2],  # Spine
    [0, -4],  # Pelvis
    [-1, -6], # Left Knee
    [1, -6],  # Right Knee
    [-1, -8], # Left Ankle
    [1, -8],  # Right Ankle
    [-1, -9], # Left Toe
    [1, -9]   # Right Toe
])

# Define the amplitude and frequency for the walking cycle
amplitude = 0.5
frequency = 0.1

# Function to update the positions of the points for each frame
def update_points(frame):
    positions = initial_positions.copy()
    
    # Simulate walking motion
    phase = frame * frequency
    
    # Spine and pelvis sway side-to-side
    positions[7, 0] += amplitude * np.sin(phase)  # Spine
    positions[8, 0] += amplitude * np.sin(phase)  # Pelvis
    
    # Arms swing opposite to legs
    positions[3, 0] -= amplitude * np.cos(phase)  # Left Elbow
    positions[4, 0] += amplitude * np.cos(phase)  # Right Elbow
    positions[5, 0] -= amplitude * np.cos(phase)  # Left Hand
    positions[6, 0] += amplitude * np.cos(phase)  # Right Hand
    
    # Legs move forward and backward
    positions[9, 1] += amplitude * np.sin(phase)  # Left Knee
    positions[10, 1] -= amplitude * np.sin(phase)  # Right Knee
    positions[11, 1] += amplitude * np.sin(phase)  # Left Ankle
    positions[12, 1] -= amplitude * np.sin(phase)  # Right Ankle
    positions[13, 1] += amplitude * np.sin(phase)  # Left Toe
    positions[14, 1] -= amplitude * np.sin(phase)  # Right Toe
    
    # Adjust for heavy, sad gait by reducing vertical displacement
    positions[:, 1] *= 0.7  # Make the gait more sluggish
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def update(frame):
    positions = update_points(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
