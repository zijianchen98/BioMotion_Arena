
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_lights = 15
duration = 100  # Frames
fps = 30
dt = 1 / fps
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),
                     xticks=[], yticks[])
ax.set_facecolor('k')

# Define the motion parameters for forward rolling
# These parameters are crucial for biomechanical plausibility
roll_amplitude = 0.6  # Amplitude of the roll motion
roll_frequency = 1.0  # Frequency of the roll motion (Hz)
roll_phase = 0.0  # Initial phase of the roll motion
forward_speed = 0.3 # speed of movement forward
forward_frequency = 1.5  # Frequency of forward movement (Hz)

# Create the light points
lights = []
for i in range(num_lights):
    light = plt.scatter(0, 0, s=50, color='w', zorder=1)
    lights.append(light)

# Animation function
def animate(frame):
    for i in range(num_lights):
        # Calculate the roll angle based on time and frequency
        angle = roll_amplitude * np.sin(2 * np.pi * roll_frequency * frame * dt + roll_phase)
        
        # Calculate forward position based on time and frequency
        forward_pos = forward_speed * np.sin(2 * np.pi * forward_frequency * frame * dt)

        # Update the x and y coordinates of the light
        x = forward_pos * np.cos(angle)
        y = forward_pos * np.sin(angle)
        lights[i].set_offsets([x, y])
    
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration, blit=True, repeat=True)

# Save the animation (optional)
# ani.save("forward_rolling.gif", writer='pillow', fps=fps)

plt.show()
