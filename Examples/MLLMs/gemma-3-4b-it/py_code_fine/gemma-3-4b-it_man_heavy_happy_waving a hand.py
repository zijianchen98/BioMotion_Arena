
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_hand_wave():
    """
    Generates an animation of a waving hand, represented by 15 white point-lights 
    against a black background.  The motion is designed to be biomechanically 
    plausible and appear natural.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    points = []
    for _ in range(15):
        points.append(np.random.rand(2))  # Initialize random positions

    line, = ax.plot(points[:, 0], points[:, 1], 'w', lw=2)

    def update(frame):
        """
        Updates the position of the points for each frame of the animation.
        The movement is designed to simulate a waving hand.
        """
        for i in range(len(points)):
            # Simulate waving motion
            points[i][0] += np.sin(frame * 0.1 + i * 0.05) * 10 
            points[i][1] += np.cos(frame * 0.1 + i * 0.05) * 5
        line.set_data(points[:, 0], points[:, 1])
        return line,

    ani = animation.FuncAnimation(fig, update, frames=150, blit=True, repeat=True)
    plt.show()

if __name__ == '__main__':
    animate_hand_wave()
