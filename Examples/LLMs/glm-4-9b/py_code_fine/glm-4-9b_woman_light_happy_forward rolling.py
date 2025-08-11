
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
duration = 10  # seconds
fps = 30
background_color = 'black'

# Define the motion parameters for a rolling motion
def rolling_position(t, amplitude=1.0, frequency=1.0, phase=0.0):
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    y = amplitude * np.cos(2 * np.pi * frequency * t + phase)
    return x, y

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10), facecolor=background_color)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.axis('off')
ax.set_facecolor(background_color)

# Create scatter plot for the point-lights
scatter = ax.scatter([], [], s=50, color='white')

# Animation update function
def update(frame):
    t = frame / fps
    positions = np.array([rolling_position(t + i / num_points * 2 * np.pi) for i in range(num_points)])
    scatter.set_offsets(positions)
    return scatter,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True)

plt.show()
