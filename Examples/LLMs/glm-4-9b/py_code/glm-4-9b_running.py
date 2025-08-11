
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_points = 15
time_steps = 200
fig, ax = plt.subplots()

# Set up the background
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 2)
ax.axis('off')

# Initialize the points
points, = ax.plot([], [], 'o', color='white', markersize=5)

def init():
    points.set_data([], [])
    return points,

def animate(i):
    t = i / 20.0
    x = 5 + 5 * np.sin(t)
    y = 1 + 0.5 * np.sin(2 * t)
    
    # Locomotion model for running legs
    leg1_x = x + 0.3 * np.sin(t)
    leg1_y = y - 0.3 * np.cos(t)
    leg2_x = x - 0.3 * np.sin(t)
    leg2_y = y - 0.3 * np.cos(t)
    
    # Arms
    arm1_x = x + 0.2 * np.sin(t + np.pi / 2)
    arm1_y = y + 0.2 * np.cos(t + np.pi / 2)
    arm2_x = x - 0.2 * np.sin(t + np.pi / 2)
    arm2_y = y + 0.2 * np.cos(t + np.pi / 2)
    
    # Head
    head_x = x
    head_y = y + 0.4
    
    # Body representation
    body_x = x
    body_y = y
    
    # Generate point-lights positions
    positions = [
        (leg1_x, leg1_y), (leg2_x, leg2_y),
        (arm1_x, arm1_y), (arm2_x, arm2_y),
        (head_x, head_y), (body_x, body_y),
        (x - 0.5, y), (x + 0.5, y),
        (leg1_x - 0.25, leg1_y - 0.25),
        (leg2_x + 0.25, leg2_y - 0.25),
        (arm1_x - 0.25, arm1_y + 0.25),
        (arm2_x + 0.25, arm2_y + 0.25),
        (head_x - 0.25, head_y - 0.25),
        (body_x - 0.25, body_y - 0.25)
    ]
    
    xs, ys = zip(*positions)
    points.set_data(xs, ys)
    
    return points,

ani = animation.FuncAnimation(fig, animate, frames=time_steps, init_func=init, blit=True, interval=20)
plt.show()
