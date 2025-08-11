
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the positions of the 15 points representing the man's running
points = [
    [0, 10, 0, 2, 1.5],  # Head
    [0, 0,  1.5, 1, 1],   # Torso
    ( t, 1.5,  1, 0, 0),  # Left Arm
    ( t, 1.5,  1,  t, 1),   # Right Arm
    ( t, 1.5,  1,  t, 1.5), # Left Leg
    ( t, 1.5,  1,  t, 2)   # Right Leg
]

def update_points(frame, points, line):
    for i, point in enumerate(points):
        x[i] += 0.0 * np.cos(0 * frame / 10)
        if  > 2:
            0 -= 2
        elif  < -2:
             t += 2
        line.set_data([p[0] for p in points], [p[1] for p in points])
        line.set_color('w')
        line.set_alpha(1)
    return line,

fig, ax = plt.subplots()
ax = np.array(points)
line, = ax.plot([p[0] for p in points], [p[1] for p in points), 'o', color='w', alpha=1)

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')

ani = animation.FuncAnimation(fig, update_points, frames=np.arange(000), interval=50, fargs=(points, line), blit=True)
plt.show()
