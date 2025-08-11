
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Define the initial positions of the point-lights
positions = np.array([
    [5.0, 8.0],  # Head
    [4.5, 7.0],  # Shoulder left
    [5.5, 7.0],  # Shoulder right
    [4.0, 6.0],  # Elbow left
    [6.0, 6.0],  # Elbow right
    [3.5, 5.0],  # Hand left
    [6.5, 5.0],  # Hand right
    [5.0, 2.0],  # Waist
    [4.0, 1.0],  # Hip left
    [6.0, 1.0],  # Hip right
    [3.5, 0.0],  # Knee left
    [6.5, 0.0],  # Knee right
    [3.0, -1.0], # Foot left
    [7.0, -1.0], # Foot right
    [5.0, 4.0]   # Torso
])

# Scatter plot for point-lights
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=50)

def update(frame):
    global positions
    
    # Define walking motion parameters
    phase = np.pi * 2 * frame / 50
    walk_amplitude = 0.7
    walk_frequency = 0.4
    
    # Update positions based on walking motion
    positions[0] = [5.0, 8.0]  # Head remains fixed
    positions[1] = [4.5 + np.sin(phase) * walk_amplitude, 7.0]  # Shoulder left
    positions[2] = [5.5 - np.sin(phase) * walk_amplitude, 7.0]  # Shoulder right
    positions[3] = [4.0 + np.sin(phase + np.pi) * walk_amplitude, 6.0]  # Elbow left
    positions[4] = [6.0 - np.sin(phase + np.pi) * walk_amplitude, 6.0]  # Elbow right
    positions[5] = [3.5 + np.sin(phase) * walk_amplitude, 5.0]  # Hand left
    positions[6] = [6.5 - np.sin(phase) * walk_amplitude, 5.0]  # Hand right
    positions[7] = [5.0 + np.sin(phase * walk_frequency) * walk_amplitude, 2.0]  # Waist
    positions[8] = [4.0 + np.sin(phase + np.pi) * walk_amplitude, 1.0]  # Hip left
    positions[9] = [6.0 - np.sin(phase + np.pi) * walk_amplitude, 1.0]  # Hip right
    positions[10] = [3.5 + np.sin(phase) * walk_amplitude, 0.0]  # Knee left
    positions[11] = [6.5 - np.sin(phase) * walk_amplitude, 0.0]  # Knee right
    positions[12] = [3.0 + np.sin(phase - np.pi/2) * walk_amplitude, -1.0]  # Foot left
    positions[13] = [7.0 - np.sin(phase - np.pi/2) * walk_amplitude, -1.0]  # Foot right
    positions[14] = [5.0, 4.0]  # Torso remains fixed
    
    # Update scatter plot data
    scat.set_offsets(positions)

# Create animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=100, repeat=True)

plt.show()
