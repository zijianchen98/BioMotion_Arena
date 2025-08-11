
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a human figure
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "hip_left", "knee_left", "ankle_left", "shoulder_right", "elbow_right",
    "wrist_right", "hip_right", "knee_right", "ankle_right", "center"
]

# Initial positions of the key points (x, y)
initial_positions = np.array([
    [0, 1.8], [0, 1.6], [-0.4, 1.5], [-0.6, 1.3], [-0.7, 1.1],
    [-0.4, 1.0], [-0.5, 0.7], [-0.5, 0.4], [0.4, 1.5], [0.6, 1.3],
    [0.7, 1.1], [0.4, 1.0], [0.5, 0.7], [0.5, 0.4], [0, 1.0]
])

# Function to simulate the jumping motion
def jump(t):
    # Parameters for the jump
    amplitude = 0.5
    frequency = 1.0
    phase = t * frequency
    
    # Update positions based on the jump
    positions = initial_positions.copy()
    
    # Apply vertical displacement for the jump
    positions[:, 1] += amplitude * np.sin(2 * np.pi * phase)
    
    # Apply horizontal displacement for the forward motion
    positions[:, 0] += 0.1 * t
    
    # Apply additional limb movements for realism
    positions[2:5, 1] -= 0.1 * np.sin(2 * np.pi * phase + np.pi / 2)  # Left arm
    positions[8:11, 1] -= 0.1 * np.sin(2 * np.pi * phase - np.pi / 2)  # Right arm
    positions[5:8, 1] -= 0.1 * np.sin(2 * np.pi * phase + np.pi / 2)  # Left leg
    positions[11:14, 1] -= 0.1 * np.sin(2 * np.pi * phase - np.pi / 2)  # Right leg
    
    return positions

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-1, 2)
ax.set_ylim(0, 2)
ax.set_aspect('equal')
ax.axis('off')

# Create the scatter plot for the point-lights
points = ax.scatter([], [], s=50, color='white')

# Animation update function
def update(frame):
    positions = jump(frame)
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2, 100), interval=50, blit=True)

# Display the animation
plt.show()
