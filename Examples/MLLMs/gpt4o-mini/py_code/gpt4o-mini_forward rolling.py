
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and the dimensions of the animation
num_points = 15
width, height = 10, 10

# Initial positions of the point-lights representing a man rolling forward
# These coordinates are set to mimic a forward roll motion
initial_positions = np.array([
    [5, 9],  # head
    [4, 8], [5, 8], [6, 8],  # shoulders
    [3, 7], [4, 7], [5, 7], [6, 7], [7, 7],  # torso
    [3, 6], [4, 6], [5, 6], [6, 6], [7, 6],  # hips
    [4, 5], [5, 5]  # legs
])

# Create a black figure
fig, ax = plt.subplots()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_facecolor('black')

# Create scatter plot for point-lights
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white')

# Define the update function for the animation
def update(frame):
    # Update the y-coordinate to create a rolling effect
    rolling_distance = np.sin(frame * np.pi / 15) * 0.5  # Simulate rolling motion
    new_positions = initial_positions.copy()
    new_positions[:, 1] -= rolling_distance
    
    # Simulate forward motion
    forward_distance = np.linspace(-0.1, 0.1, num_points)  # A subtle forward motion
    new_positions[:, 0] += forward_distance
    
    # Reset positions that go off-screen to simulate continuous rolling
    new_positions[np.where(new_positions[:, 1] < 0)[0], 1] += height
    new_positions[np.where(new_positions[:, 0] > width)[0], 0] -= width

    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.show()
