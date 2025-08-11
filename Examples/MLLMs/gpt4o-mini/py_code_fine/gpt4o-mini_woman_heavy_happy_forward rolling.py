
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of points
num_points = 15

# Point lights initial positions (simulating joints)
points = np.array([
    [0, 1],    # Head
    [-0.5, 0.5], [0.5, 0.5],  # Shoulders
    [-0.5, 0], [0.5, 0],      # Elbows
    [-0.5, -0.5], [0.5, -0.5], # Hands
    [0, 0],    # Center of mass
    [-0.2, -1], [0.2, -1],    # Hips
    [-0.3, -1.5], [0.3, -1.5], # Knees
    [-0.4, -2], [0.4, -2],   # Feet
]) * 0.8  # Scale

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 1)
ax.axis('off')

# Initialize point lights
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Update function for animation
def update(frame):
    # Forward rolling motion simulation by updating y positions
    angle = frame * np.pi / 30  # Change overframes
    # Update point positions based on a simple forward roll
    new_points = points.copy()
    for i in range(len(new_points)):
        new_points[i, 0] += np.sin(angle + i * 0.2) * 0.1  # slight horizontal movement
        new_points[i, 1] -= 0.1  # move down
    scat.set_offsets(new_points)  # Update the scatter plot with new points
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display the animation
plt.style.use('dark_background')
plt.show()
