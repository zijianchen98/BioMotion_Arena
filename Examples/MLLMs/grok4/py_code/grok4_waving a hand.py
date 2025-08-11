
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and the axis
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_facecolor('black')

# Define the number of points (joints)
num_points = 15
points = np.zeros((num_points, 2))

# Initial positions of the points (skeleton structure)
# Head, shoulders, elbows, hands, hips, knees, feet
points[0] = [0, 1]   # Head
points[1] = [0, 0.5] # Neck
points[2] = [-0.5, 0] # Left shoulder
points[3] = [-0.8, 0.2] # Left hand
points[4] = [0.5, 0] # Right shoulder
points[5] = [0.8, 0.2] # Right hand
points[6] = [-0.5, -0.5] # Left hip
points[7] = [-0.5, -1] # Left knee
points[8] = [-0.5, -1.5] # Left foot
points[9] = [0.5, -0.5] # Right hip
points[10] = [0.5, -1] # Right knee
points[11] = [0.5, -1.5] # Right foot
points[12] = [0, 0] # Body Center
points[13] = [0, -0.5] # Body Lower
points[14] = [0, -1] # Body Additional

# Create a scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

# Animation function
def animate(frame):
    # Modify points to simulate waving
    points[3][1] = 0.2 * np.sin(frame / 10)  # Left hand
    points[5][1] = 0.2 * np.cos(frame / 10)  # Right hand
    
    # Update scatter plot
    scat.set_offsets(points)
    return scat,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50, blit=True)

# Show the animation
plt.axis('off')
plt.show()
