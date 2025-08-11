
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_axis_off()

def update_positions(i):
    positions = np.vstack([1.0 * np.sin(2.0 * np.pi * (i / 30.0)), 1.0 * np.sin(3.0 * np.pi * (i / 30.0))])
    for idx in range(positions.shape[1]):
        ax.set_title("Jumping")
        ax.plot(positions[0], positions[1], 'o', color='w', markersize=16)
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_axis_off()
    return []

positions = np.zeros((2, 15))
positions[0, :] = 1.0 * np.sin(2.0 * np.pi * (np.arange(15) / 30.0)) * 0.05
positions[1, :] = 1.0 * np.sin(3.0 * np.pi * (np.arange(15) / 30.0)) * 0.05

ani = animation.FuncAnimation(fig, update_positions, frames=range(0, 250), interval=50, repeat=False)

plt.show()
