
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    # Head
    [0.0, 0.9],
    # Shoulders
    [-0.3, 0.7], [0.3, 0.7],
    # Arms
    [-0.6, 0.5], [-0.4, 0.3], [-0.2, 0.1],  # Left arm (waving)
    [0.6, 0.5], [0.4, 0.3], [0.2, 0.1],     # Right arm
    # Hips
    [-0.2, 0.2], [0.2, 0.2],
    # Legs
    [-0.3, 0.0], [-0.1, -0.2], [0.1, -0.2], [0.3, 0.0]
])

# Define the wave amplitude and frequency for the left arm
wave_amplitude = 0.2
wave_frequency = 0.5  # Hz

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Wave the left hand (points at indices 3, 4, 5)
    phase = 2 * np.pi * wave_frequency * t
    positions[3:6, 1] += wave_amplitude * np.sin(phase)
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 30.0  # Assuming 30 frames per second
    positions = update_positions(t)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=180, interval=33, blit=True  # 30 FPS
)

# Display the animation
plt.show()
