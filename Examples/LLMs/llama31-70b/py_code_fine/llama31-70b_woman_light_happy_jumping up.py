
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 point-lights
lights = [
    'Head', 'Neck', 'R Shoulder', 'L Shoulder', 'R Elbow', 'L Elbow', 
    'R Wrist', 'L Wrist', 'R Hip', 'L Hip', 'R Knee', 'L Knee', 
    'R Ankle', 'L Ankle', 'Torso'
]

# Define the initial positions of the point-lights
initial_positions = np.array([
    [0, 10],  # Head
    [0, 8],   # Neck
    [2, 7],   # R Shoulder
    [-2, 7],  # L Shoulder
    [3, 5],   # R Elbow
    [-3, 5],  # L Elbow
    [4, 3],   # R Wrist
    [-4, 3],  # L Wrist
    [2, 2],   # R Hip
    [-2, 2],  # L Hip
    [2, 0],   # R Knee
    [-2, 0],  # L Knee
    [2, -2],  # R Ankle
    [-2, -2], # L Ankle
    [0, 4]    # Torso
])

# Define the movement of the point-lights
def update(frame):
    positions = initial_positions.copy()
    
    # Jumping motion
    for i in range(15):
        if i in [0, 1, 14]:  # Head, Neck, Torso
            positions[i, 1] += np.sin(frame / 10.0) * 2
        elif i in [2, 3]:  # Shoulders
            positions[i, 1] += np.sin(frame / 10.0) * 1.5
        elif i in [4, 5]:  # Elbows
            positions[i, 1] += np.sin(frame / 10.0) * 1
        elif i in [6, 7]:  # Wrists
            positions[i, 1] += np.sin(frame / 10.0) * 0.5
        elif i in [8, 9]:  # Hips
            positions[i, 0] += np.sin(frame / 10.0) * 0.5
            positions[i, 1] += np.sin(frame / 10.0) * 1
        elif i in [10, 11]:  # Knees
            positions[i, 0] += np.sin(frame / 10.0) * 0.5
            positions[i, 1] += np.sin(frame / 10.0) * 0.5
        elif i in [12, 13]:  # Ankles
            positions[i, 0] += np.sin(frame / 10.0) * 0.5
    
    # Update the positions of the point-lights
    scatter.set_offsets(positions)

# Create a new figure
fig, ax = plt.subplots()

# Create a scatter plot of the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='white')

# Set the background color to black
ax.set_facecolor('black')

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Remove the axis
plt.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50)

plt.show()
