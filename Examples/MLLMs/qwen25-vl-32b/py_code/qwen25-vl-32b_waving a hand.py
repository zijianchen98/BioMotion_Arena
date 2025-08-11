
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (joints)
initial_positions = np.array([
    [0.5, 0.9],  # Head
    [0.4, 0.7],  # Left shoulder
    [0.6, 0.7],  # Right shoulder
    [0.3, 0.5],  # Left elbow
    [0.1, 0.3],  # Left wrist
    [0.5, 0.5],  # Torso
    [0.7, 0.5],  # Right elbow
    [0.9, 0.3],  # Right wrist
    [0.4, 0.3],  # Left hip
    [0.2, 0.1],  # Left knee
    [0.1, 0.0],  # Left ankle
    [0.6, 0.3],  # Right hip
    [0.8, 0.1],  # Right knee
    [0.9, 0.0],  # Right ankle
    [0.5, 0.1]   # Pelvis
])

# Define the wave motion for the right hand
def wave_motion(t):
    amplitude = 0.2
    frequency = 0.5  # Hz
    phase_shift = np.pi / 2  # To start at the peak
    return amplitude * np.sin(2 * np.pi * frequency * t + phase_shift)

# Update function for the animation
def update(frame, positions, scat):
    # Apply wave motion to the right wrist (index 7)
    positions[7][1] = initial_positions[7][1] + wave_motion(frame / 30)
    
    # Update the scatter plot with new positions
    scat.set_offsets(positions)
    return scat,

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look

# Create a scatter plot for the point lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Create the animation
ani = animation.FuncAnimation(
    fig,
    update,
    frames=100,  # Number of frames
    fargs=(initial_positions.copy(), scat),
    interval=30,  # Delay between frames in milliseconds
    blit=True
)

# Display the animation
plt.show()
