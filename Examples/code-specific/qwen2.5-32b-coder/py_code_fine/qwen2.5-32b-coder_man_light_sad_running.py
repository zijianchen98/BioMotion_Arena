
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames for the animation
num_frames = 100

# Define the number of point lights
num_lights = 15

# Define the initial positions of the point lights (simplified model)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.1, -0.2], [-0.2, -0.4], [-0.1, -0.6], # Left arm
    [0.1, -0.2], [0.2, -0.4], [0.1, -0.6],  # Right arm
    [0, -0.8],  # Torso
    [-0.1, -1.0], [-0.2, -1.2],              # Left leg
    [0.1, -1.0], [0.2, -1.2],               # Right leg
    [0, -1.4],  # Ground contact
])

# Define the function to update the positions of the point lights
def update(frame):
    t = frame / num_frames * 2 * np.pi  # Time variable for sinusoidal motion
    # Update positions with a simple running gait model
    positions = initial_positions.copy()
    # Arms swinging
    positions[1:4, 1] += 0.1 * np.sin(t + np.pi/2)
    positions[4:7, 1] += 0.1 * np.sin(t)
    # Legs swinging
    positions[8:10, 1] += 0.1 * np.sin(t)
    positions[10:12, 1] += 0.1 * np.sin(t + np.pi/2)
    # Forward motion
    positions[:, 0] += 0.01 * frame
    
    # Clear the previous points
    sc.set_offsets(positions)
    return sc,

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-2, 0.5)
ax.axis('off')  # Turn off the axis

# Create scatter plot for the point lights
sc = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=100, c='white')

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
