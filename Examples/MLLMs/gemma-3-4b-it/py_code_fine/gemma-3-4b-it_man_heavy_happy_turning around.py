
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_turning_around():
    """
    Generates an animation of a man turning around with point-light stimulus.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    
    points = np.array([
        [0.5, 0.5, 0],  # Head
        [0.7, 0.3, 0],  # Right Shoulder
        [0.3, 0.3, 0],  # Left Shoulder
        [0.5, -0.3, 0], # Right Elbow
        [0.3, -0.3, 0], # Left Elbow
        [0.5, 0.7, 0],  # Right Wrist
        [0.3, 0.7, 0],  # Left Wrist
        [0.5, 0.5, 0],  # Chest
        [0.7, 0.5, 0],  # Right Hip
        [0.3, 0.5, 0],  # Left Hip
        [0.5, -0.5, 0], # Right Knee
        [0.3, -0.5, 0], # Left Knee
        [0.5, 0.5, 0],  # Right Ankle
        [0.3, 0.5, 0],  # Left Ankle
        [0.5, 0.0, 0],  # Spine
        [0.5, 0.0, 0]   # Spine
    ])

    lights = ax.scatter(points[:, 0], points[:, 1], s=50, c='white')

    def update(frame):
        """
        Updates the positions of the points to simulate movement.
        """
        for i in range(len(points)):
            angle = (frame / 360) * 2 * np.pi
            x = points[i, 0] + 0.3 * np.cos(angle)
            y = points[i, 1] + 0.3 * np.sin(angle)
            points[i, 0] = x
            points[i, 1] = y
        lights.set_offsets(points)
        return lights

    ani = animation.FuncAnimation(fig, update, frames=360, interval=10, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    animate_turning_around()
