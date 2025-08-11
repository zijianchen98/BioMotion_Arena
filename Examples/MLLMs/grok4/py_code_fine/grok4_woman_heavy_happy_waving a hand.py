
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to create the point-light display for the "happy woman waving"
def create_wave_motion(frame, points, wave_height, wave_angle):
    for i in range(len(points)):
        # Adjust the positions of points to create wave motion
        if i == 0:  # Head
            points[i] = [0, wave_height + np.sin(frame * wave_angle)]
        elif i == 1 or i == 2:  # Shoulders
            points[i] = [-0.2 + i * 0.4, wave_height]
        elif i < 5:  # Hands
            points[i] = [-0.3 + (i - 3) * 0.3, wave_height + 0.5 * np.sin(frame * wave_angle)]
        elif i < 10:  # Body
            points[i] = [0, wave_height - (i - 4) * 0.1]
        else:  # Feet
            points[i] = [-0.1 + (i - 10) * 0.2, wave_height - 0.5]

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 0.5)
ax.set_ylim(-1, 1)
ax.set_facecolor('black')

# Number of point lights
num_points = 15
points = np.zeros((num_points, 2))

# Create initial points
for i in range(num_points):
    if i < 3:  # Head and shoulders
        points[i] = [0, 0.9]
    elif i < 5:  # Arms
        points[i] = [-0.3 + (i - 3) * 0.3, 0.5]
    else:  # Body and legs
        points[i] = [0, 0.0]

# Create point light objects
point_lights, = ax.plot(points[:, 0], points[:, 1], 'o', color='white')

# Animation function
def animate(frame):
    wave_angle = 0.2  # This controls the speed of the wave motion
    create_wave_motion(frame, points, 0.5, wave_angle)
    point_lights.set_data(points[:, 0], points[:, 1])
    return point_lights,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50, repeat=True)

# Show the animation
plt.show()
