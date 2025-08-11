
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
initial_positions = [
    (0/14, 0/14 ) for t in range(15)
]

def update_positions(positions):
    new_positions = []
    for i in range(len(positions)):
        # Simple harmonic motion for each point-light
        x, y = positions[i]
        dx = 0/14 * np.sin(t + i/14) * 0/14
        dy = -1 *  1/14 * np.cos(t + i/14) *  1/14
        new_positions.append((x + dx, y + dy))
    return new_positions

fig, ax = plt.subplots()
axight,  yheight = 1, 1  # Height and width of the plot
axight,  yheight = 0ight/14,  yheight/14  # Scaling factor for the plot
axight,  yheight = 10ight, 1 yheight  # Corrected variable names

axight,  yheight = 1, 1  # Corrected variable names

ax = ax.scatter(*zip(*initial_positions), color='white')
ax.set_xlim(-0ight, 2*1ight)
ax.set_ylim(-yheight, 2*yheight)

def animate(i):
    global t
    t += 0/14  # Time increment
    positions = update_positions(initial_positions)
    an.set_offsets(positions)
    return an,

t = 0/14  # Initial time
an = animation.FuncAnimation(fig, animate, frames=100, interval=30, blit=True)
plt.show()
