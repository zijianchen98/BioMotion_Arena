
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of lights and frames
num_lights = 15
num_frames = 100

# Initialize positions and velocities for the lights
positions = np.random.rand(num_lights, 2) * 100
velocities = np.random.rand(num_lights, 2) * 2 - 1

# Define the function to update positions
def update_positions(frame):
    global positions, velocities
    # Apply wave motion effect
    wave_amp = 10
    wave_freq = 0.05
    wave_phase = frame * wave_freq
    positions[:, 1] = positions[:, 1] + wave_amp * np.sin(positions[:, 0] * wave_freq + wave_phase)
    # Apply natural movement
    positions += velocities
    # Boundary conditions to keep lights within the frame
    for i in range(num_lights):
        if positions[i, 0] <= 0 or positions[i, 0] >= 100:
            velocities[i, 0] = -velocities[i, 0]
        if positions[i, 1] <= 0 or positions[i, 1] >= 100:
            velocities[i, 1] = -velocities[i, 1]

    return [plt.plot(positions[:, 0], positions[:, 1], 'wo', markersize=5)[0]]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Create the animation
ani = animation.FuncAnimation(fig, update_positions, frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()
