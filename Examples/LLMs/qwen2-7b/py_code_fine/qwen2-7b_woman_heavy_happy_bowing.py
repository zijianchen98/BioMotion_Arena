
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_bow():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_facecolor('black')
    
    # Initial position of the points
    points = np.array([(0, 0), ( (0, -4), ( (-3, -6), ( (3, -6)])
    
    def update(frame):
        global points
        # Update positions based on biomechanical principles
        for i in range(points.shape[0]):
            if frame % 2 == 0:
                # Bowing motion: adjust amplitude and frequency as needed
                points[i] += np.sin(frame / 2 * np.pi) * 2
        
        # Ensure points stay within the plot boundaries
        points = np.clip(points, -10, 10)
        
        ax.clear()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_facecolor('black')
        
        # Plot the points
        ax.scatter(points[:, 0], points[:, 1], color='white', s=100)
    
    ani = animation.FuncAnimation(fig, update, frames=np.arange((1000), interval=50)
    plt.show()

animate_bow()
