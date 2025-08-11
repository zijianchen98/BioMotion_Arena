
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the initial position of the sadman's hand
initial_position = [0_waving_hand_initial_x, te_waving_hand_initial_y ]  # Replace with actual coordinates

# Define the motion parameters
speed = 0_waving_hand_speed  # Replace with actual speed
angle =  np.radians( -45 )  # Adjust angle to match the waving motion
amplitude =  5  # Adjust amplitude to match the waving motion

# Create the figure and axis
fig, ax = plt.subplots()
axx.set_facecolor('black')

# Create the point-light stimulus
point_light = ax.plot([initial_position[0]], [initial_position[1]], 'w.', markersize=10)[0]

def update(frame):
    xnew, y = initial_position
    x += speed * frame / 100
    y += amplitude * np.sin(angle * x)
    
    point_light.set_data([x], [y))
    return point_light,

# Set the limits of the plot
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0_frames ), interval=10, blit=True)

# Show the animation
plt.show()
