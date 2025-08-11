
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames and points
num_frames = 100
num_points = 15

# Define the initial positions and velocities of the points
positions = np.random.uniform(low=-10, high=10, size=(num_points, 2))
velocities = np.random.normal(loc=0, scale=1, size=(num_points, 2))

# Define the action and subject
action = "waving a hand"
subject = "happy man with heavy weight"

# Define the function to update the positions of the points for each frame
def update_positions(frame):
    global positions
    # Update the positions based on the velocities
    positions += velocities
    # Keep the points within the screen boundaries
    positions = np.clip(positions, -10, 10)
    # Return the updated positions
    return positions,

# Define the function to plot the points for each frame
def plot_points(frame):
    # Clear the previous plot
    plt.cla()
    # Get the updated positions
    positions = update_positions(frame)
    # Plot the points
    plt.scatter(positions[0][:,0], positions[0][:,1], color='white')
    # Set the background color to black
    plt.gca().set_facecolor('black')
    # Set the limits of the plot
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    # Remove the axis labels
    plt.axis('off')
    # Set the title of the plot
    plt.title(f"{subject} {action}")

# Create the animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, plot_points, frames=num_frames, interval=50)

# Show the animation
plt.show()
