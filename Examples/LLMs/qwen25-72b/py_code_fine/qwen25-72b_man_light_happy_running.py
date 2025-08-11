
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Number of points
num_points = 15

# Initial positions and velocities of the points
positions = np.random.uniform(-5, 5, (num_points, 2))
velocities = np.zeros((num_points, 2))

# Define the scatter plot
points = ax.scatter(positions[:, 0], positions[:, 1], color='white', s=50)

# Function to update the positions of the points
def update(frame):
    global positions, velocities
    
    # Update velocities to simulate running
    for i in range(num_points):
        if positions[i, 0] > 5 or positions[i, 0] < -5:
            velocities[i, 0] *= -1
        if positions[i, 1] > 5 or positions[i, 1] < -5:
            velocities[i, 1] *= -1
        
        # Add a small random perturbation to make the motion more natural
        velocities[i, 0] += np.random.normal(0, 0.1)
        velocities[i, 1] += np.random.normal(0, 0.1)
        
        # Apply a slight forward bias to simulate running
        velocities[i, 0] += 0.1
    
    # Update positions
    positions += velocities
    
    # Update the scatter plot
    points.set_offsets(positions)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
