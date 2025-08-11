
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 180
fps = 30

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6), facecolor='black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axis('off')

# Initial positions of the point lights
positions = np.zeros((num_lights, 2))

# Angles for the joints in radians
angles = np.array([np.pi/4, np.pi/2, 3*np.pi/4, -np.pi/4, -np.pi/2, -3*np.pi/4,
                   np.pi/4, np.pi/2, 3*np.pi/4, -np.pi/4, -np.pi/2, -3*np.pi/4,
                   np.pi/2, -np.pi/2, 0])

# Radii for the joints
radii = np.array([0.3, 0.2, 0.1, 0.3, 0.2, 0.1,
                  0.3, 0.2, 0.1, 0.3, 0.2, 0.1,
                  0.2, 0.2, 0.1])

# Scatter plot for the point lights
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

def update(frame):
    # Update angles for a turning motion
    angle_offset = frame * (2 * np.pi / frames)
    updated_angles = angles + angle_offset
    
    # Calculate new positions based on updated angles and radii
    x_positions = radii * np.cos(updated_angles)
    y_positions = radii * np.sin(updated_angles)
    
    # Adjust positions to simulate 'sad woman turning around'
    x_positions[0:6] += 0.1 * np.cos(angle_offset)  # Head and shoulders
    y_positions[0:6] -= 0.1 * np.sin(angle_offset)  # Head and shoulders
    x_positions[6:12] -= 0.1 * np.cos(angle_offset)  # Hips and legs
    y_positions[6:12] += 0.1 * np.sin(angle_offset)  # Hips and legs
    
    # Update scatter plot
    scat.set_offsets(np.c_[x_positions, y_positions])
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=1000/fps, blit=True)

# Show animation
plt.show()
