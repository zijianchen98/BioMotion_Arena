
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 100

# Define the number of point-lights
num_lights = 15

# Define the figure size
fig, ax = plt.subplots(figsize=(8, 8))

# Set the background color to black
ax.set_facecolor('black')

# Remove the axis labels and ticks
ax.axis('off')

# Initialize the point-lights as empty lists
lights_x = []
lights_y = []

# Generate random initial positions for the point-lights
for _ in range(num_lights):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    lights_x.append(x)
    lights_y.append(y)

# Function to update the animation frame
def update(frame):
    # Clear the previous frame
    ax.clear()

    # Set the background color to black
    ax.set_facecolor('black')

    # Update the positions of the point-lights based on the action "lying down"
    for i in range(num_lights):
        if frame < num_frames / 2:
            # Lying down motion - moving towards the ground
            lights_y[i] -= 0.01
        else:
            # Lying down motion - staying on the ground
            pass

    # Scatter plot the point-lights
    ax.scatter(lights_x, lights_y, color='white', s=50)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Display the animation
plt.show()
