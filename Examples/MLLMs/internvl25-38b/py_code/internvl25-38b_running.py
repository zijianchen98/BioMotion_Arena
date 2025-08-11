
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of point-lights
num_points = 15

# Define the initial positions of the point-lights to form a standing figure
initial_positions = np.array([
    [-0.05, 0.0], [-0.1, -0.1], [0.1, -0.1],    # Head, shoulders
    [-0.1, -0.3], [0.1, -0.3],                    # Hips
    [-0.15, -0.4], [-0.05, -0.5], [0.05, -0.5], [0.15, -0.4],   # Legs
    [-0.2, -0.7], [0.2, -0.7],                # Feet
    [-0.05, -0.1], [0.05, -0.1],             # Arms
    [-0.05, -0.3], [0.05, -0.3]              # Hands
])

# Define the frames for running movement
def update(frame):
    angle = np.pi * 2 * frame / num_frames
    positions = initial_positions.copy()
    
    # Left leg
    positions[7] = [positions[7][0] * np.cos(angle) - positions[7][1] * np.sin(angle),
                     positions[7][0] * np.sin(angle) + positions[7][1] * np.cos(angle)]
    positions[8] = [positions[8][0] * np.cos(angle) - positions[8][1] * np.sin(angle),
                     positions[8][0] * np.sin(angle) + positions[8][1] * np.cos(angle)]
    
    # Right leg
    positions[6] = [positions[6][0] * np.cos(angle) + positions[6][1] * np.sin(angle),
                     -positions[6][0] * np.sin(angle) + positions[6][1] * np.cos(angle)]
    positions[9] = [positions[9][0] * np.cos(angle) + positions[9][1] * np.sin(angle),
                     -positions[9][0] * np.sin(angle) + positions[9][1] * np.cos(angle)]
    
    # Left arm
    positions[10] = [positions[10][0] * np.cos(angle) - positions[10][1] * np.sin(angle),
                      positions[10][0] * np.sin(angle) + positions[10][1] * np.cos(angle)]
    positions[12] = [positions[12][0] * np.cos(angle) - positions[12][1] * np.sin(angle),
                      positions[12][0] * np.sin(angle) + positions[12][1] * np.cos(angle)]
    
    # Right arm
    positions[11] = [positions[11][0] * np.cos(angle) + positions[11][1] * np.sin(angle),
                      -positions[11][0] * np.sin(angle) + positions[11][1] * np.cos(angle)]
    positions[13] = [positions[13][0] * np.cos(angle) + positions[13][1] * np.sin(angle),
                      -positions[13][0] * np.sin(angle) + positions[13][1] * np.cos(angle)]
    
    scatter.set_offsets(positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 0)
ax.set_facecolor('black')
ax.axis('off')

# Create scatter plot
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white', s=50)

# Number of frames for the animation
num_frames = 30

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, repeat=True)

# Show the animation
plt.show()
