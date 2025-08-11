
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of points and number of frames
num_points = 15
frames = 100

# Create a figure
fig, ax = plt.subplots()

# Set the background color to black
ax.set_facecolor('black')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Initialize point positions
# The points represent the positions of the joints
points = np.zeros((num_points, 2))

# Define the initial positions of the points to resemble a sad woman walking
# The arrangement of points is arbitrary to represent human joints
# 0 to 4 for upper body, 5 to 9 for lower body, and 10 to 14 for feet
points[0] = [0, 0]     # Head
points[1] = [-0.2, -0.2]  # Left shoulder
points[2] = [0.2, -0.2]   # Right shoulder
points[3] = [-0.2, -0.8]  # Left hip
points[4] = [0.2, -0.8]   # Right hip
points[5] = [0, -1.0]     # Center of body
points[6] = [-0.75, -1.5]  # Left knee
points[7] = [0.75, -1.5]   # Right knee
points[8] = [-0.5, -2.0]   # Left foot
points[9] = [0.5, -2.0]    # Right foot

# Create a scatter plot
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def update(frame):
    # Simulate the walking movement
    # Adjust the y-position to create a walking effect
    for i in range(1, 10):
        points[i, 1] += np.sin((frame + i) / 10.0) * 0.01  # Simulate a bobbing motion
        
    # Create a left-right oscillation for the legs to simulate walking
    points[6, 0] -= 0.01 if frame % 20 < 10 else -0.01  # Move left knee left and right
    points[7, 0] += 0.01 if frame % 20 < 10 else -0.01  # Move right knee right and left
    
    # Foot movement
    points[8, 0] = points[6, 0]  # Left foot follows knee
    points[9, 0] = points[7, 0]  # Right foot follows knee
    
    # Update the scatter plot data
    scat.set_offsets(points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()
