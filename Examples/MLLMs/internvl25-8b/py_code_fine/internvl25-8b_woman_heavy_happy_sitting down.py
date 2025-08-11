
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    for j in dots:
        j.set_center((0, 0))
    return lines

def update(frame):
    for j in dots:
        if frame < 8:
            j.set_center((0, -frame * 4))
        elif 8 <= frame < 15:
            j.set_center((0, -15 * 4))
    for i in range(8):
        lines[i].set_data([0, -7 * 4], [0, -frame * 4])
        lines[i].set_color('white')
    for i in range(8, 15):
        lines[i].set_data([0, -15 * 4], [0, -frame * 4])
        lines[i].set_color('white')
    return lines

# Constants
num_lights = 15
dots = []
lines = []

# Create the scatter plot for the dots
fig, ax = plt.subplots()
ax.set_xlim(-5, 10)
ax.set_ylim(-5, 30)
ax.axis('off')

for _ in range(num_lights):
    dots.append(ax.scatter([], []))

# Create the lines for each dot position
for i in range(num_lights):
    if i < 8:
        i += 1
    else:
        i -= 8
    line, = ax.plot([], [], 'W-', lw=1)
    lines.append(line)

# Set the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(16), init_func=init, blit=True, repeat=False)

plt.show()
