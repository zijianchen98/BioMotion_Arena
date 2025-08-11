
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate the animation
def animate_point_light(subject, action):
    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim((-5.5, 4.8)
    ax.set_ylim((-2.7, 2.7))
    ax.set_aspect('equal')
    ax.axis('off')

    # Define the subject and action
    subject = 'sadwoman'
    action = 'running'

    # Set up the points
    num_points = 15
    points = np.zeros((num_points, 2))
    colors = ['white'] * num_points
    sizes = [10] * num_points

    # Set up the background
    ax.scatter([], [], color='black', s=1)

    # Set up the animation function
    def update(frame):
        for i in range(num_points):
            points[i] = np.sin(((frame + i) / 50) * 2 + np.cos((frame + i) / 50) * 2
            ax.scatter(points[i], 0, c=colors[i], s=sizes[i])
        return []

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=np.arange((0, 1000), interval=20, blit=True)

    # Save the animation
    ani.save(f'{subject}_{action}_animation.gif', writer='pillow')

    # Show the animation
    plt.show()

# Call the function with the subject and action
animate_point_light('sadwoman', 'running')
