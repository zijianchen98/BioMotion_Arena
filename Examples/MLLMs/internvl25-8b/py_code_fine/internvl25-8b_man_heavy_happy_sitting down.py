
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of points and the frame rate
num_points = 15
frame_rate = 15

# Create a figure and axis with a black background
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('black')

# Initialize the list of points
points = []

# Define the initial positions of the points
initial_positions = [
    (5, 10), (6, 8), (7, 7), (8, 8), (9, 10),
    (4, 10), (3, 8), (2, 7), (1, 8), (0, 10),
    (6, 4), (7, 5), (8, 6), (9, 5), (10, 4)
]

# Create the points
for pos in initial_positions:
    points.append(ax.scatter(*pos, color='white', s=50))

# Function to update the positions of the points for each frame
def update(frame):
    # Calculate the new positions of the points
    new_positions = []
    for i, point in enumerate(points):
        dx = np.sin(np.pi * frame / frame_rate)
        dy = np.cos(np.pi * frame / frame_rate)
        new_pos = (
            initial_positions[i][0] + dx * 2,
            initial_positions[i][1] + dy * 2
        )
        new_positions.append(new_pos)
    
    # Update the points' positions
    for i, (pos, point) in enumerate(zip(new_positions, points)):
        point.set_offsets((pos,))

# Create the animation
animation = FuncAnimation(fig, update, frames=range(0, 100, 2), interval=1000 / frame_rate)

# Save the animation to a file
animation.save("point_light_sitting_down.mp4", writer='ffmpeg', fps=frame_rate)

# Display the animation
plt.show()
