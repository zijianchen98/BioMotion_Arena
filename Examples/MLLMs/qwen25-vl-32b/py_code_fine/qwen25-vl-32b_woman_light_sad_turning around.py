
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points (x, y coordinates)
# These points represent key joints of the human body:
# 0-Head, 1-Shoulder R, 2-Elbow R, 3-Wrist R, 4-Shoulder L, 5-Elbow L, 6-Wrist L,
# 7-Hip R, 8-Knee R, 9-Ankle R, 10-Hip L, 11-Knee L, 12-Ankle L, 13-Chest, 14-Pelvis
initial_positions = np.array([
    [0.0, 1.0],  # Head
    [0.5, 0.5],  # Shoulder R
    [0.7, 0.3],  # Elbow R
    [0.8, 0.1],  # Wrist R
    [-0.5, 0.5], # Shoulder L
    [-0.7, 0.3], # Elbow L
    [-0.8, 0.1], # Wrist L
    [0.3, -0.5], # Hip R
    [0.4, -0.8], # Knee R
    [0.5, -1.0], # Ankle R
    [-0.3, -0.5], # Hip L
    [-0.4, -0.8], # Knee L
    [-0.5, -1.0], # Ankle L
    [0.0, 0.7],   # Chest
    [0.0, -0.3]   # Pelvis
])

# Define the number of frames for the animation
num_frames = 100

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')  # Hide axes for a cleaner look

# Scatter plot for the points
scatter = ax.scatter([], [], s=50, c='white')

# Function to update the scatter plot for each frame
def update(frame):
    # Define the rotation angle for each frame
    angle = np.radians(360 * frame / num_frames)
    
    # Apply rotation transformation to the points
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    
    # Rotate the points around the pelvis (origin)
    rotated_positions = np.dot(initial_positions - initial_positions[14], rotation_matrix) + initial_positions[14]
    
    # Update the scatter plot data
    scatter.set_offsets(rotated_positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
