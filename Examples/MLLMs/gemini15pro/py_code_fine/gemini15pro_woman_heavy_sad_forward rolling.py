
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be adjusted for realistic motion
# Each point is represented by a list of its x and y coordinates over time
num_frames = 60  # Number of frames in the animation


def create_point(x_start, y_start, x_offset, y_offset):

    x = np.linspace(x_start, x_start + x_offset, num_frames) + np.sin(np.linspace(0, 2 * np.pi, num_frames)) * 5
    y = np.linspace(y_start, y_start + y_offset, num_frames) + np.cos(np.linspace(0, 2 * np.pi, num_frames)) * 5
    return x,y

x = []
y = []


x1, y1 = create_point(20,80,0,-40)
x2, y2 = create_point(30,70,0,-30)
x3, y3 = create_point(40,80,0,-40)


x4, y4 = create_point(20,60,0,-20)
x5, y5 = create_point(30,50,0,-10)
x6, y6 = create_point(40,60,0,-20)


x7, y7 = create_point(10,40,10,-10)
x8, y8 = create_point(20,30,20,-5)
x9, y9 = create_point(30,30,10,0)
x10, y10 = create_point(40,40,0,-10)



x11, y11 = create_point(20,10,0,5)
x12, y12 = create_point(30,10,0,5)


x13, y13 = create_point(15,-10,0,-5)
x14, y14 = create_point(25,-10,0,0)
x15, y15 = create_point(35,-10,0,-5)

x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]
y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15]


# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([0, 60])  # Set appropriate limits for x and y axes
ax.set_ylim([-20, 100])
ax.set_facecolor('black') # Setting the background to black
points = []
for i in range(15):
    point, = ax.plot([], [], 'wo', markersize=4)
    points.append(point)


# Animation update function
def update(frame):

    for i in range(15):
        points[i].set_data(x[i][frame], y[i][frame])
    return points


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(num_frames), blit=True, interval=20)

plt.show()
