
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axes
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Initialize point positions
points = [
    [5, 2], [4, 3], [6, 3], [4, 4], [6, 4],
    [3, 5], [5, 5], [7, 5], [4, 6], [6, 6],
    [5, 7], [3, 8], [7, 8], [5, 8], [5, 9]
]

scat = ax.scatter([p[0] for p in points], [p[1] for p in points], color='white')

# Animation function
def update(frame):
    # Calculate vertical displacement for each point
    vert_displacement = 1.5 * np.sin(np.pi * frame / 30)

    # Adjust each point's y-coordinate
    new_points = [[p[0], p[1] + vert_displacement] for p in points]
    
    # Update scatter plot
    scat.set_offsets(new_points)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=50, blit=True)

plt.show()
