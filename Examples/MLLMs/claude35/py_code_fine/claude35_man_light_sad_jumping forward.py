
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set the number of point-lights
NUM_POINT_LIGHTS = 15

# Create figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 0.5)
ax.axis('off')  # Turn off the axis as it is not needed

# Define initial positions of point-lights
positions = np.array([[0, 0], [-0.2, -0.2], [0.2, -0.2], 
                      [-0.3, -0.3], [0.3, -0.3], [0, -0.3],
                      [-0.4, -0.4], [0.4, -0.4], [0, -0.4],
                      [-0.2, -0.5], [0.2, -0.5], [0, -0.5],
                      [-0.1, -0.6], [0.1, -0.6], [0, -0.6]])

# Create scatter plot for the point-lights
points = ax.scatter(positions[:, 0], positions[:, 1], color='white')

# Function to update the scatter plot
def update(frame):
    global positions
    # Move points upward and a little forward
    positions[:, 1] += 0.01  # Move up
    if frame < 30:  # Initial jump
        positions[:, 0] += 0.02 * np.sin(np.linspace(0, np.pi, NUM_POINT_LIGHTS))  # Move slightly side to side
    elif 30 <= frame < 60:  # Descent
        positions[:, 1] -= 0.01  # Move down
    points.set_offsets(positions)  # Update the scatter plot
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Display animation
plt.show()
