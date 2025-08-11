
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.axis('off')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

# Number of points
n_points = 15

# Initialize the positions and velocities
positions = np.random.uniform(low=-80, high=80, size=(n_points, 2))
velocities = np.zeros((n_points, 2))

# Define initial velocities for bowing motion
velocities[:, 1] = -1.0  # Downward velocity
velocities[7:12, 1] = -2.0  # Faster downward velocity for middle points (representing the torso)

# Create scatter plot for the points
scat = ax.scatter(positions[:, 0], positions[:, 1], c='white', s=40)

def update(frame_number):
    global positions, velocities
    
    # Update positions based on velocities
    positions += velocities
    
    # Keep the points within the boundaries
    positions = np.clip(positions, -100, 100)
    
    # Update the scatter plot
    scat.set_offsets(positions)
    
    # After completing the bow, reset the velocities
    if frame_number > 50:
        velocities *= 0.95  # Slow down slightly after bowing
    
    return scat,

ani = animation.FuncAnimation(fig, update, frames=100, interval=30, blit=True)

plt.show()
