
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions represent a standing pose
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [0.2, -0.4],  # Right elbow
    [-0.3, -0.6], # Left wrist
    [0.3, -0.6],  # Right wrist
    [0.0, -0.8],  # Pelvis
    [-0.1, -1.0], # Left hip
    [0.1, -1.0],  # Right hip
    [-0.2, -1.2], # Left knee
    [0.2, -1.2],  # Right knee
    [-0.3, -1.4], # Left ankle
    [0.3, -1.4],  # Right ankle
    [0.0, -1.6]   # Feet center
])

# Define the amplitude and frequency for the jump motion
amplitude = 0.3  # Vertical displacement
frequency = 0.5  # Frequency of the jump (cycles per second)

# Define the time range for the animation
num_frames = 100  # Number of frames in the animation
dt = 0.1          # Time step between frames
t = np.linspace(0, num_frames * dt, num_frames)  # Time array

# Function to update the positions based on the jump motion
def update_positions(frame):
    # Calculate vertical displacement for the jump
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t[frame])
    
    # Apply the vertical displacement to the entire body
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += vertical_displacement
    
    # Add forward motion (horizontal displacement)
    horizontal_displacement = 0.01 * frame  # Linear forward motion
    updated_positions[:, 0] += horizontal_displacement
    
    # Simulate arm and leg movements during the jump
    updated_positions[4, 1] -= 0.1 * np.sin(2 * np.pi * frequency * t[frame])  # Right wrist
    updated_positions[5, 1] -= 0.1 * np.sin(2 * np.pi * frequency * t[frame])  # Left wrist
    updated_positions[10, 1] -= 0.1 * np.sin(2 * np.pi * frequency * t[frame]) # Left knee
    updated_positions[11, 1] -= 0.1 * np.sin(2 * np.pi * frequency * t[frame]) # Right knee
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1.8, 0.2)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_aspect('equal')

# Initialize the scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white', edgecolors='none')

# Animation function
def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
