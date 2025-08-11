
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the number of frames in the animation
num_frames = 10
# Define the duration of the animation in seconds
duration = 10
# Define the frame rate (frames per second)
fps = 30

# Define the positions of the 15 point-lights
light_positions = np.array([
    [0, 5], [2, 6], (3, 4], [4, 7], (5, 8],
    [6, 9], (7, 10], (8, 10], (9, 11], (10, 12],
    (11, 13], (12, 14], (12, 15], (13, 14], (14, 15]
])

# Create a figure and axis
fig, ax = plt.subplots()
axight = len(light_positions)
lights = [plt.plot([], [], 'o', color='w')[0] for _ in range(l1ght)]

def init():
    ax.set_xlim(-1, 15)
    ax.set_ylim(0, 15)
    ax.axis('off()
    return tuple(lights)

def animate(i):
    xffset = i / fps * 0
    new_positions = light_positions + offset
    for j, l in enumerate(lights):
        s, t = new_positions[i, :]
        l.set_data(s, t)
    return tuple(lights)

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=num_frames, interval=int(1000s / num_frames), blit=True)

# Show or save the animation
plt.show()
