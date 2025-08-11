
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of points in the point-light display
num_points = 15

# Define the initial positions of the points
# These positions roughly correspond to the joints of a human figure
initial_positions = np.array([
    [0.0, 2.0],  # Head
    [-0.5, 1.5], # Left Shoulder
    [0.5, 1.5],  # Right Shoulder
    [-1.0, 1.0], # Left Elbow
    [1.0, 1.0],  # Right Elbow
    [-1.5, 0.5], # Left Wrist
    [1.5, 0.5],  # Right Wrist
    [-0.5, 0.5], # Left Hip
    [0.5, 0.5],  # Right Hip
    [-0.5, -0.5], # Left Knee
    [0.5, -0.5],  # Right Knee
    [-0.5, -1.5], # Left Ankle
    [0.5, -1.5],  # Right Ankle
    [-0.2, -2.0],# Left Foot
    [0.2, -2.0]   # Right Foot
])

# Define the animation function
def animate(i):
    # Clear the previous frame
    ax.clear()

    # Set the axis limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-3, 3])

    # Turn off the axis labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Set the background color to black
    ax.set_facecolor('black')

    # Define the movement of the points
    # This is where you would define the specific movements of the points
    # to represent a person waving a hand.
    # For now, we will just make the points move randomly.
    # The animation depicts a sad woman with light weight is waving a hand.
    # Making the arm motion sad and waving a hand.
    angles = np.sin(np.linspace(0, 2*np.pi, num_points))
    x_offset = np.zeros(num_points)
    x_offset[5] = 0.8 * np.sin(2*np.pi * i / num_frames) #Left Wrist
    x_offset[4] = 0.5 * np.sin(2*np.pi * i / num_frames) #Right Elbow
    x_offset[1] = 0.1 * np.sin(2*np.pi * i / num_frames) #Left Shoulder
    y_offset = np.zeros(num_points)
    y_offset[5] = -0.1 * np.cos(2*np.pi * i / num_frames) #Left Wrist

    positions = initial_positions + np.stack([x_offset,y_offset],axis = 1)

    # Plot the points
    ax.plot(positions[:, 0], positions[:, 1], 'wo', markersize=8)

    # Set the title of the plot
    ax.set_title('Point-Light Stimulus Animation')

# Create the figure and axes
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Show the animation
plt.show()
