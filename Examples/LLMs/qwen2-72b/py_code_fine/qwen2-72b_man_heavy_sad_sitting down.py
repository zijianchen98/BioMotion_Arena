
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial position of the joints
joints = np.array([[0, 0], [0, -1], [-0.5, -1.5], [0.5, -1.5], [-1, -2], [1, -2]])

# Define the connections between the joints
connections = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 5)]

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-3, 1)
ax.set_aspect('equal')
ax.set_facecolor('black')

# Create lines for the stick figure
lines = [ax.plot([], [], 'o-', color='white')[0] for _ in range(len(connections))]

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i):
    # Update the position of the joints to simulate sitting down
    joints[1, 1] -= 0.01 * i  # Lower the body
    joints[2, 1] -= 0.01 * i  # Lower the left leg
    joints[3, 1] -= 0.01 * i  # Lower the right leg
    joints[4, 1] -= 0.01 * i  # Lower the left foot
    joints[5, 1] -= 0.01 * i  # Lower the right foot
    
    for j, (start, end) in enumerate(connections):
        x = [joints[start, 0], joints[end, 0]]
        y = [joints[start, 1], joints[end, 1]]
        lines[j].set_data(x, y)
    
    return lines

ani = animation.FuncAnimation(fig, animate, frames=100, init_func=init, blit=True)

plt.show()
