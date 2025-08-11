
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
points, = ax.plot([], [], 'o', color='white')  # Plot white points

# Number of points and their initial positions
num_points = 15
point_positions = np.zeros((num_points, 2))
init_positions = [
    (5, 2), (4.5, 3), (5.5, 3), (4, 4), (6, 4), 
    (5, 5), (4, 6), (6, 6), (5, 7), (4.5, 8), 
    (5.5, 8), (5, 9), (4, 8.5), (6, 8.5), (5, 7.5)
]

# Setting initial positions
for i in range(num_points):
    point_positions[i, 0] = init_positions[i][0]
    point_positions[i, 1] = init_positions[i][1]

# Walking animation update function
def update(frame):
    # Basic parameters for motion
    delta_y = 0.1
    delta_x = 0.05 * (1 if frame % 2 == 0 else -1)  # Alternating to simulate walking
    
    # Update positions
    for i in range(num_points):
        point_positions[i, 0] += delta_x
        if i < num_points // 2:
            point_positions[i, 1] += delta_y  # Move up
        else:
            point_positions[i, 1] -= delta_y  # Move down
            
    points.set_data(point_positions[:, 0], point_positions[:, 1])
    return points,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
