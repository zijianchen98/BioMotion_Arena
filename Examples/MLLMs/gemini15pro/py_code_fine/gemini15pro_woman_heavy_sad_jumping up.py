
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the number of frames in the animation
num_frames = 60

# Define the coordinates of the 15 point-lights for each frame
# This is a simplified example, you'll need to adjust these values
# to create a realistic jumping motion.
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example: Head movement
x[0,:] = 5  # Constant x-coordinate for the head
y[0,:] = 10 + np.sin(np.linspace(0, 2*np.pi, num_frames)) # Oscillating y-coordinate


# Example: Feet movement (jumping)
feet_y = np.linspace(0, 0, num_frames)
feet_y[num_frames//4:3*num_frames//4] = np.sin(np.linspace(0, np.pi, num_frames//2)) * 5 
x[13,:] = 3
y[13,:] = feet_y
x[14,:] = 7
y[14,:] = feet_y

# Other body parts... (you need to fill these in)
# Consider how each body part moves during a jump:
# - Knees bend before the jump and straighten in the air
# - Arms swing for momentum
# - Body rises and falls



# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 10) #adjust as needed
ax.set_ylim(0, 15)  #adjust as needed
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo', markersize=8) #white dots

# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)

# To save the animation as a GIF:
# ani.save('jumping_motion.gif', writer='pillow') 

plt.show()
