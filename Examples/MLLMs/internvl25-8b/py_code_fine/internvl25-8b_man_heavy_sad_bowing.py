
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to initialize the figure and axis
def init():
    ax.clear()
    ax.set_xlim([-25, 25])
    ax.set_ylim([-25, 25])
    ax.auto_scale_view()

# Function to create the animation frame
def update(frame):
    global bodies

    # Coordinates of the head, spine, and hands
    head = [5, 10]
    spine = [0, 0]
    hands = [(5, 0), (10, 0)]

    # Adjustments for each frame
    if frame < 30:
        spine = [0, frame * 0.2]
        heads = [(5, 25), (10, 25)]
        hand_adjustments = [(5, frame * 0.05), (10, frame * 0.05)]

    elif 30 <= frame < 60:
        spine = [5, 0]
        heads = [(5, 10), (10, 10)]
        hand_adjustments = [(5, frame * 0.05), (10, frame * 0.05)]

    else:
        spine = [8, 0]
        heads = [(5, -10), (10, -10)]
        hand_adjustments = [(5, -frame * 0.05), (10, -frame * 0.05)]

    # Move the points
    ax.clear()
    ax.set_xlim([-25, 25])
    ax.set_ylim([-25, 25])
    ax.auto_scale_view()

    for i, (pos, point) in enumerate(zip(bodies, bodies_data), start=1):
        ax.add_patch(plt.Circle(point, 0.5, color='white'))
        ax.update_datalim()

    bodies = [spine, heads[0], heads[1]] + [hand_adjustments[i] for i in range(2)]

# Number of point lights
num_points = 15

# Generating random positions for the bodies
bodies = [np.random.randint(-15, 15, size=(2)) for _ in range(3)]
bodies += [[np.random.randint(-15, 15, size=(2))] * 12

# Scaling the bodies appropriately
bodies[0] = [5, 10]
bodies[1] = [10, 5]
bodies[2] = [8, 15]
bodies += [[np.random.randint(-15, 15, size=(2))] for _ in range(10)]

# Data for plotting circles
bodies_data = bodies.copy()

fig = plt.figure()
ax = fig.add_subplot(111, frame_on=False, aspect='equal')
ax.set_xlim([-25, 25])
ax.set_ylim([-25, 25])
ax.set_yticks([])
ax.set_xticks([])
ax.grid(False)

# Initializing the animator
ani = animation.FuncAnimation(
    fig, update, frames=np.arange(0, 120, 0.1), blit=False, init_func=init)

plt.show()
