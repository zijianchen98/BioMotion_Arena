
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Define the animation parameters
frame_rate = 30  # Frames per second
duration = 1  # Duration of the animation in seconds

# Define the position of the points
points = np.zeros((num_points, 2))
for i in range(num_points):
    points[i, 0] = np.random.uniform(0, 1)
    points[i, 1] = np.random.uniform(0, 1)

# Define the movement parameters
movement_speed = 0.05  # Speed of the movement
movement_direction = np.array([0, 1])  # Direction of movement

# Create the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create the points
points_data = ax.scatter(points[:, 0], points[:, 1], s=10, c='white', marker='o')

# Define the function to update the animation
def animate(i):
    global points
    # Update the position of the points
    for j in range(num_points):
        points[j, 0] += movement_direction[0] * movement_speed * (i / duration)
        points[j, 1] += movement_direction[1] * movement_speed * (i / duration)
    
    # Update the points on the plot
    points_data.set_offsets(points)
    return points_data

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=int(duration * frame_rate), interval=1000 / frame_rate, blit=True)

# Show the animation
plt.show()
