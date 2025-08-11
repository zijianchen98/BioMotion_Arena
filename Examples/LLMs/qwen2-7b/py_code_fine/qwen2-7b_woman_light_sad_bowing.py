
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to simulate the movement of a point light stimulus
def simulate_biological_motion(subject, action):
    # Define the subject's and action parameters
    subject = 'sadwoman'
    action = 'bowing'

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim((-10, 10)
    ax.set_ylim((-10, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    # Initialize the point light positions
    points = np.array([[0, 0] for _ in range(15])
    points[0][0] = 0  # Center of the animation
    points[0][1] = 5  # Starting position

    def update(frame):
        # Update the positions of the points based on the action
        if action == 'bowing':
            # Bowing action logic here
            pass
        else:
            print(f'Unsupported action: {action}')
        
        # Update the positions of the points
        for i in range(15):
            points[i] += [np.sin(frame / 10 * np.pi), np.cos(frame / 10 * np.pi)]
        
        # Update the plot
        ax.clear()
        ax.set_xlim((-10, 10))
        ax.set_ylim((-10, 10))
        ax.set_aspect('equal')
        ax.axis('off')
        ax.scatter(points[:, 0], points[:, 1], color='white', s=100)

    # Create the animation
    anim = FuncAnimation(fig, update, frames=np.arange(0, 800, 1, blit=False)
    
    # Show the animation
    plt.show()

# Call the function with the specified parameters
simulate_biological_motion(subject='sadwoman', action='bowing')
