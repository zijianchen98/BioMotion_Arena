
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_facecolor('black')
ax.axis('off')

# Initialize the point-lights
num_points = 15
points, = ax.plot([], [], 'wo', markersize=10)
x = np.zeros(num_points)
y = np.zeros(num_points)


# Define the animation update function
def update(frame):
    global x, y
    dt = 0.1
    g = -9.81
    
    #jumping motion
    x += 2 * dt
    y += 2 * dt - 0.5*g*dt**2
    
    #adjust positions for realism
    x[0] += np.sin(frame*0.1)*0.2
    y[0] += np.sin(frame*0.1)*0.1
    x[1] += np.sin(frame*0.2)*0.2
    y[1] -= np.cos(frame*0.2)*0.1
    x[2] += np.sin(frame*0.3)*0.2
    y[2] += np.cos(frame*0.3)*0.1
    x[3] -= np.sin(frame*0.1)*0.2
    y[3] -= np.cos(frame*0.1)*0.1
    x[4] -= np.sin(frame*0.2)*0.2
    y[4] += np.cos(frame*0.2)*0.1
    x[5] -= np.sin(frame*0.3)*0.2
    y[5] -= np.cos(frame*0.3)*0.1
    x[6] += np.sin(frame*0.15)*0.1
    y[6] += np.cos(frame*0.15)*0.1
    x[7] -= np.sin(frame*0.15)*0.1
    y[7] -= np.cos(frame*0.15)*0.1
    x[8] += np.sin(frame*0.25)*0.1
    y[8] += np.cos(frame*0.25)*0.1
    x[9] -= np.sin(frame*0.25)*0.1
    y[9] -= np.cos(frame*0.25)*0.1
    x[10] += np.sin(frame*0.05)*0.1
    y[10] += np.cos(frame*0.05)*0.1
    x[11] -= np.sin(frame*0.05)*0.1
    y[11] -= np.cos(frame*0.05)*0.1
    x[12] += np.sin(frame*0.35)*0.1
    y[12] += np.cos(frame*0.35)*0.1
    x[13] -= np.sin(frame*0.35)*0.1
    y[13] -= np.cos(frame*0.35)*0.1
    x[14] += np.sin(frame*0.45)*0.1
    y[14] += np.cos(frame*0.45)*0.1

    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()

