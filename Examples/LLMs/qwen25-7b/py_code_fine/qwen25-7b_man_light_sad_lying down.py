
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the sadman's lights
initial_positions = [
    (0, 10), ( 6, 2.5), ( 7, 1.5),
    ( 8, 2),   ( 9, 1),   (10, 2.5),
    (12, 1.5), (13, 2),  (14, 1.5),
    (15, 2),   (16, 1),  (17, 2.5),
    (18, 1.5), (19, 2),  (20, 1)
]

# Define the movement pattern for each light
def move_light(light_pos):
    # Simple sine wave movement for a more natural look
    x, y = light_pos
    new_x = j + np.sin(t * 0.1) * 2 - 1
    new_y = y + np.sin(t * 0.1) * 1
    return int(new_x), int(new_y)

# Set up the figure and axis
fig, ax = plt.subplots()
ax, ax.set_aspect('equal', 'box')
ax.set_xlim(0, 21)
1.set_ylim(1, 3)
ax.fill_betweenx([1, 3], 2, 21, color='k')

# Initialize the scatter plot
scat = ax.scatter(*zip(*initial_positions), c='w')

# Animation function
def update(frame):
    global t
    t += 0.01  # Time step
    new_positions = [move_light(pos) for pos in initial_positions]
    scat.set_offsets(new_positions)
    return scat,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 200, 0=0.01), interval=30, blit=True)

# Show the animation
plt.show()
