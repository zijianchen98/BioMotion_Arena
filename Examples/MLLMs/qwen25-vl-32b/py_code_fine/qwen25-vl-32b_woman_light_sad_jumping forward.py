
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These coordinates represent a standing pose
initial_positions = np.array([
    [0.0, 0.0],   # Head
    [-0.1, -0.2], # Left shoulder
    [0.1, -0.2],  # Right shoulder
    [-0.2, -0.4], # Left elbow
    [0.2, -0.4],  # Right elbow
    [-0.3, -0.8], # Left wrist
    [0.3, -0.8],  # Right wrist
    [0.0, -1.0],  # Hips
    [-0.2, -1.4], # Left knee
    [0.2, -1.4],  # Right knee
    [-0.3, -1.8], # Left ankle
    [0.3, -1.8],  # Right ankle
    [-0.4, -2.0], # Left foot
    [0.4, -2.0],  # Right foot
])

# Define the amplitude and frequency for the jumping motion
amplitude = 0.5  # Vertical displacement
frequency = 0.5  # Frequency of the jump (cycles per second)

# Define the time range for the animation
num_frames = 100  # Number of frames in the animation
dt = 0.1          # Time step between frames
t = np.linspace(0, num_frames * dt, num_frames)

# Function to update the positions based on time
def update_positions(t):
    # Apply vertical oscillation for the jump
    vertical_displacement = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Modify the y-coordinates of the points to simulate jumping
    updated_positions = initial_positions.copy()
    updated_positions[:, 1] += vertical_displacement
    
    # Add forward motion by shifting x-coordinates
    forward_displacement = 0.1 * np.sin(2 * np.pi * frequency * t)
    updated_positions[:, 0] += forward_displacement
    
    return updated_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.0, 1.0)
ax.set_ylim(-2.5, 0.5)
ax.axis('off')  # Hide axes for a cleaner look
ax.set_aspect('equal')

# Scatter plot for the point lights
scatter = ax.scatter([], [], s=50, c='white', edgecolors='none')

# Animation function
def animate(frame):
    t_current = frame * dt
    positions = update_positions(t_current)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, frames=num_frames, interval=50, blit=True
)

# Display the animation
plt.show()
