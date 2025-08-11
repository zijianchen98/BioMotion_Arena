
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights representing the man lying down
initial_positions = np.array([
    [0.5, 0.2],  # Head
    [0.4, 0.3],  # Left shoulder
    [0.6, 0.3],  # Right shoulder
    [0.3, 0.4],  # Left elbow
    [0.7, 0.4],  # Right elbow
    [0.2, 0.5],  # Left hand
    [0.8, 0.5],  # Right hand
    [0.5, 0.6],  # Chest
    [0.5, 0.7],  # Navel
    [0.4, 0.8],  # Left hip
    [0.6, 0.8],  # Right hip
    [0.3, 0.9],  # Left knee
    [0.7, 0.9],  # Right knee
    [0.2, 1.0],  # Left foot
    [0.8, 1.0]   # Right foot
])

# Function to animate the lying down motion
def update(frame):
    global initial_positions
    # Adjust positions for the lying down motion
    positions = initial_positions.copy()
    # Simulate the motion by slightly adjusting the positions over time
    if frame <= 30:
        positions[0][1] += 0.01 * frame  # Move head upwards slightly
        positions[1][1] += 0.005 * frame  # Slight lift on left shoulder
        positions[2][1] += 0.005 * frame  # Slight lift on right shoulder
    else:
        positions[0][1] -= 0.01 * (frame - 30)  # Move head back down
        positions[1][1] -= 0.005 * (frame - 30)  # Return left shoulder
        positions[2][1] -= 0.005 * (frame - 30)  # Return right shoulder
    
    scat.set_offsets(positions)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide the axis
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

ani = animation.FuncAnimation(fig, update, frames=60, interval=40, repeat=True)
plt.show()
