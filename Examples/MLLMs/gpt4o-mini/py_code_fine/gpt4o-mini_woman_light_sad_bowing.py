
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of point-lights
num_points = 15

# Initial positions of point-lights representing a sad woman bowing
# (in a simple representation form)
initial_positions = np.array([
    [1, 2], [0, 2], [2, 2], # head
    [0.5, 1.5], [1, 1.5], [1.5, 1.5], # upper body
    [0, 1], [1, 1], [2, 1], # lower body
    [0.5, 0], [1, 0], [1.5, 0], # feet 
])

# Function to update positions for bowing motion
def update_frame(frame, scat):
    # Bowing motion effect
    # Modify y-coordinates over time
    bow_amount = np.pi / 10 * np.sin(frame / 10)
    
    # Update y-positions for a bowing effect (downward motion)
    new_positions = initial_positions.copy()
    new_positions[:, 1] -= bow_amount
    
    scat.set_offsets(new_positions)
    return scat,

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_facecolor('black')

# Create a scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=200)

# Create animation
ani = animation.FuncAnimation(fig, update_frame, frames=np.arange(0, 100), fargs=(scat,), interval=50, blit=True)

# Display the animation
plt.axis('off')  # Turn off the axis
plt.show()
