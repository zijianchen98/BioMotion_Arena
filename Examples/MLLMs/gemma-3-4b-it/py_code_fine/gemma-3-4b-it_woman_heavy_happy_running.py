
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_motion_stimulus():
    """
    Generates a point-light animation depicting a happy woman running,
    consisting of 15 white point-lights against a black background.
    The motion is designed to be realistic and biomechanically plausible.
    """

    # Number of frames in the animation
    num_frames = 100

    # Point light positions (x, y) - mimicking running motion
    # These coordinates are adjusted for a running motion
    points = np.array([
        [0, 0],
        [20, 5],
        [40, 10],
        [60, 10],
        [80, 5],
        [100, 0],
        [120, 5],
        [140, 10],
        [160, 10],
        [180, 5],
        [200, 0],
        [220, 5],
        [240, 10],
        [260, 10],
        [280, 5]
    ])

    # Colors (white)
    colors = 'white'

    # Create figure and axes
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Initialize the points
    scat = ax.scatter(points[:, 0], points[:, 1], s=50, c=colors)

    # Animation function
    def animate(frame):
        # Update point positions for realistic running motion
        for i in range(len(points)):
            # Simulate running motion - adjust speed and direction
            points[i][0] += np.sin(frame * 0.1) * 8
            points[i][1] += np.cos(frame * 0.1) * 8
        
        scat.set_offsets(points)
        return scat,

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, blit=True, repeat=True)

    # Save the animation (optional)
    # ani.save("running_woman_point_light.gif", writer='pillow', fps=20)  # Requires Pillow
    
    plt.show()

if __name__ == '__main__':
    generate_motion_stimulus()
