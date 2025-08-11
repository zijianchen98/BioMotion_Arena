
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define initial positions for the happyman's point lights
initial_positions = np.array([
    [0.0, 0.5],  # Head
    [-0.2, 0.4], [-0.2, 0.3], [-0.2, 0.2], [-0.2, 0.1],  # Left arm
    [0.2, 0.4], [0.2, 0.3], [0.2, 0.2], [0.2, 0.1],  # Right arm
    [0.0, 0.3],  # Body
    [0.0, 0.2], [0.0, 0.1], [0.0, 0.0],  # Legs
])

# Define frames for the lying down motion
frames = 100
positions_over_time = []
amplitude = 0.05
frequency = 0.05
time = np.linspace(0, 2 * np.pi, frames)
sine_wave = amplitude * np.sin(frequency * time)

for t in time:
    offsets = np.array([0] * len(initial_positions) + [np.sin(t)] * (len(initial_positions) - 5))
    positions_over_time.append(initial_positions + offsets[:, None])

positions_over_time = np.array(positions_over_time)

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-0.5, 0.5)
ax.set_aspect('equal')
ax.axis('off')
dots, = ax.plot([], [], 'wo', markersize=10)

def init():
    dots.set_data([], [])
    return dots,

def animate(i):
    x = positions_over_time[i, :, 0]
    y = positions_over_time[i, :, 1]
    dots.set_data(x, y)
    return dots,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=frames, init_func=init, blit=True)

# Display animation
plt.show()
