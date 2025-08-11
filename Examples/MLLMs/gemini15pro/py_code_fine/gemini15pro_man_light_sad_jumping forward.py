
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
num_frames = 30
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example motion: Jumping forward
t = np.linspace(0, 2*np.pi, num_frames)
jump_height = 20

# Head
x[0,:] = np.linspace(0, 50, num_frames)
y[0,:] = jump_height * np.sin(t) + 100

# Shoulders
x[1,:] = x[0,:] - 5
y[1,:] = y[0,:] - 5
x[2,:] = x[0,:] + 5
y[2,:] = y[0,:] - 5

# Elbows
x[3,:] = x[1,:] - 10 * np.sin(t/2)
y[3,:] = y[1,:] - 10 * np.cos(t/2)
x[4,:] = x[2,:] + 10* np.sin(t/2)
y[4,:] = y[2,:] - 10 * np.cos(t/2)

# Hands
x[5,:] = x[3,:] - 5
y[5,:] = y[3,:] - 5
x[6,:] = x[4,:] + 5
y[6,:] = y[4,:] - 5


# Hips
x[7,:] = x[0,:] - 2
y[7,:] = y[0,:] - 25

# Knees
x[8,:] = x[7,:] - 8 * np.cos(t)
y[8,:] = y[7,:] - 20 - 10 * np.sin(t)
x[9,:] = x[7,:] + 8 * np.cos(t)
y[9,:] = y[7,:] - 20 - 10 * np.sin(t)

# Ankles/Feet
x[10,:] = x[8,:]
y[10,:] = y[8,:] - 10
x[11,:] = x[9,:]
y[11,:] = y[9,:] - 10

x[12,:] = x[0,:] #mid torso
y[12,:] = y[0,:] - 15

x[13,:] = x[7,:] + 3 #mid hips
y[13,:] = y[7,:] + 3

x[14,:] = x[7,:] #mid torso and hips
y[14,:] = y[12,:]/2 + y[13,:]/2



# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-20, 70) # Adjust limits as needed
ax.set_ylim(0, 120)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')


# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# For saving
#ani.save("sad_man_jumping_forward.mp4")

plt.show()

