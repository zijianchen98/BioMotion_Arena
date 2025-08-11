
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_frames = 200
num_points = 15
frame_rate = 30  # Frames per second
interval = 1000 / frame_rate  # Delay between frames in milliseconds

# Define initial coordinates for the point-lights
initial_coords = np.array([
    [0, 10],  # Head
    [-2, 8], [2, 8],  # Shoulders
    [-3, 5], [3, 5],  # Elbows
    [-3, 2], [3, 2],  # Wrists
    [-1, 7], [1, 7],  # Hips
    [-2, 4], [2, 4],  # Knees
    [-2, 1], [2, 1],  # Ankles
    [-2, -1], [2, -1]   # Feet
])

# Function to generate point-light coordinates for each frame
def generate_frames(num_frames):
    frames = []
    for i in range(num_frames):
        # Simulate rolling motion
        angle = (i / num_frames) * 2 * np.pi  # Complete one rotation
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
        
        # Apply rotation and translation to the initial coordinates
        rotated_coords = np.dot(initial_coords, rotation_matrix)
        translated_coords = rotated_coords + [0, i/5] # Translate to the right
        
        frames.append(translated_coords)
    return frames

# Generate frames
frames = generate_frames(num_frames)

# Animation function
def update(frame_num, scat):
    scat.set_offsets(frames[frame_num])
    return scat,

# Setup plot
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-5, 25)
ax.set_aspect('equal')
ax.set_facecolor('black')
plt.axis('off')

# Create scatter plot
scat = ax.scatter(frames[0][:, 0], frames[0][:, 1], s=20, color='white')

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(scat,),
                              interval=interval, blit=True, repeat=True)

plt.show()
