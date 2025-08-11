
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_jumping_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sad woman jumping forward.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    num_lights = 15
    lights = []
    for i in range(num_lights):
        light = plt.scatter([], [], s=50, color='white')
        lights.append(light)

    def update(frame):
        # Simulate jumping motion - sinusoidal trajectory
        t = frame / fps
        x = np.sin(2 * np.pi * t)
        y = np.cos(2 * np.pi * t)
        z = 0.5  # Height of jump

        for i, light in enumerate(lights):
            light.set_offsets(np.array([[x, y, z]], dtype=float))

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=False)
    return ani

if __name__ == '__main__':
    ani = generate_sad_woman_jumping_animation()
    ani.save("sad_woman_jumping.gif", writer='pillow', fps=15)  # Save as GIF
    plt.show()
