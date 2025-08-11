
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions represent a standing posture
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [0.2, -0.4],  # Right elbow
    [-0.3, -0.6], # Left wrist
    [0.3, -0.6],  # Right wrist
    [0.0, -0.8],  # Torso
    [-0.1, -1.0], # Left hip
    [0.1, -1.0],  # Right hip
    [-0.2, -1.2], # Left knee
    [0.2, -1.2],  # Right knee
    [-0.3, -1.4], # Left ankle
    [0.3, -1.4],  # Right ankle
    [0.0, -1.6]   # Feet
])

# Define the wave cycle duration (in seconds)
wave_duration = 2.0  # Duration of one wave cycle
num_frames = 100     # Number of frames for the animation

# Define the amplitude and frequency for the wave motion
amplitude = 0.3      # Amplitude of the wave
frequency = 1.0      # Frequency of the wave (cycles per second)

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Waving motion: Move the right hand (right wrist) in a sinusoidal pattern
    positions[6, 1] += amplitude * np.sin(2 * np.pi * frequency * t)  # Right wrist vertical movement
    
    # Add some horizontal movement to the right arm for a more natural wave
    positions[6, 0] += 0.1 * np.sin(2 * np.pi * frequency * t + np.pi / 2)  # Right wrist horizontal movement
    
    # Smoothly move the right elbow and shoulder to follow the wrist
    positions[5, 1] = positions[6, 1] - 0.1  # Right elbow follows the wrist
    positions[4, 1] = positions[5, 1] - 0.1  # Right shoulder follows the elbow
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1.8, 0.2)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / num_frames * wave_duration  # Current time in seconds
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=30, blit=True)

# Display the animation
plt.show()
