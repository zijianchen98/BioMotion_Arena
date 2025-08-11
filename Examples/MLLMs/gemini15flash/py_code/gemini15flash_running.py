
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5], [1, 4], [2, 4], [3, 4],
    [0.5, 3], [1.5, 3], [2.5, 3],
    [1, 2], [2, 2],
    [1, 1], [2, 1],
    [1, 0], [2, 0],
    [1.5, -1], [2.5, -1]
])


def update_positions(frame_num, positions, fig, ax):
    """Updates the positions of the point-lights for each frame."""
    # Simple running motion simulation.  Replace with more complex biomechanical model for realism.
    x_offset = np.sin(frame_num * 0.1) * 2  # Simulate horizontal movement
    y_offset = np.sin(frame_num * 0.2)  #Simulate vertical bobbing
    new_positions = positions + np.array([x_offset, y_offset])

    # Add leg swinging animation
    leg_swing = np.sin(frame_num * 0.3) * 0.5

    new_positions[8, 0] += leg_swing
    new_positions[9, 0] -= leg_swing

    new_positions[12, 0] += leg_swing * 0.8
    new_positions[13, 0] -= leg_swing * 0.8

    # Keep points within the frame boundaries
    new_positions[:,0] = np.clip(new_positions[:,0], -5, 5)
    new_positions[:,1] = np.clip(new_positions[:,1], -5, 5)


    ax.clear()  # Clear the previous frame
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.scatter(new_positions[:, 0], new_positions[:, 1], color='white', s=50)
    ax.set_facecolor('black')
    ax.axis('off')  # Remove axis

    return fig,

# Set up the figure and axes
fig, ax = plt.subplots()
fig.set_size_inches(5, 10)


# Create the animation
ani = animation.FuncAnimation(fig, update_positions, fargs=(initial_positions, fig, ax), frames=range(200), interval=50, blit=True)

# Save the animation as a GIF (optional)
# ani.save('running_man.gif', writer='imagemagick', fps=20)

plt.show()


