
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define constants
NUM_POINTS = 15
WALKING_SPEED = 0.1
BACKGROUND_COLOR = 'black'
POINT_SIZE = 5
FPS = 60

# Initialize figure and axes
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim((-1, 1)
ax.set_ylim((-1, 1))
ax.axis('off')

# Create a list of points
points = [np.random.uniform(-0.5, 0.6, size=2) for _ in range(NUM_POINTS)]
point_lights, = ax.plot(*zip(*points), 'o', color='white', markersize=POINT_SIZE)

def update(frame):
    global points
    
    # Update each point's position based on walking speed and direction
    for i, point in enumerate(points):
        dx = np.cos(np.pi * frame / FPS) * WALKING_SPEED
        dy = np.sin(np.pi * frame / FPS) * WALKING_SPEED
        points[i] += dx, dy
        
    # Wrap around the edges of the screen
    points = [(x % 1, y % 1) for x, y in points]
    
    # Update the plot
    point_lights.set_data(*zip(*points))

ani = FuncAnimation(fig, update, frames=np.arange((FPS), blit=True, interval=1000/FPS)

plt.show()
