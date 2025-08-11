
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Define the number of frames
num_frames = 100

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 6],    # Head
    [-0.5, 5],  # Left Shoulder
    [0.5, 5],   # Right Shoulder
    [-1.5, 4],  # Left Elbow
    [1.5, 4],   # Right Elbow
    [-2, 3],   # Left Wrist
    [2, 3],    # Right Wrist
    [-0.2, 4],  # Left Hip
    [0.2, 4],   # Right Hip
    [-1, 2],   # Left Knee
    [1, 2],    # Right Knee
    [-1.2, 1],  # Left Ankle
    [1.2, 1],   # Right Ankle
    [-1, 0.2],  # Left Foot
    [1, 0.2]    # Right Foot
])

# Define the amplitude and frequency of the sine wave for each point-light
amplitudes = np.array([
    [0.0, 0.0],    # Head
    [0.2, 0.1],   # Left Shoulder
    [0.2, 0.1],   # Right Shoulder
    [0.3, 0.2],  # Left Elbow
    [0.3, 0.2],  # Right Elbow
    [0.4, 0.3],   # Left Wrist
    [0.4, 0.3],    # Right Wrist
    [0.2, 0.1],  # Left Hip
    [0.2, 0.1],   # Right Hip
    [0.3, 0.2],   # Left Knee
    [0.3, 0.2],    # Right Knee
    [0.4, 0.3],  # Left Ankle
    [0.4, 0.3],   # Right Ankle
    [0.4, 0.3],  # Left Foot
    [0.4, 0.3]    # Right Foot
])

frequencies = np.array([
    [0.0, 0.0],    # Head
    [0.5, 0.5],   # Left Shoulder
    [0.5, -0.5],   # Right Shoulder
    [0.5, 0.5],  # Left Elbow
    [0.5, -0.5],  # Right Elbow
    [0.5, 0.5],   # Left Wrist
    [0.5, -0.5],    # Right Wrist
    [0.5, -0.5],  # Left Hip
    [0.5, 0.5],   # Right Hip
    [0.5, -0.5],   # Left Knee
    [0.5, 0.5],    # Right Knee
    [0.5, -0.5],  # Left Ankle
    [0.5, 0.5],   # Right Ankle
    [0.5, -0.5],  # Left Foot
    [0.5, 0.5]    # Right Foot
])

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 7)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=20)

# Define the animation function
def animate(i):
    # Calculate the new positions of the point-lights
    new_positions = initial_positions + amplitudes * np.sin(2 * np.pi * frequencies * i / num_frames)
    
    # Update the scatter plot
    scatter.set_offsets(new_positions)
    
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

# Show the animation
plt.show()
