
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 120

# Define the positions of the 15 point-lights for a bowing action
# These positions are simplified and may need refinement for full realism
def get_positions(t):
    # Convert time to radians for smooth motion
    theta = t * 2 * np.pi / num_frames
    
    # Positions are defined as [x, y] coordinates
    positions = np.array([
        [0.5 + 0.1*np.sin(theta), 0.8 + 0.05*np.cos(2*theta)],  # Head
        [0.4 + 0.05*np.sin(theta), 0.7],                       # Left Shoulder
        [0.6 + 0.05*np.sin(theta), 0.7],                       # Right Shoulder
        [0.4 + 0.05*np.sin(theta), 0.5 + 0.05*np.cos(theta)],   # Left Elbow
        [0.6 + 0.05*np.sin(theta), 0.5 + 0.05*np.cos(theta)],   # Right Elbow
        [0.4 + 0.05*np.sin(theta), 0.3],                       # Left Wrist
        [0.6 + 0.05*np.sin(theta), 0.3],                       # Right Wrist
        [0.5 + 0.05*np.sin(theta), 0.6],                       # Torso
        [0.4 + 0.05*np.sin(theta), 0.4 + 0.05*np.cos(theta)],   # Left Hip
        [0.6 + 0.05*np.sin(theta), 0.4 + 0.05*np.cos(theta)],   # Right Hip
        [0.4 + 0.05*np.sin(theta), 0.2],                       # Left Knee
        [0.6 + 0.05*np.sin(theta), 0.2],                       # Right Knee
        [0.4 + 0.05*np.sin(theta), 0.0],                       # Left Ankle
        [0.6 + 0.05*np.sin(theta), 0.0],                       # Right Ankle
        [0.5 + 0.1*np.sin(theta), 0.9 + 0.05*np.cos(2*theta)]  # Feet
    ])
    
    # Adjust positions for bowing motion
    positions[:, 1] -= 0.1 * np.abs(np.sin(2*theta))
    return positions

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the scatter plot
scatter = ax.scatter([], [], s=100, c='white')

# Update function for the animation
def update(frame):
    positions = get_positions(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
