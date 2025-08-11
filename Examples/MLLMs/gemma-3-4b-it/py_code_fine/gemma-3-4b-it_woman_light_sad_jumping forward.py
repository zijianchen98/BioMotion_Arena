
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sad_woman_jumping_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a sad woman jumping forward.

    Args:
        duration (int): Duration of the animation in seconds.
        fps (int): Frames per second.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])

    points = []
    for i in range(15):
        angle = np.random.uniform(0, 2 * np.pi)
        radius = np.random.uniform(0.5, 1.5)
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append([x, y])

    light_points, = ax.plot(points[0][0], points[0][1], 'w', markersize=10)
    
    for i in range(1, len(points)):
        light_points, = ax.plot(points[i][0], points[i][1], 'w', markersize=10)
    
    def update(frame):
        # Simulate jumping forward motion
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            # Simple forward movement with some randomness
            x += np.sin(frame * 0.1) * 0.2  # Adjust amplitude and frequency for jump
            y += np.cos(frame * 0.1) * 0.2  # Adjust amplitude and frequency for jump
            
            points[i][0] = x
            points[i][1] = y
            
            light_points.set_data(points[i][0], points[i][1])
            
        return light_points,

    ani = animation.FuncAnimation(fig, update, frames=int(duration * fps), blit=True, repeat=False)
    return ani

if __name__ == '__main__':
    ani = generate_sad_woman_jumping_animation()
    ani.save("sad_woman_jumping.gif", writer='pillow', fps=15)
    plt.show()
