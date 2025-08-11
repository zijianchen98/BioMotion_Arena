
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def generate_sadman_animation():
    """
    Generates a point-light animation of a sadman rolling forward.
    """

    fig, ax = plt.subplots()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticks([])
    
    points = []
    for _ in range(15):
        x = np.random.uniform(-7, 7)
        y = np.random.uniform(-7, 7)
        z = 0  # Ground level
        points.append([x, y, z])

    light_sources = []
    for i in range(15):
        light_sources.append((points[i][0], points[i][1], 2)) #Light source position and radius

    scat = ax.scatter(points[:, 0], points[:, 1], s=20, c='white', marker='o')

    def animate(i):
        """
        Animation function.
        """
        for j in range(15):
            # Simulate rolling motion.  The update is based on simple forward rolling.
            points[j][0] += 0.05 * np.sin(i * 0.1)  # Simple rolling motion
            points[j][1] -= 0.03 * np.cos(i * 0.1) # Slight sideways movement
        
        scat.set_offsets(points)
        return scat,

    ani = animation.FuncAnimation(fig, animate, frames=200, blit=True, repeat=True)

    plt.show()

if __name__ == '__main__':
    generate_sadman_animation()
