
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points
num_points = 15

# Initialize positions of the points in a random manner
positions = np.random.rand(num_points, 2)

# Function to update the positions of the points
def update_positions(pos):
    return positions

# Figure and axis setup
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Initialize the scatter plot
scat = ax.scatter(positions[:, 0], positions[:, 1], s=100, c='white')

# Function to animate the positions
def animate(i):
    # Update positions to simulate running motion
    for j in range(num_points):
        positions[j, 0], positions[j, 1] = update_positions(positions[j])

    # Update the scatter
    scat.set_offsets(positions)
    return scat,

# Run the animation
ani = animation.FuncAnimation(fig, animate, blit=True, interval=30, save_count=50)
plt.show()

