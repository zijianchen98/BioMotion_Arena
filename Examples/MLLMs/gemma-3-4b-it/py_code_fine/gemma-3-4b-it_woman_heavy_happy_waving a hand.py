
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_waving_hand_animation(duration=10, fps=30):
    """
    Generates an animation of a waving hand using point-lights against a black background.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): Frames per second.
    """

    num_frames = duration * fps
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    points = []
    for _ in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.3, 0.7)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    scat = ax.scatter(points[:, 0], points[:, 1], s=100, c='white')

    def update(frame):
        for i in range(len(points)):
            angle = (frame / fps) * 2 * np.pi + np.random.uniform(-0.2, 0.2) # Add some randomness
            radius = 0.5 + 0.2 * np.sin(frame / fps)  # Vary radius slightly
            x = radius * np.cos(angle)
            y = radius * np.sin(angle)
            points[i] = [x, y]
        scat.set_offsets(points)
        return scat

    ani = animation.FuncAnimation(fig, update, frames=num_frames, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_waving_hand_animation()
