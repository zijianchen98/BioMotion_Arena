
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
time_steps = 60
coordinates = np.zeros((15, 2, time_steps))

# Example jump motion (adjust these values for realistic movement)
x_center = 200
y_center = 150
jump_height = 80
jump_duration = 30


for t in range(time_steps):

    #head
    coordinates[0, :, t] = [x_center, y_center+jump_height * np.sin(np.pi * t / jump_duration) if t<jump_duration else y_center]
    #shoulders and elbows

    coordinates[1, :, t] = [x_center-20, y_center-20 + jump_height * np.sin(np.pi * t / jump_duration) if t<jump_duration else y_center-20]
    coordinates[2, :, t] = [x_center+20, y_center-20 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-20]

    coordinates[3, :, t] = [x_center-30, y_center-40 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-40]

    coordinates[4, :, t] = [x_center+30, y_center-40 + jump_height * np.sin(np.pi * t / jump_duration) if t<jump_duration else y_center-40]



    coordinates[5, :, t] = [x_center - 20, y_center - 60 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-60]
    coordinates[6, :, t] = [x_center + 20, y_center - 60 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-60]

    coordinates[7, :, t] = [x_center - 10, y_center - 60 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-60]
    coordinates[8, :, t] = [x_center + 10, y_center - 60 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-60]





    #hips and knees


    coordinates[9, :, t] = [x_center-20, y_center-80 + jump_height * np.sin(np.pi * t / jump_duration) if t<jump_duration else y_center-80]

    coordinates[10, :, t] = [x_center+20, y_center-80 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-80]


    coordinates[11, :, t] = [x_center-20, y_center-100 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-100]
    coordinates[12, :, t] = [x_center+20, y_center-100 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center-100]



    # feet

    coordinates[13, :, t] = [x_center - 20, y_center - 120 + jump_height * np.sin(np.pi * t / jump_duration) if t<jump_duration else y_center - 120]

    coordinates[14, :, t] = [x_center + 20,y_center - 120 + jump_height * np.sin(np.pi * t / jump_duration)if t<jump_duration else y_center - 120]







# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0,400)
ax.set_ylim(0,300)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
ax.set_facecolor('black')  # Set background to black

# Initialize the point-lights
points = ax.plot([], [], 'wo', markersize=8)[0] #white color

# Animation update function
def update(frame):
    x = coordinates[:, 0, frame]
    y = coordinates[:, 1, frame]
    points.set_data(x, y)
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=20, blit=True)

# Display the animation (or save as a video file)
plt.show()


