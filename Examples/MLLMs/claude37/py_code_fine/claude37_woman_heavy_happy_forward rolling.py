
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
frames = 100
radius = 0.05
weight = np.array([0, -1])  # Direction of gravity

# Initialize point-light positions
# Head, shoulders, elbows, wrists, hips, knees, and feet
initial_positions = np.array([
    [0, 0.8],    # Head
    [0, 0.6],    # Shoulders
    [-0.2, 0.5], # Left Elbow
    [-0.4, 0.4], # Left Wrist
    [0.2, 0.5],  # Right Elbow
    [0.4, 0.4],  # Right Wrist
    [0, 0.4],    # Hips
    [-0.2, 0.2], # Left Knee
    [-0.2, 0],   # Left Foot
    [0.2, 0.2],  # Right Knee
    [0.2, 0],    # Right Foot
    [0.1, 0.6],  # Additional lights for detail
    [-0.1, 0.6],
    [-0.1, 0.8],
    [0.1, 0.8],
    [0, 0.5]
])

# Define the update function for the animation
def update(frame):
    plt.clf()  # Clear previous frame
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_facecolor('black')

    # Calculate new positions for forward roll motion
    theta = frame * np.pi / frames  # Forward roll progression
    new_positions = initial_positions.copy()
    
    # Simple rotation for forward roll simulation
    rotation_matrix = np.array([
        [np.cos(theta), np.sin(theta)],
        [-np.sin(theta), np.cos(theta)]
    ])
    
    for i in range(num_lights):
        new_positions[i] = np.dot(rotation_matrix, initial_positions[i])
    
    # Draw point lights
    for (x, y) in new_positions:
        plt.plot(x, y, 'wo', markersize=10)  # White points

# Create animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, repeat=True)

# Display the animation
plt.show()
