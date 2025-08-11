
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the points as [(x, y)]
points_order = [
    [3, 5], [1, 4], [2, 4],  # Head and Neck
    [2, 3], [0, 3], [4, 3],  # Body
    [1, 2], [2, 2], [3, 2],  # Lower Body
    [1, 1], [3, 1],           # Legs
    [0, 0], [2, 0], [4, 0]    # Feet
]

# Initial setup
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_aspect('equal')

# Define the line
scatter = ax.scatter([], [], color='white')

def update(num):
    num%=15  # animation cycles every 15 frames
    point = points_order[num]
    scatter.set_offsets(point)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(15), repeat=True)

# Display the animation
plt.axis('off')
plt.show()
