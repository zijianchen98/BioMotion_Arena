
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_sitting_down_animation(duration=10, fps=30):
    """
    Generates a point-light animation of a woman sitting down.

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

    points = []
    for i in range(15):
        # Create 3D coordinates for the points, simulating a seated posture and lowering
        x = np.random.uniform(-0.8, 0.8, 3)
        y = np.random.uniform(-0.8, 0.8, 3)
        z = np.random.uniform(-0.2, 0.2, 3)
        points.append((x, y, z))
    
    light_sources = points 

    scat = ax.scatter([p[0] for p in light_sources], 
                       [p[1] for p in light_sources], 
                       [p[2] for p in light_sources], 
                       s=20, c='white')

    ani = animation.FuncAnimation(fig, update, fargs=(light_sources, scat), blit=True, repeat=True)
    return ani

def update(frame, light_sources, scat):
    """
    Updates the position of the point lights for each frame.

    Args:
        frame (int): The current frame number.
        light_sources (list): List of point coordinates.
        scat (matplotlib.collections.PathCollection): The scatter object.
    """
    
    # Simulate movement, starting high and moving down
    for i in range(len(light_sources)):
        x, y, z = light_sources[i]
        
        # Simulate sitting down - movement downwards
        z += 0.01 * np.sin(frame * 0.1) 
        
        scat.set_offsets([x, y, z])

    return scat

if __name__ == '__main__':
    ani = create_sitting_down_animation(duration=10, fps=30)
    plt.show()
