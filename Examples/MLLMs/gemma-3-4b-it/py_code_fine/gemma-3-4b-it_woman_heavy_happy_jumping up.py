
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define parameters
num_lights = 15
duration = 100  # Frames
frame_rate = 30  # Frames per second
width, height = 600, 600

# Define the jumping motion
def generate_motion(t):
    motion = np.zeros((num_lights, 3))
    for i in range(num_lights):
        # Simulate jumping motion
        phase = t * 2 * np.pi 
        motion[i, 0] = np.sin(phase) * 50  # Vertical movement
        motion[i, 1] = np.cos(phase) * 30  # Horizontal movement
        motion[i, 2] = 0 # No rotation for simplicity
    return motion


# Create the figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')
ax.set_xticks([])
ax.set_yticks([])

# Create the lights
lights = []
for i in range(num_lights):
    light, = ax.plot(0, 0, 'w', markersize=10)
    lights.append(light)

# Animation function
def animate(frame):
    for i in range(num_lights):
        motion = generate_motion(frame/frame_rate)
        x = motion[i, 0]
        y = motion[i, 1]
        light = lights[i]
        light.set_data(x, y)
    
    return lights

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=duration * frame_rate // len(generate_motion(1)), interval=1000/frame_rate, blit=True)

# Save the animation (optional)
# ani.save("jumping_woman.gif", writer='pillow', fps=frame_rate)

plt.show()
