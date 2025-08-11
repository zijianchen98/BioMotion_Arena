
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 point lights
num_lights = 15
positions = np.random.rand(num_lights, 2)

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

lights = []
for pos in positions:
    light, = ax.plot(pos[0], pos[1], 'o', color='white', markersize=5)
    lights.append(light)

def update(frame):
    # Update the positions of the point lights
    for i, light in enumerate(lights):
        x, y = light.get_data()
        new_x = x + 0.01 * np.cos(frame / 10 + i * 2 * np.pi / num_lights)
        new_y = y + 0.01 * np.sin(frame / 10 + i * 2 * np.pi / num_lights)
        light.set_data(new_x, new_y)
    
    return lights

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100), interval=50, blit=True)

plt.show()
