
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim((-5, width)
ax.set_ylim((-height, 0))
ax.set_facecolor('black')

# Define the subject and action parameters
subject_width = 0.5
subject_height = 0.5
action = 'lying down'

# Initialize the points
points = []
for i in range(15):
    x = np.random.uniform(-width/2, width/2)
    y = np.random.uniform(-height/2, height/2)
    points.append((x, y))

def update(frame):
    global points
    for i, ( in enumerate(points):
        if action == 'lying down':
            dx = np.sin(frame * 0.1) * 0.1
            dy = np.cos(frame * 0.1) * 0.1
        else:
            raise ValueError('Invalid action')
        x, y = points[i]
        x += dx
        y += dy
        if x < -width/2 or x > width/2 or y < -height/2 or y > height/2:
            # Reset the point when it goes out of bounds
            x = np.random.uniform(-width/2, width/2)
            y = np.random.uniform(-height/2, height/2)
        points[i] = (x, y
    ax.clear()
    ax.set_xlim(-width, width)
    ax.set_ylim(-height, 0)
    ax.set_facecolor('black')
    for x, y in points:
        ax.add_patch(plt.Circle((x, y), radius=0.01, color='white'))
    return []

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), blit=True)

plt.show()

