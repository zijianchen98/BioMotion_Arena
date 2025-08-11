
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(i):
    global x, y, speed, angle
    angle += speed
    x = np.cos(angle)
    y = np.sin(angle)

    linea.set_data(x, y)
    return linea,

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')

x = 0
y = 0
speed = 0.02
angle = 0

linea, = ax.plot([], [], 'o', markersize=10, color='white')
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, interval=50, blit=True)
plt.show()

