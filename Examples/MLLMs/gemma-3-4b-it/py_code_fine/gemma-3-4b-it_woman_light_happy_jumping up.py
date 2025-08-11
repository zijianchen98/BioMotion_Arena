
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_jumping_animation():
    """
    Generates a point-light animation of a woman jumping up.
    """

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, aspect='equal', facecolor='black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 3)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis()

    points = np.random.rand(15, 2)  # Random initial positions
    colors = [(1, 1, 1)] * 15  # White points

    def init():
        for i in range(15):
            ax.scatter(points[i, 0], points[i, 1], s=50, color=colors[i], zorder=2)
        return points,

    def animate(i):
        # Simulate jumping motion
        for j in range(15):
            # Simulate a vertical jump
            points[j, 1] = 1.5 * np.sin(i * 0.1)  # Simple sine wave for movement
            
        return points,

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=150, interval=20, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_jumping_animation()
