
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.axis('off')

# Points representing the happy woman
points = ax.scatter([], [], c='white', s=100)

# Initial positions of the points for the happy woman jumping
initial_positions = np.array([
    [2.5, 4],  # Head
    [2.4, 3.5], [2.6, 3.5],  # Shoulders
    [2.3, 3], [2.7, 3],  # Hips
    [2.2, 2.5], [2.8, 2.5],  # Knees
    [2.1, 2], [2.9, 2],  # Feet
    [2.4, 3.3], [2.6, 3.3],  # Elbows
    [2.3, 2.8], [2.2, 2.4],  # Left arm
    [2.7, 2.8], [2.8, 2.4]   # Right arm
])

# Number of frames for the animation
num_frames = 50

# Function to update the point positions for the jumping motion
def update(frame):
    positions = initial_positions.copy()
    
    # Head
    positions[0, 1] = 4 + 0.5 * np.sin(frame * np.pi / num_frames)
    
    # Shoulders
    positions[1, 1] = 3.5 + 0.4 * np.sin(frame * np.pi / num_frames)
    positions[2, 1] = 3.5 + 0.4 * np.sin(frame * np.pi / num_frames)
    
    # Hips
    positions[3, 1] = 3 + 0.4 * np.sin(frame * np.pi / num_frames)
    positions[4, 1] = 3 + 0.4 * np.sin(frame * np.pi / num_frames)
    
    # Knees
    positions[5, 1] = 2.5 + 0.3 * np.sin(frame * np.pi / num_frames)
    positions[6, 1] = 2.5 + 0.3 * np.sin(frame * np.pi / num_frames)
    
    # Feet
    positions[7, 1] = 2 + 0.2 * np.sin(frame * np.pi / num_frames)
    positions[8, 1] = 2 + 0.2 * np.sin(frame * np.pi / num_frames)
    
    # Elbows
    positions[9, 1] = 3.3 + 0.2 * np.sin(frame * np.pi / num_frames)
    positions[10, 1] = 3.3 + 0.2 * np.sin(frame * np.pi / num_frames)
    
    # Left arm
    positions[11, 0] = 2.4 + 0.1 * np.sin(frame * np.pi / num_frames)
    positions[11, 1] = 2.8 + 0.1 * np.sin(frame * np.pi / num_frames)
    positions[12, 0] = 2.4 + 0.2 * np.sin(frame * np.pi / num_frames)
    positions[12, 1] = 2.4 + 0.1 * np.sin(frame * np.pi / num_frames)
    
    # Right arm
    positions[13, 0] = 2.6 - 0.1 * np.sin(frame * np.pi / num_frames)
    positions[13, 1] = 2.8 + 0.1 * np.sin(frame * np.pi / num_frames)
    positions[14, 0] = 2.6 - 0.2 * np.sin(frame * np.pi / num_frames)
    positions[14, 1] = 2.4 + 0.1 * np.sin(frame * np.pi / num_frames)
    
    points.set_offsets(positions)
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
