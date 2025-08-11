
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
time_steps = 60
coordinates = np.zeros((15, 2, time_steps))


# Example jump up motion data.
x = np.linspace(0, 1, time_steps // 2)


# Example of a jumping motion (parabolic trajectory)

y_jump = -0.5 * (x - 0.5)**2 + 0.2

y = np.concatenate((np.zeros(time_steps//2), y_jump, y_jump[::-1]))

coordinates[0, 0] = x + 0.3  # Head
coordinates[0, 1] = y + 1


coordinates[1, 0] = x + 0.2 # Neck/shoulders
coordinates[1, 1] = y + 0.9

coordinates[2, 0] = x + 0.4  # Neck/shoulders
coordinates[2, 1] = y + 0.9


coordinates[3, 0] = x + 0.1 # left Elbow
coordinates[3, 1] = y + 0.7

coordinates[4, 0] = x + 0.5  #right Elbow
coordinates[4, 1] = y + 0.7



coordinates[5, 0] = x  #left Hand
coordinates[5, 1] = y + 0.5


coordinates[6, 0] = x + 0.6  #right Hand
coordinates[6, 1] = y + 0.5



coordinates[7, 0] = x + 0.15 #Pelvis
coordinates[7, 1] = y + 0.45


coordinates[8, 0] = x + 0.35 #Pelvis
coordinates[8, 1] = y + 0.45


coordinates[9, 0] = x + 0 # Left Knee
coordinates[9, 1] = y + 0.2

coordinates[10, 0] = x + 0.5 # Right Knee
coordinates[10, 1] = y + 0.2



coordinates[11, 0] = x - 0.1 # left Ankle
coordinates[11, 1] = y 

coordinates[12, 0] = x + 0.6 # right Ankle
coordinates[12, 1] = y


coordinates[13, 0] = x - 0.15 # left foot
coordinates[13, 1] = y - 0.1

coordinates[14, 0] = x + 0.65 # right foot
coordinates[14, 1] = y - 0.1



# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-0.3, 1.3)
ax.set_ylim(-0.3, 1.3)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')



# Update function for the animation
def update(frame):
    x_coords = coordinates[:, 0, frame]
    y_coords = coordinates[:, 1, frame]
    points.set_data(x_coords, y_coords)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=30, blit=True)

plt.show()

