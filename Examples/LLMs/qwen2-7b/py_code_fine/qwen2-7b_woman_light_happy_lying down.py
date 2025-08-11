
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_point_light_animation(subject='happy woman', action='lying down', num_lights=15, duration=30):
    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim((-1.5, 1.5)
    ax.set_ylim((-1.5, 1.5))
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Background color
    ax.set_facecolor('black')

    # Initialize the positions of the points
    positions = np.random.uniform(-1, 1, (num_light, 2)

    def update(frame):
        # Update the positions of the points based on the action
        if action == 'lying down':
            # Lying down motion
            positions[:, 0] += 0.05 * np.sin(frame / 10)  # small horizontal oscillation
            positions[:, 1] += 0.05 * np.cos(frame / 10)  # small vertical oscillation
        elif action == 'standing':
            # Standing motion
            positions[:, 0] += 0.05 * np.sin(frame / 10)  # small horizontal oscillation
            positions[:, 1] += 0.02 * np.cos(frame / 10)  # larger vertical oscillation
        elif action == 'walking':
            # Walking motion
            positions[:, 0] += 0.03 * np.sin(frame / 5)  # medium horizontal oscillation
            positions[:, 1] += 0.03 * np.cos(frame / 5)  # medium vertical oscillation
        else:
            raise ValueError("Invalid action")

        # Ensure points stay within the bounds
        positions = np.clip(positions, -1, 1)

        # Clear the previous frame and plot the updated points
        ax.clear()
        ax.set_facecolor('black')
        ax.scatter(positions[:, 0], position[:, 1], s=50, c='white', edgecolors='none')

    ani = animation.FuncAnimation(fig, update, frames=np.arange(duration), interval=20, blit=False)

    # Show the animation
    plt.show()

# Example usage:
create_point_light_animation(subject='happy woman', action='lying down', duration=60)
