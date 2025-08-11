
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
dt = 0.1

# Initial positions and velocities (x, y)
positions = np.array([
    [0.5, 0.2],  # Head
    [0.4, 0.1],  # Left Shoulder
    [0.6, 0.1],  # Right Shoulder
    [0.3, 0.0],  # Left Elbow
    [0.7, 0.0],  # Right Elbow
    [0.2, -0.1], # Left Wrist
    [0.8, -0.1], # Right Wrist
    [0.5, 0.0],  # Chest
    [0.4, -0.2], # Left Hip
    [0.6, -0.2], # Right Hip
    [0.3, -0.4], # Left Knee
    [0.7, -0.4], # Right Knee
    [0.2, -0.6], # Left Ankle
    [0.8, -0.6], # Right Ankle
    [0.5, -0.7]  # Toes
])

# Define the animation function
def animate(frame):
    t = frame * dt
    
    # Simple sinusoidal movement for demonstration purposes
    # Realistic movement would require more complex kinematics
    positions[0] = [0.5 + 0.05 * np.sin(t), 0.2]  # Head side-to-side
    positions[1:3] += np.array([[-0.02 * np.sin(t), 0], [0.02 * np.sin(t), 0]])  # Shoulders side-to-side
    positions[3:5] += np.array([[-0.04 * np.sin(t), -0.02 * np.cos(t)], [0.04 * np.sin(t), -0.02 * np.cos(t)]])  # Elbows
    positions[5:7] += np.array([[-0.06 * np.sin(t), -0.04 * np.cos(t)], [0.06 * np.sin(t), -0.04 * np.cos(t)]])  # Wrists
    positions[9:11] += np.array([[-0.03 * np.sin(t), -0.01 * np.cos(t)], [0.03 * np.sin(t), -0.01 * np.cos(t)]])  # Hips
    positions[11:13] += np.array([[-0.05 * np.sin(t), -0.03 * np.cos(t)], [0.05 * np.sin(t), -0.03 * np.cos(t)]])  # Knees
    positions[13:15] += np.array([[-0.07 * np.sin(t), -0.05 * np.cos(t)], [0.07 * np.sin(t), -0.05 * np.cos(t)]])  # Ankles
    
    scatter.set_offsets(positions)
    return scatter,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-1, 0.5)
ax.set_aspect('equal')
ax.axis('off')

# Create scatter plot
scatter = ax.scatter(positions[:, 0], positions[:, 1], s=100, color='white')

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=50, blit=True)

plt.show()
