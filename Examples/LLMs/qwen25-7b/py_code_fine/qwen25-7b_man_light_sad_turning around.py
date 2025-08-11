
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parameters for the sadman's turning around
angle = 0 = np.linspace(0 = 0 - 2 * np.pi, t =  0 + 2 * np.pi, num = 15)
x = np.cos(angle)
y = np.sin(angle)

fig, ax = plt.subplots(figsize=(6, 6))
ax, = ax.plot(x, y, 'o', color='white')  # Plot the points

def update(frame):
    angle += 0 = frame / 100
    x.set_data(np.cos(angle), np.sin(angle))
    return o,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0 - 2 * np.pi, t =  2 * np.pi, step=0/100), interval=50, blit=True)

plt.show()
