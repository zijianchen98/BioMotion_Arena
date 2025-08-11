
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 0], [10, 0], [20, 0],
    [5, 10], [10, 10], [15, 10],
    [0, 20], [5, 20], [10, 20], [15, 20], [20, 20],
    [10, 30], [15, 30],
    [5,40], [15, 40]

])


# Define a function to update the positions of the point-lights at each frame
def update(frame_num, points, data):
    points.set_data(data[frame_num, :, 0], data[frame_num, :, 1])
    return points,


# Generate the animation data (example running motion)

num_frames = 100
data = np.zeros((num_frames, 15, 2))
for i in range(num_frames):
    angle = i * 0.1  # Adjust the speed and amplitude as needed
    for j in range(15):
        x = initial_positions[j, 0] + np.sin(angle + j*0.2) * 10  # adjust parameters for realistic motion
        y = initial_positions[j, 1] + np.cos(angle + j*0.2) * 5 + i # adjust parameters for realistic motion
        data[i, j, :] = [x,y]



# Create the figure and axes
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(-20, 50), ylim=(-20, 70))  # adjust limits
ax.set_facecolor('black')

# Create the point-light scatter plot
points, = ax.plot([], [], 'wo', markersize=8)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, fargs=(points, data), interval=50, blit=True)

# Show the animation
plt.show()
