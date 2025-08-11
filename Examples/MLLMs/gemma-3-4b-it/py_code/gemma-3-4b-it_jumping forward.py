
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_jumping_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a man jumping forward.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(10, 30)
        points.append([radius * np.cos(angle), radius * np.sin(angle)])

    line, = ax.plot([], [], 'w', lw=2)
    
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        xdata = [p[0] for p in points]
        ydata = [p[1] for p in points]
        
        # Simulate jumping motion - linear movement forward
        for point in points:
            point[0] += 0.1 * np.sin(i * 0.2)
            point[1] -= 0.05 * np.cos(i * 0.2) 
            
        line.set_data(xdata, ydata)
        return line,
    
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=int(duration * fps), blit=True, repeat=True)
    return ani


if __name__ == '__main__':
    ani = create_jumping_animation()
    plt.show()
