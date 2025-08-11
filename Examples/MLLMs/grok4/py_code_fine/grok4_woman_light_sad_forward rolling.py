
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15  # Number of point lights
frames = 100     # Number of frames in the animation
roll_duration = 3  # Duration of the roll in seconds

# Define the point-light positions (initial positions)
# In this case, we'll use a simple vertical line as a starting point
def initialize_positions():
    return np.array([[0, i] for i in range(num_points)])

# Update function to evolve the point lights over time
def update_positions(frame, points):
    # Simple forward roll movement (sine wave)
    t = frame / frames * (2 * np.pi * roll_duration)

    # Update the points as they roll forward
    for i in range(num_points):
        # Add horizontal motion and a slight vertical motion for `rolling` effect
        points[i][0] = np.sin(t + (i * np.pi / num_points)) * 0.5  # Forward motion
        points[i][1] = -np.cos(t + (i * np.pi / num_points)) * (i/num_points)  # Falling motion
    return points

# Main animation function
def animate(i):
    plt.cla()  # Clear previous frame
    points = update_positions(i, point_lights)
    plt.scatter(points[:, 0], points[:, 1], color='white')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_facecolor('black')
    plt.axis('off')  # Turn off the axis
    return

# Initialize point lights
point_lights = initialize_positions()

# Create figure for animation
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=frames, interval=1000/30)  # 30 FPS

# Display the animation
plt.show()
