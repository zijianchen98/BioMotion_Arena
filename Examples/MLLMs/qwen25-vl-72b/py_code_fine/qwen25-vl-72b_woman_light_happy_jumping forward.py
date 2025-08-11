
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the points based on the provided image
initial_positions = np.array([
    [0, 1], [-0.5, 0.7], [0, 0.7], [0.5, 0.7],
    [-0.7, 0.4], [-0.3, 0.4], [0.3, 0.4], [0.7, 0.4],
    [-0.8, 0.1], [-0.4, 0.1], [0, 0.1], [0.4, 0.1], [0.8, 0.1],
    [-0.3, -0.2], [0.3, -0.2]
])

# Define the target positions for jumping forward
target_positions = initial_positions + [0.5, 0]

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create the point lights
points = []
for pos in initial_positions:
    point, = ax.plot(pos[0], pos[1], 'w.', markersize=10)
    points.append(point)

def animate(frame):
    # Calculate the interpolation factor between initial and target positions
    t = frame / 100.0
    
    for i, point in enumerate(points):
        # Interpolate the position of each point
        x = initial_positions[i][0] * (1 - t) + target_positions[i][0] * t
        y = initial_positions[i][1] * (1 - t) + target_positions[i][1] * t
        
        # Update the position of the point
        point.set_data(x, y)
    
    return points

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=20, blit=True)

plt.show()
