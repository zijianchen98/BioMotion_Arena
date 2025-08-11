
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 points
initial_positions = [
    (4, 10), (5, 10), (6, 10), (7, 10), (8, 10),
    (5, 8), (6, 8), (7, 8), (8, 8), (9, 8),
    (6, 6), (7, 6), (8, 6), (9, 6), (10, 6)
]

# Function to update the positions of the points
def update_positions(frame):
    global positions
    positions = [
        (x - 0.1, y + 0.1) for x, y in positions
    ]
    return positions

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

# Initialize the points
positions = initial_positions
points = ax.plot(*zip(*positions), 'bo')

# Animation function
def animate(frame):
    global positions
    positions = update_positions(frame)
    points[0].set_data(*zip(*positions))
    return points

# Create animation
anim = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Save animation as a GIF
anim.save('point_light_animation.gif', writer='imagemagick', fps=20)

# Display the animation
plt.show()
