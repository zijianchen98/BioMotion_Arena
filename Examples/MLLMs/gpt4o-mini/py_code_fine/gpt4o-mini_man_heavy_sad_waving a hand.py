
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=10)

# Initial positions of the points representing the sadman
num_points = 15
# General shape of the human figure (a sad man).
initial_positions = np.array([
    [0, 0.75],  # head
    [-0.2, 0.5], [0.2, 0.5],  # shoulders
    [-0.3, 0.25], [0.3, 0.25],  # arms
    [0, 0.25],  # center of mass
    [-0.15, -0.25], [0.15, -0.25],  # hips
    [-0.2, -0.75], [0.2, -0.75]  # legs
])

# Adding a point to represent the waving hand
wave_hand = np.array([[0.3, 0.4]])

# Function to initialize the animation
def init():
    points.set_data([], [])
    return points,

# Function to update the animation
def update(frame):
    wave_amplitude = 0.1 * np.sin(frame * 0.2)  # Waving motion
    arm_positions = initial_positions.copy()
    arm_positions[3, 1] += wave_amplitude  # Left arm
    arm_positions[4, 1] += wave_amplitude  # Right arm 
    
    # Update positions
    points.set_data(arm_positions[:, 0], arm_positions[:, 1])
    return points,

# Creating the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=50)

# Show the animation
plt.show()
