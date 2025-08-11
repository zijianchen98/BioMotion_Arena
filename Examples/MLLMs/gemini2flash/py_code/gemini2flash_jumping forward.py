
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and point-lights
num_frames = 50
num_points = 15

# Define the initial positions of the point-lights (adjust these to match the jumping action)
initial_positions = np.array([
    [0, 6],  # Head
    [-1, 5],  # Left shoulder
    [1, 5],   # Right shoulder
    [-2, 4],  # Left elbow
    [2, 4],   # Right elbow
    [-3, 3],  # Left wrist
    [3, 3],   # Right wrist
    [-0.5, 4],  # Center spine
    [-1, 2],  # Left hip
    [1, 2],   # Right hip
    [-2, 1],  # Left knee
    [2, 1],   # Right knee
    [-1.5, 0],  # Left ankle
    [1.5, 0],   # Right ankle
    [0, 0.5] # Hip center
])

# Define the motion of the point-lights over time (adjust these to create a jumping motion)
motion = np.zeros((num_frames, num_points, 2))

# Example motion: a simple jump forward
for frame in range(num_frames):
    # General upward movement for the jump
    motion[frame, :, 1] += 0.1 * np.sin(frame * np.pi / num_frames) 
    
    # Forward movement for the jump
    motion[frame, :, 0] += 0.05 * frame / num_frames

    # Simulate arm swing during jump
    motion[frame, 3, 0] += 0.02 * np.sin(frame * np.pi / (num_frames/2)) # Right Elbow
    motion[frame, 2, 0] -= 0.02 * np.sin(frame * np.pi / (num_frames/2)) # Right Shoulder
    motion[frame, 4, 0] -= 0.02 * np.sin(frame * np.pi / (num_frames/2)) # Left Elbow
    motion[frame, 1, 0] += 0.02 * np.sin(frame * np.pi / (num_frames/2)) # Left Shoulder
    
    # Leg movements (example: alternating knee positions)
    motion[frame, 10, 1] += 0.03 * np.sin(frame * np.pi / (num_frames / 2)) # Left Knee
    motion[frame, 11, 1] -= 0.03 * np.sin(frame * np.pi / (num_frames / 2)) # Right Knee
    motion[frame, 12, 1] += 0.05 * np.sin(frame * np.pi / (num_frames / 2)) # Left Ankle
    motion[frame, 13, 1] -= 0.05 * np.sin(frame * np.pi / (num_frames / 2)) # Right Ankle

# Calculate the positions of the point-lights for each frame
positions = initial_positions + motion.cumsum(axis=0)

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')
plt.axis('off')

# Create the scatter plot for the point-lights
scat = ax.scatter([], [], c='white', s=20)

# Animation function
def animate(i):
    scat.set_offsets(positions[i])
    return (scat,)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
