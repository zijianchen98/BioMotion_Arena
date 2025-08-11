
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize constants and parameters
num_points = 15
frames = 100
interval = 50  # Interval in milliseconds
black_bg = np.zeros((300, 300, 3))

# Create a figure
fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 300)
scat = ax.scatter([], [], s=50, facecolor="white")

def init():
    """Initialize the animation."""
    scat.set_offsets(np.zeros((num_points, 2)))
    return scat,

def update(frame):
    """
    Update the positions of the point-lights for each frame.
    
    frame: the current frame number.
    """
    scat.set_offsets(generate_positions(frame))
    return scat,

def generate_positions(frame):
    """
    Generate positions for the point-lights based on the frame number.
    
    frame: the current frame number.
    Returns: An array of new positions with shape (num_points, 2).
    """
    angle = 2 * np.pi * frame / frames
    positions = np.zeros((num_points, 2))
    
    # Create the positions for the happyman lying down
    positions[:7, 0] = 150 + 35 * np.cos(angle)
    positions[:7, 1] = 150 + 20 * np.sin(angle)
    
    # Create the positions for the legs
    positions[7:12, 0] = 150 - 35 * np.cos(angle)
    positions[7:12, 1] = 150 + 20 * np.sin(angle)
    
    # Create the positions for the arms
    positions[12:15, 0] = 150
    positions[12:15, 1] = 150 + 40 * np.sin(angle) 

    return positions

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, repeat=True, interval=interval)

# Display the animation
plt.show()
