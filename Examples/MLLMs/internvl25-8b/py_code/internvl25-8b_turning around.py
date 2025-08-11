
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Number of point lights
n_lights = 15

# Create a blank figure and axis
fig, ax = plt.subplots()

# Create an array of light positions
points = np.zeros((n_lights, 2))
# Define the initial positions in a circular formation
for i in range(n_lights):
    x = np.cos(2 * np.pi * i / n_lights)
    y = np.sin(2 * np.pi * i / n_lights)
    points[i] = [x, y]

# Define initial speeds and angles for rotation
speeds = np.linspace(0.01, 0.1, n_lights)
angles = np.linspace(0, 2 * np.pi, n_lights)

def animate(i):
    # Animation loop
    for idx in range(n_lights):
        # Update position along initial circular path
        points[idx][0] += speeds[idx] * np.cos(angles[idx])
        points[idx][1] += speeds[idx] * np.sin(angles[idx])
        
        # Ensure points are within the bounds for a more realistic motion
        points[idx][0] %= 1
        points[idx][1] %= 1
        
    # Remove previous lines and draw new ones
    lines = [ax.plot([], [], 'k.', markersize=5)[0]]
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')  # Hide axes
    ax.set_title('Man Turning Around', fontsize=15, color='gray')
    return lines

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()
