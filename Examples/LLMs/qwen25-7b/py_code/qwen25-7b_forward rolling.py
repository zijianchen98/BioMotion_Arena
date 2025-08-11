
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the number of frames for the animation
num_frames = 10
# Define the duration of the animation in seconds
duration = 5

# Define the time interval for each frame
frame_duration = duration / num_frames

# Define the initial position of the point-lights
initial_positions = [
    [0, 7], [6, 8], [7, 9], [8, 10], (9, 10],
    [10, 14], (11, 13], (12, 12], (13, 11], (14, 10],
    (15, 10], (16, 11], (17, 10], (18, 11], (19, 10]
]

# Define the positions of the point-lights during the roll
positions = []
for t in np.linspace(0, 10, num_frames):
    new_positions = [
        [t * 10 + (1 - t) * x, 7], 
        [t * 10 + (1 - t) *6, 8], 
        [t * 11 + (1 - t) *7, 9], 
        [t * 12 + (1 - t) *8, 10], 
        [t * 13 + (1 - t) *9, 11], 
        [t * 14 + (1 - t) *10, 12], 
        [t * 15 + (1 - t) *11, 11], 
        [t * 16 + (1 - t) *12, 11], 
        (t * 17 + (1 - t) *13, 11], 
        (t * 18 + (1 - t) *14, 11], 
        (t * 19 + (1 - t) *15, 11], 
        (t * 20 + (1 - t) *16, 11], 
        (t * 22 + (1 - t) *17, 11], 
        (t * 23 + (1 - t) *18, 11], 
        (t * 24 + (1 - t) *19, 11]
    ]
    positions.append(new_positions)

# Create the figure and axis
fig, ax = plt.subplots()
ax ax.set_xlim(-5, 25)
ax ax.set_ylim(0, 25)
ax ax.set_aspect('equal')
ax ax.set_facecolor('k')

# Initialize the scatter plot
scatter = ax.scatter([], [], c='w', s=100)

def update(frame):
    scatter.set_offsets(positions[frame])
    return scatter,

# Create the animation
animation = FuncAnimation(fig, update, frames=num_frames, blit=True, interval=frame_duration*1000)

# Show the animation
plt.show()
