
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def get_coordinates():
    """Return coordinates of the points in the form: (x, y, dx, dy)."""
    centers = [(38,5),(51,5),(64,5),(77,5),(90,5),(103,5),(116,5),(129,5),(142,5),(155,5),(168,5),(181,5)]
    sizes = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    points = [{'center': center, 'size': size} for center, size in zip(centers, sizes)]
    return points

def move_points(points):
    """Move points based on a simple animation function."""
    for p in points:
        p['center'] = ((0.99 * p['center'][0]) + (0.5 * np.random.randn()), (0.99 * p['center'][1]) + (0.5 * np.random.randn()))

def animate(i, points, scat):
    """Animation function."""
    move_points(points)
    scat.set_offsets(np.array([[p['center'][0], p['center'][1]] for p in points]))
    return scat,

def init():
    """Initialize plot."""
    return [],

def main():
    points = get_coordinates()
    fig, ax = plt.subplots()
    ax.set_facecolor('black')
    scat = ax.scatter([p['center'][0] for p in points], [p['center'][1] for p in points], 
                      s=[p['size'] for p in points], c='white')
    ani = animation.FuncAnimation(fig, animate, init_func=init,
                                  fargs=(points, scat), interval=50)
    plt.show()

if __name__ == '__main__':
    main()
