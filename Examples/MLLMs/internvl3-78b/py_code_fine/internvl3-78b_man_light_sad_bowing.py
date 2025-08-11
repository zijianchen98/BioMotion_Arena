
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis for plotting
fig, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
ax.set_aspect("equal")
ax.set_facecolor("black")

# Initialize the point-lights
dots, = ax.plot([], [], 'bo')

# Function to update the position of the point-lights
def update(frame):
    # Define the positions for the sadman bowing
    # These positions are calculated for a sad, bowing motion
    y2 = np.sin(np.array([1, 2, 4, 8, 16]) / (frame + 1)) * (10 - frame // 3) + (frame // 1) + 15
    x2 = np.array([15, 12, 10, 12, 15]) + (3 - frame // 3)
    y3 = np.sin(np.array([3, 6, 12, 18, 24]) / (frame + 1)) * (10 - frame // 3) + (frame // 1) + 15
    x3 = np.array([5, 8, 10, 12, 15]) + (3 - frame // 3)
    y4 = np.sin(np.array([7, 14, 21, 28, 35]) / (frame + 1)) * (10 - frame // 3) + (frame // 1) + 15
    x4 = np.array([20, 22, 24, 26, 28]) + (3 - frame // 3)

    x_data = np.concatenate((x2, x3, x4))
    y_data = np.concatenate((y2, y3, y4))

    dots.set_data(x_data, y_data)
    return dots,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(50), interval=50, blit=True)

# Remove the axes for better visualisation
ax.axis('off')

# Display the animation
plt.show()
