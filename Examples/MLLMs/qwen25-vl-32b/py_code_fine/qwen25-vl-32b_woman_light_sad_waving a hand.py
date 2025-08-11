
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    # Head
    [0.0, 0.9],
    # Shoulders
    [-0.3, 0.6], [0.3, 0.6],
    # Arms
    [-0.4, 0.4], [-0.6, 0.2], [-0.7, 0.0],  # Left arm
    [0.4, 0.4], [0.6, 0.2], [0.7, 0.0],     # Right arm
    # Torso
    [0.0, 0.5], [0.0, 0.3], [0.0, 0.1],
    # Legs
    [-0.2, 0.0], [0.2, 0.0]
])

# Define the wave amplitude and frequency for the right hand
wave_amplitude = 0.2
wave_frequency = 0.5  # Hz

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Wave the right hand (points 6, 7, 8)
    wave_angle = wave_amplitude * np.sin(2 * np.pi * wave_frequency * t)
    positions[6:9, 1] += wave_angle
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes
ax.set_aspect('equal')

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 30.0  # Time in seconds (assuming 30 fps)
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=120, interval=33, blit=True  # 30 FPS
)

# Display the animation
plt.show()
