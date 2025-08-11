
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the initial positions of the 15 points (joints)
# These positions are relative and will be updated for each frame
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, -1], # Left shoulder
    [0.5, -1],  # Right shoulder
    [-1, -2],   # Left elbow
    [1, -2],    # Right elbow
    [-1.5, -3], # Left wrist
    [1.5, -3],  # Right wrist
    [0, -4],    # Hips
    [-1, -5],   # Left hip
    [1, -5],    # Right hip
    [-1.5, -6], # Left knee
    [1.5, -6],  # Right knee
    [-2, -7],   # Left ankle
    [2, -7],    # Right ankle
    [0, -8]     # Tailbone
])

# Define the amplitude and frequency for the running motion
amplitude = 0.5
frequency = 0.1

# Function to update the positions for each frame
def update_positions(frame):
    positions = initial_positions.copy()
    
    # Simulate running motion by oscillating the legs and arms
    phase = frame * frequency
    
    # Move the left leg forward and right leg backward
    positions[9][0] += amplitude * np.sin(phase)  # Left hip
    positions[11][0] -= amplitude * np.sin(phase) # Right hip
    positions[12][0] += amplitude * np.sin(phase + np.pi / 2)  # Left knee
    positions[13][0] -= amplitude * np.sin(phase + np.pi / 2)  # Right knee
    positions[14][0] += amplitude * np.sin(phase + np.pi)  # Left ankle
    positions[15][0] -= amplitude * np.sin(phase + np.pi)  # Right ankle
    
    # Move the arms in opposition to the legs
    positions[3][0] -= amplitude * np.sin(phase)  # Left elbow
    positions[4][0] += amplitude * np.sin(phase)  # Right elbow
    positions[5][0] -= amplitude * np.sin(phase + np.pi / 2)  # Left wrist
    positions[6][0] += amplitude * np.sin(phase + np.pi / 2)  # Right wrist
    
    return positions

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-8, 2)
ax.axis('off')  # Hide axes for a cleaner look

# Initial scatter plot
scatter = ax.scatter([], [], s=50, c='white')

def animate(frame):
    positions = update_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
