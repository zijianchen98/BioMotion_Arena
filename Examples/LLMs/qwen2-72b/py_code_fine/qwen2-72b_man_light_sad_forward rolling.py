
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 point-lights
# These coordinates are just placeholders and do not represent actual biological motion
point_lights = [
    [0.1, 0.9], [0.2, 0.8], [0.3, 0.7], [0.4, 0.6], [0.5, 0.5],
    [0.6, 0.4], [0.7, 0.3], [0.8, 0.2], [0.9, 0.1], [0.1, 0.8],
    [0.2, 0.7], [0.3, 0.6], [0.4, 0.5], [0.5, 0.4], [0.6, 0.3]
]

# Function to update the frame of the animation
def update(frame_number):
    # Clear the current plot
    ax.clear()
    # Update the position of each point-light based on the frame number
    for i, (x, y) in enumerate(point_lights):
        # Simple forward motion for demonstration purposes
        new_x = x + 0.01 * frame_number
        if new_x > 1:
            new_x -= 1  # Wrap around the screen
        point_lights[i][0] = new_x
        # Plot the point-light
        ax.scatter(new_x, y, color='white')

# Create a figure and axis
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')  # Set background to black

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# Show the animation
plt.show()
