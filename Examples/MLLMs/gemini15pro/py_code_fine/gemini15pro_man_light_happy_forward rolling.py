
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the coordinates of the 15 point-lights over time
# This is a simplified example and would need to be refined for realistic motion
num_frames = 60
x = np.zeros((15, num_frames))
y = np.zeros((15, num_frames))

# Example motion: Head (top 3 points)
x[0:3, :] = np.linspace(50, 450, num_frames)  # Move horizontally
y[0, :] = 450 + 20 * np.sin(np.linspace(0, 2 * np.pi, num_frames)) # Oscillate slightly
y[1, :] = 400 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
y[2, :] = 400 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_frames))

# Example motion: Shoulders and elbows (next 4 points)
x[3:7, :] = np.linspace(75, 425, num_frames) + 10 * np.sin(np.linspace(0, 4 * np.pi, num_frames))[:, np.newaxis]
y[3, :] = 300 + 20 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
y[4, :] = 300 + 20 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
y[5, :] = 350 + 15 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
y[6, :] = 350 + 15 * np.sin(np.linspace(0, 2 * np.pi, num_frames))



# Example motion: Hands (points 7, 8)
x[7:9, :] = np.linspace(100, 400, num_frames) + 20 * np.sin(np.linspace(0, 4 * np.pi, num_frames))[:, np.newaxis]

y[7, :] = 250 + 25 * np.sin(np.linspace(0, 2 * np.pi, num_frames))
y[8, :] = 250 + 25 * np.sin(np.linspace(0, 2 * np.pi, num_frames))


# Example motion: Torso (points 9-11)
x[9:12, :] = np.linspace(100, 400, num_frames)

y[9, :] = 250
y[10, :] = 200 
y[11, :] = 150


# Example motion: Knees and Feet
x[12:14, :] = np.linspace(125, 375, num_frames)
y[12:14, :] = 75


x[14, :] = np.linspace(150, 350, num_frames)
y[14, :] = 25




# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(0, 500)
ax.set_ylim(0, 500)
ax.set_aspect('equal')
ax.set_facecolor('black')
points, = ax.plot([], [], 'wo')


# Animation update function
def update(frame):
    points.set_data(x[:, frame], y[:, frame])
    return points,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=30, blit=True)

plt.show()

