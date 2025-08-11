
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of point-lights
num_points = 15

# Define the initial positions of the point-lights (skeleton of a lying down person)
initial_positions = np.array([
    [0, 2],  # head
    [-0.5, 1.5], [0.5, 1.5],  # shoulders
    [-0.75, 1], [0, 1], [0.75, 1],  # elbows
    [-0.5, 0.5], [0.5, 0.5],  # wrists
    [-0.5, 0], [0, 0], [0.5, 0],  # hips
    [-0.75, -0.5], [0.75, -0.5],  # knees
    [-0.5, -1], [0.5, -1]  # feet
])

# Define the movement for the animation (lying down motion)
motion = [
    initial_positions,
    initial_positions + [0, -0.1],  # slight downward movement
]

# Create a figure for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 3)
ax.set_facecolor('black')

# Initialize point-lights in the plot
points, = ax.plot([], [], 'o', color='white')

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to animate the point-lights
def update(frame):
    pos = motion[frame % len(motion)]
    points.set_data(pos[:, 0], pos[:, 1])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(motion), init_func=init, blit=True, interval=500)

# Show the animation
plt.show()
