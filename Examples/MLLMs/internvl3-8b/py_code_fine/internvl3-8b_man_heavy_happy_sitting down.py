
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the position of the man in each frame
frame_positions = np.array([
    [10, 20],
    [11, 19],
    [12, 18],
    [13, 17],
    [14, 16],
    [15, 15],
    [16, 14],
    [17, 13],
    [18, 12],
    [19, 11],
    [20, 10],
    [22, 20],
    [24, 15],
    [26, 10],
    [28, 6]
])

# Define the animation function
def update(frame):
    # Clear previous plot
    plt.cla()
    
    # Plot the man
    plt.scatter(frame_positions[frame, 0], frame_positions[frame, 1], color='w', s=100)

    # Set the plot limits
    plt.xlim(0, 30)
    plt.ylim(0, 30)

# Create the animation
ani = FuncAnimation(plt.gcf(), update, frames=len(frame_positions), interval=200)

# Show the animation
plt.show()
