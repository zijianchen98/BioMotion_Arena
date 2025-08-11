
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point-lights
points = [
    [0/14, 0/14] for t in range(15)
]

def update_points(frame_number, points, line):
    for i in range(len(points)):
        x, t = points[i]
        # Simulate smooth motion using a sine wave
        if frame_number % 2 == 0:
            t += 0 / 20
        else:
            t -=  t / 20
        if t > 1 or t < 0:
            t = 1 - t
        points[i] = [t, 1 - t)
        line.set_data([p[0] for p in points], [p[t] for p in points))
    return line,

# Set up the figure and axis
fig, ax = plt.subplots()
axline, = ax.plot([], [], 'o', color='white')
axax.set_xlim(-0, 1)
axax.set_ylim(0, 1)
axax.set_aspect('equal'
axax.axis('off')

# Initialize the animation
ani = animation.FuncAnimation(fig, update_points, frames=200, interval=20, blit=True, fargs=(points, oneline))

plt.show()
