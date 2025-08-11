
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.2, -0.2], # Left Shoulder
    [0.2, -0.2],  # Right Shoulder
    [-0.4, -0.6], # Left Elbow
    [0.4, -0.6],  # Right Elbow
    [-0.6, -1.0], # Left Wrist
    [0.6, -1.0],  # Right Wrist
    [0.0, -0.8],  # Torso
    [-0.2, -1.4], # Left Hip
    [0.2, -1.4],  # Right Hip
    [-0.4, -2.0], # Left Knee
    [0.4, -2.0],  # Right Knee
    [-0.6, -2.6], # Left Ankle
    [0.6, -2.6],  # Right Ankle
    [0.0, -3.0]   # Feet
])

# Define the amplitude and frequency for the waving motion
amplitude = 0.3
frequency = 0.5  # Hz

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Simulate waving motion for the right hand
    wave_angle = np.sin(2 * np.pi * frequency * t)
    right_elbow_x = 0.4 + amplitude * np.cos(wave_angle)
    right_wrist_x = 0.6 + amplitude * np.cos(wave_angle + np.pi / 2)
    
    positions[4, 0] = right_elbow_x  # Update right elbow x-coordinate
    positions[5, 0] = right_wrist_x  # Update right wrist x-coordinate
    
    return positions

# Create the plot
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-3.5, 0.5)
ax.axis('off')  # Hide axes
points = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t = frame / 30.0  # Time in seconds (assuming 30 FPS)
    positions = update_positions(t)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=33, blit=True
)

# Display the animation
plt.show()
