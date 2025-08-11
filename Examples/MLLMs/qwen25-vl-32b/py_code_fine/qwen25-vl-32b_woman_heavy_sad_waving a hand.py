
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    # Head
    [0.0, 0.9],
    # Shoulders
    [-0.2, 0.7], [0.2, 0.7],
    # Arms
    [-0.4, 0.5], [-0.6, 0.3], [-0.8, 0.1],  # Left arm
    [0.4, 0.5], [0.6, 0.3], [0.8, 0.1],     # Right arm
    # Torso
    [0.0, 0.5], [0.0, 0.3], [0.0, 0.1],
    # Legs
    [-0.2, -0.1], [0.2, -0.1]
])

# Define the amplitude and frequency for the wave-like motion
amplitude = 0.1
frequency = 0.5  # Hz

# Define the heaviness factor (slower movement)
heaviness_factor = 0.5

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Add wave-like motion to the right arm (waving)
    wave_offset = amplitude * np.sin(2 * np.pi * frequency * t)
    positions[6:9, 1] += wave_offset
    
    # Add heaviness to the entire body (slower vertical oscillation)
    heaviness_offset = heaviness_factor * amplitude * np.sin(2 * np.pi * frequency * t / 2)
    positions[:, 1] -= heaviness_offset
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 30  # Assuming 30 frames per second
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=33, blit=True)

# Display the animation
plt.show()
