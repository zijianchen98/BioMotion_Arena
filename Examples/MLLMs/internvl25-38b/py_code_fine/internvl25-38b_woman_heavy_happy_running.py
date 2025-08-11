
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Initial positions for the point-lights
x = np.array([
    0.2, 0.4, 0.6, 0.8, 0.2, 0.4, 0.6, 0.8, 0.3, 0.5, 0.7,
    0.3, 0.5, 0.7, 0.5
])
y = np.array([
    0.1, 0.3, 0.3, 0.1, 0.5, 0.5, 0.5, 0.5, 0.7, 0.7, 0.7,
    0.9, 0.9, 0.9, 0.8
])

# Function to update positions based on running motion
def update_position(i):
    global x, y
    
    # Oscillate the vertical positions
    y[0] = 0.1 + 0.1 * np.sin(i / 10.0)
    y[1] = 0.3 - 0.1 * np.sin(i / 10.0)
    y[2] = 0.3 + 0.1 * np.sin(i / 10.0)
    y[3] = 0.1 - 0.1 * np.sin(i / 10.0)
    
    y[4] = 0.5 + 0.1 * np.sin(i / 10.0)
    y[5] = 0.5 - 0.1 * np.sin(i / 10.0)
    y[6] = 0.5 + 0.1 * np.sin(i / 10.0)
    y[7] = 0.5 - 0.1 * np.sin(i / 10.0)
    
    y[8] = 0.7 + 0.1 * np.sin(i / 10.0)
    y[9] = 0.7 - 0.1 * np.sin(i / 10.0)
    y[10] = 0.7 + 0.1 * np.sin(i / 10.0)
    
    y[11] = 0.9 + 0.1 * np.sin(i / 10.0)
    y[12] = 0.9 - 0.1 * np.sin(i / 10.0)
    y[13] = 0.9 + 0.1 * np.sin(i / 10.0)
    
    # Oscillate the horizontal positions for a running motion
    x[0] = 0.2 + 0.1 * np.cos(i / 10.0)
    x[1] = 0.4 + 0.1 * np.cos(i / 10.0)
    x[2] = 0.6 + 0.1 * np.cos(i / 10.0)
    x[3] = 0.8 + 0.1 * np.cos(i / 10.0)
    
    x[4] = 0.2 + 0.1 * np.cos(i / 10.0)
    x[5] = 0.4 + 0.1 * np.cos(i / 10.0)
    x[6] = 0.6 + 0.1 * np.cos(i / 10.0)
    x[7] = 0.8 + 0.1 * np.cos(i / 10.0)
    
    x[8] = 0.3 + 0.1 * np.cos(i / 10.0)
    x[9] = 0.5 + 0.1 * np.cos(i / 10.0)
    x[10] = 0.7 + 0.1 * np.cos(i / 10.0)
    
    x[11] = 0.3 + 0.1 * np.cos(i / 10.0)
    x[12] = 0.5 + 0.1 * np.cos(i / 10.0)
    x[13] = 0.7 + 0.1 * np.cos(i / 10.0)
    
    y[14] = 0.8 + 0.1 * np.sin(i / 5.0)

    return x, y

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_facecolor('black')
散点图 = ax.scatter(x, y, c='white')

def animate(i):
    x_new, y_new = update_position(i)
    散点图.set_offsets(np.column_stack((x_new, y_new)))
    return 散点图,

ani = animation.FuncAnimation(fig, animate, frames=200, interval=50, blit=True)
plt.show()
