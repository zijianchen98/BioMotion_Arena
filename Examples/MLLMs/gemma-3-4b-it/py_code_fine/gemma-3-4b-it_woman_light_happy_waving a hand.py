
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_waving_hand_animation(duration=5, fps=30):
    """
    Generates a point-light animation depicting a waving hand.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = 15
    lights = []
    for _ in range(points):
        lights.append(plt.plot([], [], 'w')[0])

    def animate(frame):
        for i in range(points):
            # Define the waving motion parameters
            angle = np.linspace(0, 2 * np.pi, 100, endpoint=False)
            radius = 0.5 + 0.2 * np.sin(frame * 0.5) # Scale the radius based on time
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)

            lights[i].set_data(x, y)
        return lights

    ani = animation.FuncAnimation(fig, animate, frames=int(duration * fps), blit=True, repeat=True)
    return ani

if __name__ == '__main__':
    ani = generate_waving_hand_animation()
    ani.save('waving_hand.gif', writer='pillow', fps=15)
    plt.show()
