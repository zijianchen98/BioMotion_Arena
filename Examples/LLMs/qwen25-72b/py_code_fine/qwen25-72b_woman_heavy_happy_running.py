
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points for a running woman with heavy weight
# These points are simplified and may need to be adjusted for more realism
points = np.array([
    [0, 0],  # Head
    [-1, -1], [1, -1],  # Shoulders
    [-1.5, -2], [1.5, -2],  # Elbows
    [-2, -3], [2, -3],  # Hands
    [0, -2],  # Waist
    [-1, -4], [1, -4],  # Hips
    [-1.5, -6], [1.5, -6],  # Knees
    [-2, -8], [2, -8]  # Feet
])

# Function to update the position of the points
def update(num, points, scat):
    # Simulate running motion
    angle = num / 10
    new_points = points.copy()
    
    # Head bobbing
    new_points[0, 1] += 0.5 * np.sin(angle)
    
    # Shoulder movement
    new_points[1, 1] += 0.5 * np.sin(angle + np.pi)
    new_points[2, 1] += 0.5 * np.sin(angle)
    
    # Elbow and hand movement
    new_points[3, 1] += 1.5 * np.sin(angle + np.pi)
    new_points[4, 1] += 1.5 * np.sin(angle)
    new_points[5, 1] += 2 * np.sin(angle + np.pi)
    new_points[6, 1] += 2 * np.sin(angle)
    
    # Hip movement
    new_points[8, 1] += 0.5 * np.sin(angle + np.pi)
    new_points[9, 1] += 0.5 * np.sin(angle)
    
    # Knee and foot movement
    new_points[10, 1] += 2 * np.sin(angle + np.pi)
    new_points[11, 1] += 2 * np.sin(angle)
    new_points[12, 1] += 3 * np.sin(angle + np.pi)
    new_points[13, 1] += 3 * np.sin(angle)
    
    scat.set_offsets(new_points)
    return scat,

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-9, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')
scat = ax.scatter(points[:, 0], points[:, 1], color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(points, scat), interval=50, blit=True)

plt.show()
