
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuration
num_points = 15
frames = 100
time_interval = 50  # milliseconds

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

# Generate initial positions (skeleton configuration)
# 5 points for head, 6 for upper body, 4 for legs
points = np.array([
    [0, 1],  # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],  # Elbows
    [0, -1],  # Torso
    [-0.5, -1.5], [0.5, -1.5],  # Hips
    [-0.3, -2], [0.3, -2],  # Knees
    [-0.8, -2.5], [0.8, -2.5],  # Feet
    [-0.3, -2], [0.3, -2]  # Align the feet points
])

# Initialize scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Simulating running motion by modifying y-coordinates and x positions
    y_offset = np.sin(frame / 10) * 0.1  # Vertical oscillation
    x_offset = (frame / frames) * 2 - 1  # Horizontal movement
    
    # Update point positions for animation
    points[:, 0] += 0.02  # Move forward
    points[:, 1] += y_offset

    # Reset points when moving out of bounds (simulation of running)
    if points[0, 0] > 2:
        points[:, 0] = -2  # Reset position to the left
    
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=time_interval, blit=True)

# Show the animation
plt.axis('off')  # Turn off axis
plt.show()
