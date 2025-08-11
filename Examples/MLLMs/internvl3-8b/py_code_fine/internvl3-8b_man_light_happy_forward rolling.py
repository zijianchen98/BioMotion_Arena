
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 points
positions = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), 
             (5, 9), (6, 8), (7, 7), (8, 6), (9, 5), 
             (10, 4), (11, 3), (12, 2), (13, 1), (14, 0)]
# Define the initial light position
points = [(np.array(pos), 'lightweight') for pos in positions]

def update(frame, points):
    for i, p in enumerate(points):
        # Update the position to simulate rolling movement
        # For this example, we use sinusoidal movement.
        x = 2 * np.pi * (frame / frame_limit) + i
        y = np.sin(x) + 1
        points[i] = (np.array([x, y]), 'lightweight')
    return points

fig, ax = plt.subplots()
scatter = ax.scatter(*zip(*points))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_facecolor('black')

frame_limit = (fps * duration_of_animation)  # where fps is frames per second, duration_of_animation is the animation duration in seconds
interval = 1000/fps  # interval is the delay for updating frames, in milliseconds

ani = animation.FuncAnimation(fig, update, fargs=(points,), frames=frame_limit, interval=interval, blit=True)

plt.show()
