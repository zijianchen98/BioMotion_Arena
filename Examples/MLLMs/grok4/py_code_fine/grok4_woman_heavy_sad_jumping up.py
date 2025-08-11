
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to define the animation of the point-lights
def update_positions(frame, points, scat):
    # Update the positions of each point
    y_jump = np.sin(2 * np.pi * (frame / 30)) * 0.5  # Vertical jump motion
    if frame < 15:  # Ascending
        points[:, 1] = base_y + y_jump
    else:  # Descending
        points[:, 1] = base_y + (1.0 - y_jump)
    
    scat.set_offsets(points)
    return scat,

# Parameters for the points
num_points = 15
base_y = np.linspace(-1, 1, num_points)  # Base y positions of points
base_x = np.zeros(num_points)  # Fixed x positions

# Create an array to hold the points' positions
points = np.vstack((base_x, base_y)).T

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=60, fargs=(points, scat),
                              interval=100, blit=True)

# Show the animation
plt.show()
