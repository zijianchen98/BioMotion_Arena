
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial and final positions for the point-lights
# Points: Head, Shoulders, Elbows, Wrists, Hips, Knees, Ankles
initial_positions = np.array([
    [0.5, 1.0],  # Head
    [0.3, 0.8],  # Left Shoulder
    [0.7, 0.8],  # Right Shoulder
    [0.2, 0.5],  # Left Elbow
    [0.8, 0.5],  # Right Elbow
    [0.4, 0.3],  # Left Wrist
    [0.6, 0.3],  # Right Wrist
    [0.4, 0.6],  # Left Hip
    [0.6, 0.6],  # Right Hip
    [0.3, 0.4],  # Left Knee
    [0.7, 0.4],  # Right Knee
    [0.2, 0.2],  # Left Ankle
    [0.8, 0.2],  # Right Ankle
])

final_positions = np.array([
    [0.5, 0.6],  # Head (slumped)
    [0.3, 0.7],  # Left Shoulder
    [0.7, 0.7],  # Right Shoulder
    [0.2, 0.4],  # Left Elbow
    [0.8, 0.4],  # Right Elbow
    [0.4, 0.2],  # Left Wrist
    [0.6, 0.2],  # Right Wrist
    [0.4, 0.5],  # Left Hip
    [0.6, 0.5],  # Right Hip
    [0.3, 0.3],  # Left Knee
    [0.7, 0.3],  # Right Knee
    [0.2, 0.1],  # Left Ankle
    [0.8, 0.1],  # Right Ankle
])

# Number of frames for the animation
num_frames = 50

# Interpolate between initial and final positions
positions = np.linspace(initial_positions, final_positions, num_frames)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')  # Hide axes for a cleaner look
scat = ax.scatter([], [], s=50, c='white', edgecolors='none')

def init():
    """Initialize the scatter plot."""
    scat.set_offsets([])
    return scat,

def update(frame):
    """Update the scatter plot for each frame."""
    x, y = positions[frame].T
    scat.set_offsets(np.c_[x, y])
    return scat,

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

# Display the animation
plt.show()
