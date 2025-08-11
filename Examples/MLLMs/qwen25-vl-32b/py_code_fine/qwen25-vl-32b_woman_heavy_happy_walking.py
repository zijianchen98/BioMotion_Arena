
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent the body parts: head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.3, 0.6], # Left shoulder
    [0.3, 0.6],  # Right shoulder
    [-0.5, 0.4], # Left elbow
    [0.5, 0.4],  # Right elbow
    [-0.7, 0.2], # Left wrist
    [0.7, 0.2],  # Right wrist
    [0.0, 0.0],  # Hips
    [-0.3, -0.2], # Left hip
    [0.3, -0.2], # Right hip
    [-0.5, -0.4], # Left knee
    [0.5, -0.4], # Right knee
    [-0.7, -0.6], # Left ankle
    [0.7, -0.6], # Right ankle
])

# Define the amplitude and frequency for the walking motion
amplitude = 0.1  # Amplitude of the walking cycle
frequency = 0.05  # Frequency of the walking cycle

# Function to update the positions of the points for each frame
def update_points(frame):
    global initial_positions
    
    # Calculate the phase of the walking cycle
    phase = frame / num_frames * 2 * np.pi
    
    # Update the positions based on the walking cycle
    updated_positions = initial_positions.copy()
    
    # Move the left leg forward and right leg backward
    updated_positions[9, 0] += amplitude * np.sin(phase)  # Left hip
    updated_positions[11, 0] += amplitude * np.sin(phase + np.pi)  # Left knee
    updated_positions[13, 0] += amplitude * np.sin(phase + np.pi)  # Left ankle
    
    updated_positions[10, 0] += amplitude * np.sin(phase + np.pi)  # Right hip
    updated_positions[12, 0] += amplitude * np.sin(phase)  # Right knee
    updated_positions[14, 0] += amplitude * np.sin(phase)  # Right ankle
    
    # Sway the upper body slightly
    updated_positions[1, 0] += amplitude * 0.5 * np.cos(phase)  # Left shoulder
    updated_positions[2, 0] += amplitude * 0.5 * np.cos(phase + np.pi)  # Right shoulder
    
    # Update the plot data
    scatter.set_offsets(updated_positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')  # Hide the axes
ax.set_facecolor('black')  # Set background to black

# Plot the initial positions as white points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, interval=50, repeat=True)

# Display the animation
plt.show()
