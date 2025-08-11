
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
background_color = 'black'
point_color = 'white'

# Initial positions and velocities for the lights
np.random.seed(0)
positions = np.zeros((num_lights, 2))
velocities = np.zeros((num_lights, 2))

# Define the joints and their connections for a walking figure
joints = [
    (0, 1), (1, 2), (2, 3),  # Head, Neck, Torso
    (3, 4), (4, 5), (3, 6), (6, 7),  # Left Arm, Right Arm
    (3, 8), (8, 9), (9, 10), (8, 11), (11, 12),  # Left Leg, Right Leg
]

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor(background_color)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')

# Create scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c=point_color)

def update(frame):
    global positions, velocities
    
    # Simple harmonic motion for the torso
    t = frame / fps
    positions[3, 0] = 0.5 * np.sin(t)
    positions[3, 1] = -0.5 + 0.2 * np.cos(t)
    
    # Arms swinging
    positions[4, 0] = positions[3, 0] + 0.3 * np.cos(t + np.pi / 2)
    positions[4, 1] = positions[3, 1] + 0.3 * np.sin(t + np.pi / 2)
    positions[5, 0] = positions[4, 0] + 0.3 * np.cos(t + np.pi / 2)
    positions[5, 1] = positions[4, 1] + 0.3 * np.sin(t + np.pi / 2)
    
    positions[6, 0] = positions[3, 0] + 0.3 * np.cos(t - np.pi / 2)
    positions[6, 1] = positions[3, 1] + 0.3 * np.sin(t - np.pi / 2)
    positions[7, 0] = positions[6, 0] + 0.3 * np.cos(t - np.pi / 2)
    positions[7, 1] = positions[6, 1] + 0.3 * np.sin(t - np.pi / 2)
    
    # Legs moving
    positions[8, 0] = positions[3, 0] - 0.3 * np.cos(t)
    positions[8, 1] = positions[3, 1] - 0.3 * np.sin(t)
    positions[9, 0] = positions[8, 0] - 0.3 * np.cos(t)
    positions[9, 1] = positions[8, 1] - 0.3 * np.sin(t)
    positions[10, 0] = positions[9, 0] - 0.3 * np.cos(t)
    positions[10, 1] = positions[9, 1] - 0.3 * np.sin(t)
    
    positions[11, 0] = positions[3, 0] + 0.3 * np.cos(t)
    positions[11, 1] = positions[3, 1] - 0.3 * np.sin(t)
    positions[12, 0] = positions[11, 0] + 0.3 * np.cos(t)
    positions[12, 1] = positions[11, 1] - 0.3 * np.sin(t)
    
    # Head position
    positions[0, 0] = positions[1, 0] = positions[2, 0] = positions[3, 0]
    positions[0, 1] = positions[1, 1] = positions[2, 1] = positions[3, 1] + 0.5
    
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)
plt.show()
