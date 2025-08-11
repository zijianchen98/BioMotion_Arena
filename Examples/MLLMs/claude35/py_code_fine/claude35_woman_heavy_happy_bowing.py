
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to set up the figure and axes
def setup_plot():
    fig, ax = plt.subplots()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_facecolor('black')
    return fig, ax

# Define the initial positions of the point lights
def initialize_bow():
    # 15 point lights in a basic configuration for "bowing"
    positions = np.array([
        [0, 1],    # head
        [-0.5, 0.7], [0.5, 0.7],  # shoulders
        [-0.7, 0.3], [0.7, 0.3],   # elbows
        [-0.9, -0.1], [0.9, -0.1],  # wrists
        [-0.3, -1], [0.3, -1],     # feet
    ])
    return positions

# Function to update positions for animation
def update(frame, scat):
    # Adjust the vertical position to simulate bowing
    height_change = np.maximum(-0.05 * frame, -0.5)  # Simulate downward motion
    # Update the y-coordinates based on bowing
    new_positions = initialize_bow() + np.array([[0, height_change]]*15)
    scatter.set_offsets(new_positions)
    return scat,

# Main code
fig, ax = setup_plot()
initial_positions = initialize_bow()
scat = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], color='white', s=50)

# Create and run the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 30), fargs=(scat,),
                              interval=100, blit=True)

# Show the plot
plt.show()
