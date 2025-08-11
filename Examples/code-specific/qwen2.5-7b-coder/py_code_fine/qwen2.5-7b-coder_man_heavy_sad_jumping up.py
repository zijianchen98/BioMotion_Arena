
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FPS = 30
DURATION = 4  # seconds
TIME_STEPS = FPS * DURATION
WIDTH, HEIGHT = 800, 600

# Initial positions of the lights
np.random.seed(42)
initial_positions = np.random.rand(NUM_LIGHTS, 2) * [WIDTH, HEIGHT]

# Define the jumping motion
def jumping_motion(t):
    t_normalized = t / TIME_STEPS
    amplitude = HEIGHT / 4
    frequency = 1
    phase = np.pi / 2
    y_offset = HEIGHT / 2
    y_position = y_offset + amplitude * np.sin(frequency * t_normalized + phase)
    x_positions = np.linspace(0, WIDTH, NUM_LIGHTS)
    return np.column_stack((x_positions, y_position))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.set_facecolor('black')

# Create the scatter plot for the point-lights
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Update function for the animation
def update(frame):
    positions = jumping_motion(frame)
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(TIME_STEPS), interval=1000/FPS, blit=True)

# Show the animation
plt.show()
