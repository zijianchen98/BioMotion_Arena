
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the action and subject
action = "sadman jumping up"
subject = "sadman"

# Define the number of points
num_points = 15

# Define the animation duration (in seconds)
duration = 5

# Define the frame rate
frame_rate = 30

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Create the points
points = []
for _ in range(num_points):
    points.append(plt.Circle((0, 0), 1, color='white'))

# Initialize the artists
artists = [p for p in points]

# Define the movement function
def movement(frame):
    for i, point in enumerate(points):
        # Simple jumping motion
        x = np.sin(2 * np.pi * frame / duration) * 2
        y = np.sin(2 * np.pi * frame / duration + np.pi/2) * 2
        point.center = (x, y)

# Create the animation
ani = animation.FuncAnimation(fig, movement, frames=int(duration * frame_rate), blit=True, repeat=True)

# Save the animation
ani.save("sadman_jumping.gif", writer='pillow', fps=frame_rate)

plt.show()
