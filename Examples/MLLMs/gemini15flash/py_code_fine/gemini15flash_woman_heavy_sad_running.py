
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the point lights
initial_positions = np.array([
    [0, 0],
    [1, 1],
    [2, 0],
    [1, -1],
    [0, -2],
    [-1, -1],
    [-2, 0],
    [-1, 1],
    [0.5, -3],
    [-0.5, -3],
    [1.5, -4],
    [0.5, -4],
    [-0.5, -4],
    [-1.5, -4],
    [0, -5]
])

# Define the animation parameters
num_frames = 100
dt = 0.1

# Function to update the positions of the point lights at each frame
def update(frame_num, points, data):
    # Simple animation: circular motion of lights with some individual variation
    for i in range(len(points)):
        angle = 2 * np.pi * frame_num * dt / 10 + i * 0.1  # Vary speed for individual lights
        radius = 3 + i * 0.1  #Vary Radius slightly for variation in amplitude of motion
        points[i, 0] = initial_positions[i, 0] + radius * np.cos(angle)
        points[i, 1] = initial_positions[i, 1] + radius * np.sin(angle)

    data.set_offsets(points)
    return data,

# Create the animation figure and axes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-5, 5), ylim=(-6, 6))
ax.set_facecolor('black')

# Create the point light scatter plot
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(initial_positions, points), interval=20, blit=True)

# Show the animation (or save it to a file)
plt.show()

