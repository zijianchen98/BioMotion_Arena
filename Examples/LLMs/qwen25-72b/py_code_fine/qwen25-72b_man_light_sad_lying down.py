
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the key points for a lying down person
key_points = [
    "head", "neck", "shoulder_left", "elbow_left", "wrist_left",
    "hip_left", "knee_left", "ankle_left", "shoulder_right",
    "elbow_right", "wrist_right", "hip_right", "knee_right",
    "ankle_right", "spine"
]

# Define initial positions of the points
initial_positions = {
    "head": np.array([0, 1]),
    "neck": np.array([0, 0.8]),
    "shoulder_left": np.array([-0.3, 0.6]),
    "elbow_left": np.array([-0.4, 0.4]),
    "wrist_left": np.array([-0.5, 0.2]),
    "hip_left": np.array([-0.2, 0.3]),
    "knee_left": np.array([-0.3, 0.1]),
    "ankle_left": np.array([-0.4, 0]),
    "shoulder_right": np.array([0.3, 0.6]),
    "elbow_right": np.array([0.4, 0.4]),
    "wrist_right": np.array([0.5, 0.2]),
    "hip_right": np.array([0.2, 0.3]),
    "knee_right": np.array([0.3, 0.1]),
    "ankle_right": np.array([0.4, 0]),
    "spine": np.array([0, 0.4])
}

# Convert initial positions to a list of arrays
positions = [initial_positions[key] for key in key_points]

# Function to update the positions of the points
def update_positions(frame):
    # Apply a small random perturbation to simulate breathing
    for i in range(len(positions)):
        positions[i] += np.random.normal(0, 0.01, 2)
    
    # Ensure the points remain within a reasonable range
    for pos in positions:
        pos[0] = np.clip(pos[0], -0.5, 0.5)
        pos[1] = np.clip(pos[1], 0, 1)

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
scat = ax.scatter([], [], s=50, color='white')

# Initialize the scatter plot
def init():
    scat.set_offsets([])
    return scat,

# Update function for the animation
def animate(frame):
    update_positions(frame)
    scat.set_offsets(positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, interval=100)

# Show the animation
plt.show()
