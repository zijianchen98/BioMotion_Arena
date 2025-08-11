
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 60

# Define the positions of the point lights
positions = np.zeros((num_frames, 15, 2))

# Initialize the starting position of each light
for i in range(15):
    positions[0, i] = [np.random.randint(0, 8), np.random.randint(0, 6)]

# Define the speed and direction of each light
speeds = np.random.rand(15)
directions = np.random.choice([-1, 1], size=(15, 2))

# Define the acceleration of each light
accelerations = np.random.rand(15)

# Update the positions of the point lights over time
for t in range(1, num_frames):
    for i in range(15):
        # Calculate the new velocity based on the current velocity and acceleration
        velocities = speeds[i] + accelerations[i]
        
        # Update the position based on the current velocity
        positions[t, i] = positions[t-1, i] + velocities * directions[i]
        
        # Ensure the light stays within the bounds of the screen
        if positions[t, i][0] < 0:
            positions[t, i][0] = 0
            directions[i][0] *= -1
        elif positions[t, i][0] > 7:
            positions[t, i][0] = 7
            directions[i][0] *= -1
        
        if positions[t, i][1] < 0:
            positions[t, i][1] = 0
            directions[i][1] *= -1
        elif positions[t, i][1] > 5:
            positions[t, i][1] = 5
            directions[i][1] *= -1

# Create a figure and axis to display the animation
fig, ax = plt.subplots()
ax.set_xlim(0, 7)
ax.set_ylim(0, 5)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Define the point lights
point_lights = [ax.plot([], [], 'o', color='white')[0] for _ in range(15)]

# Update function for the animation
def update(frame):
    for i in range(15):
        point_lights[i].set_data(positions[frame, i])
    return point_lights

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50, blit=True)

# Show the animation
plt.show()
