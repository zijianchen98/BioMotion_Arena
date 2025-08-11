
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of points and their initial positions
num_points = 15
points = np.zeros((num_points, 2))
points[0] = [0.5, 0.5]
points[1] = [0.5, 0.8]
points[2] = [0.4, 0.9]
points[3] = [0.6, 0.9]
points[4] = [0.7, 0.8]
points[5] = [0.8, 0.7]
points[6] = [0.9, 0.5]
points[7] = [0.9, 0.3]
points[8] = [0.7, 0.1]
points[9] = [0.5, 0.1]
points[10] = [0.3, 0.1]
points[11] = [0.2, 0.3]
points[12] = [0.1, 0.5]
points[13] = [0.1, 0.7]
points[14] = [0.2, 0.9]

# Define the animation function
def animate(i):
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    frame.fill(0)
    frame[:,:] = [0, 0, 255]  # Black background

    for j in range(num_points):
        frame[int(points[j][1] * 100), int(points[j][0] * 100)] = [255, 255, 255]

    return frame

# Create the animation
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=100, interval=40, blit=True)

# Display the animation
plt.axis('off')
plt.show()
