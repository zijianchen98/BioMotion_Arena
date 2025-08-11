
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 15 points that make up the human body
# Each point is represented as a tuple (x, y)
points = [
    (0, 0),  # Head
    (-1, 2), (-1, 4), (1, 2), (1, 4),  # Left and right shoulders, elbows
    (-2, 6), (-2, 8), (2, 6), (2, 8),  # Left and right hands, wrists
    (0, 2), (0, 4),  # Torso
    (-1, 6), (1, 6),  # Left and right hips
    (-2, 10), (2, 10)  # Left and right feet
]

# Define the animation frames
# Each frame is represented as a list of 15 points
frames = []
for i in range(100):
    frame = []
    # Move the points to simulate the jumping motion
    for point in points:
        x, y = point
        # Head
        if point == (0, 0):
            frame.append((x, y + i / 10))
        # Shoulders and elbows
        elif point in [(-1, 2), (-1, 4), (1, 2), (1, 4)]:
            frame.append((x, y + i / 10 + np.sin(i / 10) * 0.5))
        # Hands and wrists
        elif point in [(-2, 6), (-2, 8), (2, 6), (2, 8)]:
            frame.append((x, y + i / 10 + np.sin(i / 10) * 1.0))
        # Torso
        elif point in [(0, 2), (0, 4)]:
            frame.append((x, y + i / 10 + np.sin(i / 10) * 0.2))
        # Hips
        elif point in [(-1, 6), (1, 6)]:
            frame.append((x, y + i / 10 + np.sin(i / 10) * 0.8))
        # Feet
        elif point in [(-2, 10), (2, 10)]:
            frame.append((x, y + i / 10 + np.sin(i / 10) * 1.5))
    frames.append(frame)

# Create a new figure
fig, ax = plt.subplots()

# Initialize the plot with the first frame
points_x, points_y = zip(*frames[0])
ax.scatter(points_x, points_y, c='white', s=50)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 15)
ax.set_facecolor('black')
ax.set_aspect('equal')

# Animation function
def animate(i):
    ax.clear()
    points_x, points_y = zip(*frames[i])
    ax.scatter(points_x, points_y, c='white', s=50)
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 15)
    ax.set_facecolor('black')
    ax.set_aspect('equal')

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=len(frames), interval=50)

plt.show()
