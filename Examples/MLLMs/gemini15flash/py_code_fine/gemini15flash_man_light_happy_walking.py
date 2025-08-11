
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 50], [10, 40], [20, 40], [30, 40],
    [5, 30], [15, 30], [25, 30],
    [10, 20], [20, 20],
    [10, 10], [20, 10],
    [15, 0], [0, 0], [30, 0]
])


def update(frame_num, points, data):
    # Simulate walking motion.  This is a simplified example;
    # more sophisticated motion capture data or animation techniques
    # could create a more realistic gait.
    x_offset = 2 * np.sin(frame_num * 0.1)  # Adjust frequency for walking speed
    y_offset = 0
    
    #Apply a sine wave to each point for a more complex motion
    for i in range(len(initial_positions)):
        data[i, 0] = initial_positions[i, 0] + x_offset + 5*np.sin(i*0.3 + frame_num*0.2) #add some variation to each point
        data[i, 1] = initial_positions[i, 1] + y_offset + 2*np.sin(i*0.2 + frame_num*0.1)


    points.set_data(data[:, 0], data[:, 1])
    return points,


fig = plt.figure(figsize=(5, 7)) #Maintain aspect ratio
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-20, 50), ylim=(-10, 60))
ax.set_facecolor('black')  # Set background color to black
ax.get_xaxis().set_visible(False) # Hide axes
ax.get_yaxis().set_visible(False)

# Initialize the point-lights
points, = ax.plot([], [], 'wo', markersize=8)

# Animation data
data = np.copy(initial_positions)


ani = animation.FuncAnimation(fig, update, frames=range(100), fargs=(points, data),
                              interval=50, blit=True)

plt.show()

