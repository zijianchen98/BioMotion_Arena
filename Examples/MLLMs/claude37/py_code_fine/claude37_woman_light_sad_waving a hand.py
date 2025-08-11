
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the animation
num_points = 15
duration = 100  # Duration of the animation
frames = 60     # Number of frames in the animation
wave_amplitude = 0.1  # Amplitude of the hand wave

# Initial positions for the points
# These points represent joints of a sad woman waving a hand
positions = np.array([
    [0, 1.5],  # head
    [-0.5, 1.0],  # left shoulder
    [0.5, 1.0],  # right shoulder
    [-0.3, 0.5],  # left elbow
    [0.3, 0.5],  # right elbow
    [-0.1, 0.2],  # left wrist
    [0.1, 0.2],  # right wrist
    [0, 0],  # torso
    [-0.5, 0],  # left hip
    [0.5, 0],  # right hip
    [-0.4, -1],  # left knee
    [0.4, -1],  # right knee
    [-0.2, -1.5],  # left ankle
    [0.2, -1.5],  # right ankle
    [-0.5, -2],  # left foot
    [0.5, -2]   # right foot
])

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Create a scatter plot for the points
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate the points
def animate(i):
    # Updating positions for waving hand
    wave_offset = wave_amplitude * np.sin(2 * np.pi * i / frames)
    
    # Apply some offsets for animation
    positions[5, 1] += wave_offset  # Left wrist
    positions[6, 1] += wave_offset * 1.2  # Right wrist
    
    # Set the new positions
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, repeat=True)

# Show the animation
plt.show()
