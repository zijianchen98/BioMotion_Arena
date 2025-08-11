
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def wave_hand(num_points):
    positions = np.zeros((num_points, 2))
    # Define the hand points (center of mass)
    half_length = 0.2
    radius = 0.05
    base = 0.5
    positions[:, 0] = np.linspace(-base, np.linspace(base, base) * 1.75, num_points)
    positions[:, 1] = np.linspace(base - half_length, base - half_length) + np.linspace(base + half_length, base, num_points)

    def init():
        line.set_data(positions[:, 0], positions[:, 1])
        return (line,)

    def animate(i):
        angle = 2 * np.pi * i / 0.1
        positions[:, 0] = base * np.cos(angle / 2) + np.linspace(base * (1 + np.cos(angle / 2)), base * (1 + np.cos(angle / 2)), num_points)
        positions[:, 1] = base * np.sin(angle / 2) + np.linspace(base - half_length + np.sin(angle / 2), base - half_length + np.sin(angle / 2), num_points)
        line.set_data(positions[:, 0], positions[:, 1])
        return (line,)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'o', markersize=np.sqrt(1 / 10), color='white')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.35, 1.35])
    ax.set_aspect('equal')
    line.set_data([], [])

    ani = animation.FuncAnimation(fig, animate, frames=range(20), init_func=init, blit=True, interval=50, repeat=False)
    plt.xticks(np.array([]))
    plt.yticks(np.array([]))
    plt.gca().spines.set_visible(False)
    plt.style.use('dark_background')
    plt.show()

wave_hand(15)
