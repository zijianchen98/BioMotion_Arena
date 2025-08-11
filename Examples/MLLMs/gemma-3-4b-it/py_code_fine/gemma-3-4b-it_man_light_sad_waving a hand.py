
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_waving_hand():
    """
    Generates an animation of a sadman waving his hand using 15 white point-lights 
    against a black background, aiming for realistic and biomechanically plausible motion.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        points.append([np.random.uniform(-0.8, 0.8), np.random.uniform(-0.8, 0.8)])

    line, = ax.plot([], [], 'w', lw=2)

    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        # Simulate waving motion - simple sinusoidal movement
        for j in range(len(points)):
            x = points[j][0] + 0.5 * np.sin(i * 0.1)
            y = points[j][1] + 0.5 * np.cos(i * 0.1)
            points[j] = [x, y]

        line.set_data(points, repeat=True)  #repeat data for animation
        return line,
    
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    animate_waving_hand()
