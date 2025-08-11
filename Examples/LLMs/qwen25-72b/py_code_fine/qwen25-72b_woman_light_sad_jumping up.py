
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

# Initial positions and velocities
positions = np.random.uniform(-5, 5, (num_points, 2))
velocities = np.zeros((num_points, 2))

# Gravity and jump force
gravity = 0.1
jump_force = 3.0

# Points
points = [plt.Circle((positions[i][0], positions[i][1]), 0.2, color='white') for i in range(num_points)]

# Add points to the plot
for point in points:
    ax.add_patch(point)

def init():
    return points

def update(frame):
    global positions, velocities
    
    # Apply gravity
    velocities[:, 1] -= gravity
    
    # Check if any point is on the ground
    for i in range(num_points):
        if positions[i][1] <= -9.5:
            positions[i][1] = -9.5
            velocities[i][1] = jump_force * np.random.uniform(0.8, 1.2)
    
    # Update positions
    positions += velocities
    
    # Update point positions
    for i in range(num_points):
        points[i].center = (positions[i][0], positions[i][1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
