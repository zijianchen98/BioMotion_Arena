
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [-0.4, -0.6], # Left wrist
    [0.2, -0.4],  # Right elbow
    [0.4, -0.6],  # Right wrist
    [-0.3, -1.0], # Left hip
    [-0.5, -1.2], # Left knee
    [-0.7, -1.4], # Left ankle
    [0.3, -1.0],  # Right hip
    [0.5, -1.2],  # Right knee
    [0.7, -1.4],  # Right ankle
    [0.0, -1.6],  # Center of gravity (to emphasize heaviness)
    [0.0, -1.8]   # Ground reference
])

# Define the amplitude and frequency for the wave-like motion
amplitude = 0.1
frequency = 0.5  # Hz

# Define the time array for the animation
num_frames = 100
dt = 0.1  # Time step in seconds
t = np.linspace(0, num_frames * dt, num_frames)

# Function to update the positions based on time
def update_positions(t):
    positions = initial_positions.copy()
    
    # Add wave-like motion to the right hand (right wrist)
    positions[5, 0] += amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Add a slight downward tilt to the head (sadness)
    positions[0, 1] -= 0.05
    
    # Add a subtle sway to the body (heaviness)
    positions[:, 1] += 0.02 * np.sin(2 * np.pi * frequency * t / 2)
    
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-2.0, 0.5)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white')

# Animation function
def animate(frame):
    t_current = frame * dt
    positions = update_positions(t_current)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=1000*dt, blit=True)

# Display the animation
plt.show()
