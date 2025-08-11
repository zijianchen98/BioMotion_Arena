
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_lights = 15

# Initial positions of the point-lights in a vertical format
initial_positions = np.array([
    [0, 1], [0.5, 2], [-0.5, 2], 
    [0, 3], [0.5, 3.5], [-0.5, 3.5],
    [0, 4], [0.5, 5], [-0.5, 5],
    [0, 6], [0.5, 6.5], [-0.5, 6.5],
    [0, 7], [0.5, 8], [-0.5, 8]
])

# Jumping motion function
def jumping_motion(frame):
    # Calculate the new positions based on the frame number
    height_offset = 0.2 * np.sin(frame * 0.4)  # Sine for smooth jumping motion
    forward_offset = frame * 0.02  # Moving forward
    new_positions = initial_positions + np.array([forward_offset, height_offset])
    
    # Update point-lights
    scat.set_offsets(new_positions)
    return scat,

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 10)
ax.set_facecolor('black')

# Create scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Create animation
ani = animation.FuncAnimation(fig, jumping_motion, frames=30, interval=100, blit=True)

# Display the animation
plt.axis('off')  # Turn off the axis
plt.show()
