
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24

# Initial positions of the lights (approximate starting position for sitting)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.3], [-0.2, -0.7], [-0.2, -1.1],  # Left arm
    [0.1, -0.3], [0.2, -0.7], [0.2, -1.1],   # Right arm
    [-0.1, 0.3], [-0.2, 0.6], [-0.2, 0.9],   # Left leg
    [0.1, 0.3], [0.2, 0.6], [0.2, 0.9],     # Right leg
    [0, -0.1]    # Torso
])

# Function to generate smooth motion
def generate_motion(t):
    # Simple harmonic motion for sitting down
    head = initial_positions[0] + np.array([0, 0.1 * np.sin(0.1 * t)])
    left_arm = initial_positions[1:4] + np.array([[-0.05 * np.sin(0.1 * t), 0],
                                                 [-0.1 * np.sin(0.1 * t), 0],
                                                 [-0.1 * np.sin(0.1 * t), 0]])
    right_arm = initial_positions[4:7] + np.array([[0.05 * np.sin(0.1 * t), 0],
                                                  [0.1 * np.sin(0.1 * t), 0],
                                                  [0.1 * np.sin(0.1 * t), 0]])
    left_leg = initial_positions[7:10] + np.array([[-0.05 * np.sin(0.1 * t), 0],
                                                   [-0.1 * np.sin(0.1 * t), 0],
                                                   [-0.1 * np.sin(0.1 * t), 0]])
    right_leg = initial_positions[10:13] + np.array([[0.05 * np.sin(0.1 * t), 0],
                                                    [0.1 * np.sin(0.1 * t), 0],
                                                    [0.1 * np.sin(0.1 * t), 0]])
    torso = initial_positions[13] + np.array([0, 0.1 * np.sin(0.1 * t)])
    
    return np.vstack((head, left_arm, right_arm, left_leg, right_leg, torso))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 1)
ax.set_aspect('equal')
ax.axis('off')

# Initialize scatter plot
scat = ax.scatter([], [], s=100, color='white')

# Update function for animation
def update(frame):
    positions = generate_motion(frame)
    scat.set_offsets(positions)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show the plot
plt.show()
