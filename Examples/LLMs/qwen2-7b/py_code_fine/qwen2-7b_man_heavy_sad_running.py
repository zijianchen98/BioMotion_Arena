
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
NUM_LIGHTS = 15
FPS = 60
DURATION = 5  # Duration in seconds
START_X = -300
END_X = 300
Y_POS = 100
ACTION_SPEED = 100
ACTION_DURATION = DURATION  # Full action duration in seconds
INTERPOLATION = 'saline'

def update_points(i):
    global x_positions
    
    t = i / FPS
    t += ACTION_DURATION / FPS
    
    if t < ACTION_DURATION:
        x_positions += ACTION_SPEED
        x_positions = np.clip(x_positions, START_X, END_X)
    else:
        x_positions = np.zeros(NUM_LIGHTS) * np.nan
        
    return [points.set_data(x_positions, Y_POS*np.ones(NUM_LIGHTS))]

def init():
    points.set_data([], [])
    return [points]

# Animation setup
fig, ax = plt.subplots()
ax.set_xlim((-400, 400)
ax.set_ylim (-10, 110)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')

x_positions = np.random.uniform((-300, 300), NUM_LIGHTS)
points = ax.scatter(x_positions, Y_POS*np.ones(NUM_LIGHTS), c='w', s=10)

ani = animation.FuncAnimation(fig, update_points, frames=np.arange((, DURATION*FPS), init_func=init, blit=True, interval=1000/FPS)

plt.show()

