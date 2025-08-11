
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_jump_up():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_facecolor('black')
    
    points, = ax.plot([], [], 'wo')
    
    def init():
        points.set_data([], [])
        return points,

    def animate(frame):
        x_data = np.array([5, 4, 6, 4.5, 5.5, 4.2, 5.8, 4.7, 5.3, 4, 6, 5, 3.5, 6.5, 5])
        y_data = np.array([0.5, 0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 2.5, 2.5, 3.5, 3.5, 5.5, 6.5, 6.5, 8.5])
        
        amplitude = 1.5 * np.sin(2 * np.pi * frame / 60)
        
        points.set_data(x_data, y_data + amplitude)
        return points,
    
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)
    plt.show()

animate_jump_up()
