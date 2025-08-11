
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial positions of the 15 point-lights
initial_positions = np.array([
    [0, 5],  [ -1, 4], [0, 4], [1, 4],
    [-2, 3], [-1, 3], [0, 3], [1, 3], [2, 3],
    [-1, 2], [0, 2], [1, 2],
    [0, 1], [ -0.5, 0], [0.5, 0]
])


# Function to update the positions of the point-lights for each frame
def update_points(frame_num, points, line):
    # Simulate bowing motion (adjust parameters for different movements)

    x_shift = 0.5 * np.sin(frame_num * 0.1)  # Adjust frequency 0.1
    y_shift = 0.5 * np.sin(frame_num * 0.1 + np.pi/2) # Adjust frequency 0.1


    new_positions = initial_positions.copy()

    # Apply the shift to simulate bowing motion.  Adjust indices and scaling as needed to target specific points.

    new_positions[:,0] += x_shift 
    new_positions[1:4, 1] += y_shift*0.8  #Upper body  adjust scaling 0.8
    new_positions[4:9, 1] += y_shift*0.6 #mid body adjust scaling 0.6
    new_positions[9:12,1] += y_shift*0.4 #lower body adjust scaling 0.4
    new_positions[12:, 1] += y_shift*0.2 # Legs adjust scaling 0.2

    points.set_data(new_positions[:, 0], new_positions[:, 1])
    return points,


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-4, 4])  # Adjust limits as needed
ax.set_ylim([-2, 8])  # Adjust limits as needed
ax.set_aspect('equal')  # Maintain aspect ratio
ax.set_facecolor('black')  # Set background color

# Create the point-lights
points, = ax.plot([], [], 'wo', markersize=8)


# Create the animation
ani = animation.FuncAnimation(
    fig, update_points, fargs=(points, ), frames=200, interval=50, blit=True
)


plt.show()

