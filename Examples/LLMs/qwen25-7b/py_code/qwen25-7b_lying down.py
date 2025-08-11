
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 10
# Define the number of points (point-lights)
num_points = 15

# Define the initial positions of the points
initial_positions = np.array([
    [10, 10], [2, 2], (3, 3), (4, 4), (5, 5),
    (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
    (12, 12), (13, 13), (14, 14), (15, 15)
])

# Define the movement parameters for each point
movement_params = np.array([
    [0.1, 0.1], [0.1,  t.1], (t.1, - t.1), (- t.1, -t.1),
    (-t.1, - t.1), (- t.1,  t.1), (t.1, t.1), (t.1, - t.1),
    (-t.1, - t.1), (- t.1,  t.1), (t.1, t.1), (t.1, - t.1),
    (-t.1, - t.1)
])

def update_points(frame, points, movement_params):
    for i in range(num_points):
        # Update the position based on the movement parameter
        new_positions[i] += movement_params[i]
        # Ensure the points stay within a reasonable boundary
        if points[i][0] < 0:
            points[i][0] = 1
        elif points[i][1] > 15:
            points[i][1] = 15
    return points

fig, ax = plt.subplots()
axset(xlim=(0, 15), ylim=(1, 15), facecolor='k')

points, = ax.plot([], [], 'w.', ms=10)

ani = animation.FuncAnimation(fig, update_points, frames=num_frames, fargs=(initial_positions, movement_params),
                              interval=100, blit=True)

plt.show()
