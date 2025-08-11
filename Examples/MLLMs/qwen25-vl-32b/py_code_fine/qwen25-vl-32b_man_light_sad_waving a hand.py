
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure:
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0, 0],   # Head
    [-1, -1], # Left shoulder
    [1, -1],  # Right shoulder
    [-2, -3], # Left elbow
    [2, -3],  # Right elbow
    [-1, -4], # Left wrist
    [1, -4],  # Right wrist
    [0, -5],  # Hips
    [-1, -7], # Left knee
    [1, -7],  # Right knee
    [-1, -9], # Left ankle
    [1, -9],  # Right ankle
])

# Define the wave amplitude and frequency
wave_amplitude = 0.5
wave_frequency = 0.5  # Hz

# Define the number of frames for the animation
num_frames = 100

# Function to update the positions for waving the right hand
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Waving the right hand (right wrist and right elbow)
    positions[6, 1] += wave_amplitude * np.sin(2 * np.pi * wave_frequency * frame / num_frames)  # Right wrist vertical movement
    positions[5, 1] += wave_amplitude * np.sin(2 * np.pi * wave_frequency * frame / num_frames)  # Right elbow vertical movement
    
    # Slight sagging for a "sad" posture
    positions[:, 1] -= 0.1  # All points move slightly downward
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-10, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Update function for the animation
def update(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
