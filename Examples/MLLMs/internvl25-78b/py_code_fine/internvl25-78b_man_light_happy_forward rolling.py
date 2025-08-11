
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')

# Create a list to hold the point lights
points = [ax.plot([], [], 'wo', ms=8)[0] for _ in range(15)]

# Initialize function to set up the plot
def init():
    for point in points:
        point.set_data([], [])
    return points

# Animation frames
def animate(frame):
    t = frame / 100.0
    # Define point positions
    positions = [
        (0.5, 0.5 + 0.2 * np.sin(2 * np.pi * t)),  # head
        (0.48, 0.55 + 0.2 * np.sin(2 * np.pi * t + np.pi/4)),  # neck
        (0.45, 0.6 + 0.2 * np.sin(2 * np.pi * t + np.pi/2)),  # upper body
        (0.4, 0.65 + 0.2 * np.sin(2 * np.pi * t + np.pi)),  # lower body
        (0.35, 0.7 + 0.2 * np.sin(2 * np.pi * t + 3 * np.pi/4)),  # upper leg
        (0.3, 0.75 + 0.2 * np.sin(2 * np.pi * t)),  # lower leg
        (0.25, 0.8 + 0.2 * np.sin(2 * np.pi * t + np.pi/4)),  # foot
        (0.55, 0.6 + 0.2 * np.sin(2 * np.pi * t + np.pi/2)),  # upper body other side
        (0.6, 0.65 + 0.2 * np.sin(2 * np.pi * t + np.pi)),  # lower body other side
        (0.65, 0.7 + 0.2 * np.sin(2 * np.pi * t + 3 * np.pi/4)),  # upper leg other side
        (0.7, 0.75 + 0.2 * np.sin(2 * np.pi * t)),  # lower leg other side
        (0.75, 0.8 + 0.2 * np.sin(2 * np.pi * t + np.pi/4)),  # foot other side
        (0.48, 0.5),  # shoulder center
        (0.45, 0.55),  # shoulder left
        (0.55, 0.55)  # shoulder right
    ]
    
    for i, point in enumerate(points):
        point.set_data(*positions[i])
    
    return points

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True, interval=50)

plt.show()
