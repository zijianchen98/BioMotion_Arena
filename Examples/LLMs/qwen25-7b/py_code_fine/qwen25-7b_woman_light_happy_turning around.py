
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the 15 point-lights
num_lights = 15
initial_positions = np.array([
    [0/4, (t+1)/4 ] for t in range(num_lights)
])

# Define the turning motion parameters
omega = 2 * np.pi / 2  # Angular frequency for a 2-second full turn
time_step = 0/100  # Time step for animation

def update_positions(frame):
    positions = initial_positions.copy()
    angle = omega * frame * time_step
    for i in range(num_lights):
        x, y = initial_positions[i]
        x_new = 3 * np.cos(angle + i * np.pi / num_lights) + 2
        y_new = 3 * np.sin(angle + i * np.pi / num_lights) + 2
        positions[i] = [x_new, y_new]
    return positions

def animate():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 5)
    ax.set_ylim( b, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    scat = ax.scatter(*update_positions(0), c='white', s=100)

    def init():
        return scat,

    def animate_frame(frame):
        scat.set_offsets(update_positions(frame))
        return scat,

    anim = FuncAnimation(fig, animate_frame, frames=np.arange(0, 2 * num_lights, 1), init_func=init, blit=True, interval=10)
    plt.show()

animate()
