
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters of the animation
num_lights = 15
num_frames = 100
time_jump = 2  # seconds
Jump_height = 2  # maximum height of the jump

# Function to calculate the jump motion of the lights
def calculate_jump_position(t, max_height, base_frequency=1.0):
    # Simple sinusoidal function to model the jump
    return max_height * np.sin(2 * np.pi * base_frequency * t)

# Function to update the positions of the lights
def update(frame):
    t = frame / num_frames * time_jump
    jump_height = calculate_jump_position(t, Jump_height)
    
    # Generate random positions for the point lights
    positions = np.random.rand(num_lights, 2) * 10 - 5  # within a 10x10 area centered at (0, 0)
    # Adjust y-position to simulate jumping
    positions[:, 1] += jump_height
    return positions,

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-2, 5)
ax.set_facecolor('black')
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')  # Hide axes and background for a clean look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, color='white')

# Animation update function
def animate(frame):
    positions = update(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
animation = FuncAnimation(fig, animate, frames=num_frames, interval=1000/30)

# Display the animation
plt.show()
