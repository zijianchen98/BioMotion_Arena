
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
fps = 24
background_color = 'black'
point_color = 'white'

# Initial positions of the lights (simplified)
initial_positions = np.array([
    [0, 0],   # Head
    [-0.5, 1], [0.5, 1],  # Shoulders
    [-1, 2], [1, 2],      # Elbows
    [-1.5, 3], [1.5, 3],  # Hands
    [0, 1],              # Hip
    [-1, 2.5], [1, 2.5],  # Knees
    [-1.5, 4], [1.5, 4],  # Feet
    [-0.5, 0.5], [0.5, 0.5], # Arms
    [0, -1]              # Tail end of spine
])

# Function to create a jumping motion
def jump_motion(t):
    x = initial_positions[:, 0]
    y = initial_positions[:, 1] + 0.5 * np.sin(2 * np.pi * t / frames) - 0.5
    return np.column_stack((x, y))

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 5)
ax.axis('off')
ax.set_facecolor(background_color)

# Initialize points
points, = ax.plot([], [], 'o', color=point_color, markersize=10)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    positions = jump_motion(i)
    points.set_data(positions[:, 0], positions[:, 1])
    return points,

ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True, interval=1000/fps)
plt.show()
