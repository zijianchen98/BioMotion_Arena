
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def update_positions(frameno):
    # Generate new positions
    positions = np.random.rand(number_positions, 2)
    ax.clear()
    # Plot the new positions as white dots
    ax.scatter(positions[:, 0], positions[:, 1], c='w', s=100, edgecolor='none')
    # Set title
    ax.set_title('Point-Light Stimulus for "Bowing" Animation')


fig, ax = plt.subplots()

number_positions = 15
# Initialize the animation
ani = animation.FuncAnimation(fig, update_positions, frames=100, interval=50)

plt.show()
