
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_POINTS = 15
WIDTH = 640
HEIGHT = 480
JUMP_HEIGHT = 100
JUMP_DISTANCE = 200
JUMP_FRAMES = 30

# Define the initial positions of points representing a standing figure
# Points positions can be arbitrary and should represent a humanoid shape
initial_positions = np.array([
    [0, 0],    # Head
    [-10, 50], [10, 50],  # Shoulders
    [-10, 20], [10, 20],  # Arms
    [-5, 0], [5, 0],      # Hands
    [0, -30],             # Body
    [-20, -60], [20, -60], # Legs
    [-15, -100], [15, -100],  # Feet
    [-10, -60], [10, -60]  # Knees
])

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-WIDTH // 2, WIDTH // 2)
ax.set_ylim(-HEIGHT // 2, HEIGHT // 2)
ax.set_facecolor('black')
points, = plt.plot([], [], 'wo', markersize=10)  # White points

def init():
    points.set_data([], [])
    return points,

def animate(frame):
    # Compute jumping motion
    if frame < JUMP_FRAMES:
        jump_y = JUMP_HEIGHT * np.sin(np.pi * frame / JUMP_FRAMES)
        jump_x = (JUMP_DISTANCE * frame / JUMP_FRAMES) - JUMP_DISTANCE / 2
        current_positions = initial_positions + np.array([jump_x, jump_y])
    else:
        current_positions = initial_positions + np.array([JUMP_DISTANCE / 2, JUMP_HEIGHT])

    points.set_data(current_positions[:, 0], current_positions[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=JUMP_FRAMES + 15, 
                              init_func=init, blit=True, interval=1000/30)

# Show the animation
plt.show()
