
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points
num_points = 15

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')  # Hide axes for a clean background

# Create scatter plot for the point-lights
scatter = ax.scatter([], [], c='white', s=50)

# Initial positions of the points (forming a simple human-like structure)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, -1], [0.5, -1],  # Shoulders
    [-1, -2], [1, -2],      # Hips
    [-1.5, -3], [-0.5, -3], [0.5, -3], [1.5, -3],  # Legs
    [-0.5, -4], [0.5, -4],  # Feet
    [-0.5, -5], [0.5, -5]   # Additional points for rolling effect
])

# Animation parameters
roll_speed = 0.1  # Speed of rolling
roll_amplitude = 1.0  # Amplitude of rolling motion
frame_rate = 30  # Frames per second
duration = 5  # Duration of animation in seconds
num_frames = duration * frame_rate

# Function to update the positions of the points
def update(frame):
    # Calculate the rolling motion
    theta = roll_speed * frame  # Angular position
    x_offset = np.sin(theta) * roll_amplitude  # Horizontal displacement
    y_offset = np.cos(theta) * roll_amplitude  # Vertical displacement
    
    # Apply the rolling motion to each point
    positions = initial_positions.copy()
    positions[:, 0] += x_offset  # Update x-coordinates
    positions[:, 1] += y_offset  # Update y-coordinates
    
    # Update the scatter plot
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, interval=1000 / frame_rate, blit=True)

# Display the animation
plt.show()
