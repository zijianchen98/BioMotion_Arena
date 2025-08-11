
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define figure and axis
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initial position of points
points = np.array([
    [5, 6], [4, 7], [6, 7], [3.5, 7.5], [6.5, 7.5], 
    [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], 
    [3, 9], [7, 9], [3.5, 8.5], [6.5, 8.5], [5, 9.5]
])

# Create point objects
dots, = ax.plot(points[:, 0], points[:, 1], 'wo', markersize=10)

def init():
    dots.set_data(points[:, 0], points[:, 1])
    return dots,

def animate(frame):
    global points
    amplitude = 0.5
    frequency = 0.15
    phase = frame * frequency

    # Update position of each point
    for i in range(len(points)):
        points[i, 1] = 5 + amplitude * np.sin(points[i, 0] * frequency + phase)
    
    dots.set_data(points[:, 0], points[:, 1])
    return dots,

# Animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.show()
