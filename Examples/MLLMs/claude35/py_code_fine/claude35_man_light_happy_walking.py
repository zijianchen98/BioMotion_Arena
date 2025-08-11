
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the walking motion for the key points of the happy man's skeleton
# For a simple walking motion, we will animate the 'leg' and 'arm' positions
# Using sine and cosine functions for smooth motion

def get_positions(frame):
    # Base positions of the point lights
    positions = {
        'head': (0, 1),
        'shoulder_left': (-0.15, 0.85),
        'shoulder_right': (0.15, 0.85),
        'elbow_left': (-0.25 + 0.05 * np.sin(frame * 2 * np.pi / num_frames), 0.7),
        'elbow_right': (0.25 - 0.05 * np.sin(frame * 2 * np.pi / num_frames), 0.7),
        'wrist_left': (-0.35, 0.6),
        'wrist_right': (0.35, 0.6),
        'hip_left': (-0.1, 0.6),
        'hip_right': (0.1, 0.6),
        'knee_left': (-0.1, 0.4 - 0.1 * np.sin(frame * 2 * np.pi / num_frames)),
        'knee_right': (0.1, 0.4 + 0.1 * np.sin(frame * 2 * np.pi / num_frames)),
        'ankle_left': (-0.1, 0.2),
        'ankle_right': (0.1, 0.2),
        'foot_left': (-0.1, 0.1),
        'foot_right': (0.1, 0.1),
    }
    return np.array(list(positions.values()))

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.5)
ax.set_facecolor('black')
# Turn off axes
ax.axis('off')

# Initialize point lights
points, = ax.plot([], [], 'o', color='white')

# Animation update function
def update(frame):
    positions = get_positions(frame)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=1000/30, blit=True)

# Display the animation
plt.show()
