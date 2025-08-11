
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
# These positions are based on a typical human body structure:
# Head, shoulders, elbows, wrists, hips, knees, ankles
initial_positions = np.array([
    [0.0, 0.8],  # Head
    [-0.3, 0.6], # Left shoulder
    [0.3, 0.6],  # Right shoulder
    [-0.5, 0.4], # Left elbow
    [0.5, 0.4],  # Right elbow
    [-0.4, 0.2], # Left wrist
    [0.4, 0.2],  # Right wrist
    [0.0, 0.0],  # Hips
    [-0.3, -0.2], # Left knee
    [0.3, -0.2], # Right knee
    [-0.4, -0.4], # Left ankle
    [0.4, -0.4], # Right ankle
    [-0.2, 0.4], # Left hip
    [0.2, 0.4],  # Right hip
    [0.0, 0.6]   # Center of shoulders
])

# Define the amplitude and frequency for the oscillation
amplitude = 0.05
frequency = 0.5  # Hz

# Function to update the positions of the points over time
def update_points(frame):
    global initial_positions
    
    # Apply a slight oscillation to simulate movement
    t = frame / 30.0  # Time in seconds (assuming 30 fps)
    
    # Add oscillation to specific joints to simulate sitting posture
    oscillation = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Adjust head position to show a slumped posture
    initial_positions[0][1] = 0.8 + oscillation * 0.5
    
    # Adjust shoulder and hip positions to show a slumped posture
    initial_positions[1][1] += oscillation * 0.3  # Left shoulder
    initial_positions[2][1] += oscillation * 0.3  # Right shoulder
    initial_positions[12][1] += oscillation * 0.3  # Left hip
    initial_positions[13][1] += oscillation * 0.3  # Right hip
    
    # Adjust wrist positions to show a relaxed posture
    initial_positions[5][1] += oscillation * 0.2  # Left wrist
    initial_positions[6][1] += oscillation * 0.2  # Right wrist
    
    # Adjust knee and ankle positions to show a slumped posture
    initial_positions[8][1] += oscillation * 0.2  # Left knee
    initial_positions[9][1] += oscillation * 0.2  # Right knee
    initial_positions[10][1] += oscillation * 0.2  # Left ankle
    initial_positions[11][1] += oscillation * 0.2  # Right ankle
    
    return initial_positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.7, 0.7)
ax.set_ylim(-0.7, 1.0)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Animation function
def animate(frame):
    updated_positions = update_points(frame)
    scatter.set_offsets(updated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=33, blit=True)

# Display the animation
plt.show()
