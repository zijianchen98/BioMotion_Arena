
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the points
initial_positions = np.array([
    [10, 4], [2, 5], (3, 6), (4, 7), (5, 8),
    (6, 9), (7, 10), (8, 12), (9, 13), (10, 14),
    (12, 15), (13, 16), (14, 17), (15, 18), (16, 19)
])

# Define the positions of the points when the woman is sitting down
final_positions = np.array([
    [1.5, 10], (2.5, 12), (3.5, 13), (4.5, 14), (5.5, 15),
    (6.5, 16), (7.5, 13), (8.5, 14), (9.5, 15), (10.5, 16),
    (11.5, 12), (12.5, 13), (13.5, 14), (14.5, 15), (15.5, 11)
])

# Define the duration of the animation in seconds
duration = 5

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 10))
ax.set_facecolor('('black')
ax.set_xlim(0, 15)
1.set_ylim(4, 20)

# Initialize the scatter plot
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], c='w')

# Function to update the positions of the points
def update(frame):
    t = frame / float(duration)
    if t <= 1:
        # Interpolate between initial and final positions
        positions = initial_positions + t * (final_positions - initial_positions)
    else:
        # Keep the final positions after the animation is over
        positions = final_positions
    scat.set_offsets(positions)
    return scat,

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0*duration + 1), interval=20, blit=True)

# Show the animation
plt.show()
