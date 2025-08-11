
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the initial positions of the 15 white point-lights
positions = [
    (0, 10), (1, 9), (1, 1), (0, 0), (-1, 1), (-1, 9),
    (2, 5), (3, 4), (3, 3), (1, 3), (-1, 3), (-3, 4), (-2, 5),
    (0, 4), (0, 6)
]

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-1, 12)
ax.axis('off')

# Create the scatter plot for the point-lights
sc = ax.scatter([p[0] for p in positions], [p[1] for p in positions], c='white')

# Function to update the positions of the point-lights for each frame
def update(frame):
    global positions
    positions = [
        (0, 10), (1, 9), (1, 1), (0, 0), (-1, 1), (-1, 9),
        (2, 5), (3, 4), (3, 3), (1, 3), (-1, 3), (-3, 4), (-2, 5),
        (0, 4), (0, 6)
    ]
    
    if frame % 2 == 0:
        positions[2] = (1, 1.5)
        positions[3] = (0, 0.5)
        positions[4] = (-1, 0.5)
    else:
        positions[2] = (1, 0.5)
        positions[3] = (0, -0.5)
        positions[4] = (-1, -0.5)
    
    sc.set_offsets(positions)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(20), interval=200)

# Display the animation
plt.show()
