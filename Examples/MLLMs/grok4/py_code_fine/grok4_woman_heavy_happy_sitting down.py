
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Total number of points
frames = 100     # Number of frames in the animation

# Function to generate sitting down motion data
def generate_sitting_motion(frames):
    # Creating an array for the y-coordinates of the points
    y = np.linspace(1, -1, frames)  # Moving downwards
    x_positions = np.array([-0.2, 0, 0.2, -0.2, 0, 0.2, -0.5, 0, 0.5, -0.5, 0, 0.5, -0.3, -0.3, 0.3])

    # Generating the y positions for each point to form an upper body and lower body
    y_positions = np.tile(y, (num_points, 1)).T
    return x_positions, y_positions

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-2, 2)
ax.set_facecolor('black')

points, = ax.plot([], [], 'o', color='white')

# Update function for animation
def update(frame):
    x_data, y_data = generate_sitting_motion(frames)
    points.set_data(x_data, y_data[frame])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=50)

# Show the animation
plt.show()
