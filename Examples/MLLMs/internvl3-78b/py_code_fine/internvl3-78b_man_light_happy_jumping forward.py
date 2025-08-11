
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_xlim(0, 6)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Number of points
num_points = 15

# Initialize a list to store point objects
points = []
for _ in range(num_points):
    point, = ax.plot([], [], 'bo', markersize=5)
    points.append(point)

# Initial position of the points
positions = np.array([
    [3, 5], [3.2, 5.3], [2.8, 5.3], [3.4, 5.6], [2.6, 5.6], [3.3, 5.9], [2.7, 5.9],
    [3.2, 6.2], [2.8, 6.2], [3.3, 6.5], [2.7, 6.5], [3, 6.8], [3, 7.1], [3, 7.4],
    [3, 7.7]
])

velocity = np.zeros_like(positions)

# Animation update function
def animate(i):
    global positions, velocity
    
    # Update velocities and positions
    for j, pos in enumerate(positions):
        # Compute the force applied due to jumping
        if j in range(num_points - 6, num_points):
            force = np.array([0, -0.5])  # Gravity
        else:
            force = np.array([0, -0.2])  # Gravity for lower body parts
        
        # Introduce a forward jumping motion
        force += np.array([0.1, 0.0])
        
        # Basic simulation of motion using simple mechanics
        velocity[j] += force * 0.05  # Scale factor for time step
        positions[j] += velocity[j]
    
    # Ensure all points are within the visible area to avoid clipping
    positions[:, 0] = np.clip(positions[:, 0], 0, 6)
    positions[:, 1] = np.clip(positions[:, 1], 0, 10)
    
    # Update the points in the plot
    for j, point in enumerate(points):
        point.set_data(positions[j][0], positions[j][1])
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=200, interval=30, blit=True)

plt.show()
