
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_sitting_animation(duration=10, fps=30):
    """
    Generates a point-light animation depicting a man sitting down.

    Args:
        duration (int): The duration of the animation in seconds.
        fps (int): The frames per second of the animation.

    Returns:
        matplotlib.animation.FuncAnimation: The animation object.
    """

    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    points = []
    for i in range(15):
        # Define the trajectory for each point
        x = np.linspace(0.5, 0, 10)  # Starting from the back, moving to the front
        y = np.linspace(-0.5, 0.5, 10)
        z = np.linspace(0, 0.7, 10)
        
        # Adjust the trajectory for each point to create a more natural motion
        x = x + np.random.normal(0, 0.02, 10)
        y = y + np.random.normal(0, 0.02, 10)
        z = z + np.random.normal(0, 0.02, 10)
        
        points.append(list(zip(x, y, z)))
        
    light = plt.PointCollection(points, zdir='z')
    ax.add_collection(light)

    ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, duration, int(fps * duration)), interval=int(1000/fps), blit=True, repeat=True)
    return ani

def update(frame):
    """Updates the animation frames."""
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    z_coords = [p[2] for p in points]
    
    light.set_offsets(np.column_stack([x_coords, y_coords, z_coords]))
    return light,

if __name__ == '__main__':
    ani = generate_sitting_animation()
    plt.show()
