
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need more frames for a smooth animation
# and to accurately depict a happy man turning around with heavy weight.
# The structure below represents [frame][point_light][x, y]
point_light_positions = [
    # Frame 0
    [
        [50, 180], [60, 170], [70, 180],  # Head
        [40, 150], [60, 150],              # Shoulders
        [30, 120], [70, 120],              # Elbows
        [20, 90], [80, 90],               # Hands
        [45, 100], [55, 100],             # Hips - weighted down a little lower than normal
        [40, 70], [60, 70],              # Knees
        [35, 40], [65, 40],               # Feet
    ],
    # Frame 1 (Slightly rotated)
    [
        [55, 180], [65, 170], [75, 180],  # Head
        [45, 150], [65, 150],               # Shoulders
        [35, 120], [75, 120],               # Elbows
        [25, 90], [85, 90],               # Hands
        [50, 100], [60, 100],             # Hips
        [45, 70], [65, 70],              # Knees
        [40, 40], [70, 40],              # Feet
    ],

     # Frame 2 (More rotated)
    [
         [60, 180], [70, 170], [80, 180], # Head
         [50, 150], [70, 150],            # Shoulders
         [40, 120], [80, 120],             # Elbows
         [30, 90], [90, 90],              # Hands
         [55, 100], [65, 100],             # Hips
         [50, 70], [70, 70],              # Knees
         [45, 40], [75, 40],               # Feet
     ]

]




# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 200)
ax.set_aspect('equal')  # Ensure correct aspect ratio
ax.set_facecolor('black') # Set background to black
scat = ax.scatter([], [], s=20, c='white')  # Initialize scatter plot


def animate(i):
    positions = np.array(point_light_positions[i % len(point_light_positions)]) #Loop through frames
    scat.set_offsets(positions)
    return scat,

ani = animation.FuncAnimation(fig, animate, frames=len(point_light_positions), interval=200, blit=True)

plt.show()

