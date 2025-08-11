
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points
points = np.array([
    [0.5, 0.4], [0.6, 0.4], [0.7, 0.4], # Head
    [0.5, 0.5], [0.6, 0.5], [0.7, 0.5], # Shoulders
    [0.4, 0.6], [0.8, 0.6],             # Arms
    [0.5, 0.7], [0.7, 0.7],             # Body
    [0.4, 0.8], [0.8, 0.8],             # Hands
    [0.5, 0.9], [0.7, 0.9],             # Legs
    [0.4, 1.0], [0.8, 1.0]              # Feet
])

# Define the wave motion for the right hand
def wave_motion(t):
    amplitude = 0.1
    frequency = 1
    return amplitude * np.sin(2 * np.pi * frequency * t)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scat = ax.scatter(points[:, 0], points[:, 1], color='white')

def animate(i):
    global points
    t = i / 60  # Assuming 60 frames per second
    points[10][0] += wave_motion(t)  # Update x position of the right hand
    scat.set_offsets(points)

ani = animation.FuncAnimation(fig, animate, interval=16, blit=False)
plt.show()
