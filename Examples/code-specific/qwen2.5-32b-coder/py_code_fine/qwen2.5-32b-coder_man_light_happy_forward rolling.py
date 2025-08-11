
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
num_lights = 15
frames = 100
dt = 0.1
g = 9.81
radius = 0.5
mass = 1.0
omega = 2 * np.pi / frames

# Initial positions of the lights (approximate forward rolling)
theta = np.linspace(0, 2 * np.pi, num_lights, endpoint=False)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Velocities
vx = -np.sin(theta)
vy = np.cos(theta)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')

scat = ax.scatter(x, y, s=100, color='white')

def update(frame):
    global x, y, vx, vy
    
    # Update positions
    x += vx * dt
    y += vy * dt
    
    # Simple physics to simulate rolling
    for i in range(num_lights):
        if y[i] < -radius:
            y[i] = -radius
            vy[i] = -vy[i]
    
    # Rotate the lights around the center to simulate rolling
    angle = omega * frame
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    points = np.vstack((x, y)).T
    rotated_points = np.dot(points, rotation_matrix.T)
    x, y = rotated_points.T
    
    # Update scatter plot
    scat.set_offsets(np.c_[x, y])
    return scat,

ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
plt.show()
