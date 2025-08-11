
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 50], [10, 40], [20, 40], [30, 40],
    [5, 30], [15, 30], [25, 30], [35, 30],
    [10, 20], [20, 20], [15, 10], [25, 10],
    [15, 0], [25, 0], [20, -10]
])


# Function to update the positions of the point-lights for each frame
def update(frame_num, points, line):
    # Simulate walking motion (replace with more sophisticated biomechanical model if needed)
    x_shift = 2 * np.sin(frame_num * 0.1)  # Adjust speed and amplitude as desired
    y_shift = 1 * np.sin(frame_num * 0.1)  # Adjust speed and amplitude as desired
    
    # Apply motion to the point-lights
    new_positions = initial_positions + np.array([x_shift, y_shift])
    
    # Add small random noise to mimic natural gait variations
    noise = np.random.normal(0, 0.5, size=initial_positions.shape)
    new_positions += noise

    # Update the plot data
    points.set_data(new_positions[:, 0], new_positions[:, 1])

    return points,

# Set up the figure and axes
fig = plt.figure(figsize=(5, 7))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-50, 100), ylim=(-50, 100))  # Adjust limits as needed
ax.set_facecolor('black')  # Set background to black

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=5)

# Create the animation
ani = animation.FuncAnimation(fig, update, fargs=(points,),
                              frames=200, interval=50, blit=True)

# Save animation as MP4 (requires ffmpeg)
ani.save('biological_motion.mp4', writer='ffmpeg', fps=20)

# Show the animation (optional - you can remove this if only saving the animation)
plt.show()
