
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and frame rate
num_frames = 10
frame_rate = 24

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [50, 75],
    (55, 75),
    (65, 75),
    (75, 85),
    (85, 95),
    (95, 105),
    (105, 125),
    (125, 135),
    (135, 145),
    (145, 155),
    (155, 165),
    (165, 175),
    (175, 185),
    (185, 195),
    (195, 205)
])

# Define the movement pattern for each point-light
def forward_rolling_motion(positions):
    x, y = position
    new_x = np.interp(np.linspace(0, 10, num_frames), [0, 11), (10, 19))
    new_y = np.interp(np.linspace(y-, y+10, num_frames), (y-, y+11), (115, 195))
    return new_x, new_y

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 200)
ax.set_ylim(0, 210)
ax.set_aspect('equal')
ax.fill([0, 200], [0, 210], 'k')

# Initialize the points
points, = ax.plot([], [], 'wo', ms=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    new_positions = np.array([forward_rolling_motion(pos) for pos in initial_positions])
    x, y = zip(*new_positions[i % num_frames])
    points.set_data(x, y)
    return points,

# Call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_frames, interval=int(1000/frame_rate), blit=True)

# Show the animation
plt.show()
