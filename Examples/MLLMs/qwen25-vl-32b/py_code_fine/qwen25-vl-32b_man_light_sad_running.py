
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the initial positions of the 15 points (x, y coordinates)
# Points: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left Shoulder
    [1, -1],  # Right Shoulder
    [-2, -3], # Left Elbow
    [2, -3],  # Right Elbow
    [-1, -4], # Left Wrist
    [1, -4],  # Right Wrist
    [0, -5],  # Hip
    [-1, -7], # Left Knee
    [1, -7],  # Right Knee
    [-1, -9], # Left Ankle
    [1, -9],  # Right Ankle
])

# Function to update the positions for running motion
def update_positions(frame, positions):
    # Define the amplitude and frequency for the running motion
    amplitude = 0.5
    frequency = 2 * np.pi / num_frames
    
    # Update the positions based on the frame
    positions[:, 1] = initial_positions[:, 1]  # Reset vertical positions
    
    # Add oscillatory motion for running
    phase = frame * frequency
    positions[0, 1] += amplitude * np.sin(phase)  # Head bobs up and down
    
    # Left leg (hip, knee, ankle)
    positions[8, 1] += amplitude * np.sin(phase + np.pi / 2)  # Left knee
    positions[10, 1] += amplitude * np.sin(phase + np.pi / 2)  # Left ankle
    
    # Right leg (hip, knee, ankle)
    positions[9, 1] += amplitude * np.sin(phase - np.pi / 2)  # Right knee
    positions[11, 1] += amplitude * np.sin(phase - np.pi / 2)  # Right ankle
    
    # Arms (elbows and wrists)
    positions[4, 1] += amplitude * np.sin(phase + np.pi)  # Left wrist
    positions[5, 1] += amplitude * np.sin(phase + np.pi)  # Right wrist
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-10, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=50, c='white')

# Animation function
def animate(frame):
    updated_positions = update_positions(frame, initial_positions.copy())
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
