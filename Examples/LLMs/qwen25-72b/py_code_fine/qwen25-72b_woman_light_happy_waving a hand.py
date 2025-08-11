
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_facecolor('black')
plt.axis('off')

# Number of point-lights
num_points = 15

# Initialize the point-lights
points = [plt.plot([], [], 'o', color='white')[0] for _ in range(num_points)]

# Define the initial positions and velocities of the point-lights
positions = np.random.uniform(-8, 8, (num_points, 2))
velocities = np.zeros((num_points, 2))

# Define the wave motion parameters
wave_amplitude = 2.0
wave_frequency = 0.5
wave_phase = 0.0

def update(frame):
    global wave_phase
    wave_phase += 0.1  # Increment phase for each frame

    # Update positions based on wave motion
    for i in range(num_points):
        x, y = positions[i]
        if i < 5:  # Points representing the waving hand
            x += wave_amplitude * np.sin(wave_frequency * wave_phase + i * 0.5)
        else:  # Other points move slightly to simulate body motion
            x += 0.1 * np.sin(wave_frequency * wave_phase + i * 0.1)
            y += 0.1 * np.cos(wave_frequency * wave_phase + i * 0.1)

        # Update the position of the point
        points[i].set_data(x, y)

    return points

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Display the animation
plt.show()
