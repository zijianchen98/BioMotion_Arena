
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point light stimulus
def create_point_light_stimulation(duration, num_points):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    ax.axis('off')
    
    points, = ax.plot([], [], 'o', markersize=2, color='white')
    
    def init():
        points.set_data([], [])
        return points,
    
    def update(frame):
        if frame == 0:
            # Define the initial positions of the light points
            positions = np.zeros((15, 2))
            positions[:, 0] += np.sin(2 * np.pi * frame / 100 + np.pi/4)
            positions[:, 1] += np.sin(2 * np.pi * frame / 100 + np.pi/3)
            
            directions = np.array([[1, 0], [0, 1], [np.cos(np.pi/3), np.sin(np.pi/3)],
                                   [1,0], [-1,0], [0,1], [0,-1], [-1,0],
                                   [0, 0], [0.5, np.sqrt(3)/2], [0.5, np.sqrt(3)/2],
                                   [0.5, np.sqrt(3)/2], [0, np.sqrt(3)/2], [0, np.sqrt(3)/2],
                                   [0, np.sqrt(3)/2]])  # Vectors for turning around
        
            points.set_data(np.sum(positions + directions, axis=1), np.sum(positions + directions*1j, axis=1))
        
        return points,

    ani = animation.FuncAnimation(fig, update, frames=duration, init_func=init, blit=True)
    plt.show()

# Set the duration of the animation and the number of points
duration = 100
num_points = 15

# Create the animation
create_point_light_stimulation(duration, num_points)
