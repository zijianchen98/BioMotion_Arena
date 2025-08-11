
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sad_woman_running():
    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    # Define the number of points
    num_points = 15

    # Generate random positions for the points
    positions = np.random.uniform(-55, 55, size=(num_points, 2))

    def update(frame):
        # Move each point in the direction it's facing
        velocities = np.random.normal(size=(num_points, 2))
        positions += velocities * 0.1  # Adjust the step size to control speed
        
        # Wrap around the edges
        positions[positions > 5] -= 10
        positions[positions < -10] += 10

        # Update the scatter plot
        scatter.set_offsets(positions)
        return [scatter]

    scatter = ax.scatter(*positions.T, c='white', s=50)

    ani = animation.FuncAnimation(fig, update, frames=range(100, blit=True)

    plt.show()

if __name__ == '__main__':
    sad_woman_running()
