
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights for a single frame
# These coordinates are placeholders and should be replaced with real motion capture data
# or data that simulates the "turning around" action.
# The structure below mimics the arrangement of points in the example image.


def get_coordinates(frame):
    # Example: Simple rotation to illustrate the concept.
    # Replace this with actual motion data.
    angle = frame * (2 * np.pi / 60)  # Rotate over 60 frames
    center_x = 100
    center_y = 50
    radius = 10

    x = [
        center_x + radius * np.cos(angle),
        center_x + radius * np.cos(angle + np.pi/2),
        center_x + radius * np.cos(angle + np.pi),
        center_x + radius * np.cos(angle + 3*np.pi/2)
    ]


    y = [
        center_y + radius * np.sin(angle),
        center_y + radius * np.sin(angle + np.pi/2),
        center_y + radius * np.sin(angle + np.pi),
        center_y + radius * np.sin(angle + 3*np.pi/2)

    ]

    x = np.array(x)
    y = np.array(y)

    coords = np.zeros((15, 2))

    coords[0] = [center_x, center_y + 3*radius]
    coords[1] = [center_x - radius, center_y + 2*radius]
    coords[2] = [center_x, center_y + 2*radius]
    coords[3] = [center_x + radius, center_y + 2*radius]

    coords[4] = [center_x - radius, center_y + radius]
    coords[5] = [center_x, center_y + radius]
    coords[6] = [center_x + radius, center_y + radius]

    coords[7] = [center_x - radius, center_y]
    coords[8] = [center_x, center_y]
    coords[9] = [center_x + radius, center_y]

    coords[10] = x[0] + 0, y[0] - 2*radius
    coords[11] = x[1] + 0, y[1] - 2*radius


    coords[12] = x[0] + 0, y[0] - 3*radius
    coords[13] = x[1] + 0, y[1] - 3*radius

    coords[14] = [center_x, center_y - 4*radius]





    return coords




# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 200])  # Adjust limits as needed
ax.set_ylim([0, 100])
ax.set_aspect('equal')  # Maintain aspect ratio
ax.set_facecolor('black')  # Set background color to black
scatter = ax.scatter([], [], s=20, c='white')  # Initialize scatter plot


# Animation update function
def update(frame):
  coords = get_coordinates(frame)
  scatter.set_offsets(coords)
  return scatter,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=60, interval=20, blit=True)  # 60 frames, 20ms delay

plt.show()
