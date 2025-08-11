
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Total number of point-lights
num_frames = 100  # Total frames in the animation
speed = 0.05  # Movement speed increment

# Initial positions (y-coordinates)
y_positions = np.linspace(0.5, -0.5, num_points)

# Function to define the walking motion
def update_points(frame):
    plt.clf()  # Clear the figure
    plt.axis([-1, 1, -1, 1])  # Set limits
    plt.gca().set_facecolor('black')  # Background color

    # Calculate current x positions based on frame number
    x_positions = np.sin(frame * speed + np.linspace(0, 3 * np.pi, num_points))
    
    # Update point-lights
    plt.scatter(x_positions, y_positions, color='white', s=100)

# Create the figure and axis
fig = plt.figure()

# Create animation
ani = animation.FuncAnimation(fig, update_points, frames=num_frames, repeat=True)

# Show the animation
plt.show()
