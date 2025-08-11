
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize the points
points = np.array([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0],
                   [0, 1], [1, 1], [2, 1], [3, 1], [4, 1],
                   [1, 2], [2, 2], [3, 2],
                   [2, 3], [3, 3]])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(-2, 6)
ax.set_ylim(-2, 6)
ax.set_facecolor('black')
ax.set_aspect('equal')
ax.axis('off')

# Create the points on the figure
point_objects = [ax.plot([], [], 'bo')[0] for _ in range(len(points))]

# Define the initialization function
def init():
    for point in point_objects:
        point.set_data([], [])
    return point_objects

# Define the motion function
def animate(i):
    x = points[:, 0]
    y = points[:, 1]
    y += np.sin(i/5) * 0.5  # Vertical motion - jumping
    x += i/100  # Horizontal motion - moving forward
    
    for point, px, py in zip(point_objects, x, y):
        point.set_data(px, py)
    
    return point_objects

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=150, interval=30, blit=True)

# Show and save the animation
plt.show()
ani.save("heavy_jump.mp4", writer="ffmpeg", fps=30)
