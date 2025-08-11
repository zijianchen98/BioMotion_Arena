
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initialize parameters
num_lights = 15
frames = 60
sitting_down_positions = np.array([
    [0, 2], [1, 3], [-1, 3],  # head and shoulders
    [0, 1], [0.5, 2], [-0.5, 2],  # upper body
    [0, 0], [0.4, 1], [-0.4, 1],  # lower body
    [0, -1], [0.2, 0], [-0.2, 0],  # legs
    [0, -2], [0.5, -1], [-0.5, -1]  # feet
])

# Add jitter for animation effect
def animation_func(i):
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    # Apply small random movement to the lights for realism
    jitter = np.random.normal(0, 0.05, sitting_down_positions.shape)
    positions = sitting_down_positions + jitter

    ax.scatter(positions[:, 0], positions[:, 1], color='white', s=100)

# Create figure and axis
fig, ax = plt.subplots()

# Animate
ani = animation.FuncAnimation(fig, animation_func, frames=frames, interval=50, repeat=True)

# Show the animation
plt.show()
